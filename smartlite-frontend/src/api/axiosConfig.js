import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://<raspberry_pi_ip>:5000/', // backend URL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default axiosInstance;
