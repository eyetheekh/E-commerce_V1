

$(document).ready(function () {
    console.log("scripts.js working");
    $(".owl-carousel").owlCarousel({
        loop: false,
        margin: 15,
        nav: false,
        autoplay: true,
        autoplayTimeout: 3000, // Set autoplay speed in milliseconds (e.g., 3000ms = 3 seconds)
        dots: false,
        responsive: {
            0: {
                items: 1, // Display 1 item on screens smaller than 600px
            },
            576: {
                items: 2, // Display 2 items on screens between 576px and 767px
            },
            768: {
                items: 3, // Display 3 items on screens between 768px and 991px
            },
            992: {
                items: 4, // Display 4 items on screens between 992px and 1199px
            },
            1200: {
                items: 6, // Display 6 items on screens larger than or equal to 1200px
            },
        },
    });
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

    // add to cart
    $(".add-to-cart-btn").click(function (e) {

        let addButton = $(this);
        console.log("add-to-cart-btn clicked");


        let id = addButton.attr('data-index');
        console.log("add-to-cart-btn : id :", id);



        let quantity = $("#no_of_quantity_"+id).val()
        console.log("quantity :", quantity);

        $.ajax({
            dataType: 'json',
            type: 'GET',
            url: '/add-to-cart',

            data: {
                "id": id,
                "quantity": quantity,

            },

            beforeSend: function () {
                console.log('trying to send data');
            },

            success: function (res) {
                console.log('data send');
                addButton.html("Added To Cart");
                console.log(res);
                no_of_items = res.no_of_cart_items;
                $(".cart-count").text(no_of_items);
            },

            error: function (response) {
                console.log(response)
            }
        });

    });

});


