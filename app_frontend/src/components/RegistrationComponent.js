import React, { useState } from 'react';
import './RegistrationComponent.css';
import axios from 'axios';
import { Link, useNavigate} from 'react-router-dom';
import API_URLs from '../common';

const Registration = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [role, setRole] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    if (!name || !email || !password) {
      setError('All fields are required.');
      return;
    }

    if (!email.includes('@')) {
      setError('Invalid email format.');
      return;
    }

    if (password.length < 6 || !/[A-Z]/.test(password)) {
      setError('Password should be at least 6 characters long and contain one capital letter.');
      return;
    }

    try {
      const response = await axios.post(`http://127.0.0.1:8000/api/user/register/`, { name, email, password, role });
      console.log(response)
      localStorage.setItem("user",response)
      
      console.log(response)
    } catch (error) {
      console.error('Registration failed', error);
    }
  };

  return (
    <div className="registration-container">
      <h4 className='appname'>IOT Device Management platform</h4>
      <h2 className='signup-header'>Sign Up</h2>
      <form className="registration-form" method='POST'>
        <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
        <input type="text" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <input type="Role" placeholder="Role" value={role} onChange={(e) => setRole(e.target.value)} />
        <div className='button-style'>
          <button type="button" onClick={handleRegister}>Register</button>
        </div>
        {error && <p className="error-message">{error}</p>}
        <div className='switch-login'>
        <p>Already have an account?<Link to="/login"> Login </Link></p>
        </div>
      </form>
    </div>
  );
};

export default Registration;
