class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        '''
        2. remove all contains before '@'
        3. count string which does not have '+'
        '''
        setEmail = set()
        for item in emails:
            i = item.index('@')
            item_front = item[0:i]
            item_back = item[i+1:len(item)]
            if '+' in item_front:
                item_front = item_front[0:item_front.index('+')]
            if '.' in item_front:
                item_front = item_front.replace('.','')
            newItem = item_front + '@' + item_back
            setEmail.add(newItem)
            print newItem
        return len(setEmail)


    '''
    google for this one:
    1. string.contains('i') --- turn to be 'i' in string

    2. string.remove('i') --- turn to be string.replace('i', '')
    2.1 string in python is immutable, so string.replace is creating a new string not edit the old one
    
    3. set.append(i) --- set.add(i)

    30min past and have no answer
    '''

    """
    improvement:
    1. using string.split() to get thefront and the back of the string
    """
