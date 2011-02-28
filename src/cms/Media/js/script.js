window.onload=function(){ 
    iconDraw("icon","Home");
}

function iconDraw(id,text){
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
        i.fillText(text,20,20);
    }
}