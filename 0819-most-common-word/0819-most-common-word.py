class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = " ".join(re.findall(r"[a-zA-Z0-9]+", paragraph))
        c = Counter(paragraph.lower().split())
        c = OrderedDict(c.most_common())
        for word in c:
            if word not in banned:
                return word        