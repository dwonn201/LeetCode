class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)

        if target < nums[0]:
            return 0

        for i in range(l):
            if nums[i] == target:
                return i
            elif i > 0 and target > nums[i-1] and target < nums[i]:
                return i
        return l



        