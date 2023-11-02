class Solution {
    public int[] solution(int[] arr) {
        
        if (arr.length-1 == 0) {
            int[] answer = new int[]{-1};
            return answer;
        }
        
        int min = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if (min > arr[i]) {
                min = arr[i];
            }
        }
        // System.out.println(min);
        int[] answer = new int[arr.length-1];
        int idx = 0;
        for (int num : arr) {
            if (num != min) {
                answer[idx++] = num;
            }
        }
        
        return answer;
    }
}