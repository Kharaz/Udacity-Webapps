window.onload = function() {
	var CANVAS_WIDTH = 480;
	var CANVAS_HEIGHT = 320;

	var x = 50;
	var y = 50;

	var vx = 5;
	var vy = 5;


	var canvasElement = $("<canvas width='" + CANVAS_WIDTH +
						  "' height='" + CANVAS_HEIGHT + "'></canvas>");
	var canvas = canvasElement.get(0).getContext("2d");
	canvasElement.appendTo('.canvasContainer');

	var FPS = 60;

	setInterval(function() {
		update();
		draw();
	}, 1000/FPS);

	function clear() {
			canvas.clearRect(0,0, CANVAS_WIDTH, CANVAS_HEIGHT);
		}

	function update() {
		clear();
		if (x > (CANVAS_WIDTH-20) || x < 0){
			vx = -vx;
		}

		if (y > (CANVAS_HEIGHT-20) || y < 20){
			vy = -vy;
		}

		x += vx;
		y += vy;

		draw(x,y);
	}

	function draw(x,y) {
		canvas.fillStyle = "#000";
		canvas.fillText("Sup.", x,y);
	}
}