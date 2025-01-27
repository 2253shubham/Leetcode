# Problem description here https://leetcode.com/problems/top-k-frequent-elements/description/

import numpy as np
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        num_vals = []
        num_freq = []
        for key, val in cnt.items():
            num_vals.append(key)
            num_freq.append(val)

        idx = np.argsort(np.array(num_freq))[::-1]
        output = []
        for i in range(k):
            output.append(num_vals[idx[i]])

        return output
    
# Time Complexity = O(NlogN), Space Complexity = O(N)
