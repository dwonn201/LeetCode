class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0
        while True:
            if 2**x == n:
                return True
            elif 2**x < n:
                x+=1
            elif 2**x > n:
                return False