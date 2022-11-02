class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            divisible = True
            char = str(i)
            if '0' not in char:
                for  digit in char:
                    if i % int(digit) != 0:
                        divisible = False
                if divisible :
                    res.append(i)
        return res
                        