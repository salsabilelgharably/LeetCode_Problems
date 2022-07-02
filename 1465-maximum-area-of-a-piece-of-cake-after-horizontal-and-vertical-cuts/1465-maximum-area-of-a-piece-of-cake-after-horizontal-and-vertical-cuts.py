class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        if horizontalCuts[-1] != h:
            horizontalCuts.append(h)
        if verticalCuts != w:
            verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        h_list =[horizontalCuts[0]]
        v_list =[verticalCuts[0]]
        for x in range(len(horizontalCuts)-1):
            h_list.append(horizontalCuts[x+1] -horizontalCuts[x])
        for y in range(len(verticalCuts) - 1):
            v_list.append(verticalCuts[y+1] - verticalCuts[y])
        
        return max(h_list) * max(v_list)  %(10**9+7)