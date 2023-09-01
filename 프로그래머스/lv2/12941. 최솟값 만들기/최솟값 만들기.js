function solution(A,B){
    A.sort((a,b)=>a-b)
    B.sort((a,b)=>b-a)
    let answer = A.reduce((acc,val,idx)=>acc+val*B[idx], 0)
    
    return answer;
}