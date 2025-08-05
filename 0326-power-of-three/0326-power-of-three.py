class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power_of_3 = 1
        while power_of_3 < n:
            power_of_3 *= 3
        return power_of_3 == n
