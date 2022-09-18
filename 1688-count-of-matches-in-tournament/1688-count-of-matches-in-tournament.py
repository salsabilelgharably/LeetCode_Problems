class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 1
        teams = n
        if n <= 1:
            return 0
        while(teams > 2):
            if teams %2 == 0:
                matches += teams / 2
                teams = teams / 2
            else:
                matches += (teams-1)/2
                teams = (teams-1)/2 + 1
        return int(matches)