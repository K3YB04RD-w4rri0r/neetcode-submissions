class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # print("ROWS")
        for r in range(9):
            row = board[r]
            print(row)
            seen = set()
            for e in row:
                if e in seen and e != ".":
                    return False
                seen = seen | set(e)
                

        # print("BOXES")
        for bhstart in range(0,9, 3):
            for bwstart in range(0,9,3):
                row = (board[bhstart][bwstart:bwstart + 3] +
                        board[bhstart + 1][bwstart:bwstart + 3] +
                        board[bhstart + 2][bwstart:bwstart + 3])
                # print(row)
                seen = set()
                for e in row:
                    if e in seen and e != ".":
                        return False
                    seen = seen | set(e)

        columns = list(zip(*board))
        # print("COLS")
        for r in range(9):
            row = columns[r]
            # print(row)
            seen = set()
            for e in row:
                if e in seen and e != ".":
                    return False
                seen = seen | set(e)

        return True
