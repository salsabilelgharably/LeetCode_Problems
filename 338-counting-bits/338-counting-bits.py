class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_list=[]
        for i in range(n+1):
            bit_list.append(bin(i).count("1"))
        return bit_list
            