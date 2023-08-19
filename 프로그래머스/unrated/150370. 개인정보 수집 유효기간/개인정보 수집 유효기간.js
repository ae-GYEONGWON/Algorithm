function solution(today, terms, privacies) {
    var answer = [];
    
    today = today.split('.')
    for (let i = 0; i < privacies.length; ++i) {
        let temp_privacies = privacies[i].split(' ')
        for (let j = 0; j < terms.length; ++j) {
            let temp_terms = terms[j].split(' ')
            if ( temp_privacies[1] === temp_terms[0] ) {
                // console.log(temp_privacies[0], temp_terms[1])
                let temp_privacies_date = temp_privacies[0].split('.')
                let year = parseInt(temp_privacies_date[0]);
                let month = parseInt(temp_privacies_date[1]) + parseInt(temp_terms[1])
                let date = parseInt(temp_privacies_date[2])
                
                if (month > 12) {
                    year = parseInt(month/12) + year
                    month = month % 12
                    if (month === 0) {
                        month = 12
                        year--;
                    }
                }
                
                if (date === 1) {
                    month--;
                    date = 28
                    if (month === 0) {
                        month = 12
                        year--;
                    }
                } else {
                    date--;
                }

                // 이제 비교만 하면 됨.
                if (parseInt(today[0]) > year) {
                    answer.push(i+1)
                } else if (parseInt(today[0]) === year){
                    if (parseInt(today[1]) > month) {
                        answer.push(i+1)
                    } else if (parseInt(today[1]) === month) {
                        if (parseInt(today[2]) > date) {
                            answer.push(i+1)
                        }
                    }
                }
            }
        }
    }
    
    return answer;
}