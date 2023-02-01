// https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem
'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion(s) {
    // Write your code here
    let status = s.slice(-2) == 'PM';
    let hours = s.slice(0,2);
    if(status) { // Status is PM; status = true
        let time = hours == '12' ? '12' : (parseInt(hours) + 12).toString();
        return time + s.slice(2,-2); 
    }
    else { // Status is AM, undefined, ...; status = false
        let time = hours == '12' ? '00' : hours;
        return time + s.slice(2,-2);
    }
    
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const result = timeConversion(s);

    ws.write(result + '\n');

    ws.end();
}
