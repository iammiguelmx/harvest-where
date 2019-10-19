$(document).ready(function() {
	$("#years-range").on("input", updateInputYear);
	$("#years-range").on("change", getInfoOfYear);

	init();
});

function updateInputYear() {
	// Get value
	var year = $(this).val();
	// Update year counter
	$("#current-year").html(year);
}

function getInfoOfYear() {
	// Get value
	var year = $(this).val();
	// Update year counter
	$("#current-year").html(year);
}

function init(){
	
}