
// getting audio player
let audioPlayer = document.getElementById("audioPlayer");

// selecting all song cards
let cards = document.querySelectorAll(".card");

// selecting play button
let playBtn = document.querySelector(".play");

// click song card
cards.forEach(function(card){

card.addEventListener("click", function(){

let song = card.getAttribute("data-song");
let title = card.querySelector("h4").innerText;
let artist = card.querySelector("p").innerText;
let img = card.querySelector("img").src;

audioPlayer.src = song;
audioPlayer.play();

// update bottom player
document.querySelector(".song-info h4").innerText = title;
document.querySelector(".song-info p").innerText = artist;
document.querySelector(".song-info img").src = img;


});

});


// play pause button
playBtn.addEventListener("click", function(){

if(audioPlayer.paused){

audioPlayer.play();
playBtn.classList.remove("fa-play-circle");
playBtn.classList.add("fa-pause-circle");

}

else{

audioPlayer.pause();
playBtn.classList.remove("fa-pause-circle");
playBtn.classList.add("fa-play-circle");

}

});
volume.addEventListener("click", function(){

audioPlayer.muted = !audioPlayer.muted;


});
let likeButtons = document.querySelectorAll(".like-btn");

likeButtons.forEach(function(btn){

btn.addEventListener("click", function(e){

e.stopPropagation();

let status = btn.nextElementSibling;

if(btn.innerText === "🤍"){

btn.innerText = "❤️";
status.innerText = "Liked";

}else{

btn.innerText = "🤍";
status.innerText = "Unliked";

}

});

});


let userIcon = document.getElementById("user")
let loginBox = document.getElementById("loginBox")

userIcon.addEventListener("click",function(){

if(loginBox.style.display === "block"){

loginBox.style.display="none";

}else{
    loginBox.style.display="block";

}

})
let loginBtn = document.getElementById("loginBtn")
let registerBtn = document.getElementById("registerBtn")

let loginForm = document.getElementById("loginForm")
let registerForm = document.getElementById("registerForm")

loginBtn.addEventListener("click",(e)=>{
e.stopPropagation;
loginForm.style.display = "block"
registerForm.style.display = "none"

})



/* register button */

registerBtn.addEventListener("click",()=>{

registerForm.style.display = "block"
loginForm.style.display = "none"

})

let loginSubmit = document.getElementById("loginSubmit")
let registerSubmit = document.getElementById("registerSubmit")

/* login submit */

loginSubmit.addEventListener("click",()=>{

loginForm.style.display = "none"

})


/* register submit */

registerSubmit.addEventListener("click",()=>{

registerForm.style.display = "none"

})
