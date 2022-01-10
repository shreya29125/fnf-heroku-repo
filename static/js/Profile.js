function allposts(){
    document.getElementById('audio').style.display = "none";
    document.getElementById('all-post').style.display = "grid";
    document.getElementById('video').style.display = "none";
    document.getElementById('blogs').style.display = "none"; 
}

function audio(){
    document.getElementById('audio').style.display = "grid";
    document.getElementById('all-post').style.display = "none";
    document.getElementById('video').style.display = "none";
    document.getElementById('blogs').style.display = "none";
}

function video(){
    document.getElementById('audio').style.display = "none";
    document.getElementById('all-post').style.display = "none";
    document.getElementById('video').style.display = "grid";
    document.getElementById('blogs').style.display = "none"; 
}

function blog(){
    document.getElementById('audio').style.display = "none";
    document.getElementById('all-post').style.display = "none";
    document.getElementById('video').style.display = "none";
    document.getElementById('blogs').style.display = "grid"; 
}
