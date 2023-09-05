function solution(id_list, report, k) {
    let reportIdsSet = {} // 신고한 사람과 신고 당한 사람을 객체로 저장
    let reportCountsSet = {} // 신고 당한 사람의 신고 당한 횟수 세어주기
    
    // 객체를 초기화
    id_list.forEach((id) => {
        reportIdsSet[id] = []
        reportCountsSet[id] = 0
    })
    
    // 주어진 입력(report)를 이용해 위에 초기환된 객체에 알맞게 저장.
    for(let i = 0; i<report.length; i++) {
        let [reporter, reported] = report[i].split(" ");
        if (!reportIdsSet[reporter].includes(reported)) {
            reportIdsSet[reporter].push(reported);
            reportCountsSet[reported]++
        }
    }
    
    // 신고 횟수가 k이상인 사람의 id추출
    const pauseIds = Object.entries(reportCountsSet).filter(([id, reportCount])=>reportCount >= k).map(([id, reportCount])=>id)
    
    // pauseIds에 해당하는 사람을 신고한 사람은 카운트해서 return해준다.
    const answer = id_list.map((id) =>{
        const reportIds = reportIdsSet[id]
        let reportCount = 0
        
        reportIds.forEach((reportId) => {
            if(pauseIds.includes(reportId)) {
                reportCount++
            }
        })
        return reportCount
    })
    
    return answer;
}