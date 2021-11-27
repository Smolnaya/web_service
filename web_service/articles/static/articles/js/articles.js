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
}

function clearFilters() {
    localStorage.setItem('dateFrom', '');
    localStorage.setItem('dateTo', '');
    $('#dateTo').val('');
    $('#dateFrom').val('');
    setLists();
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
