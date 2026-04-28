const express = require('express');
const http = require('http');
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const session = require('express-session');
const app = express();
const server = http.createServer(app);

// 1. DATABASE
const mongoURI = "mongodb+srv://vivek1308:951vivek@cluster0.wvflgtv.mongodb.net/vchat?retryWrites=true&w=majority&appName=Cluster0";
mongoose.connect(mongoURI).then(() => console.log("✅ MongoDB Connected"));

// 2. USER MODEL
const User = mongoose.model('User', new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    password: { type: String, required: true }
}));

// 3. MIDDLEWARE
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));
app.use(session({ secret: 'vchat_secret', resave: false, saveUninitialized: true }));

// 4. AUTH ROUTES
app.post('/register', async (req, res) => {
    try {
        const hashedPassword = await bcrypt.hash(req.body.password, 10);
        const newUser = new User({ username: req.body.username, password: hashedPassword });
        await newUser.save();
        res.send("Account Created! <a href='/'>Login here</a>");
    } catch (err) { res.status(400).send("User already exists."); }
});

app.post('/login', async (req, res) => {
    const user = await User.findOne({ username: req.body.username });
    if (user && await bcrypt.compare(req.body.password, user.password)) {
        req.session.user = user.username;
        res.redirect('/chat.html');
    } else {
        res.status(401).send("Invalid Login. <a href='/'>Try Again</a>");
    }
});

// 5. SOCKET.IO (ROOMS & TYPING)
const io = require('socket.io')(server);
const users = {};

io.on('connection', socket => {
    socket.on('new-user-joined', data => {
        const room = data.room || 'Global';
        socket.join(room);
        users[socket.id] = { name: data.name, room: room };
        socket.to(room).emit('user-joined', data.name);
    });

    socket.on('send', message => {
        const user = users[socket.id];
        if(user) socket.to(user.room).emit('receive', { message, name: user.name });
    });

    socket.on('typing', name => {
        const user = users[socket.id];
        if(user) socket.to(user.room).emit('display-typing', name);
    });

    socket.on('disconnect', () => {
        const user = users[socket.id];
        if(user) {
            socket.to(user.room).emit('left', user.name);
            delete users[socket.id];
        }
    });
});

server.listen(10000, '0.0.0.0', () => console.log(`🚀 Server on port 10000`));