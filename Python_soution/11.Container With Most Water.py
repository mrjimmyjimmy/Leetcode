class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        area = width * maxhight (L, R)
        """
        maxarea = 0
        for i in range(len(height) - 1):
            for j in range(len(height) - 1 - i):
                k = j + 1 + i
                width = k - i
                high = min(height[i], height[k])
                maxarea = max(maxarea, width * high)
        return maxarea
