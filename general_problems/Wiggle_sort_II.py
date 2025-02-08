# Problem description here https://leetcode.com/problems/wiggle-sort-ii/description/


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        k1 = nums[: (len(nums) + 1) // 2][::-1]
        k2 = nums[(len(nums) + 1) // 2 :][::-1]

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = k1.pop(0)
            else:
                nums[i] = k2.pop(0)


# Time Complexity = O(NlogN), Space Complexity = O(N)
