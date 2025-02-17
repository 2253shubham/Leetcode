# Problem description here https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n
        if guess(1) == 0:
            return 1
        lower = 1
        upper = n
        flag = -1
        guess_num = 0
        while flag == -1:
            guess_num = int((lower + upper) / 2)
            if guess(guess_num) == 0:
                flag = 0
            elif guess(guess_num) == 1:
                lower = guess_num
            else:
                upper = guess_num

        return guess_num
    
# Time Complexity = O(logN), Space Complexity = O(1)
