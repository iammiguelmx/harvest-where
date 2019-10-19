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

	$.ajax({
	    type:"POST", // la variable type guarda el tipo de la peticion GET,POST,..
	    url:"getInfoOfYear", //url guarda la ruta hacia donde se hace la peticion
	    data: JSON.stringify({year: year}), // data recive un objeto con la informacion que se enviara al servidor
	    contentType: "application/json; charset=utf-8",
	    success:function(){ //success es una funcion que se utiliza si el servidor retorna informacion
	         console.log("success")
	     },
	    dataType: 'json' // El tipo de datos esperados del servidor. Valor predeterminado: Intelligent Guess (xml, json, script, text, html).
	})
}