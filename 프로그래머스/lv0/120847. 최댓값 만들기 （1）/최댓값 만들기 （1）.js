function solution(numbers) {
    var answer = 0;
    
    numbers.sort(function (a, b) {
        if (a > b){
            return -1;
        } else if (b > a) {
            return 1;
        } else {
            return 0;
        }
    })
    
    return numbers[0]*numbers[1];
}