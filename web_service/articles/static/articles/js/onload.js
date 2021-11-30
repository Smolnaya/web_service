$(document).ready(function () {
    setLists();
});

function setLists() {
    $.ajax({
        url: 'get_topic',
        success: function (response) {
            var select = $('#topic-select').empty();
            select.append("<option value='' selected>Все</option>")
            for (const i in response.topics) {
                if (response.topics[i] !== '') {
                    select.append("<option value='" + response.topics[i] + "'>" + response.topics[i] + "</option>")
                }
            }
        },
        error: function (response) {
            console.log('failed to load the list of topics');
        }
    });
}