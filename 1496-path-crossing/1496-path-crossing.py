class Solution:
    def isPathCrossing(self, path: str) -> bool:
        N,S,E,W = 0,0,0,0
        points=[]
        for i in path:
            if i == 'N':
                N += 1
            elif i == 'S':
                S -= 1
            elif i == 'E':
                E += 1
            else:
                W -= 1
            if N + S == 0 and E + W == 0:
                return True
            if str(N+S)+','+str(E+W) not in points:
                    points.append(str(N+S)+','+str(E+W))
            else:
                return True
        return False           