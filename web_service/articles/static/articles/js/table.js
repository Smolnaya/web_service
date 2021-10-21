function draw_table(resp) {
    const post_table = $('#post_table').empty();

    if (resp.length === 0) {
        post_table.append("<tr>" +
            "        <td colspan=\"8\" class=\"text-center bg-warning\">" +
            "Пусто, попробуйте сформулировать запрос по-другому</td>" +
            "    </tr>")
    }
    for (const i in resp) {
        post_table.append("<tr style=\"padding: 10px\">"
            // + "<td>" + resp[i].id + "</td>"
            + "<td>" + resp[i].title + "</td>"
            + "<td style='white-space: nowrap;'>" + resp[i].author + "</td>"
            + "<td style='white-space: nowrap;'>" + resp[i].publication_date + "</td>"
            + "<td>" + resp[i].source + "</td>"
            + "<td>" + resp[i].tags + "</td>"
            + "<td style=\"width: 150px\">" +
            "            <button type=\"button\"" +
            "                    class=\"btn btn-info btn-sm js-open-article\"" +
            "                data-url=\"" + resp[i].id + "/open/\">" +
            "                <span class=\"glyphicon glyphicon-eye-open\"></span>" +
            "            </button>" +
            "            <button type=\"button\"" +
            "                    class=\"btn btn-warning btn-sm js-update-article\"" +
            "                    data-url=\"" + resp[i].id + "/update/\">" +
            "                <span class=\"glyphicon glyphicon-pencil\"></span>" +
            "            </button>" +
            "            <button type=\"button\"" +
            "                    class=\"btn btn-danger btn-sm js-delete-article\"" +
            "                    data-url=\"" + resp[i].id + "/delete/\">" +
            "                <span class=\"glyphicon glyphicon-trash\"></span>" +
            "            </button>" +
            "        </td>"
            + "</tr>");
    }
}
