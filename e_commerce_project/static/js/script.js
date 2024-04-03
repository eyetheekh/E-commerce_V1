

$(document).ready(function () {
    console.log("scripts.js working");
    // Attach click event handler to logout link
    $('.logout').click(function (event) {
        // Prevent the default action of the link
        event.preventDefault();

        // Show an alert to confirm logout
        if (confirm('Are you sure you want to logout?')) {
            // If the user confirms, redirect to the logout URL
            window.location.href = $(this).attr('href');
        } else {
            // If the user cancels, do nothing
            return false;
        }
    });

    // Timer for alerts
    setTimeout(function () {
        $(".alert").alert("close");
    }, 5000);
});

