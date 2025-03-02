# Problem description here https://leetcode.com/problems/frog-jump/description/


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)  # Convert to set for O(1) lookups
        last_stone = stones[-1]  # Last stone position

        @lru_cache(None)
        def dp(curr: int, step: int) -> bool:
            if curr == last_stone:
                return True  # Reached the last stone

            if curr not in stone_set:
                return False  # The current position is not a stone

            for next_step in {step - 1, step, step + 1}:
                if next_step > 0 and (curr + next_step) in stone_set:
                    if dp(curr + next_step, next_step):
                        return True  # If we can reach the last stone, return True

            return False  # No valid jump leads to the last stone

        return dp(1, 1) if stones[1] == 1 else False


# Time Complexity = O(N^2), Space Complexity = O(N^2)
