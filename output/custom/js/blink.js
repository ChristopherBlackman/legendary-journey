/*
 * author: Christopher Blackman 
 * description: makes an element visible and invisible by toggle of the css
 */

var img_console = document.getElementById("img_console");
blink(img_console, 1000);

function blink(theDocument,time){
	var isHidden = true
	
	function toggle(){
		if(isHidden){
			theDocument.style.visibility = "hidden";
		}
		else{
			theDocument.style.visibility = "visible";
		}
		isHidden = !isHidden;
	}
	
	setInterval(toggle,time);
}