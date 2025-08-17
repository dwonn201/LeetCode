class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        def generate_next(s: str) -> str:
            """
            주어진 문자 s의 run-length encoding 수행 
            """ 
            new_string = []
            i = 0
            while i < len(s):
                char = s[i]
                count = 1
                j = i + 1
                while j < len(s) and s[j] == char:
                    count += 1
                    j += 1
                new_string.append(str(count))
                new_string.append(char)
                i = j
            return "".join(new_string)
        
        result = "1"
        for _ in range(2, n+1):
            result = generate_next(result)
        return result


                
            



        