// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/LoginComponent';
import Registration from './components/RegistrationComponent';
// import ProtectedRoute from './components/ProtectedRoute';
import ProfileComponent from './components/Profile';
import DeviceComponent from './components/DeviceComponent';
import AddDevice from './components/AddDevice';
import ProtectedRoute from './components/ProtectedRoute';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Registration />} />
        {/* <Route element={<ProtectedRoute/>}> */}
          <Route path="/profile" element={<ProfileComponent role="lev_engineer" info="this is owner" />}/>
          <Route path="/profile/devices" element={<DeviceComponent role="lev_engineer" />} />
          <Route path="/profile/devices/new" element={<AddDevice />} />
          <Route path="/profile/devices/edit/:deviceId" element={<AddDevice />} />
        {/* </Route> */}
      </Routes>
    </Router>
  );
};

export default App;