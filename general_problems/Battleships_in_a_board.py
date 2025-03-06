# Problem description here https://leetcode.com/problems/battleships-in-a-board/description/


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        # Loop over rows and columns
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Check if current cell is part of a battleship
                if board[i][j] == "X":
                    # Check if it's the beginning of a new battleship
                    if (i == 0 or board[i - 1][j] == ".") and (
                        j == 0 or board[i][j - 1] == "."
                    ):
                        count += 1

        return count


# Time Complexity = O(N*M), Space Complexity = O(1)
