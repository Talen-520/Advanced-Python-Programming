$(document).ready(function () {
    $('#message-form').on('submit', function (e) {
        e.preventDefault();
        let message = $('#message').val();
        $('#chat-box').append(`<p>User: ${message}</p>`);
        $('#message').val('');

        $.ajax({
            type: 'POST',
            url: '/send_message',
            data: { message },
            success: function (data) {
                $('#chat-box').append(`<p>ChatGPT: ${data.response}</p>`);
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            },
        });
    });
});
