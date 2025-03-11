class Node:
    def __init__(self, data):
        self.data = data
        self.next, self.prev = None, None

double_linked_list = Node(1)
double_linked_list_2 = Node(2)
double_linked_list_2.prev = double_linked_list
double_linked_list.next = double_linked_list_2
print(double_linked_list.data, "double_linked_list.data")
print(double_linked_list.next.data, "double_linked_list_2.data")
print(double_linked_list_2.prev.data, "double_linked_list_2.prev.data")
