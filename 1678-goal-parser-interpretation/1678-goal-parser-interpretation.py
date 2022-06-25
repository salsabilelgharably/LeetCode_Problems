class Solution:
    def interpret(self, command: str) -> str:
        Goal =""
        cmd =""
        for i in range(len(command)):
            if command[i] == "G":
                Goal += "G"
            elif command[i] == "(" or ")" or "a" or "l":
                cmd += command[i]
            if cmd == "()":
                Goal += "o"
                cmd = ""
            elif cmd == "(al)":
                Goal += "al"
                cmd =""
        return Goal