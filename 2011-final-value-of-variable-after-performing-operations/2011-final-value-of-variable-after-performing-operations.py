class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return str(operations).count('++')+ (str(operations).count('--') * -1)
        