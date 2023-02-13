// Day 8: Create a Button
const incrementValue = document.querySelector('#btn').addEventListener('click', (e) => {
    let currentVal = Number(e.target.innerHTML)
    e.target.innerHTML = currentVal + 1;
});
