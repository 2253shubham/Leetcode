# Problem description here https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        tot = len(matrix) * len(matrix[0])
        out = [0] * tot
        c = 0
        i = 0
        j = 0
        while c < tot:
            if matrix[i][j] != 10000:
                out[c] = matrix[i][j]
                matrix[i][j] = 10000
                c += 1
            if i == top and j < right:
                if matrix[i][j + 1] != 10000:
                    j += 1
                else:
                    right -= 1
                continue
            if j == right and i < bottom:
                if matrix[i + 1][j] != 10000:
                    i += 1
                else:
                    bottom -= 1
                continue
            if i == bottom and j > left:
                if matrix[i][j - 1] != 10000:
                    j -= 1
                else:
                    left += 1
                continue
            if j == left and i > top:
                if matrix[i - 1][j] != 10000:
                    i -= 1
                else:
                    top += 1
                continue

        return out


# Time Complexity = O(M * N), Space Complexity = O(M * N)
# where M is the number of rows and N is the number of columns
