"""
Runtime
78ms
Beats 63.48%of users with Python3

Memory
25.87MB
Beats 91.18%of users with Python3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n)
# Space Complexity：O(1)
# Approach 1 ：Due to the use of a LinkedList data structure, it is necessary to find the median value and split it into two lists based on this median. Then, reverse the latter list and subsequently concatenate the two LinkedLists together.
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        # Find the middle value and split it into two lists based on it.
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow

        # Then, reverse the second array.
        pre = None
        current = middle
        
        while current:
            current.next, pre, current = pre, current, current.next
        
        second_head = pre

        # Merge the two lists together.
        first = head
        second = second_head

        while second.next:

            next_pointer = first.next
            first.next = second
            first = next_pointer

            next_pointer = second.next
            second.next = first
            second = next_pointer
