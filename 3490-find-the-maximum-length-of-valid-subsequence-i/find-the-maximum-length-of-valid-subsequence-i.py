class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_ev = sum(1 for i in nums if i%2==0)
        c_od = sum(1 for i in nums if i%2==1)

        c_max = max(c_ev,c_od)

        curl=1
        longest=1
       

        for i in range(1,len(nums)):
            if (nums[i]+nums[i-1])%2==1:
                curl+=1
                
                longest=max(curl,longest)
            else:
                continue
            
        return max(c_max,longest)