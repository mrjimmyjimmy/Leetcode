class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        b = []
        for item in A:
            b.append(item * item)

        b.sort()

        return b
        
