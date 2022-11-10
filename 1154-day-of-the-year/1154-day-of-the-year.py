class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split('-')
        y = int(date[0])
        m = int(date[1])
        d = int(date[2])
        day_counts = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,}
        res = 0
        for i in range(m-1):
            res += day_counts[i+1]
        if m >2:
            if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                res += 1
        return res + d
        