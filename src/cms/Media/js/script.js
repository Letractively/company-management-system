window.onload=function() { 
    iconDraw("icon");
    iconSlider();
}

function iconDraw(id) {
    var icon=document.getElementById(id);
    if(icon.getContext) {
        var i=icon.getContext("2d");
        i.fillStyle="#000000";
        i.beginPath();
        i.arc(20,20,20,0,Math.PI*2,true);
        i.closePath();
        i.fill();
        
        i.shadowOffsetX=2;
        i.shadowOffsetY=2;
        i.shadowBlur=5;
        i.shadowColor="#666";
        
        i.fillStyle="#FFFFFF";
        i.textAlign="center";
        i.fillText(icon.title,20,20);
    }
}

function iconHighlight(id) {
    var icon=document.getElementById(id);
    if(icon.getContext) {
        var i=icon.getContext("2d");
        i.fillStyle="#FFFFFF";
        i.beginPath();
        i.arc(20,20,20,0,Math.PI*2,true);
        i.closePath();
        i.fill();
        
        i.shadowOffsetX=2;
        i.shadowOffsetY=2;
        i.shadowBlur=5;
        i.shadowColor="#666";
        
        i.fillStyle="#000000";
        i.textAlign="center";
        i.fillText(icon.title,20,20);
    }
}

function iconSlider(){
    $("canvas.icon").click(
    function() {
        $("ul.menu").slideToggle("medium");
    });
}