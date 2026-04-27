const http = require('http').createServer();
const io = require('socket.io')(http, {
    cors: {
        origin: "*", // Kisi bhi website (Frontend) ko connect hone ki permission deta hai
    }
});

// const PORT = process.env.PORT || 8000; // Render ke liye PORT dynamic rakha hai
// const users = {};
const PORT = process.env.PORT || 10000;

server.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 Server is running on port ${PORT}`);
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

http.listen(PORT, () => {
    console.log(`🚀 Server is running on port ${PORT}`);
});