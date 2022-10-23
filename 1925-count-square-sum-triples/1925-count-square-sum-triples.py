class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=0
        for i in range(1,n-1):
            for j in range(i+1,n):
                tri=math.sqrt((i**2+j**2))
                if tri<=n and int(tri)==tri :
                    x+=2


        return x