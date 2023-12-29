# iot-device-management-platform

## Objective
Developed a RESTful API using Django and Django REST Framework to manage IoT devices,
incorporating PostgreSQL, InfluxDB or TimescaleDB for data storage, and implementing a
role-based access control system. Docker Containerization is used for api.

## Installation
Clone this api locall and run the below commands:
1. **Installation Command**
```
docker-compose build
```
2. **Running the Application**

```
docker-compose up
```
3. **Browsing the API Docs**
```
http:127.0.0.1:8000/api/docs
```


## API Endpoints
**Device Endpoints**
```
GET /api/device/device/{id}/
PUT /api/device/device/{id}/
PATCH /api/device/device/{id}/
DELETE /api/device/device/{id}/
```
These endpoint are only accessible by user having role as `lev_manager` and 'owner'


**Devices Endpoint**
```
GET /api/device/devices_list/
POST /api/device/devices_list/
```
User having roles `lev_manager`,`lev_engineer` and `lev_operator` will see list of all the devices while user having role as `owner` will see his owned devices list.

Schema
```
GET /api/schema/
```
This endpoint display **SCHEMA** of the API

User Endpoints
```
POST /api/user/login/
POST /api/user/login/refresh/
GET /api/user/me/
PUT /api/user/me/
PATCH /api/user/me/
POST /api/user/register/
```
All these endpoints are related to **user management** which can be used for `registration`, `login`, `Token Refresh`, `Profile` and `Updat Profile`.

# Front-End Application 
## Getting Started with React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:
### `npm install`
This will install all the dependencies for your project so you can all libraries.

### `npm start`
This will run your project on local server.
Project Description

### Routes
Route path="/" This is default route of application. This will route you to Login component.Route path="/login" This will route you to Login component.
Route path="/register" This will route you to Registration component
Route path="/profile" This will load profile component upon successful login or sign up.
Route path="/profile/devices" This is a tab in profiles tab to click on and show all Devices List.
Route path="/profile/devices/new" This opens a form to add new device
Route path="/profile/devices/edit/:deviceId" This opens a form to edit or update a device

### 1
Login Sign Up with specific role with authentication

### 2
Profile page which displays information and you can edit information from there then u can click on devices to see the devices related information

### 3
Being hiring manager you can add, edit and delete new devices while you can view information in other cases. 
