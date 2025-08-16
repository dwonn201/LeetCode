class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        index = []
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                index.append(i)
        
        if not index:
            return -1
        return min(index)

        