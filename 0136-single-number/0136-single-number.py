class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        counts ={}
        for n in nums:
            if n in counts:
                counts[n]+=1
            else:
                counts[n]=1
        
        i = 0
        for number, count in counts.items():
            if count == 1:
                return number
        