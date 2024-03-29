class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        s = 0
        for i in range(len(points)-1):
            s += max(abs(points[i+1][1]-points[i][1]), 
                     abs(points[i+1][0]-points[i][0]))
        return s