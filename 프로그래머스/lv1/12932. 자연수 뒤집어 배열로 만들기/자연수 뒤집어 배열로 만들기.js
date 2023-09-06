function solution(n) {
    var answer = [];
    
    n = n.toString()
    for (let i = n.length-1; i>-1; i--) {
        answer.push(parseInt(n[i]))
    }
    return answer;
}