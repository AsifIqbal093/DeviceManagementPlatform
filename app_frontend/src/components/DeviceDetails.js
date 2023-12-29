import React from 'react';
import './DeviceDetails.css';

const DeviceDetails = ({ device, onClose }) => {

    return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={onClose}>&times;</span>
        <h2>Device Details</h2>
        <p><strong>ID:</strong> {device.id}</p>
        <p><strong>Name:</strong> {device.name}</p>
        <p><strong>Description:</strong> {device.description}</p>
      </div>
    </div>
  );
};

export default DeviceDetails;
