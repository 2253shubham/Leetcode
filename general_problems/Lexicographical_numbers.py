# Problem description here https://leetcode.com/problems/lexicographical-numbers/description/


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        results = []
        current = 1

        for i in range(n):
            results.append(current)

            if current * 10 <= n:
                current *= 10
            else:
                while current % 10 == 9 or current >= n:
                    current = current // 10
                current += 1

        return results


# Time Complexity = O(N), Space Complexity = O(N)
