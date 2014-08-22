
function getCookieValue(name){
	var value = "; " + document.cookie;
	var parts = value.split("; "+name+"=");

	if (parts.length == 2) {
		return parts.pop().split(";").shift();
	}
}

//GREAT we can get the cookie...
//but we can't access the GQL database (for good reason)
//now what


//window.onload = function() {
var CANVAS_WIDTH = 480;
var CANVAS_HEIGHT = 320;

var canvasElement = $("<canvas width='" + CANVAS_WIDTH +
					  "' height='" + CANVAS_HEIGHT + "'></canvas>");

var x = 50;
var y = 50;

var vx = 5;
var vy = 5;

var FPS = 60;

//ctx is canvas context
function drawHexagon(ctx, position){
	ctx.beginPath();
	ctx.fillStyle="yellow";
	ctx.strokeStyle="black";
	ctx.moveTo(position[0], position[1]);
	ctx.lineTo(position[0]+25, position[1]);
	ctx.lineTo(position[0]+14+25, position[1]+22);
	ctx.lineTo(position[0]+25, position[1]+18+25);
	ctx.lineTo(position[0], position[1]+25+18);
	ctx.lineTo(position[0]-14, position[1]+22);
	ctx.lineTo(position[0], position[1]);
	ctx.stroke();
	ctx.fill();
}

function drawOctagon(ctx, position){
	ctx.beginPath();
	ctx.fillStyle="yellow";
	ctx.strokeStyle="black";

	var x = position[0];
	var y = position[1];

	ctx.moveTo(x,y);
	ctx.lineTo();
	

	ctx.stroke();
	ctx.fill();
}


function updateXY(){
	if (x > (CANVAS_WIDTH-20) || x < 0){
		vx = -vx;
	}
	if (y > (CANVAS_HEIGHT-20) || y < 20){
		vy = -vy;
	}
	x += vx;
	y += vy;

}

//var textString = "Hello";
function draw(canvas, x,y, textString) {
	canvas.fillStyle = "#000";
	canvas.fillText(textString, x,y);
	//console.log(x+","+y);
}	

/*
function draw(canvas, x,y) {
	canvas.fillStyle = "#000";
	canvas.fillText("Sup.", x,y);
}
*/

function clear(canvas) {
		canvas.clearRect(0,0, CANVAS_WIDTH, CANVAS_HEIGHT);
}	

//update canvans
function update(canvas, text) {
	clear(canvas);
	updateXY();
	draw(canvas, x,y, text);
	drawHexagon(canvas, [50,50]);
}


window.onload = function() {
	var textString = $("#html5text").text();
	var canvas = canvasElement.get(0).getContext("2d");
	canvasElement.appendTo('.canvasContainer');

	setInterval(function() { //what to call every frame
		update(canvas, textString);
		//draw();
	}, 1000/FPS);
}