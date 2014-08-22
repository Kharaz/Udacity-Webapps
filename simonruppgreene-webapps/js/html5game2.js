
var CANVAS_WIDTH = 480;
var CANVAS_HEIGHT = 320;

var canvasElement = $("<canvas width='"+CANVAS_WIDTH+"' height='"+CANVAS_HEIGHT+"'></canvas>");
var canvas = canvasElement.get(0).getContext("2d");

var fps = 30;

setInterval(mainLoop, 1000/fps);

function mainLoop(){
	update();
	draw();
}

function clearCanvas(){
	canvas.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
}

function update(){
	if(keydown.left){
		player.x -= 5;
	}
	if(keydown.right){
		player.x += 5;
	}
	if(keydown.space){
		player.shoot();
	}

	player.x = clamp(player.x, 0, CANVAS_WIDTH - player.width);
}

function clamp(val, min, max){
	if(val < min) return min;
	if(val > max) return max;
	return val;
}

function draw(){
	clearCanvas();
	player.draw();
}

var player = {
	color: "#00A",
	x: 200,
	y: 200,
	xV: 0,
	yV: 0,
	xVMax: 10,
	yVMax: 10,
	width: 32,
	height: 32,
	draw: function() {
		canvas.fillStyle = this.color;
		canvas.fillRect(this.x+this.xV, this.y+this.yV, this.width, this.height);
	},
	shoot: function(){
		console.log("bang");
	}
};

function bindKeyHandlers(){
  window.keydown = {};

  function keyName(event) {
    return jQuery.hotkeys.specialKeys[event.which] ||
        String.fromCharCode(event.which).toLowerCase();
  }

  $(document).bind("keydown", function(event) {
    keydown[keyName(event)] = true;
  });

  $(document).bind("keyup", function(event) {
    keydown[keyName(event)] = false;
  });
}

window.onload = function(){
	canvasElement.appendTo('.canvasContainer');
	bindKeyHandlers();
}
