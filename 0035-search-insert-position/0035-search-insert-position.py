class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[0] > target:
                return 0
            elif nums[i] == target:
                return i
            elif i+1 < n and nums[i] < target and target < nums[i+1]:
                return i+1     
        return n
        