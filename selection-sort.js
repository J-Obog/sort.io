var selectionMarker = 0;

function selectionSort() {
var a = selectionMarker;
var b = a + 1;

for(var i = 0;i<(values.length-selectionMarker)-1;i++) {

if(values[a]>values[b]) {
a = b;
b = a + 1;
} else {
a+=0;
b++
}

}


var temp = values[selectionMarker];
values[selectionMarker] = values[a];
values[a] = temp;

selectionMarker++;
formBars();

}

