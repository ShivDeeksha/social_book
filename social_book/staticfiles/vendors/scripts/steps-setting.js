$(document).ready(function() {
    $(".tab-wizard").steps({
        headerTag: "h5",
        bodyTag: "section",
        transitionEffect: "fade",
        titleTemplate: '<span class="step">#index#</span> #title#',
        labels: {
            finish: "Submit"
        },
        onStepChanged: function(event, currentIndex, priorIndex) {
            $('.steps .current').prevAll().addClass('disabled');
        },
        onFinished: function(event, currentIndex) {
            // Collect form data
            var formData = new FormData($(".tab-wizard")[0]);
            
            // Append the upload_book field
            formData.append('upload_book', 'true');
            
            // Print each form field to the console (for debugging purposes)
            for (var pair of formData.entries()) {
                console.log(pair[0] + ': ' + pair[1]);
            }
            
            // Submit the form using Ajax
            $.ajax({
                url: $(".tab-wizard").attr("action"),  // Ensure form's action attribute is correctly set
                type: "POST",
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    if (response.success) {
                        window.location.href = response.redirect_url;  // Redirect on success
                    } else {
                        alert('Error: ' + response.message);  // Display error message
                    }
                },
                error: function(xhr, status, error) {
                    alert('Something went wrong. Please try again.');
                }
            });

            // Optionally, show a success modal if not redirecting
            // $('#success-modal').modal('show');
        }
    });
});


$(".tab-wizard2").steps({
	headerTag: "h5",
	bodyTag: "section",
	transitionEffect: "fade",
	titleTemplate: '<span class="step">#index#</span> <span class="info">#title#</span>',
	labels: {
		finish: "Submit",
		next: "Next",
		previous: "Previous",
	},
	onStepChanged: function(event, currentIndex, priorIndex) {
		$('.steps .current').prevAll().addClass('disabled');
	},
	onFinished: function(event, currentIndex) {
		$('#success-modal-btn').trigger('click');
	}
});