// JavaScript to dynamically update floors and bathrooms based on building selection
document.getElementById('building').addEventListener('change', function() {
    document.getElementById('filterForm').submit();
});

document.getElementById('floor').addEventListener('change', function() {
    document.getElementById('filterForm').submit();
});

document.getElementById('gender').addEventListener('change', function() {
    document.getElementById('filterForm').submit();
});