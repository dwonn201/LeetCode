class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(
            current_combination: list,
            current_sum: int,
            start_index: int
        ):

            if current_sum == target:
                result.append(list(current_combination))
                return 

            if current_sum > target:
                return 
            
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                current_combination.append(candidate)
                backtrack(
                    current_combination,
                    current_sum + candidate,
                    i
                )
                current_combination.pop()

        backtrack([],0,0)
        return result


        