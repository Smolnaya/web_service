async function search() {
    getArticleData();
}

function getArticleData() {
    const local_store = storeToURL();
    $.ajax({
        url: 'search_articles?' + local_store,
        success: function (response) {
            draw_table(response);
        },
        error: function (response) {
            console.log('fail to draw the table');
        }
    });
}

function storeToURL() {
    return 'search=' + localStorage.getItem('search') + '&' +
        'sort=' + localStorage.getItem('sort') + '&' +
        'topic=' + localStorage.getItem('topic') + '&' +
        'dateFrom=' + localStorage.getItem('dateFrom') + '&' +
        'dateTo=' + localStorage.getItem('dateTo');
}

function setData() {
    $('#searchInput').val(localStorage.getItem('search'));
}

function updateLocalStore(key, value) {
    localStorage.setItem(key, value);
    search();
}

function clearFilters() {
    $('#dateTo').val('');
    document.getElementById("dateTo").setAttribute("min", '2021-08-01');
    $('#dateFrom').val('');
    document.getElementById("dateFrom").setAttribute("max", "2021-11-01");
    $('#searchInput').val('')
    document.getElementById('sort-selection').value="title";
    localStorage.setItem('dateFrom', '');
    localStorage.setItem('dateTo', '');
    localStorage.setItem('search', '');
    localStorage.setItem('topic', '');
    localStorage.setItem('sort', 'title');
    setLists();
    search();
}

document.addEventListener("DOMContentLoaded", () => {
    localStorage.setItem('search', '');
    localStorage.setItem('sort', 'title');
    localStorage.setItem('topic', '');
    localStorage.setItem('dateFrom', '');
    localStorage.setItem('dateTo', '');
    setData();
    getArticleData();
})

function do_date_to(key, value) {
    document.getElementById("dateFrom").setAttribute("max", value);
    updateLocalStore(key, value);
}

function do_date_from(key, value) {
    document.getElementById("dateTo").setAttribute("min", value);
    updateLocalStore(key, value);
}
