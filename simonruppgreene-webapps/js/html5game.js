window.onload = function() {
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

	var CANVAS_WIDTH = 480;
	var CANVAS_HEIGHT = 320;

	var x = 50;
	var y = 50;

	var vx = 3;
	var vy = 4;


	var canvasElement = $("<canvas width='" + CANVAS_WIDTH +
						  "' height='" + CANVAS_HEIGHT + "'></canvas>");
	var canvas = canvasElement.get(0).getContext("2d");
	canvasElement.appendTo('.canvasContainer');

	//var textString = "bob";
	var textString = $("#html5text").text();

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
		canvas.fillText(textString, x,y);
	}
}