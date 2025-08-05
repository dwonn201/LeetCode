class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True 
        if n < 1:
            return False


        power_of_four = 4
        while power_of_four < n:
            power_of_four *= 4
        
        return power_of_four == n
        