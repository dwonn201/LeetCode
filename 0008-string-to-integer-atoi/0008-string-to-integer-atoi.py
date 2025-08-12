class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        sign = 1
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        result = 0
        for char in s:
            if char.isdigit():
                digit = int(char)
                result = result*10 + digit
            else:
                break
        final = sign * result

        int_min = -2**31
        int_max = 2**31-1

        if final < int_min:
            return int_min
        elif final > int_max:
            return int_max
        else:
            return final
