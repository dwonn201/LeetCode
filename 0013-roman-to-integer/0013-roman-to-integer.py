class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value=0

        for char in reversed(s):
            value = roman_map[char]
            if value < prev_value:
                total -= value 
            else:
                total += value
            prev_value = value
        return total


        nums = [chars for chars in s]
        length = len(nums)
        number = []
        for i in range(length):
            if nums[i] == "I":
                if (nums[i+1] == 'V') and (i+1 <= length):
                    number.append(4)
                else:
                    number.append(1)
            elif nums[i] == "V":
                if i > 0 and nums[i-1] =='I':
                    pass
                number.append(5)
            elif nums[i] == "X":
                number.append(10)
            elif nums[i] == "L":
                number.append(50)
            elif nums[i] == "C":
                number.append(100)
            elif nums[i] == "D":
                number.append(500)
            elif nums[i] == "M":
                number.append(1000)
        return sum(number)


        