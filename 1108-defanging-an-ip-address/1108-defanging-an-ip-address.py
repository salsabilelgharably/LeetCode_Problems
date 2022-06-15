class Solution:
    def defangIPaddr(self, address: str) -> str:
        str_address = ""
        for i in range(len(address)):
            if address[i] == ".":
                str_address +="[.]"
            else:
                str_address += address[i]
        return str_address
        