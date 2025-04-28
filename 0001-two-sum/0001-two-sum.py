class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result = 0
        for i in range(n):
            m = i+1
            for j in range(m,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        