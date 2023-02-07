// Day 2: Loops (Even though I didn't even solve it with loops, lol)
/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vowels = ['a','e','i','o','u'];
    let str1 = Array.from(s).filter((word) => vowels.includes(word)).join('\n');
    let str2 = Array.from(s).filter((word) => !vowels.includes(word)).join('\n');
    console.log(str1.concat('\n', str2));
}
