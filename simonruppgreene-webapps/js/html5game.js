function clear() {
			canvas.clearRect(0,0, CANVAS_WIDTH, CANVAS_HEIGHT);
		}



window.onload = function() {
	var CANVAS_WIDTH = 480;
	var CANVAS_HEIGHT = 320;

	var canvasElement = $("<canvas width='" + CANVAS_WIDTH +
						  "' height='" + CANVAS_HEIGHT + "'></canvas>");
	var canvas = canvasElement.get(0).getContext("2d");
	canvasElement.appendTo('body');

	var FPS = 30;

	setInterval(function() {
		update();
		draw();
	}, 1000/FPS);

	function update() {
		clear();
	}

	function draw() {
		canvas.fillStyle = "#000";
		canvas.fillText("Sup.", 50,50);
	}
}