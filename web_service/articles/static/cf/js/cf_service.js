function predict_topic() {
    var text = $('#text_area').val();
    $.ajax({
        url: 'predict_category',
        data: {'data_text': JSON.stringify(text)},
        dataType: 'json',
        success: function (response) {
            var topic = response['topic']
            var panel = $('#panel_row').empty();
            panel.append(
                "<div class=\"panel panel-primary\">" +
                "   <div class=\"panel-heading\">Предполагаемая категория:</div>" +
                "   <div class=\"panel-body\">" + topic +
                "</div></div>");
        },
        error: function (response) {
            console.log('failed to load the topic');
        }
    });
}

function clean_area() {
    var panel = $('#panel_row').empty();
    var text = $('#text_area').val('');
}