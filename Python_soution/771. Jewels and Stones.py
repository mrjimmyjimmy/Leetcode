class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        '''
        iterate J
        iterate S, find same element in S
        time n*n
        space n

        '''

        count = 0
        for j in J:
            for s in S:
                if j == s:
                    count += 1
        return count
            
        '''
        google for:
        1. count ++ --- count += 1
        '''
