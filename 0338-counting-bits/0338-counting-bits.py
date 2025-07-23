class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n+1):
            binary = str(bin(i))
            count = 0
            for j in range(len(binary)):
                if binary[j] == '1':
                    count += 1
            output.append(count)
        return output