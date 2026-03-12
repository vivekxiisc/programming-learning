
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