$(document).ready(function() {
	$("#years-range").on("input", updateInputYear);
	$("#years-range").on("change", getInfoOfYear);
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
	// Get info
    var request = $.ajax({
        url: "getInfoOfYear",   
        type: "POST",
        data: "{year: " + year + "}"
        dataType: "JSON"    
    });

    // Execute if successfull
    request.done(function(respuesta) {
    	console.log("success");       
    });

    // Execute if fails
    request.fail(function(jqXHR, textStatus) {
        console.log("fail");
    });
}