class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left= 0 
        row_right= len(matrix) - 1
        num_left= 0 
        num_right= len(matrix[0]) - 1
        
        while row_left <= row_right:
            row_mid= int((row_left + row_right)/2)
            if matrix[row_mid][0] > target:
                row_right= row_mid -1
            elif matrix[row_mid][0] < target and  matrix[row_mid][-1] < target:
                row_left= row_mid +1
                
            else:
                while num_left <= num_right:
                    num_mid= int((num_right + num_left)/2)
                    if matrix[row_mid][num_mid] > target:
                        num_right= num_mid - 1
                    elif matrix[row_mid][num_mid] < target:
                        num_left= num_mid + 1
                    else:
                        return True
                return False
        
        return False