class Solution:
    def romanToInt(self, s: str) -> int:
        rom_Dection = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value_int_to_roman = 0
        for i in range(len(s)):
            if i > 0 and rom_Dection[s[i]] > rom_Dection[s[i - 1]]:
                value_int_to_roman += rom_Dection[s[i]] - 2 * rom_Dection[s[i - 1]]
            else:
                value_int_to_roman += rom_Dection[s[i]]
        return value_int_to_roman
        