function solution(k, tangerine) {
    var answer = 0;
    
    let countTangerine = {}
    tangerine.forEach(v=> {
        if (countTangerine[v] === undefined) {
            countTangerine[v] = 1
        } else {
            countTangerine[v] += 1
        }
    })
    // console.log(countTangerine)
    
const tangerineGroup = Object.entries(countTangerine).map(([key,value])=>({key,value}))    

    // console.log(tangerineGroup)
    tangerineGroup.sort((a,b) => b.value-a.value)
    // console.log(tangerineGroup)
    for (let i = 0; i<tangerineGroup.length; i++) {
        answer += 1
        k -= tangerineGroup[i].value
        if (k<=0) {
            break
        }
    }
    return answer;
}