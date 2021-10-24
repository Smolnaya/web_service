$(document).ready(function () {
    setLists();
});

function setLists() {
    $.ajax({
        url: 'get_authors',
        success: function (response) {
            var select = $('#author-select').empty();
            for (const i in response.authors) {
                select.append("<option value='" + response.authors[i] + "'>" + response.authors[i] + "</option>")
            }
        },
        error: function (response) {
            console.log('failed to load the list of authors');
        }
    });

    $.ajax({
        url: 'get_source',
        success: function (response) {
            var select = $('#source-select').empty();
            for (const i in response.sources) {
                select.append("<option value='" + response.sources[i] + "'>" + response.sources[i] + "</option>")
            }
        },
        error: function (response) {
            console.log('failed to load the list of sources');
        }
    });
}