// word_counter.js
function countWords(str) {
    if (str.trim() === "") return 0;
    return str.trim().split(/\s+/).length;
}

let sentence = "  이것은 자바스크립트 문자열 예제입니다.  ";
console.log("입력된 문장:", sentence);
let count = countWords(sentence);
console.log("단어 수:", count);