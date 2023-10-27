class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        
        for (int i = 0; i<seoul.length; i++) {
            String item = seoul[i];
            if ("Kim".equals(item)) {
                return "김서방은 " + i + "에 있다";
            }
        }
        
        return answer;
    }
}