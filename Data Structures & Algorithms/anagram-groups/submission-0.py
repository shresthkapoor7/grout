class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        answer = []
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in my_dict:
                my_dict[sorted_word] = [word]
            else:
                my_dict[sorted_word].append(word)
        for group in my_dict:
            answer.append(my_dict[group])
        return answer