class Solution {
    public int solution(int hp) {
        int answer;
        int a=hp/5;
        int b=(hp-(a*5))/3;
        int c=(hp-(a*5)-(b*3))/1;
        answer=a+b+c;
        return answer;
    }
}