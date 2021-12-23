function template(data){
    let html = '';
    $.each(data, function(index, item){
        html +=
            "<tr style=\"padding: 10px\">"
            // + "<td>" + resp[i].id + "</td>"
            + "<td>" + item.title + "</td>"
            + "<td style='white-space: nowrap;'>" + item.publication_date + "</td>"
            + "<td>" + item.topic + "</td>"
            + "<td style=\"width: 150px\">" +
            "            <button type=\"button\"" +
            "                    class=\"btn btn-info btn-sm js-open-article\"" +
            "                data-url=\"" + item.id + "/open/\">" +
            "                <span class=\"glyphicon glyphicon-eye-open\"></span>" +
            "            </button>" +
            "            <button type=\"button\"" +
            "                    class=\"btn btn-warning btn-sm js-update-article\"" +
            "                    data-url=\"" + item.id + "/update/\">" +
            "                <span class=\"glyphicon glyphicon-pencil\"></span>" +
            "            </button>" +
            "            <button type=\"button\"" +
            "                    class=\"btn btn-danger btn-sm js-delete-article\"" +
            "                    data-url=\"" + item.id + "/delete/\">" +
            "                <span class=\"glyphicon glyphicon-trash\"></span>" +
            "            </button>" +
            "        </td>"
            + "</tr>"
    });
    return html;
}

function draw_table(resp) {
    const post_table = $('#post_table').empty();

    if (resp.length === 0) {
        post_table.append("<tr>" +
            "        <td colspan=\"8\" class=\"text-center bg-warning\">" +
            "Пусто, попробуйте сформулировать запрос по-другому</td>" +
            "    </tr>")
    } else
        $('#article_quantity').val("Статей: " + resp.length)
        $('#pagination-container').pagination({
            dataSource: resp,
            callback: function(data) {
                const html = template(data);
                post_table.html(html);
            }
        })
}
