class Solution {
    public int solution(int n, String control) {
        int answer = 0;
        
        for (int i = 0; i<control.length(); i++) {
             char currentChar = control.charAt(i);
            
            if (currentChar == 'w') {
                n += 1;
            } else if (currentChar == 's') {
                n -= 1;
            } else if (currentChar == 'd') {
                n += 10;
            } else if (currentChar == 'a') {
                n -= 10;
            }
        }
        
        return n;
    }
}