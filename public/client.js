const socket = io();
const form = document.getElementById('send-container');
const messageInput = document.getElementById('messageInp');
const messageContainer = document.querySelector(".container");
const typingDisplay = document.getElementById('typing-display');

// Private Room Logic
const urlParams = new URLSearchParams(window.location.search);
const room = urlParams.get('room') || 'Global';

const name = prompt(`Room: ${room}\nEnter your name:`);
socket.emit('new-user-joined', { name, room });

const append = (message, position) => {
    const el = document.createElement('div');
    el.innerText = message;
    el.classList.add('message', position);
    messageContainer.append(el);
    messageContainer.scrollTop = messageContainer.scrollHeight;
}

// Typing Indicator
messageInput.addEventListener('input', () => {
    socket.emit('typing', name);
});

socket.on('display-typing', (n) => {
    typingDisplay.innerText = `${n} is typing...`;
    setTimeout(() => { typingDisplay.innerText = ''; }, 2000);
});

socket.on('user-joined', n => append(`${n} joined`, 'left'));
socket.on('receive', d => append(`${d.name}: ${d.message}`, 'left'));
socket.on('left', n => append(`${n} left`, 'left'));

form.addEventListener('submit', (e) => {
    e.preventDefault();
    if(messageInput.value.trim()){
        append(`You: ${messageInput.value}`, 'right');
        socket.emit('send', messageInput.value);
        messageInput.value = '';
    }
});