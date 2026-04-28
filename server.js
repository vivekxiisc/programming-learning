const express = require('express');
const http = require('http');
const socketio = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketio(server);

app.use(express.static(path.join(__dirname, 'public')));

io.on('connection', (socket) => {
    console.log('New connection detected');

    socket.on('joinRoom', ({ username, room }) => {
        socket.join(room); // User ko specific room mein daal diya
        
        // Welcome message sirf join karne wale ko
        socket.emit('message', { username: 'System', text: `Welcome to room: ${room}`, time: new Date().toLocaleTimeString() });

        // Dusron ko batana ki koi aaya hai (Sirf ussi room mein)
        socket.to(room).emit('message', { username: 'System', text: `${username} has joined the chat`, time: new Date().toLocaleTimeString() });
    });

    // Message sirf room ke andar bhejna
    socket.on('chatMessage', (data) => {
        io.to(data.room).emit('message', {
            username: data.username,
            text: data.text,
            time: new Date().toLocaleTimeString()
        });
    });

    socket.on('disconnect', () => {
        console.log('User left');
    });
});

const PORT = process.env.PORT || 10000;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));