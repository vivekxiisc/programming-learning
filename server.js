const express = require('express');
const http = require('http');
const app = express();
const server = http.createServer(app);

// Socket.io initialization
const io = require('socket.io')(server, {
    cors: {
        origin: "*", 
    }
});

const PORT = process.env.PORT || 10000;
const users = {};

// Static files serve karne ke liye (agar aapka frontend isi folder mein hai)
app.use(express.static('public')); 

// Home route (Default page)
app.get('/', (req, res) => {
    res.send("<h1>Server is running!</h1>");
});

io.on('connection', socket => {
    // Jab koi naya user join kare
    socket.on('new-user-joined', name => {
        users[socket.id] = name;
        socket.broadcast.emit('user-joined', name);
    });

    // Jab koi message bheje
    socket.on('send', message => {
        socket.broadcast.emit('receive', { message: message, name: users[socket.id] });
    });

    // Jab koi chat chhod kar jaye
    socket.on('disconnect', () => {
        socket.broadcast.emit('left', users[socket.id]);
        delete users[socket.id];
    });
});

// Port '0.0.0.0' Render ke liye bahut zaroori hai
server.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 Server is running on port ${PORT}`);
});