class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        candy = [1] * l
        if len(ratings) == 1:
            return 1
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = max(candy[i], candy[i-1] + 1)

            if ratings[l-i] < ratings[l-i-1]:
                candy[l-i-1] = max(candy[l-i-1], candy[l-i] + 1)
        return sum(candy)