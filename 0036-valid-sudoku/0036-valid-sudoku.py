class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 각 행,열, 3x3박스 숫자들을 저장할 해시값 
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] 

        # 보드를 순회 
        for i in range(9): 
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue
                
                # 3x3 박스 index 계산 
                box_index = (i // 3) * 3 + (j // 3)

                # 중복 검사 
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                # 중복이 없으면 값 추가 
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        # 모든 검사를 통과하면 True
        return True
                    



        