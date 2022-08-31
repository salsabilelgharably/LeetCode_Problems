class Solution:
    def countValidWords(self, sent: str) -> int:
        if len(sent)==1:
            if sent[0]=="-"or sent[0].isnumeric() or sent[0].isupper():
                return 0
            else:
                return 1
        s = sent.split()
        count = 0


        for i in range(len(s)):
            p = 0
            c = 1                                   # variable used as a flag
            x = s[i]
            for j in range(len(x)):
                if x[j].isnumeric() or x[j].isupper():
                    c = 0
                    break
                if x[j]=="!" or x[j]=="," or x[j]==".":
                    if j==len(x)-1:
                        continue
                    elif x[j+1].isalpha() or x[j+1]=="." or x[j+1]=="," or x[j+1].isnumeric() or x[j+1].isupper() or x[j+1]=="!":

                        c = 0
                        break
                if x[j]=="-":
                    if j==len(x)-1:
                        c = 0
                        break
                    p+=1
                    if (x[j+1].isalpha()) and (x[j-1].isalpha()) and p<=1 and j > 0:
                        continue
                    else:
                        c = 0
                        break
            if c==1:            
                count+=1
        return count  