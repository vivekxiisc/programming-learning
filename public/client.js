const socket = io();
const chatForm = document.getElementById('chat-form');
const chatMessages = document.getElementById('chat-messages');

// URL se Username aur Room ID nikalna
const urlParams = new URLSearchParams(window.location.search);
const username = urlParams.get('username');
const room = urlParams.get('room');

// Server ko join karne ka signal bhejna
socket.emit('joinRoom', { username, room });

// Message receive karna
socket.on('message', (message) => {
    const div = document.createElement('div');
    div.classList.add('message');
    div.innerHTML = `<p class="meta">${message.username} <span>${message.time}</span></p>
                    <p class="text">${message.text}</p>`;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
});

// Message bhejte waqt Room ID saath bhejna
chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const msg = e.target.elements.msg.value;

    socket.emit('chatMessage', {
        username: username,
        text: msg,
        room: room // Ye sabse important hai
    });

    e.target.elements.msg.value = '';
    e.target.elements.msg.focus();
});
