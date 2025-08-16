class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        output = ['_'] * n
        i = 0

        for j in range(1,n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1



        