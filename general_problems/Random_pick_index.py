# Problem description here https://leetcode.com/problems/random-pick-index/description/


class Solution:

    def __init__(self, nums: List[int]):
        self.content = defaultdict(list)
        for i in range(len(nums)):
            self.content[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.content[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


# Time Complexity = O(N), Space Complexity = O(N)
