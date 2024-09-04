// api.js
import axiosInstance from '../api/axiosConfig';

// Check if frontend can connect to backend
export const healthCheck = async () => {
  return await axiosInstance.get('/api/healthcheck/')
};

// export const verifyEmail = async (token) => {
//   return await axiosInstance.get(`/api/auth/confirm/${token}`)
// };

export const updateStack = async (isEntry) => {
  return await axiosInstance.post('/api/update', {is_entry: isEntry});
};

