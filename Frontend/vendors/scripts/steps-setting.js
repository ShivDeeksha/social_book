document.addEventListener("DOMContentLoaded", function () {
    $(".tab-wizard").steps({
        headerTag: "h5",
        bodyTag: "section",
        transitionEffect: "fade",
        titleTemplate: '<span class="step">#index#</span> #title#',
        labels: {
            finish: "Submit"
        },
        onFinished: async function(event, currentIndex) {
            const accessToken = localStorage.getItem('access_token');
            if (!accessToken) {
                alert('Please log in again.');
                return;
            }

            const formData = new FormData($(".tab-wizard")[0]);

            // Format the publish date to YYYY-MM-DD if necessary
            const publishDate = formData.get('publish_date');
            if (publishDate) {
                // Assuming the date picker gives a date like "15 September 2009"
                const formattedDate = new Date(publishDate).toISOString().split('T')[0];
                formData.set('publish_date', formattedDate);
            }

            try {
                const response = await fetch($(".tab-wizard").attr("action"), {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${accessToken}`
                    },
                    body: formData
                });

                if (response.ok) {
                    const result = await response.json();
                    if (result.success) {
                        window.location.href = result.redirect_url;
                    } else {
                        alert('Error: ' + result.message);
                    }
                } else {
                    alert('Something went wrong. Please try again.');
                }
            } catch (error) {
                alert('An error occurred: ' + error.message);
            }
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