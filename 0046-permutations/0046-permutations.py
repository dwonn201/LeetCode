class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 최종 결과를 저장할 리스트
        result = []
        # 현재까지 만들어진 순열을 저장할 리스트
        current_permutation = []
        # 이미 사용된 원소를 추적하기 위한 집합
        used = set()

        def backtrack():
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return 
            
            # 재귀 단계: nums의 모든 원소를 순회
            for num in nums:
                # 만약 현재 원소가 이미 사용된 원소가 아니면
                if num not in used:
                    # 현재 원소를 순열에 추가하고
                    current_permutation.append(num)
                    # 사용된 것으로 표시합니다.
                    used.add(num)
                    
                    # 재귀 호출하여 다음 원소를 선택
                    backtrack()

                    # 백트래킹: 다음 조합을 위해 마지막에 추가한 원소 제거
                    current_permutation.pop()
                    # 사용된 원소에서도 제거하여 다음 탐색에서 사용할 수 있게 합니다.
                    used.remove(num)
        # 백트래킹 시작
        backtrack()
        return result



        

        