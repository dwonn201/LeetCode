class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split(" ")
        s_list = [s for s in s_list if s != '']
        last_word = s_list[-1]
        return len(last_word)