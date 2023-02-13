// Day 8: Buttons Container
const incrementValue = document.querySelectorAll('#btns button').forEach((button) => {
    button.addEventListener('click', (e) => {
        rotation();
    });
});

var initialOrder = [1, 2, 3, 6, 9, 8, 7, 4];
var rotator = [1, 2, 3, 6, 9, 8, 7, 4];
function rotation() {
    initialOrder.unshift(initialOrder.pop());
    initialOrder.map((num, i) => {
        document.querySelector('#btn' + rotator[i]).innerHTML = initialOrder[i];
    });
}