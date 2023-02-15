// Day 9: Binary Calculator

const buttons = document.querySelectorAll('button').forEach((button) => {
    button.addEventListener('click', (e) => {
        calculate(e.target.innerHTML);
        console.log('Clicked:', e.target.innerHTML);
    });
});



function calculate(operator) {
    switch(operator) {
        case 'C': {
            result.innerHTML = '';
            break;
        }
        case '=': {
            let convertion = result.innerHTML.replace(/(\d+)g/, (value) => parseInt(value, 2));

            result.innerHTML = eval(convertion).toString(2);
            break;
        }
        default: {
            result.innerHTML += operator;
            break;
        }
    }
}