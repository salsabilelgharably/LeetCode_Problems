class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_1 = {}
        map_2 = {}
        s = s.split()
        if len(s) != len(pattern): return False
        for i,j in zip(pattern,s):
            if (i not in map_1) and (j not in map_2):
                map_1[i] = j
                map_2[j] = i
            elif map_1.get(i) != j or map_2.get(j) !=i:
                return False
        return True