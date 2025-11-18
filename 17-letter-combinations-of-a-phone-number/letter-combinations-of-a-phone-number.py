class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        tus={2:("a","b","c"),3:("d","e","f"),
           4:("g","h","i"),5:("j","k","l"),6:("m","n","o"),
           7:("p","q","r","s"),8:("t","u","v"),9:("w","x","y","z")}
        
        if digits=="":
            return []
        if len(digits)==1:
            return list(tus[int(digits)])              
        else:
            harf=[tus[int(d)]  for d in digits ]
            com= product(*harf)

            return ["".join(k) for k in com]
