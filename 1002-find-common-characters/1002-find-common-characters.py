class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_chars = []
        for ltr in words[0]:
            found_in_all = True
            for i in range(1, len(words)):
                ltr_pos = words[i].find(ltr)
                if ltr_pos == -1:
                    found_in_all = False
                    break
                else:
                    words[i] = words[i][0:ltr_pos] + '0' + words[i][ltr_pos+1:]
            if found_in_all:
                common_chars.append(ltr)
        return common_chars