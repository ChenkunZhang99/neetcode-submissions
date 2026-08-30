class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]
        for j in range(9):
            for k in range(9):
                row_val = board[j][k]
                index = (j // 3) * 3 + (k // 3)
                if row_val != ".":
                    if row_val in row_sets[j] or row_val in box_sets[index]:
                        return False
                    row_sets[j].add(row_val)
                    box_sets[index].add(row_val)

                col_val = board[k][j]
                if col_val != ".":
                    if col_val in col_sets[j]:
                        return False
                    col_sets[j].add(col_val)




        return True        