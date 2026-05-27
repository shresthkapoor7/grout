class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mylist = []
        temp = head

        while temp:
            mylist.append(temp)
            temp = temp.next

        if n == len(mylist):
            return head.next
        
        node_to_remove = mylist[len(mylist) - n]
        prev = mylist[len(mylist) - n - 1]
        prev.next = node_to_remove.next
        
        return head
        