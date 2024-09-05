// api.js
import axiosInstance from '../config/axiosConfig';

// Check if frontend can connect to backend
export const healthCheck = async () => {
  return await axiosInstance.get('/api/healthcheck/')
};

export const verifyEmail = async (token) => {
  return await axiosInstance.get(`/api/auth/confirm/${token}`)
};

// Handle account creation
export const registerUser = async (userData) => {
  return await axiosInstance.post('/api/auth/register/', userData, { 
    headers: {
      'Content-Type': 'application/json'
    }
  });
};

export const registerAdmin = async (userData) => {
  return await axiosInstance.post('/api/auth/register/admin', userData, { 
    headers: {
      'Content-Type': 'application/json'
    }
  });
};

export const registerVendor = async (userData) => {
  return await axiosInstance.post('/api/auth/register/vendor', userData, { 
    headers: {
      'Content-Type': 'application/json'
    }
  });
};

export const registerCustomer = async (userData) => {
  return await axiosInstance.post('/api/auth/register/customer', userData, { 
    headers: {
      'Content-Type': 'application/json'
    }
  });
};


// handle authentication
export const loginUser = async (credentials) => {
  return await axiosInstance.post('/api/auth/login', credentials);
};

export const logoutUser = async () => {
  return await axiosInstance.post('/api/auth/logout');
};

export const confirmEmail = async (token) => {
  return await axiosInstance.get(`/api/auth/confirm/${token}`);
};

export const getUserProfile = async () => {
  const response = await axiosInstance.get('api/user/profile');
  return response.data.data;
};

export const requestPasswordReset = async (email) => {
  return await axiosInstance.post('/api/auth/password-reset', { email });
};

export const resetPassword = async (token, newPassword) => {
  return await axiosInstance.post(`/api/auth/password-reset/${token}`, { newPassword });
};

// Manage vendor products
export const addProduct = async (productId) => {
  return await axiosInstance.post(`/api/products/${productId}`);
};


// Manage customer products
export const searchProducts = async (query) => {
  return await axiosInstance.get(`/api/products/search?query=${query}`);
};

export const getAllProducts = async (page, sortValue = '', limit = 18 ) => {
  return await axiosInstance.get(`/api/products/?page=${page}&limit=${limit}&sortBy=${sortValue}`);
};

export const getNewArrivals = async (page, sortValue = '', limit = 18) => {
  return await axiosInstance.get(`/api/products/?page=${page}&limit=${limit}&sortBy=${sortValue ||'new'}`);
};

export const getFeaturedProducts = async (page, sortValue = '', limit = 18) => {
  return await axiosInstance.get(`/api/products/featured?page=${page}&limit=${limit}&sortBy=${sortValue}`);
};

export const getProduct = async (productId) => {
  return await axiosInstance.get(`/api/products/${productId}`);
};


//Handle wishlist
export const addToWishlist = async (productId) => {
  return await axiosInstance.post('/api/wishlist/add', { productId });
};

export const getWishlist = async () => {
  return await axiosInstance.get('/api/wishlist/');
};

export const removeFromWishlist = async (productId) => {
  return await axiosInstance.post('/api/wishlist/delete', { productId });
};

// Manage cart
export const addToCart = async (productId, quantity) => {
  return await axiosInstance.post('/api/cart/add', { productId, quantity });
};

export const getCartItems = async () => {
  return await axiosInstance.get('/api/cart/items');
};

export const removeFromCart = async (productId) => {
  return await axiosInstance.post('/api/cart/delete', { productId });
};

export const updateCartQuantity = async (productId, quantity) => {
  return await axiosInstance.post('/api/cart/update-quantity', { productId, quantity });
};


// Handle order
export const checkout = async () => {
  return await axiosInstance.post('/api/order/checkout')
};

export const verifyPayment = async (reference) => {
  return await axiosInstance.get(`/api/payment/verify?reference=${reference}`)
};
