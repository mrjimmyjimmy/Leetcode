package Two_pointers;

public class TwoSum_167 {
	public int[] twoSum(int[] numbers, int target) {
		int min = 0;
		int max = numbers.length - 1;
		while(min < max) {
			int sum = numbers[min] + numbers[max];
			if(sum == target) {
				return new int[] {min+1, max+1};
			} else if(sum < target) {
				min++;
			} else {
				max--;
			}
		}
		return null;
	}
}
