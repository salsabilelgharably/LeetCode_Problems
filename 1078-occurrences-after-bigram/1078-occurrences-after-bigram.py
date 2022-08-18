class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        txt = text.split(' ')
        res = []
        com = first+second
        if len(txt) < 3 or len(text) <= len(first) + len(second):
            return res
        for i in range(len(txt)-2):
            if com == txt[i]+txt[i+1]:
                res.append(txt[i+2])
        return res