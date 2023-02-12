from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(
    l1: Optional[ListNode],
    l2: Optional[ListNode]
)-> Optional[ListNode]:
    head = ListNode()
    ans = ListNode(next=head)

    rem = 0
    while l1 and l2:
        cur_sum = l1.val + l2.val + rem
        if cur_sum >= 10:
            rem = 1
            cur_sum -= 10
        else:
            rem = 0
        head.next = ListNode(cur_sum)
        head = head.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        cur_sum = l1.val + rem
        if cur_sum == 10:
            rem = 1
            cur_sum = 0
        else:
            rem = 0
        head.next = ListNode(cur_sum)
        head = head.next
        l1 = l1.next

    while l2:
        cur_sum = l2.val + rem
        if cur_sum == 10:
            rem = 1
            cur_sum = 0
        else:
            rem = 0
        head.next = ListNode(cur_sum)
        head = head.next
        l2 = l2.next

    if rem == 1:
        head.next = ListNode(1)
        head = head.next

    return ans.next.next


def create_linked_list(nodes: List[ListNode]) -> ListNode:
    if len(nodes) == 1:
        return nodes[0]

    tmp = nodes[0]
    dummy = ListNode(next=tmp)
    for node in nodes[1:]:
        tmp.next = node
        tmp = tmp.next
    return dummy.next


def print_linked_list(node: ListNode):
    tmp = node
    while tmp:
        print(tmp.val)
        tmp = tmp.next


if __name__ == '__main__':
    # a = create_linked_list([ListNode(2), ListNode(4), ListNode(3)])
    # b = create_linked_list([ListNode(5), ListNode(6), ListNode(4)])

    # a = create_linked_list([ListNode(2), ListNode(4), ListNode(3), ListNode(7)])
    # b = create_linked_list([ListNode(5), ListNode(6), ListNode(4)])

    # a = create_linked_list([ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9), ListNode(9)])
    # b = create_linked_list([ListNode(9), ListNode(9), ListNode(9), ListNode(9)])

    a = create_linked_list([ListNode(0)])
    b = create_linked_list([ListNode(0)])

    ans = addTwoNumbers(a, b)

    print_linked_list(ans)