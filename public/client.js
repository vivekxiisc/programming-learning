
const socket = io();
const chatMsgs = document.getElementById('chat-messages');
const chatForm = document.getElementById('chat-form');
const msgInput = document.getElementById('msg');
const typingStatus = document.getElementById('typing-status');
const notify = new Audio('https://assets.mixkit.co/active_storage/sfx/2354/2354-preview.mp3');

let currentUser = "";
// --- Private Room Logic ---
const urlParams = new URLSearchParams(window.location.search);
const room = urlParams.get('room') || "GlobalRoom"; 

fetch('/get-user').then(res => res.json()).then(data => {
    currentUser = data.username;
    socket.emit('joinRoom', { username: currentUser, room });
}).catch(() => window.location.href = '/login.html');

// Typing logic
msgInput.addEventListener('keypress', () => {
    socket.emit('typing', { username: currentUser, room });
});

socket.on('displayTyping', (data) => {
    typingStatus.innerText = `${data.username} is typing...`;
    setTimeout(() => { typingStatus.innerText = ""; }, 2000);
});

chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (msgInput.value.trim()) {
        socket.emit('chatMessage', { username: currentUser, room, text: msgInput.value });
        msgInput.value = '';
    }
});

socket.on('message', (data) => {
    const div = document.createElement('div');
    const isMe = (data.username === currentUser);
    
    if (data.username === 'System') {
        div.className = 'system-event';
        div.innerHTML = `<span>${data.text}</span>`;
    } else {
        div.className = `msg-wrapper ${isMe ? 'sent-wrapper' : 'received-wrapper'}`;
        div.innerHTML = `
            <div class="msg ${isMe ? 'sent' : 'received'}">
                ${!isMe ? `<small><b>${data.username}</b></small><br>` : ''}
                ${data.text}
                <div class="time">${data.time} <span class="status">${isMe ? '✓' : ''}</span></div>
            </div>`;
        
        if (!isMe) {
            notify.play().catch(() => {});
            socket.emit('messageSeen', { room }); // Send seen status
        }
    }
    chatMsgs.appendChild(div);
    chatMsgs.scrollTop = chatMsgs.scrollHeight;
});

// Update Blue Ticks
socket.on('userSeenMessage', () => {
    document.querySelectorAll('.status').forEach(s => {
        s.innerText = '✓✓';
        s.classList.add('seen-tick');
    });
});