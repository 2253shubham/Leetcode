# Problem description here https://leetcode.com/problems/maximum-average-pass-ratio/description/


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(pass_, total):
            return (pass_ + 1) / (total + 1) - pass_ / total

        max_heap = []
        sum_ = 0.0

        for pass_, total in classes:
            sum_ += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        for i in range(extraStudents):
            cur_max_gain, pass_, total = heapq.heappop(max_heap)
            sum_ -= pass_ / total
            pass_ += 1
            total += 1
            sum_ += pass_ / total
            heapq.heappush(max_heap, (-gain(pass_, total), pass_, total))

        return sum_ / len(classes)


# Time Complexity = O((N+k)logN), Space Complexity = O(N)
# Where N is the number of classes and k is the number of extraStudents
