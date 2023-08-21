function solution(slice, n) {
    var answer = 0;
    if (n%slice === 0){
        return parseInt(n/slice);
    } else {
        return parseInt(n/slice)+1;
    }
}