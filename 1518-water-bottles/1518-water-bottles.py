class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        remain = numBottles
        wait = 0
        
        drinked_bottles = numBottles
        empty_bottles = numBottles           
    
        while empty_bottles//numExchange>0:
            new_bottles = empty_bottles//numExchange
            drinked_bottles += new_bottles
            empty_bottles = empty_bottles % numExchange + new_bottles
            
        return drinked_bottles