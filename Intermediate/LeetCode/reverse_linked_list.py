'''
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    problem at : https://leetcode.com/problems/reverse-linked-list/description/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pred, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = pred
            pred = curr
            curr = nxt

        return pred