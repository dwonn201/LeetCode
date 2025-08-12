class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        _x = str(abs(x))
        reversed_ = _x[::-1]
        reversed_x = int(reversed_)

        if is_negative:
            reversed_x = -reversed_x

        int_max = 2**31 -1 
        int_min = -2**31

        if reversed_x > int_max or reversed_x < int_min:
            return 0
        else:
            return reversed_x


        