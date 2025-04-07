# Problem description here https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = Counter(nums)
        output = 0

        for key, val in count.items():
            if target.startswith(key):
                output += val * count[target[len(key) :]]

                if key == target[len(key) :]:
                    output -= val

        return output


# Time Complexity = O(N), Space Complexity = O(N)

"""
# My original solution (Time Complexity = O(N^2), Space Complexity = O(N))

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = defaultdict(int)
        count[target] = 0
        for i in nums:
            if i == target:
                continue
            for j in count.keys():
                if i + j == target:
                    count[target] += count[j]
                if j + i == target:
                    count[target] += count[j]
            count[i] += 1

        return count[target]

"""
