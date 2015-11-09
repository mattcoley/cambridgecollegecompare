$(document).ready(function (){
	var college_table = $('#college_table').DataTable({
		"paging": false,
		"info": false,
		"scrollY" : "300px",
		"bScrollCollapse": true,
		"dom":' <"search"fl><"top">rt<"bottom"ip><"clear">'
	});

	$("#college_search").on("keyup search input paste cut", function() {
	   college_table.search(this.value).draw();
	});  
});
   