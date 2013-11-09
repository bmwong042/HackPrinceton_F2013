var startPos = new Array();
var endPos = new Array();
var isMouseDown = false;
document.onmousedown = function(e) { 
	isMouseDown = true;
	startPos[0] = e.pageX;
	startPos[1] = e.pageY;

};
document.onmouseup   = function(e) { 
	isMouseDown = false;
	endPos[0] = e.pageX;
	endPos[1] = e.pageY; 
	var rect = new Object();
	rect.setParams = function(startPos, endPos) {
		if (startPos[0] < endPos[0]) {
			rect.xmin = startPos[0];
			rect.xmax = endPos[0];
		}
		else {
			rect.xmin = endPos[0];
			rect.xmax = startPos[0];
		}
		if (startPos[1] < endPos[1]) {
			rect.ymin = startPos[1];
			rect.ymax = endPos[1];
		}
		else {
			rect.ymin = endPos[1];
			rect.ymax = startPos[1];
		}


	}
	rect.setParams(startPos, endPos);
	rect.getParams = function() {
		return "xmin: " + rect.xmin + " xmax: " + rect.xmax + " ymin: " + rect.ymin + " ymax: " + rect.ymax; 
	}
	alert(rect.getParams());
};	
