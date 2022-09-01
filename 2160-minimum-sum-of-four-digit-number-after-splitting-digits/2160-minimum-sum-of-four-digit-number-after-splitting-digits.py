class Solution:
    def minimumSum(self, num: int) -> int:
        x = [int(a) for a in str(num)]
        n1=''
        n2=''
        for i in range(2):
            n1 +=str(min(x))
            x.remove(min(x))
            n2 += str(min(x))
            x.remove(min(x))
        return int(n1) + int(n2)