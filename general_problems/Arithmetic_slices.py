# Problem description here https://leetcode.com/problems/arithmetic-slices/description/


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        count = 0
        left = 0
        right = 2
        diff = nums[1] - nums[0]  # Initialize the difference

        while right < len(nums):
            # Check if the current element continues the arithmetic sequence
            if nums[right] - nums[right - 1] == diff:
                right += 1  # Extend the sequence
            else:
                # Calculate the number of arithmetic slices in the valid segment
                length = right - left
                if length >= 3:
                    count += (length - 2) * (length - 1) // 2

                # Reset the segment
                left = right - 1
                diff = nums[right] - nums[left]
                right += 1

        # Handle the last valid segment (if the loop exits with a valid sequence)
        length = right - left
        if length >= 3:
            count += (length - 2) * (length - 1) // 2

        return count


# Time Complexity = O(N), Space Complexity = O(1)

"""

# Alternate way (Same time and space complexity)

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        count = 0
        curr = 0  # Stores the number of arithmetic subarrays ending at the current index
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr += 1  # Extend the previous arithmetic sequence
                count += curr  # Add the count of arithmetic subarrays ending at index i
            else:
                curr = 0  # Reset count when sequence breaks

        return count

"""
