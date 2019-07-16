package Two_pointers;

public class SumOfSquare_633 {
    public boolean judgeSquareSum(int c) {
        int min = 0;
        int max = (int) Math.sqrt(c);
        while(min <= max){
            int square = min*min + max*max;
            if(square == c){
                return true;
            } else if(square < c){
                min++;
            } else{
                max--;
            }
        }
        return false;
    }
}
