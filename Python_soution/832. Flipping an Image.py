class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        '''
        iterate image to get each piexl
        invert each pixel
        replace 0 with 1'''
        a = []
        for image in A:
            image.reverse()
            b = [0 if x == 1 else 1 for x in image]


            a.append(b)
        return a

    '''
    google:
    1. how to replace elements in array
    2. array.invert() --- turns to be array.reverse()
    '''

        
