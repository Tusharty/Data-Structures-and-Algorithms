#!/usr/bin/env python
"""
Given a sorted linked list, delete all duplicates such that each element appears
only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->, return 1->2->3.
"""

from LinkedList import LinkedListNode

head = LinkedListNode(1)
head.next = LinkedListNode(1)
head.next.next = LinkedListNode(2)


# @params {LinkedListNode} head of a linked list

def remove_duplicates(head):
    if not head or not head.next:
        return head

    slow_pointer = head            #assign head to slow pointer vatriable
    fast_pointer = head.next        #assign next from head to fast_pointer variable

    while fast_pointer:
        if slow_pointer.data == fast_pointer.data:   #if head and next matches
            slow_pointer.data = fast_pointer.data
            fast_pointer = fast_pointer.next
        else:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
    return head

if __name__ == '__main__':
    print (remove_duplicates(head))