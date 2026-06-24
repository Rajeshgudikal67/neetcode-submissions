class Solution:
    def scoreOfString(self, s: str) -> int:
        m=0
        for i in range(len(s)-1):
            m+=abs(ord(s[i])-ord(s[i+1]))
        return m

            

