'''
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

'''

'''
Daily Coding problem solution
'''
import ctypes #provides C compatible data types

class Node(object):
    def __init__(self, val):
        self.val = val
        self.both = 0


class XorLinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = [] # Prevents garbage collection

    def add(self, node):
        print ('node: ', node.val)
        if self.head is None:
            self.head = self.tail = node
        else:
            # the ^, caret symbol is an XOR bitwise operator
            # print (self.tail.val)
            # The id() function returns identity of the object. This is an integer which is unique for the given object and remains constant during its lifetime.
            # print ('id node: ', id(node))
            # print ('self tail both: ', self.tail.both)
            self.tail.both = id(node) ^ self.tail.both
            # print ('self tail both: ', self.tail.both)
            node.both = id(self.tail)
            self.tail = node

        self.__nodes.append(node)

    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = id(node)
                node = __get_obj(next_id)
            else:
                raise IndexError('Linked list index out of range')
        return node


    def output_list(self):
        for n in self.__nodes:
            print (n.val)


def __get_obj(id):
    # this is the opposite of id() to find out what object is associated to an id number
    # cast() is used for assigning pointers between a value and a type
    return ctypes.cast(id, ctypes.py_object).value

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')

track = XorLinkedList()

for current_node in [node1, node2, node3]:
    track.add(current_node)
    # print (track.output_list())


track.output_list()



'''
Alternative more involved solution
'''

# class ListNode:
#     def __init__(self, data):
#         "constructor class to initiate this object"
#
#         # store data
#         self.data = data
#
#         # store reference (next item)
#         self.next = None
#
#         # store reference (previous item)
#         self.previous = None
#         return
#
#     def has_value(self, value):
#         "method to compare the value with the node data"
#         if self.data == value:
#             return True
#         else:
#             return False
#
# class DoubleLinkedList:
#     def __init__(self):
#         "constructor to initiate this object"
#
#         self.head = None
#         self.tail = None
#         return
#
#     def list_length(self):
#         "returns the number of list items"
#
#         count = 0
#         current_node = self.head
#
#         while current_node is not None:
#             # increase counter by one
#             count = count + 1
#
#             # jump to the linked node
#             current_node = current_node.next
#
#         return count
#
#     def output_list(self):
#         "outputs the list (the value of the node, actually)"
#         current_node = self.head
#
#         while current_node is not None:
#             print(current_node.data)
#
#             # jump to the linked node
#             current_node = current_node.next
#
#         return
#
#     def unordered_search (self, value):
#         "search the linked list for the node that has this value"
#
#         # define current_node
#         current_node = self.head
#
#         # define position
#         node_id = 1
#
#         # define list of results
#         results = []
#
#         while current_node is not None:
#             if current_node.has_value(value):
#                 results.append(node_id)
#
#             # jump to the linked node
#             current_node = current_node.next
#             node_id = node_id + 1
#
#         return results
#
#     def add_list_item(self, item):
#         "add an item at the end of the list"
#
#         if isinstance(item, ListNode):
#             if self.head is None:
#                 self.head = item
#                 item.previous = None
#                 item.next = None
#                 self.tail = item
#             else:
#                 self.tail.next = item
#                 item.previous = self.tail
#                 self.tail = item
#
#         return
#
#
# # create three single nodes
# node1 = ListNode(15)
# node2 = ListNode(8.2)
# node3 = ListNode("Berlin")
# node4 = ListNode(15)
#
# track = DoubleLinkedList()
# print("track length: %i" % track.list_length())
#
# for current_node in [node1, node2, node3, node4]:
#     track.add_list_item(current_node)
#     print("track length: %i" % track.list_length())
#     track.output_list()

# results = track.unordered_search(15)
# print(results)
#
# track.remove_list_item_by_id(4)
# track.output_list()
