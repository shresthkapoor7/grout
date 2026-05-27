class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while n:
            curr = curr.next
            n -= 1
        
        while curr:
            prev = prev.next
            curr = curr.next
        
        prev.next = prev.next.next
        return dummy.next