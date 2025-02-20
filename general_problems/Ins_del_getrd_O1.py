# Problem description here https://leetcode.com/problems/insert-delete-getrandom-o1/description/


class RandomizedSet:

    def __init__(self):
        self.rd = {}
        self.rl = []

    def insert(self, val: int) -> bool:
        if val in self.rd:
            return False
        else:
            self.rd[val] = len(self.rl)
            self.rl.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.rd:
            return False
        else:
            req_idx = self.rd[val]
            last_val = self.rl[-1]
            self.rl[req_idx] = last_val
            self.rd[last_val] = req_idx
            self.rl.pop()
            del self.rd[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.rl)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Time Complexity = O(1), Space Complexity = O(N)
