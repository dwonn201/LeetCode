class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
    
        while columnNumber > 0:
            # 1을 빼서 0-based 인덱스로 변환
            columnNumber -= 1
            
            # 26으로 나눈 나머지로 문자 결정
            result = chr(ord('A') + columnNumber % 26) + result
            
            # 다음 자리수로 이동
            columnNumber //= 26
        
        return result