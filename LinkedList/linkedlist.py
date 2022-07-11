'''
--- Delete nodes ---
Sentinel Node Approach (Widely used in trees and linked list as pseudo-heads, pseudo-tails, markers of level end)

Algorithm:
    + Initialize sentinel node as ListNode(0)
    + Set it to be the new head: sentinel.next = head
    + Initialize two pointers to track the current node and its predecessor:
        (curr and prev)
    + while curr is not a null pointer:
        - Compare the value of the current node with the value to delete
            + In the values are equal, delete the current node: prev.next = curr.next
            + Otherwise, set predecessor to be equal to the current node
        - Move to the next node: current = current.next
    + Return sentinel.next

'''