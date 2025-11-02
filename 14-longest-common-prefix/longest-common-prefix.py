class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        x=strs[0]

        for i in strs[1:]:
           
           while not i.startswith(x):
               x=x[:-1]
               if not x:
                return ""
        return x       