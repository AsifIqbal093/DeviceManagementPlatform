import React, { useState } from 'react';
import './LoginComponent.css'; 
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import API_URLs from '../common';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  
  const handleLogin = async (e) => {
    try {
      e.preventDefault();
      const response = await axios.post(`http://127.0.0.1:8000/api/user/login/`, { email, password });
      console.log(response)
      localStorage.setItem('accessToken', response.data.access);
      localStorage.setItem('refreshToken', response.data.refresh);
      navigate('/profile')
    } catch (error) {
      console.error('Login failed', error);
    }
  };

  return (
    <div className="login-container">
      <h4 className='appname'>IOT Device Management platform</h4>
      <h2 className='login-header'>Login</h2>
      <form className="login-form">
        <input type="text" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <div className='button-style'>
        <button onClick={handleLogin}>Login</button>
        </div>
        <div className='switch-login'>
        <p>Dont have an account?<Link to="/register"> Sign Up </Link></p>
        </div>
      </form>
    </div>
  );
};

export default Login;


