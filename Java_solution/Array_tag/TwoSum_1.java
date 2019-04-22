package Array_tag;

public class TwoSum_1 {
    public int[] twoSum(int[] nums, int target) {
        int indexOne = 0;
        int indexTwo = 0;
        for(int i = 0; i < nums.length; i ++){
            for(int j = i + 1; j < nums.length; j ++){
                if (target == nums[i] + nums[j]){
                    // System.out.println("find");
                    indexOne = i;
                    indexTwo = j;
                }
            }
        }
        int[] index = {indexOne, indexTwo};
        return index;
    }
    
// iterate array, find j = traget - i
}
