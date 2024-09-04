import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import ToggleSwitch from '../components/ToggleSwitch';
import LightsStatus from '../components/LightsStatus';
import PeopleCount from '../components/PeopleCount';
import axios from '../api/axiosConfig';
import lightOn from '../assets/images/light-on.png'
import lightOff from '../assets/images/light-off.png'

const Home = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [method, setMethod] = useState("");
  const [lightsStatus, setLightsStatus] = useState(false);
  const [peopleCount, setPeopleCount] = useState(0);

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
    document.body.classList.toggle('dark-mode');
  };

  // useEffect(() => {
  //   // Fetch initial data
  //   axios.get('/status').then(response => {
  //     setLightsStatus(response.data.lightsStatus);
  //     setPeopleCount(response.data.peopleCount);
  //   });
  // }, []);

  // const toggleLights = () => {
  //   axios.post('/toggle-lights', { status: !lightsStatus })
  //     .then(response => {
  //       setLightsStatus(response.data.lightsStatus);
  //     });
  // };

  return (
    <div className={`home-container ${isDarkMode ? 'dark-mode' : 'light-mode'}`}>
      <Header />
      <ToggleSwitch isDarkMode={isDarkMode} onToggle={toggleDarkMode} />
      <div className='image-container'>
        <img src={lightsStatus ? lightOn : lightOff} alt="" className='my-image'/>
      </div>
      <LightsStatus status={lightsStatus} />
      <button onClick={() => {
        setLightsStatus(!lightsStatus)
        setMethod("Manually")
      }} className="toggle-button">
        {lightsStatus ? 'Turn Off Lights' : 'Turn On Lights'}
      </button>
      <PeopleCount count={peopleCount} />
      <p>Method: {method}</p>
    </div>
  );
};

export default Home;
