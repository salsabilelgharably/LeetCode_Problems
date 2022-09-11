class Solution:
    def maximum69Number (self, num: int) -> int:
        
        fnd = str(num).find('6')
        if fnd == -1:
            return num
        else:
            return int(str(num).replace("6","9",1))
        