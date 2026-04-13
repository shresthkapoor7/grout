class Solution:
    def bruteForce(self, s: str, t: str) -> bool:
        flag = True
        for c in s:
            flag = True
            for j in t:
                if j == c:
                    flag = False
                    break
            if flag:
                return False
        return not flag
    
    def sortingApproach(self, s: str, t: str) -> bool:
        str1 = sorted(s)
        str2 = sorted(t)
        for i in range (len(str1)):
            if str1[i] != str2[i]:
                return False
        return True

        
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.sortingApproach(s, t)
        