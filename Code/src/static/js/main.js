$(document).ready(function() {

	$('.burger').click(function(){
		$('header').toggleClass('clicked');
	});

	$('nav ul li').click(function(){
		$('nav ul li').removeClass('selected');
		$('nav ul li').addClass('notselected');
		$(this).toggleClass('selected');
		$(this).removeClass('notselected');
	});

	$('#submit_addRoom').click(function(){
		$.ajax({
			data: {
				name: $('#name').val(),
				seat_capacity: $('#seat_capacity').val(),
			},
			type: "POST",
			url: "/addRoom"
		})
		.done(function(data){
			if (data.error) {
				$('#errorAlert').text('ERROR').show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}
		});
	});
	
});