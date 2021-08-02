const chatSearchForm = $('.chat-search-form')
const sendMessageForm = $('#send-message')
const sendMessageButton = $('#send-button')

$(document).ready(() => {

    let csrfToken = $('input[name=csrfmiddlewaretoken]').val()

    chatSearchForm.submit(() => false).find('.search-button').click(() => {
        $.ajax({
            url: chatSearchForm.attr('action'),
            type: 'GET',
            data: {
                q: chatSearchForm.find('input[name="q"]').val()
            },
            success: response => {
                let htmlTemplate = ''

                let chats = response.chats;
                for (let chatId in chats) {
                    htmlTemplate += `<div class='chat-list search'><a href="${chats[chatId].slug}">${chats[chatId].name}</a></div>`
                }
                if (htmlTemplate.includes('undefined')) {
                    htmlTemplate = "<strong> По данному запросу не найденно подходящих результатов </strong>"
                }
                $('.chat-content').html(htmlTemplate);
            },
            error: error => {
                $('.chat-content').html("<strong> По данному запросу не найденно подходящих результатов </strong>");
            }
        })
    });

//     sendMessageButton.on('click', '.message-box', () => {
//         $.ajax({
//             url: '',
//             type: 'POST',
//             data: {
//                 'message-text': sendMessageForm.find('#id_message-text').val(),
//                 csrfmiddlewaretoken: csrfToken
//             },
//             success: response => {
//                 $('message').append(`<h1>${response.data}</h1>`)
//             }
//         })
//     })
});
