import React, { useState, useEffect } from 'react';
import './DeviceComponent.css'; 
import axios from 'axios';
import { useNavigate, useLocation } from 'react-router-dom';
import API_URLs from '../common';

const AddDevice = () => {
  const [deviceName, setDeviceName] = useState('');
  const [deviceDescription, setDeviceDescription] = useState('');
  const navigate = useNavigate();
  const accessToken = localStorage.getItem('accessToken');
  const location = useLocation();
  const { isEdit, id, name: initialName, description: initialDescription } = location.state || {};

  useEffect(() => {
    if (isEdit) {
      setDeviceName(initialName || '');
      setDeviceDescription(initialDescription || '');
    }
  }, [isEdit, initialName, initialDescription]);

  const handleAddDevice = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`http://127.0.0.1:8000/api/device/devices_list/`, { device_name: deviceName, description: deviceDescription },
      {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json', 
        },
      }
      );
      console.log(response);
      navigate('/profile/devices');
    } catch (error) {
      console.error('Failed to add device', error);
    }
  };

  const handleEditDevice = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.patch(`http://127.0.0.1:8000/api/device/device/${id}/`, { id, device_name: deviceName, description: deviceDescription },
      {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json', 
        },
      }
      );
      console.log(response);
      navigate('/profile/devices');
    } catch (error){
      console.error('Failed to edit device', error);
    }
  };

  const handleUpdateDevice = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.put(`http://127.0.0.1:8000/api/device/${id}/`, { id, device_name: deviceName, description: deviceDescription },
      {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json', 
        },
      });
      console.log(response);
      navigate('/profile/devices');
    } catch (error){
      console.error('Failed to update device', error);
    }
  };

  return (
    <div className="login-container">
      <h4 className='appname'>IOT Device Management platform</h4>
      <h2 className='login-header'>{isEdit ? 'Edit Device' : 'Add Device'}</h2>
      <form className="login-form">
        <input type="text" placeholder="Name" value={deviceName} onChange={(e) => setDeviceName(e.target.value)} />
        <input type="text" placeholder="Description" value={deviceDescription} onChange={(e) => setDeviceDescription(e.target.value)} />
        <div className='button-style'>
          {(!isEdit) && <button onClick={handleAddDevice}>Add Device</button>}
          {/* {(!isEdit && isUpdate) && <button onClick={handleUpdateDevice}>Update Device</button>} */}
          {(isEdit ) && <button onClick={handleEditDevice}>Edit Device</button>}
        </div>
      </form>
    </div>
  );
};

export default AddDevice;
