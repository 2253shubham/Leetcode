# Problem description here https://leetcode.com/problems/super-pow/description/

# Uses Euler formula of Modulus

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result, factor = 1, a % 1337
        for n in reversed(b):
            result = result * (factor ** n) % 1337
            factor = (factor ** 10) % 1337
        return result
    
# Time Complexity = O(N), Space Complexity = O(1)