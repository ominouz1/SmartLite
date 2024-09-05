import React from 'react';

const LightsStatus = ({ status }) => {
  return (
    <div className="lights-status">
      <p>Lights are <span className={status ? 'on' : 'off'}>{status ? 'On' : 'Off'}</span></p>
    </div>
  );
};

export default LightsStatus;
