"""
Runtime
37ms
Beats 86.12%of users with Python3

Memory
17.67MB
Beats 97.50%of users with Python3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity： O(n)
# Space Complexity：O(1)
# Approach 1 ：Reverse the list by altering the pointers using a LinkedList.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current


        return prev
        