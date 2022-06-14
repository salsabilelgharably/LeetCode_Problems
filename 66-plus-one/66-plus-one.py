class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Variables
        Sum_num = 0
        len_list = len(digits)
        List_plus_one = []
        # sum Number
        for x in range(len_list):
            Sum_num += digits[x] * (10**(len_list-1)) 
            len_list = len_list -1
        res = str(Sum_num + 1)
        # Final list
        for i in range(len(res)):
            List_plus_one.append(int(res[i]))
        return List_plus_one