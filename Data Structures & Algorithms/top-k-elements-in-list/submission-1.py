class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i, num in enumerate (nums):
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        
        arr = []
        for num, cnt in freq_dict.items():
            arr.append([cnt, num])
        arr.sort()
        arr.reverse()

        return [pair[1] for pair in arr[:k]]