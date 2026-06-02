class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def listApproach(s: str, t: str) -> bool:
            # time -> O(n^2), space -> O(n)
            if len(s) != len(t):
                return False
            
            list1 = list(s)
            list2 = list(t)

            for i in range (0, len(s)):
                c = list1[i]
                if c in list2:
                    list2.remove(c)
                else:
                    return False
            
            return len(list2) == 0
        
        def sortingApproach(s: str, t: str) -> bool:
            # time -> O(nlogn), space -> O(n)
            return sorted(s) == sorted(t)
        
        def freqApproach(s: str, t: str) -> bool:
            # time -> O(n), space -> O(n)
            if len(s) != len(t):
                return False
            
            freq = {}
            for c in s:
                freq[c] = freq.get(c, 0) + 1
            
            for c in t:
                if c not in freq:
                    return False
                freq[c] -= 1
                if freq[c] < 0:
                    return False
            return True
            

        return freqApproach(s, t)