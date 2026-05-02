class Solution:
    def isPalindrome(self, s: str) -> bool:
        # queue approach, pop front and pop back should be same

        q = deque()
        q = deque(char.lower() for char in s if char.isalnum())

        while q and len(q) > 1:
            if q.pop() != q.popleft():
                return False
        return True