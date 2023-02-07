// Day 2: Conditional Statements: Switch
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    // Write your code here
    switch(true) {
        case (/a|e|i|o|u/).test(s[0]): {
            letter = 'A';
            break;
        }
        case (/b|c|d|f|g/).test(s[0]): {
            letter = 'B';
            break;
        }
        case (/h|j|k|l|m/).test(s[0]): {
            letter = 'C';
            break;
        }
        case (/n|p|q|r|s|t|u|v|w|x|y|z/).test(s[0]): {
            letter = 'D';
            break;
        }
        default: {
            console.log('Error!');
            break;
        }
    }
    
    return letter;
}

