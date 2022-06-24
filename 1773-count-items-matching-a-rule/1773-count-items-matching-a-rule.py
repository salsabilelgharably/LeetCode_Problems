class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        Count_item = 0
        for item in range(len(items)):
            if ruleKey == "type":
                if items[item][0] == ruleValue:        
                    Count_item += 1
                    
            if ruleKey == "color":
                if items[item][1] == ruleValue:        
                    Count_item += 1
                    
            if ruleKey == "name":
                if items[item][2] == ruleValue:        
                    Count_item += 1
        return Count_item
        