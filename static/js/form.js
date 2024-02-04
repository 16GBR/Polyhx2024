// Update output elements with current slider values
document.addEventListener('input', function(event) {
    if (event.target.tagName.toLowerCase() === 'input' && event.target.type === 'range') {
        var output = event.target.nextElementSibling;
        output.value = event.target.value;
    }
});