window.onload = function () {
    $('.basket_list input[type="number"]').on('click', function(event) {
        $.ajax({
            url: "/basket/edit/" + event.target.name + "/" + event.target.value + "/",
            success: function (data) {
                $('.basket_list').html(data);
            },
        });
    });
}