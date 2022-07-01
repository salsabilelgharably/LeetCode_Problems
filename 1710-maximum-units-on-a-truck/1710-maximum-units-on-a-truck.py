class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda row: row[1], reverse=True)
        max_unit = 0
        
        for box in boxTypes:
            N_box = box[0]
            unit_box = box[1]
            
            if truckSize < N_box:
                max_unit += unit_box * truckSize

            else:
                max_unit += unit_box * N_box 
            truckSize -= N_box
            
            if truckSize <= 0:
                return max_unit
        return max_unit
            