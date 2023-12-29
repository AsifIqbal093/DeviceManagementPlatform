import React, { useEffect, useState } from 'react';
import './ProfileComponent.css';
// import DeviceComponent from './DeviceComponent';
import { Link } from 'react-router-dom';
import axios from 'axios';
import API_URLs from '../common';

const Profile = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('');
  const user = localStorage.getItem('user');
  const accessToken = localStorage.getItem('accessToken');
  // const roleInfo = {
  //   lev_operator: {
  //     title: 'LEV Operator',
  //     info: 'This is information for LEV Operators.',
  //   },
  //   lev_engineer: {
  //     title: 'LEV Engineer',
  //     info: 'This is information for LEV Engineers.',
  //   },
  //   lev_manager: {
  //     title: 'LEV Manager',
  //     info: 'This is information for LEV Managers.',
  //   },
  //   owner: {
  //     title: 'Owner',
  //     info: 'This is information for Owners.',
  //   },
  // };


   useEffect ( ()=>{
    const fetchData = async ()=>{
    const response = await axios.get(`http://127.0.0.1:8000/api/user/me/`,
      {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json', 
        },
      })
      console.log("response: ",response)
      setName(response?.data?.name);
      setEmail(response?.data?.email);
      setRole(response?.data?.role);
     }
    fetchData();
  },[])
  const [activeTab, setActiveTab] = useState('display'); 

   
  const handleEditProfile = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.patch(`http://127.0.0.1:8000/api/user/me/`, { name , email },
      {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json', 
        },
      }
      );
      console.log(response);
    } catch (error){
      console.error('Failed to edit device', error);
    }
  };

  const handleTabChange = (tab) => {
    setActiveTab(tab);
  };

  return (
    <div className="profile-container">
      <h4 className='app-name'>IOT_Device_Management_platform</h4>
      <header className="profile-header">
        {/* <h2>{title}</h2> */}
        <p>Role: {role}</p>
      </header>
      <div className="profile-tabs">
        <button
          className={activeTab === 'display' ? 'active' : ''}
          onClick={() => handleTabChange('display')}
        >
          Display Information
        </button>
        <button
          className={activeTab === 'editable' ? 'active' : ''}
          onClick={() => handleTabChange('editable')}
        >
          Editable Information
        </button>
        <button>
          <Link className="link-style" to='/profile/devices'>Devices</Link>
        </button>
      </div>
      <section className="profile-info">
        {activeTab === 'display' ? (
          <>
            <h3 className='sub-header'>Information</h3>
            <h3>{name}</h3>
            <h3>{email}</h3>
          </>
        ) : (
          <>
            <h3 className='sub-header'>Edit Information</h3>
            <form className='fields'>
              <label>Name:</label>
              <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
              <label>Email:</label>
              <input type="text" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
              <label>Role:</label>
              <input type="text" placeholder="Role" value={role} onChange={(e) => setRole(e.target.value)} />
              <div className='button-style'>
              <button type="submit" onClick={handleEditProfile }>Save</button>
              </div>
            </form>
          </>
        )}
      </section>
      {/* <Route path='/profile/devices' element={<DeviceComponent role={role}/>}/> */}
    </div>
  );
};

export default Profile;
