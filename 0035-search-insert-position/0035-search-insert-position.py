class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                index = i + 1
        return index
