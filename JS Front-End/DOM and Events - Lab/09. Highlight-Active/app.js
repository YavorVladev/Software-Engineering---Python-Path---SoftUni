function focused() {
    let inputs = document.querySelectorAll('input');
    for (let input of inputs) {
        input.addEventListener("focus", focusHandler);
        input.addEventListener('blur', blurHandler);
    }

    function focusHandler(event) {
        let parentDiv = event.target.parentNode;
        parentDiv.classList.add('focused');
    }

    function blurHandler(event) {
        let parentDiv = event.target.parentNode;
        parentDiv.classList.remove('focused');
    }
}