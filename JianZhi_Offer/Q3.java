import java.lang.reflect.Array;
import java.util.Arrays;

public class Q3 {
	public static int nonDul(int[] input) {
		Arrays.sort(input);
		for(int i = 0; i < input.length; i++) {
			if(input[i] == input[i+1]) {
				return input[i];
			}
		}
		return -1;
	}
	
	public static void main(String[] args) {
		int[] i = {2,5,3,2,5,4,2,5,7,9,3,1,3,0};
		System.out.println(nonDul(i));
	}
}
