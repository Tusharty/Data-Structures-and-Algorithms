#!/usr/bin/env python

"""
Write code to remove duplicates from an unsorted linked list
How would you solve this problem if a temporary buffer is not allowed?
"""
import random
from linked_list import LinkedListNode


def delete_duplicates(linked_list_node)
  
    if not linked_list_node:
        return

    current_node = linked_list_node
    already_found = {}
    previous_node = None
    while current_node != None:
        # it is impossible for the first node to have already been found
        if current_node.data in already_found:
            previous_node.next = current_node.next
        else:
            already_found[current_node.data] = 1
            previous_node = current_node
        current_node = current_node.next

    return str(linked_list_node)


def delete_dup_no_buffer(linked_list_node):
    if not linked_list_node:
        return

    current_pointer = linked_list_node
    forward_pointer = linked_list_node
    while current_pointer.next != None:
        while forward_pointer.next != None:
            if forward_pointer.next.data == current_pointer.data:
                forward_pointer.next = forward_pointer.next.next
            else:
                forward_pointer = forward_pointer.next

        current_pointer = current_pointer.next
        forward_pointer = current_pointer

    return str(linked_list_node)


root = LinkedListNode(5)
current_node = root
for i in range(0, 10):
    random_key = random.randint(0, 10)
    new_node = LinkedListNode(random_key)
    current_node.next = new_node
    current_node = new_node

print("Original list: " + str(root))
print("Unique list 1: " + delete_duplicates(root))
print("Unique list 2: " + delete_dup_no_buffer(root))