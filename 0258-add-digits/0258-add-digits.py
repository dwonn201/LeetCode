class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            n = 0
            nums = [d for d in str(num)]
            for i in range(len(nums)):
                n += int(nums[i])
                num = n
        return num

        
            
            
        