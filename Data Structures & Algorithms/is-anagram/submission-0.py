class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sortedS = sorted(s)
        sortedT = sorted(t)

        for x in range(len(s)):
            if sortedS[x] != sortedT[x]:
                return False
        
        return True
            


# check if s and t are same length
# sort the 2 strings
# compare each, if diff, return False
# if end of loop, return true