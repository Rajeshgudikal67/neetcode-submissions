class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        b=False
        for i,j in d.items():
            if j>1:
                b=True
                break
            else:
                b=False
        return b