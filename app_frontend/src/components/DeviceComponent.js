import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './DeviceComponent.css';
import { Link, useNavigate } from 'react-router-dom';
import API_URLs from '../common';
import DeviceDetails from './DeviceDetails'; 


const DeviceComponent = () => {
  const [devices, setDevices] = useState([]);
  const [owner, setOwner] = useState('');
  const [selectedDevice, setSelectedDevice] = useState(null);
  const [isEdit,setIsEdit] = useState(false);
  const [isUpdate,setIsUpdate] = useState(false);
  const [editDevice, setEditDevice] = useState(null);
  const navigate = useNavigate();
  const accessToken = localStorage.getItem('accessToken');;

  
  const handleRowClick = (device) => {
    setSelectedDevice(device); 
  };

  const handleCloseModal = () => {
    setSelectedDevice(null); 
  };

  useEffect(() => {
    const fetchDevices = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/device/devices_list/`,{
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'Content-Type': 'application/json', 
          },
        })
        console.log(response)
        setDevices(response.data)
        
      } catch (error) {
        console.error('Error fetching devices', error);
      }
    };

    fetchDevices();
  }, []);

  const handleEdit = (deviceId, name, description) => {
    navigate(`/profile/devices/edit/${deviceId}`, {
      state: {
        isEdit: true,
        id: deviceId,
        name,
        description
      }
    });
  };
  

  const handleUpdate = (deviceId, name, description) => {
    setIsEdit(true);
    setIsUpdate(true); 
    setEditDevice({ id: deviceId, name, description });
    console.log(`Updating device with ID: ${deviceId}`);
  };

  const handleDelete = async (deviceId) => {
    // e.preventDefault();
    const response = await axios.delete(`http://127.0.0.1:8000/api/device/device/${deviceId}/`,{
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json', 
      },
    })
    navigate('/profile/devices');
    console.log(`Deleted device: ${response}`);
  };

const isAdmin = true;
  return (
    <>
      {selectedDevice && (
        <DeviceDetails device={selectedDevice} onClose={handleCloseModal} />
      )}
    <div className="device-container">
      <h2 className='login-header'>Devices</h2>
      {isAdmin && (
        <button className="action-button add-button"><Link to = '/profile/devices/new' style={{textDecoration: 'none', color: 'black'}}>Add New Device</Link></button>
      )}
      <div className="table-container">
      {devices.length > 0 ? ( 
        <table className="device-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Description</th>
              <th>Owner</th>
              {isAdmin && <th>Actions</th>}
            </tr>
          </thead>
          <tbody>
            {devices.map((device) => (
              <tr key={device.id} onClick={()=>handleRowClick(device)}>
                <td>{device?.id}</td>
                <td>{device?.device_name}</td>
                <td>{device?.description}</td>
                <td>{device?.owner}</td>
                {isAdmin && (
                  <td>
                    <button onClick={() => handleEdit(device.id,device.device_name,device.description)}>Edit</button>
                    {/* <button onClick={() => handleUpdate(device.id,device.name,device.description)}>Update</button> */}
                    <button onClick={() => handleDelete(device.id)}>Delete</button>
                  </td>
                )}
              </tr>
            ))}
          </tbody>
        </table>
         ) : (
          <p>Loading devices...</p>
        )}
      </div>
      
    </div>
    </>

  );
};

export default DeviceComponent;
