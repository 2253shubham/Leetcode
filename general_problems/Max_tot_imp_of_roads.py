# Problem description here https://leetcode.com/problems/maximum-total-importance-of-roads/description/

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        sm = 0
        lt = defaultdict(int)
        for i in range(len(roads)):
            lt[roads[i][0]] += 1
            lt[roads[i][1]] += 1
        km = sorted(zip(lt.values(), lt.keys()))
        for j in range(len(km) - 1, -1, -1):
            sm += lt[km[j][1]] * n
            n -= 1
        return sm 

# Time Complexity = O(M + NlogN), Space Complexity = O(N)
# where M is the number of roads and N is the number of cities

