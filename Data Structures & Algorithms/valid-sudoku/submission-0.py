class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            counts = collections.Counter(row)
            for val, count in counts.items():
                if val!= '.' and count > 1:
                    return False
        for col in zip(*board):
            counts = collections.Counter(col)
            for val, count in counts.items():
                if val!= '.' and count > 1:
                    return False
        for row in range(0, 9, 3):
            for col in range(0,9,3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[row+i][col+j])
                counts = collections.Counter(box)
                for val, count in counts.items():
                    if val!= '.' and count > 1:
                        return False
        return True

