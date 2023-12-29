# consumers.py
import os
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from influxdb_client import InfluxDBClient

url = os.environ.get('URL', None)
org = os.environ.get('ORG', None)
token = os.environ.get('TOKEN', None)
bucket = os.environ.get('BUCKET', None)


class InfluxDBConsumer(AsyncWebsocketConsumer):
    """
    A class that handles WebSocket connections and queries an InfluxDB
    database based on received data.

    Example Usage:
    ```python
    consumer = InfluxDBConsumer()
    await consumer.connect()  # Connects to the WebSocket
    await consumer.receive('{"bucket": "test",
      "start_time": "2022-01-01T00:00:00Z",
      "stop_time": "2022-01-02T00:00:00Z"}')
      # Receives data and queries InfluxDB
    await consumer.disconnect(1000)  # Closes the WebSocket connection
    ```

    Methods:
    - connect(): Connects to the WebSocket.
    - disconnect(close_code): Closes the WebSocket connection with
    the given close code.
    - send(text_data): Placeholder method that does nothing.
    - receive(text_data): Parses the received JSON data, extracts the bucket,
    start time, and stop time, and calls the query_influxdb() method.
    - query_influxdb(bucket, start_time, stop_time):
    Queries the InfluxDB database using
    the provided bucket, start time, and stop time. Formats the query result
    and returns it as a dictionary.
    """

    async def connect(self):
        """
        Connects to the WebSocket and prints a connection message.
        """
        print("You are connected with web socket")
        await self.accept()

    async def disconnect(self, close_code):
        """
        Closes the WebSocket connection with the given close code
        and prints a disconnection message.

        Args:
        - close_code: The close code for the WebSocket connection.
        """
        print(f"WebSocket connection closed with code: {close_code}")
        return super().disconnect(close_code)

    async def send(self, text_data):
        """
        Placeholder method that does nothing.

        Args:
        - text_data: The text data to be sent.
        """
        pass

    async def receive(self, text_data):
        """
        Parses the received JSON data, extracts the bucket, start time,
        and stop time, and calls the query_influxdb() method.

        Args:
        - text_data: The received JSON data.
        """
        data = json.loads(text_data)
        bucket = data.get('bucket', 'test')
        start_time = data.get('start_time')
        stop_time = data.get('stop_time')

        result = await self.query_influxdb(bucket, start_time, stop_time)
        await self.send(text_data=json.dumps(result))

    async def query_influxdb(self, bucket, start_time, stop_time):
        """
        Queries the InfluxDB database using the provided bucket, start time,
        and stop time. Formats the query result and returns it as a dictionary.

        Args:
        - bucket: The InfluxDB bucket to query.
        - start_time: The start time for the query.
        - stop_time: The stop time for the query.

        Returns:
        - A dictionary containing the formatted query result.
        """
        try:
            client = InfluxDBClient(url=url, token=token, org=org)

            query = f"""
            from(bucket: "{bucket}")
            |> range(start: {start_time}, stop: {stop_time})
            |> filter(fn: (r) => r._measurement == "my_measurement")
            |> filter(fn: (r) => r._field == "temperature")
            |> group(columns: ["status"])
            |> last()
            """
            tables = client.query_api().query(query)

            # Format the result as needed
            result = [{
                'table': table.name,
                'records': [record.values for record in table.records]} for table in tables  # noqa
            ]
        except Exception as e:
            result = {
                'msg': e
            }
        return {'result': result}
