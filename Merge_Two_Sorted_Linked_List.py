class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

def mergeTwoLists(list1, list2):
    dummy = ListNode(-1)
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return dummy.next

# Taking input for both linked lists
values1 =[1,2,4] #list(map(int, input("Enter sorted values for list1: ").split()))
values2 =[1,3,4] #list(map(int, input("Enter sorted values for list2: ").split()))

list1 = create_linked_list(values1)
list2 = create_linked_list(values2)

# Printing the original linked lists
print("List1:")
print_linked_list(list1)
print("List2:")
print_linked_list(list2)
print('Merged List:')
merged = mergeTwoLists(list1, list2)
print_linked_list(merged)
