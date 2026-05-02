class Solution:
    def isPalindrome(self, s: str) -> bool:
        # magic
        
        normal = "".join(c for c in s if c.isalnum()).lower()
        return normal == normal[::-1]