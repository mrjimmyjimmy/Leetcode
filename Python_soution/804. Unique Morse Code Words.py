class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        '''
        give two list, one is morse, one is alpha
        iterate string, find index in alpha and replace with morse
        '''

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]

        setMorse = set()
        for i in words:
            newWords = ''
            for j in i:
                newWords = newWords + morse[alpha.index(j)]
            setMorse.add(newWords)
        return len(setMorse)
