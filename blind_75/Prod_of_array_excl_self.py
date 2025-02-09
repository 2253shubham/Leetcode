# Problem description here https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        out = []
        for i in range(len(nums)):
            out.append(product)
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * product
            product *= nums[i]
        return out


# Time Complexity = O(N), Space Complexity = O(N)
