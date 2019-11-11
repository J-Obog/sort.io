var looping = true; 
//var counting = 0;

function bubbleSort() {
	
var swaps = 0;

//bsMarker

for(var i = 0;i<values.length;i++) {
if(values[i] > values[i + 1]) {
temp = values[i + 1];
values[i + 1] = values[i];
values[i] = temp;
swaps = 1;
}
/*counting++;
console.log("Comparison : " + counting);*/
}


if(swaps == 0) {
looping = false;
}

//bsMarker--;

formBars();
}

