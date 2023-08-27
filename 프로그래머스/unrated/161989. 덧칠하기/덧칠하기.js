function solution(n, m, section) {
    var answer = 0;
    let painted = 0;
    
    for (let i = 0; i<section.length; i++) {
        let willPaint = section[i] + m - 1;
        if (painted < section[i]) {
            painted = willPaint
            answer += 1
        } else if (painted > section[i]){
            continue
        }
    }
    
    return answer;
}