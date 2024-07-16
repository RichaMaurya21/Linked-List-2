## Problem3 (https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1)
class Solution:
    # Function to delete a node without any reference to the head pointer.
    def deleteNode(self, del_node):
        # Copy the value from the next node to the current node
        del_node.data = del_node.next.data
        
        # Update the next pointer to skip the next node
        del_node.next = del_node.next.next
