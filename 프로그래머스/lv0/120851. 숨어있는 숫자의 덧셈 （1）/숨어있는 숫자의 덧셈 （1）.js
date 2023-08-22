function solution(my_string) {
    var answer = 0;
    let temp_list = my_string.split("");
    temp_list.map(function(v) {
        const temp_num = Number(v)
        if (!isNaN(v)) {
            answer += temp_num
        }
    })
    
    return answer;
}