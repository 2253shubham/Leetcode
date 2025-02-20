# Problem description here https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/

class RandomizedCollection:

    def __init__(self):
        self.rd = defaultdict(set)  # or {}
        self.rl = []

    def insert(self, val: int) -> bool:
        if val in self.rd:
            self.rd[val].add(len(self.rl))
            self.rl.append(val)
            return False
        else:
            self.rd[val] = set([len(self.rl)])  # {len(self.rl)}
            self.rl.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.rd:
            return False
        else:
            req_idx = self.rd[val].pop()
            last_val = self.rl[-1]
            if req_idx != len(self.rl) - 1:
                self.rl[req_idx] = last_val
                self.rd[last_val].remove(len(self.rl) - 1)
                self.rd[last_val].add(req_idx)

            self.rl.pop()
            if self.rd[val] == set():  # or {}:
                del self.rd[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.rl)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Time Complexity = O(1), Space Complexity = O(N)