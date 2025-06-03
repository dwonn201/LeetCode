class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        hay_len = len(haystack)

        if n == 0:
            return 0

        for i in range(hay_len - n + 1):
            if haystack[i:i+n] == needle:
                return i

        return -1