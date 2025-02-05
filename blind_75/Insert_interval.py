# Problem description here 


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        intervals.append(newInterval)
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
          
        for i in range(len(intervals)):
            if left <= intervals[i][0] <= right:
                if right <= intervals[i][1]:
                    right = intervals[i][1]
            else:
                out.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        
        out.append([left, right])
        return out
        

# Time Complexity = O(NlogN) , Space Complexity = O(N) 