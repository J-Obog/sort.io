var counts = [];
var countingMarker = 0;
var fired = false;


function countingSort() {
	
if(!fired) { 
for(var i = 0;i<maxValue+1;i++) {
counts.push(0);
for(var j = 0;j<values.length;j++) {
if(values[j] == i) {
counts[counts.length-1] = counts[counts.length-1] + 1;
}
}
}
values = [];
fired = true;
}

for(var i = 0;i<counts.length;i++) {
for(var j = 0;j<counts[i];j++) {
values.push(countingMarker);
formBars();
}
countingMarker++;
}

}