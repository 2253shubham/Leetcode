# Problem description here https://leetcode.com/problems/increasing-triplet-subsequence/description/


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = float("inf")  # Smallest number found
        mid = float("inf")  # Second smallest number found

        for num in nums:
            if num <= small:
                small = num  # Update the smallest number
            elif num <= mid:
                mid = num  # Update the second smallest number
            else:
                return True  # Found a number greater than both

        return False


# Time Complexity = O(N), Space Complexity = O(1)

"""
# My original solution (same time and space complexity)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        vt1 = nums[0]
        vt2 = nums[1]
        vt3 = nums[2]
        if vt1 < vt2 < vt3:
            return True
        for i in range(3, len(nums)):
            if vt1 < vt2 < nums[i]:
                return True
            elif vt2 < vt3 < nums[i]:
                return True
            elif vt1 < vt3 < nums[i]:
                return True
            else:
                if (
                    max([vt1, vt2, vt3]) == vt1 or min([vt1, vt2, vt3]) == vt2
                ) and vt1 != vt2:
                    vt1 = vt2
                    vt2 = vt3
                    vt3 = nums[i]
                elif min([vt1, vt2, vt3]) == vt1 and vt1 == vt3 and vt2 != vt3:
                    continue
                else:
                    vt2 = vt3
                    vt3 = nums[i]

        return False
"""
