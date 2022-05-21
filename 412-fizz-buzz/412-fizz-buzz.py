class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        str_out = []
        for i in range(1, n +1):
            if i %3 == 0 and i%5==0:
                str_out.append("FizzBuzz")
            elif i % 3 == 0:
                str_out.append("Fizz")
            elif i % 5 == 0:
                str_out.append("Buzz")
            else:
                str_out.append(str(i))
        return str_out