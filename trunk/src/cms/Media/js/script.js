window.onload=function() { 
    iconDraw("icon");
    iconDraw("weekends");
    iconDraw("forms");
    iconDraw("inspections");
    iconDraw("personalInformation");
}

/**
 * iconDraw(id)
 * draws icon white background, black text
 * @param id
*/
function iconDraw(id) {
    var icon=document.getElementById(id);
    if(icon.getContext) {
        var ctx=icon.getContext("2d");
        ctx.fillStyle="#000000";
        ctx.beginPath();
        ctx.arc(20,20,20,0,Math.PI*2,true);
        ctx.closePath();
        ctx.fill();
        
        ctx.shadowOffsetX=2;
        ctx.shadowOffsetY=2;
        ctx.shadowBlur=5;
        ctx.shadowColor="#666";
        
        ctx.fillStyle="#FFFFFF";
        ctx.font="6pt sans-serif";
        ctx.textAlign="center";
        
        var words = getLines(ctx, icon.title, 35, ctx.font);
        var spacing = new Array(4);
        spacing[0]=[20];
        spacing[1]=[15,25];
        spacing[2]=[10,20,30];
        spacing[3]=[5,15,25,35];

        for( var i = 0; i<words.length; i++ ){
            var y = spacing[words.length-1][i];
            ctx.fillText(words[i],20,y);
        }

    }
}

/**
 * iconHighlight(id)
 * draws icon white background, black text
 * @param id
*/
function iconHighlight(id) {
    var icon=document.getElementById(id);
    if(icon.getContext) {
        var ctx=icon.getContext("2d");
        ctx.fillStyle="#FFFFFF";
        ctx.beginPath();
        ctx.arc(20,20,20,0,Math.PI*2,true);
        ctx.closePath();
        ctx.fill();
        
        ctx.shadowOffsetX=2;
        ctx.shadowOffsetY=2;
        ctx.shadowBlur=5;
        ctx.shadowColor="#666";
        
        ctx.fillStyle="#000000";
        ctx.font="regular 6px sans-serif";
        ctx.textAlign="center";
        
        //Parse to fit text
        var words = getLines(ctx, icon.title, 35, ctx.font);
        var spacing = new Array(4);
        spacing[0]=[20];
        spacing[1]=[15,25];
        spacing[2]=[10,20,30];
        spacing[3]=[5,15,25,35];

        for( var i = 0; i<words.length; i++ ){
            var y = spacing[words.length-1][i];
            ctx.fillText(words[i],20,y);
        }
    }
}

/**
 * Divide an entire phrase in an array of phrases, all with the max pixel length given.
 * @param phrase
 * @param length
 * @return
*/
function getLines(ctx,phrase,maxPxLength,textStyle) {
    var words=phrase.split(" "),
        phraseArray=[],
        lastPhrase="",
        l=maxPxLength,
        measure=0;
        ctx.font = textStyle;

    for (var i=0;i<words.length;i++) {
        var word=words[i];
        measure=ctx.measureText(lastPhrase+word).width;
        if (measure<l) {
            lastPhrase+=(" "+word);
        }else {
            phraseArray.push(lastPhrase);
            lastPhrase=word;
        }
        if (i==words.length-1) {
            phraseArray.push(lastPhrase);
            break;
        }
    }
    return phraseArray;
}

/**
 * iconSlider(id, buttonid)
 * toggles elements of id
 * @param id
 * @param buttonid
*/
function iconSlider(id, buttonid){
        var icon = document.getElementById(buttonid);
        var icon_menu = document.getElementById(id);
        if(icon_menu.style.display=="none") {
            icon_menu.style.display="block";
        } else {
            icon_menu.style.display="none";
        }
        $(".menu").each(function(){
            if(this!=icon_menu) this.style.display="none";
        })
}