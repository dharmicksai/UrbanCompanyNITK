$(document).ready(function(e) {
	$('button#searchBtn').click(function(e) {
		if( ! document.getElementById('mySearch').value.length > 0 ) {
			$('.searchIcon input').toggleClass('searchBox');
		}
		else {
			$('#searchForm').submit();
		}
	});
});
