import React from 'react';
import '../styles/components/ToggleSwitch.css';


const ToggleSwitch = ({ isDarkMode, onToggle }) => {
  return (
    <div className="mode-toggle">
      <label className="switch">
        <input type="checkbox" checked={isDarkMode} onChange={onToggle} />
        <span className="slider"></span>
      </label>
      {/* <span>{isDarkMode ? "Dark Mode" : "Light Mode"}</span> */}
    </div>
  );
};

export default ToggleSwitch;
