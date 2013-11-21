
/* currently working on this part
var world = {
	CANVAS_WIDTH: 0,
	CANVAS_HEIGHT: 0,
	fps: 30,
	worldCanvas: null,
	objects: []
}

world.instantiate = function(width, height){
	world.CANVAS_WIDTH = width;
	world.CANVAS_HEIGHT = height;

	var canvasElement = $("<canvas width='" + world.CANVAS_WIDTH +
					      "' height='" + world.CANVAS_HEIGHT + "'></canvas>");

	worldCanvas = canvasElement.get(0).getContext("2d");
	canvasElement.appendTo('body');
}

world.step = function(){
	world.update();
	world.draw();
}

world.update = function(){

}
*/



window.onload = function() {
	var CANVAS_WIDTH = 480;
	var CANVAS_HEIGHT = 320;

	var canvasElement = $("<canvas width='" + CANVAS_WIDTH +
					      "' height='" + CANVAS_HEIGHT + "'></canvas>");
	var canvas = canvasElement.get(0).getContext("2d");
	canvasElement.appendTo('body');

	var FPS = 30;

	var vX = 2;
	var vY = 2;

	var textX = 50;
	var textY = 50;

	setInterval(function() {
		update();
		draw();
	}, 1000/FPS);

	function update() {
		if(textX > 460 || textX < 0){
			vX *= -1;
		}
		if(textY > 310 || textY < 10){
			vY *= -1;
		}

		textX+=vX;
		textY+=vY;
	}

	function clear() {
		canvas.clearRect(0,0, CANVAS_WIDTH, CANVAS_HEIGHT);
	}

	function draw() {
		clear()
		canvas.fillStyle = "#000";
		canvas.fillText("Sup.", textX, textY);
	}

}