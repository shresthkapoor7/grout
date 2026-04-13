class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i, num in enumerate (nums):
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in freq_dict[:k]]