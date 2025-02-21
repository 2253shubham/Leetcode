# Problem description here https://leetcode.com/problems/shuffle-an-array/description/

class Solution:

    def __init__(self, nums: List[int]):
        self.org = nums

    def reset(self) -> List[int]:
        return self.org

    def shuffle(self) -> List[int]:
        sff = self.org[:] # deepcopy needed!
        for i in range(len(sff)):
            ch = random.randrange(i, len(sff))
            sff[i], sff[ch] = sff[ch], sff[i]
        
        return sff     


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# Time Complexity = O(N), Space Complexity = O(N)