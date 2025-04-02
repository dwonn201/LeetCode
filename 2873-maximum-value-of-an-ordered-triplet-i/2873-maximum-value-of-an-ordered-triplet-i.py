class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = 0

        for j in range(1, n-1):
            max_left = max(nums[:j])
            for k in range(j+1, n):
                value = (max_left - nums[j]) * nums[k]
                max_num = max(max_num, value)
        return max_num

        