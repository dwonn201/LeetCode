class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = str(bin(n))

        count = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                count += 1
        return count

