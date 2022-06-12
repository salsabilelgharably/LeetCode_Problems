class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        Alph_chess = ['a','b','c','d','e','f','g','h']
        x_num= Alph_chess.index(coordinates[0])
        y_num = int( coordinates[1])
        Z_num = x_num+y_num
        if Z_num %2 ==0:
            return True
        else:
            return False