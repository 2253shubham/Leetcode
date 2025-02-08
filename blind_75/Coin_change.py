# Problem description here https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)  
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)  # Take the minimum number of coins

        return dp[amount] if dp[amount] != float('inf') else -1  # Return -1 if impossible 
    

# Time Complexity = O(M * N), Space Complexity = O(N)
# Where M is the number of coins and N is the amount

"""
# My original code (Same time and space complexity)

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        def dp(amount, demo):
            if amount in coins:
                return 1
            if amount == 0:
                return 0
            if min(coins) > amount:
                return -1
            mincount = -1
            for i in coins:
                if not demo.get(amount - i):
                    curr = dp(amount - i, demo)
                    if curr == -1:
                        demo[amount - i] = curr
                    else:
                        demo[amount - i] = 1 + curr
                if mincount > -1 and demo[amount - i] != -1:
                    mincount = min(demo[amount - i], mincount)
                else:
                    mincount = -min(-demo[amount - i], -mincount)
            
            return mincount

        return dp(amount, {})

"""