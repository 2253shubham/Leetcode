# Problem description here https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        heap_sum = []
        heapq.heapify(heap_sum)
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap_sum, (nums1[i] + nums2[0], i, 0))

        out = []
        for _ in range(k):
            if not heap_sum:
                break

            summ, i, j = heapq.heappop(heap_sum)
            out.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap_sum, (nums1[i] + nums2[j + 1], i, j + 1))

        return out


# Time Complexity = O(KlogK), Space Complexity = O(K)
