class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxItem = -1
        res = [-1] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > maxItem:
                temp = arr[i]

                res[i] = maxItem
                maxItem = temp
            else:
                res[i] = maxItem

        return res

        

