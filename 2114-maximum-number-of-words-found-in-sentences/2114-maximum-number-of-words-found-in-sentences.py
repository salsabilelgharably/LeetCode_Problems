class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_list = []
        for i in range(len(sentences)):
            max_list.append(sentences[i].count(" ") + 1)
        return max(max_list)