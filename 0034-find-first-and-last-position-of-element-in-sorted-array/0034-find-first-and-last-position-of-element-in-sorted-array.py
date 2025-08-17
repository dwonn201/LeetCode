class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = []

        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                if len(output) < 2:
                    output.append(i)
                elif len(output) >= 2:
                    output[1] = i

        if not output:
            return [-1,-1]
        if len(output) < 2:
            return output * 2

        return output
        