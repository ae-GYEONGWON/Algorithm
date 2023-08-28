function solution(n)
{
    var answer = 0;
    let str_n = n.toString()
    for (let i = 0; i<str_n.length; i++) {
        answer += parseInt(str_n[i])
    }

    return answer;
}