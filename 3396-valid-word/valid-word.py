import re
class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            return False
        if not re.match(r'^[A-Za-z0-9]+$', word):
            return False

        if not re.search(r'[aeiouAEIOU]', word):
            return False
        if not re.search(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', word):
            return False
        
        return True