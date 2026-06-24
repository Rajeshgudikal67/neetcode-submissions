class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in nums:
            if i in s:
                return True
                break
            s.add(i)
        return False