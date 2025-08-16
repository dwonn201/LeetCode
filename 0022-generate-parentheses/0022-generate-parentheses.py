class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(current_string:str, open_count:int, close_count:int):
            if len(current_string) == 2 * n:
                result.append(current_string)
                return 

            if open_count < n:
                backtracking(current_string + '(',  open_count + 1, close_count)
            
            if close_count < open_count:
                backtracking(current_string + ')', open_count, close_count+1)

        backtracking("", 0, 0)
        return result
        