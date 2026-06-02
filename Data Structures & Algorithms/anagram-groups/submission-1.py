class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        answer = []
        for i in range (0, len(strs)):
            c = ''.join(sorted(strs[i]))
            if c in freq:
                freq[c].append(strs[i])
            else:
                freq[c] = [strs[i]]

        for key, value in freq.items():
            answer.append(value)
        return answer