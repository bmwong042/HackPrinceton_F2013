function Rect(xmin, ymin, xmax, ymax) {
	this.xmin = xmin;
	this.xmax = xmax;
	this.ymin = ymin;
	this.ymax = ymax;
}
var outerTable;
$( document ).ready(function() {
  	var elem = document.getElementById("test").getBoundingClientRect();
    outerTable = new Rect(elem.left, elem.bottom, elem.right, elem.top); 
    console.log(JSON.stringify(outerTable, null, 4));
});
  
var startPos = new Array();
var endPos = new Array();
var isMouseDown = false;
function intersects(pageRect, userRect) {
	  return pageRect.xmax >= userRect.xmin && pageRect.ymax <= userRect.ymin
            && userRect.xmax >= pageRect.xmin && userRect.ymax <= pageRect.ymin;
}
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
		if (startPos[0] <= endPos[0]) {
			rect.xmin = startPos[0];
			rect.xmax = endPos[0];
		}
		else {
			rect.xmin = endPos[0];
			rect.xmax = startPos[0];
		}
		if (startPos[1] >= endPos[1]) {
			rect.ymin = startPos[1];
			rect.ymax = endPos[1];
		}
		else {
			rect.ymin = endPos[1];
			rect.ymax = startPos[1];
		}


	}
	rect.setParams(startPos, endPos);
	console.log(JSON.stringify(rect, null, 4));
	alert(intersects(outerTable, rect));

	
};	
