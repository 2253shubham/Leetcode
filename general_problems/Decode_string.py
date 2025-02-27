# Problem description here https://leetcode.com/problems/decode-string/description/


class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        brackets = []
        out = ""
        temp_out = {}
        num = ""
        for i in s:
            if i == "[":
                brackets.append(i)
                nums.append(int(num))
                temp_out[len(brackets)] = ""
                num = ""
            elif i == "]":
                temp_out[len(brackets)] *= nums.pop()
                brackets.pop()
                if len(brackets) == 0:
                    out += temp_out[1]
                    del temp_out[1]
                else:
                    temp_out[len(brackets)] += temp_out[len(brackets) + 1]
                    del temp_out[len(brackets) + 1]
            elif 0 <= ord(i) - ord("a") <= 25:
                if len(brackets) == 0:
                    out += i
                else:
                    temp_out[len(brackets)] += i
            else:
                num += i
        return out


# Time Complexity = O(N), Space Complexity = O(N)
