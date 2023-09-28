# def solution(sequence, k):
#     answer = []
#     subseq_len = 1000000
    
#     for i, v in enumerate(sequence):
#         subseq_sum = 0
#         next_idx = i
#         while next_idx < len(sequence):
#             subseq_sum += sequence[next_idx]
#             if subseq_sum == k:
#                 if subseq_len > next_idx-i+1:
#                     answer = [i, next_idx]
#                     subseq_len = next_idx-i+1
#             elif subseq_sum > k:
#                 break
#             next_idx += 1
    
#     return answer


def solution(sequence, k):
    answer = [0, 0]
    ans_len = 1000001
    
    start = 0; end = 0
    subseq_sum = sequence[0]
    while start < len(sequence) and end < len(sequence):
        if subseq_sum == k:
            if ans_len > end-start+1:
                ans_len = end-start+1
                answer[0] = start; answer[1] = end
            subseq_sum -= sequence[start]
            start += 1; end += 1
            if end < len(sequence):
                subseq_sum += sequence[end]
        elif subseq_sum > k:
            subseq_sum -= sequence[start]
            start += 1
        else:
            end += 1
            if end < len(sequence):
                subseq_sum += sequence[end]        
    
    return answer