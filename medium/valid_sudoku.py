class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for line in board:
            if self.isValidArray(line) != True: return False
        for i in range(0, len(board)):
            row = []
            for index in range(0, len(board)):
                row.append(board[index][i])
            if self.isValidArray(row) != True: return False
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                row = [board[x][y] for x in range(m, m + 3) for y in range(n, n + 3)]
                if self.isValidArray(row) != True: return False
        return True

    def isValidArray(self, arr: List[str]) -> bool:
        filtered = [x for x in arr if x != "."]
        return len(filtered) == len(set(filtered))
