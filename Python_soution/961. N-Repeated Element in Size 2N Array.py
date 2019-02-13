class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        '''
        //1. iterate once to find duplicate elements
        //2. iterate again in this fupliate elements to find the repeat times == N

        its so fucing easy, only one of the element is repeating, so find it

        '''
        seen = []
        for i in A:
            if i in seen:
                return i
            else:
                seen.append(i)


        '''
        google for:
        1. array.remove(i) --- del array[i]
        '''
        
