class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += '+k+' + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        decoded = s.split('+k+')
        return decoded[1:len(decoded)]
