class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        num = 0
        new_nums = []
        for i in range(len(nums)):
            num += nums[i]
            new_nums.append(num)
        return new_nums
        