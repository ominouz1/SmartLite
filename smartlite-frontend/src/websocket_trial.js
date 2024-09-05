const socket = io('http://localhost:5000');

socket.on('status_update', (data) => {
  console.log('Light status:', data.light_status ? 'ON' : 'OFF');
});
