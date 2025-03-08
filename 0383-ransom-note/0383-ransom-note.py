class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_cnt = Counter(ransomNote)
        magazine_cnt = Counter(magazine)

        for char, count in ransom_cnt.items():
            if magazine_cnt[char] < count:
                return False 
                
        return True