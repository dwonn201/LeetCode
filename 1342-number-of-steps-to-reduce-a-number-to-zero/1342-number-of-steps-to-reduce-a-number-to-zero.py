class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num ==0:
            return 0

        steps = 0
        result = num
        while result != 0:
            result = result//2 if result%2==0 else result-1
            steps+=1
        return steps
        