# Problem description here https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        minl = nums[0]
        maxl = nums[-1]
        leng = len(nums)

        if minl == maxl:
            if minl == 0 or minl < leng:
                return -1
            else:
                return leng

        if leng <= minl:
            return leng
        else:
            for i in range(minl + 1, leng, 1):
                if nums[leng - i] >= i and nums[leng - i - 1] < i:
                    return i
            return -1


# Time Complexity = O(NlogN), Space Complexity = O(1)
