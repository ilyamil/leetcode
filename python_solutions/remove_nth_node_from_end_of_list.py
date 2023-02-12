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


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = head
    fast = head
    for _ in range(n):
        if fast:
            fast = fast.next
        else:
            break
    # in case if n equals to position of first node
    if not fast:
        return slow.next
    
    dummy = ListNode(next=slow)

    while fast.next:
        slow = slow.next
        fast = fast.next

    tmp = slow.next
    slow.next = tmp.next

    return dummy.next


def print_linked_list(node: ListNode):
    tmp = node
    vals = []
    while tmp:
        vals.append(tmp.val)
        tmp = tmp.next
    print(*vals, sep=' -> ')


if __name__ == '__main__':
    test_cases = [
        {'input': create_linked_list([1,2,3,4,5]), 'n': 2, 'output': create_linked_list([1,2,3,5])},
        {'input': create_linked_list([1,2,3,4,5]), 'n': 1, 'output': create_linked_list([1,2,3,4])},
        {'input': create_linked_list([1,2]), 'n': 1, 'output': create_linked_list([1])},
        {'input': create_linked_list([1,2]), 'n': 2, 'output': create_linked_list([2])},
        {'input': create_linked_list([1, 2, 3]), 'n': 3, 'output': create_linked_list([2, 3])},
        {'input': create_linked_list([1, 2, 3]), 'n': 2, 'output': create_linked_list([1, 3])},
        {'input': create_linked_list([1]), 'n': 1, 'output': None}
    ]

    for test_case in test_cases:
        ans = removeNthFromEnd(test_case['input'], test_case['n'])
        print_linked_list(ans)