class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        f=strs[0]
        for i in range(len(f)):
            for j in strs:
                if i>=len(j) or f[i]!=j[i]:
                    return s
            s+=f[i]
        return s