class Solution(object):
    def sortArrayByParity(self, A):
        b = []
        for a in A:
            if a % 2 == 0:
                b.append(a)
        for a in A:
            if a % 2 == 1:
                b.append(a)
        return b
