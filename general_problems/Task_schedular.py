# problem link here https://leetcode.com/problems/task-scheduler/description/

import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # charc = defaultdict(int)
        charc = collections.Counter(tasks)
        # for i in tasks:
        #    charc[i] += 1
        lend = len(charc.keys())
        lent = len(tasks)
        lenf = max(charc.values())
        if lenf == 1:
            return lent
        if n >= lend:
            return (n + 1) * (lenf - 1) + list(charc.values()).count(lenf)
        else:
            if lenf < lent // n:
                return lent
            else:
                return max(
                    lent, (n + 1) * (lenf - 1) + list(charc.values()).count(lenf)
                )
