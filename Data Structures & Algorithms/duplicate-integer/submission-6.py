class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        n=True
        if not nums:
            return False
        for i in nums:
            if i not in s:
                s.add(i)
                n=False
            else:
                return True
                break
        return n
