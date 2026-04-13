class Solution:
    def bruteForce(self, s: str, t: str) -> bool:
        # Doesn't work stupid, just because a character exists won't make it work, DUH!
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
        return sorted(s) == sorted(t)

    def dictionaryApproach(self, s: str, t: str) -> bool:
        # doesn't work should have thought about this s and t both will have duplicates inside them making count even
        count_dict = {}
        for i in range (len(s)):
            if s[i] in count_dict:
                count_dict[s[i]] += 1
            else:
                count_dict[s[i]] = 1
        for i in range (len(t)):
            if t[i] in count_dict:
                count_dict[t[i]] -= 1
            if t[i] not in count_dict or count_dict[t[i]] < 0:
                return False
        
        return True
    
    # O(1) space and most optimal approach
    def optimalApproach(self, s: str, t: str) -> bool:
        char_counts = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            char_counts[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            char_counts[index] -= 1
            if char_counts[index] < 0:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.optimalApproach(s, t)
        