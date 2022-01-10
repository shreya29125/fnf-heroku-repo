 function play(thumbnail,caption,author,file) {
     var audio = document.getElementById("audio");
     var img = document.getElementById("audio_player_artist_img");
     var song_name = document.getElementById("song_name");
     var artist_name = document.getElementById("audio_artist");

     var modal = document.getElementById('playlist-modal');
     var modal_playing_song_img = document.getElementById("modal-playing-song-img");
     var modal_playing_song_album = document.getElementById('playing-song-Album'); 
     var modal_playing_song_artist = document.getElementById("playing-song-artist");
     var modal_song_name = document.getElementById('modal-song-name');

     modal.style.display = "flex";
     document.getElementById('audio_player').style.display = "flex";

         audio.src = file;
         img.src = thumbnail;
         song_name.innerHTML = caption;
         artist_name.innerHTML = author;
        
         modal_playing_song_img.src=thumbnail;
         modal_playing_song_album.innerHTML = 'Album1';
         modal_playing_song_artist.innerHTML = 'Shawn';
         modal_song_name.innerHTML = 'Streets';
    
    

    

   }
  
  function hide()
  {
      document.getElementById('playlist-modal').style.display = "none";
  }

 // function play()
 // {
 //     document.getElementById('audio_player').style.display = "flex";
 // }

   window.onclick = function(event) {
     var modal = document.getElementById('playlist-modal');
     if (event.target==modal) {
       modal.style.display = "none";
     }
   }

