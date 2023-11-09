"""

"""

# Time complexity: O(n)
# Space Complexity：O(1)
# Approach 1 ：Delete the nth node from the end of a singly linked list.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      
      slow, fast = head, head
      # First, move the fast pointer until it is n nodes apart from the slow pointer.
      while fast.next:
        fast = fast.next
        if n:
          n -= 1
        else:
          slow = slow.next

      # If the value of n is greater than the length of the list, it means that the head node needs to be deleted, in which case return head.next directly.
      if n:
        return head.next
      # Set the 'next' field of the slow pointer to 'slow.next.next', thereby skipping the current 'slow.next' node and accomplishing the deletion.
      slow.next = slow.next.next
      return head