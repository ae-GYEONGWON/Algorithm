function solution(my_string) {
    var answer = '';
    let vowel = 'aeiou';
    let flag = false;
    for (let i = 0; i<my_string.length; ++i) {
        for (let j = 0; j<vowel.length; ++j) {
            if (my_string[i] === vowel[j]) {
                flag = true;
            }
        }
        if (flag === false) {
            answer += my_string[i]
        }
        flag = false;
    }
    
    return answer;
}