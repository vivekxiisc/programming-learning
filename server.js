const express = require('express');
const http = require('http');
const socketio = require('socket.io');
const path = require('path');
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const session = require('express-session');

const app = express();
const server = http.createServer(app);
const io = socketio(server);

mongoose.connect('mongodb+srv://vivek1308:951vivek@cluster0.wvflgtv.mongodb.net/vchat_db?retryWrites=true&w=majority&appName=Cluster0')
    .then(() => console.log('✅ DB Connected'))
    .catch(err => console.log('❌ DB Error:', err));

const User = mongoose.model('User', new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true }
}));

app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));
app.use(session({ secret: 'vchat-secret-key', resave: false, saveUninitialized: false }));

// server.js mein login route ko update karo
app.post('/login', async (req, res) => {
    try {
        const user = await User.findOne({ username: req.body.username });
        if (user && await bcrypt.compare(req.body.password, user.password)) {
            req.session.username = user.username;
            res.redirect('/room.html'); // <-- Yahan change kiya
        } else {
            res.send('Invalid Login! <a href="/login.html">Try Again</a>');
        }
    } catch (err) { res.status(500).send('Server Error'); }
});
app.get('/get-user', (req, res) => {
    if (req.session.username) res.json({ username: req.session.username });
    else res.status(401).json({ error: 'Not logged in' });
});

io.on('connection', (socket) => {
    let userData = {};

    socket.on('joinRoom', ({ username, room }) => {
        userData = { username, room };
        socket.join(room);
        io.to(room).emit('message', { username: 'System', text: `${username.toUpperCase()} JOINED` });
    });

    socket.on('chatMessage', (data) => {
        io.to(data.room).emit('message', { 
            username: data.username, 
            text: data.text, 
            time: new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) 
        });
    });

    // --- NEW: Typing Logic ---
    socket.on('typing', (data) => {
        socket.to(data.room).emit('displayTyping', data);
    });

    // --- NEW: Seen/Blue Tick Logic ---
    socket.on('messageSeen', (data) => {
        socket.to(data.room).emit('userSeenMessage');
    });

    socket.on('disconnect', () => {
        if (userData.username) {
            io.to(userData.room).emit('message', { username: 'System', text: `${userData.username.toUpperCase()} LEFT THE CHAT` });
        }
    });
});

server.listen(10000, () => console.log('🚀 Server running on Port 10000'));