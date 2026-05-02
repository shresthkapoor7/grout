class Solution:
    def isPalindrome(self, s: str) -> bool:
        # queue approach, pop front and pop back should be same

        q = deque()
        for char in s:
            if char.isalnum():
                q.append(char.lower()) # add lower

        print(q)
        while q and len(q) > 1:
            if q.pop() != q.popleft():
                return False

        return True

        