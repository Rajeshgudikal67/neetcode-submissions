class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r=-1
        for i in range(len(arr)-1,-1,-1):
            t=arr[i]
            arr[i]=r
            r=max(r,t)
        return arr






        