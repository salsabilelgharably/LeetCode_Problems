class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst1 = s1.split()
        lst2 =s2.split()
        res=[]
        for i in lst1:
            if i not in lst2 and lst1.count(i)==1:
                res.append(i)
        for x in lst2:
            if x not in lst1 and lst2.count(x)==1:
                res.append(x)
                
        return res