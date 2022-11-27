class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = -1
        for i in range(len(arr)-1,-1,-1):
            save = arr[i]
            arr[i] = max_
            if save > max_:
                max_ = save
        return arr
        