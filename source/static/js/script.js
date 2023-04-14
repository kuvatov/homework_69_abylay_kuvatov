$(document).ready(function() {
    $('button').click(function() {
        let a = $('#a').val();
        let b = $('#b').val();
        let action = $(this).data('action');
        let url = action + '/';
        $.ajax({
            type: 'POST',
            url: url,
            data: JSON.stringify({'A': a, 'B': b}),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function(data) {
                $('#result').html(data['answer']).css('color', 'green');
            },
            error: function(xhr, textStatus, errorThrown) {
                $('#result').html(xhr.responseJSON['error']).css('color', 'red');
            }
        });
    });
    });