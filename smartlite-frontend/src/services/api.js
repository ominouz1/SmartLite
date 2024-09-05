// api.js
import axiosInstance from '../api/axiosConfig';

// Check if frontend can connect to backend
export const healthCheck = async () => {
  return await axiosInstance.get('/api/healthcheck/')
};

export const getStatus = async () => {
  try {
    const response =  await axiosInstance.get('/status');
    return response.data;
  } catch (error) {
    console.error('Error fetching status:', error);
    throw error;
  }
};

export const toggleLight = async (status) => {
  try {
    const response =  await axiosInstance.post('/manual-toggle', status);
    return response.data;
  } catch (error) {
    console.error('Error toggling light:', error);
    throw error;
  }
};
