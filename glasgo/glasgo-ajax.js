$(document).ready(function() {
    $('#like_btn').click(function(){
        var post_numberVar;
        post_numberVar = $(this).attr('data-postnumber');

        $.get('/glasgo/like/',
            {'post_number': post_numberVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });
});
