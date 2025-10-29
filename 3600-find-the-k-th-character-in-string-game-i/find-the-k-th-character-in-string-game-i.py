class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        if 1 <= k <= 500:
        
            word=["a"]

            while len(word)<k:
           
              for ch in list(word):
                   if len(word)>=k:
                        break

                   word.append(change(ch))
            
            return word[k-1]
         
def change(x):
    
     return "a" if x=="z" else chr(ord(x)+1)        