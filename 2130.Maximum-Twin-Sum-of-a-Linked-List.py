# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def middle(head):
            slow = fast = head
            while fast and fast.next:
                slow=slow.next
                fast = fast.next.next
            return slow

        stack = []
        mid_next = middle(head)
        temp = mid_next
        while temp:
            stack.append(temp.val)
            temp = temp.next
        ll=head
        length = len(stack)
        sum=0
        for i in range(length):
            sum=max(sum,ll.val + stack.pop())
            ll = ll.next
        return sum

