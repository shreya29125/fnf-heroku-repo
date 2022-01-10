

function openStory(x){
    var storymodal = document.getElementById('stories_modal'+x)
    storymodal.style.display = 'block';
    console.log(x)
}

function closeStoryModal(x){
    document.getElementById('stories_modal'+x).style.display = 'none';
}

function moveStoryRight(x){
    document.getElementById('stories_modal'+x).style.display = 'none';
    x++;
    document.getElementById('stories_modal'+x).style.display = 'block';
}

function moveStoryLeft(x){
    document.getElementById('stories_modal'+x).style.display = 'none';
    x--;
    document.getElementById('stories_modal'+x).style.display = 'block';
}

function toggleComments(){
    if(document.getElementById('post-comments').style.display != 'block')
        document.getElementById('post-comments').style.display = 'block';
    else
    document.getElementById('post-comments').style.display = 'none';
}