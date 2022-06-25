class Solution:
    def interpret(self, command: str) -> str:
        Goal =""

        for i in range(len(command)):
            if command[i] == "G":
                Goal += "G"
            elif command[i] == "(" and command[i+1] == ")":
                Goal += "o"
                i = i+2
            elif command[i] == "(" and command[i+1] == "a":
                Goal += "al"
                i = i+4
        return Goal