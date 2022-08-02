class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic={}
        alphabet = []
        keys = ""
        res=""
        for k in key:
            if(k in keys) or k == " " :
                pass
            else:
                keys += k
        for c in range(97, 123):
            alphabet.append(chr(c))

        for i in range(len(keys)):
                dic[keys[i]] = alphabet[i]

        for l in range(len(message)):
            if message[l] == " ":
                res += " "
            else:
                res += dic[message[l]]
        return res