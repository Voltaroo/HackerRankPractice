// https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
    // Write your code here
    let plus = arr.filter((num) => num > 0).length;
    let minus = arr.filter((num) => num < 0).length;
    let zeros = arr.filter((num) => num == 0).length;
    console.log(`${(plus/arr.length).toFixed(6)}\n${(minus/arr.length).toFixed(6)}\n${(zeros/arr.length).toFixed(6)}`);
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
