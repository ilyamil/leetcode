from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values: List[int]) -> ListNode:
    if not values:
        return None

    tmp = ListNode(values[0])
    dummy = ListNode(next=tmp)
    for val in values[1:]:
        tmp.next = ListNode(val)
        tmp = tmp.next
    return dummy.next


def print_linked_list(node: ListNode):
    tmp = node
    vals = []
    while tmp:
        vals.append(tmp.val)
        tmp = tmp.next
    print(*vals, sep=' -> ')


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1

    tmp = ListNode()
    dummy = ListNode(next=tmp)

    while list1 and list2:
        if list1.val < list2.val:
            tmp.next = list1
            list1 = list1.next
        else:
            tmp.next = list2
            list2 = list2.next
        tmp = tmp.next

    while list1:
        tmp.next = list1
        tmp = tmp.next
        list1 = list1.next

    while list2:
        tmp.next = list2
        tmp = tmp.next
        list2 = list2.next

    return dummy.next.next


if __name__ == '__main__':
    l1 = create_linked_list([1,2,4])
    l2 = create_linked_list([1,3,4])
    merged = mergeTwoLists(l1, l2)
    print_linked_list(merged)
