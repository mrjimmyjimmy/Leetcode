class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        find = False
        
        for i in range(len(nums)):
            if find == True:
                break
            else:  
                remain = target - nums[i]
                if remain in nums:
                    j = nums.index(remain) 
                    if not i == j:
                        indices.append(i)
                        indices.append(j)
                        find = True
        return indices
