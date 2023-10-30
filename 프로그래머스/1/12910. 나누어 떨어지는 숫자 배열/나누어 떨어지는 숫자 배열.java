import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int num : arr) {
            if (num % divisor == 0) {
                list.add(num);
            }
        }

        // divisor로 나누어 떨어지는 수가 하나도 없는 경우
        if (list.size() == 0) {
            return new int[] {-1};
        }

        // ArrayList를 배열로 변환
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        // 배열 정렬
        Arrays.sort(answer);
        
        return answer;
    }
}
