var insertionMarker = 0;

function insertionSort() {
	
var traverse = insertionMarker;

while(values[traverse] < values[traverse - 1]) {
temp = values[traverse - 1];
values[traverse - 1] = values[traverse];
values[traverse] = temp;
traverse--;
}

insertionMarker++;
formBars();
}

