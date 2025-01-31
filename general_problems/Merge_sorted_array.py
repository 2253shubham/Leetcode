# Problem description here https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c1 = 0
        c2 = 0
        c3 = 0
        mid = len(nums1) - len(nums2)
        nums3 = nums1[0: mid]
        while c2 < len(nums2) and c3 < len(nums3):
            if nums3[c3] <= nums2[c2]:
                nums1[c1] = nums3[c3]
                c3 += 1
            else:
                nums1[c1] = nums2[c2]
                c2 += 1
            c1 += 1

        while c2 < len(nums2):
            nums1[c1] = nums2[c2]
            c2 += 1
            c1 += 1

        while c3 < len(nums3):
            nums1[c1] = nums3[c3]
            c3 += 1
            c1 += 1

# Time Complexity = O(N + M), Space Complexity = O(N)
# where M and N are sizes of the 2 arrays with N being the size of the duplicated array


"""

# Better approach --> needs O(1) space

        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If any elements remain in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

"""