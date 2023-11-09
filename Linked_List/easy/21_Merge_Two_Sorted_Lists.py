"""
Runtime
46ms
Beats 38.27%of users with Python3

Memory
16.16MB
Beats 84.74%of users with Python3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n)
# Space Complexity：O(1)
# Approach 1 ：Using a Linked List, compare the elements of the two lists one by one.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()

        while list1 and list2:
            # If an element in list1 is smaller than an element in list2, the pointer should point to the element in list1, and update the current position in list1 and the 'cur' value.
            if list1.val < list2.val:
                cur.next = list1
                list1,cur = list1.next, list1
            else:
                cur.next = list2
                list2,cur = list2.next, list2
        # If one of the two lists still has elements, then point the pointer to the remaining elements.
        if list1 or list2:
            cur.next = list1 if list1 else list2


        return dummy.next
