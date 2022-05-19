class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
            max_wealth =0
            value_wealth =0
            for x in range(len(accounts)):
                value_wealth = sum(accounts[x])
                if value_wealth > max_wealth :
                    max_wealth =value_wealth
            return max_wealth
        