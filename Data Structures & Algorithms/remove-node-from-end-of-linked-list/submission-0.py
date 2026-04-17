# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        arr =[]
        point = head 
        while point:
            arr.append(point)
            point = point.next
        
        length = len(arr)
        remove_index = length - n

        if remove_index == 0:
            return head.next

        prev = arr[remove_index -1]
        prev.next = arr[remove_index].next

        return head




        

