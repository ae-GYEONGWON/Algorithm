function solution(s) {
    var answer = '';
    let temp_list = s.split(" ");
    // console.log(temp_list)
    temp_list = temp_list.map(v=> parseInt(v))
    // console.log(temp_list)
    temp_list.sort((a,b)=>a-b)
    answer += temp_list[0].toString()
    answer += " "
    answer += temp_list[temp_list.length-1].toString()
    
    return answer;
}