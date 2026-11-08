class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def from_values(values):
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def to_values(head):
    values = []
    while head is not None:
        values.append(head.value)
        head = head.next
    return values


def reverse(head):
    previous = None
    while head is not None:
        following = head.next
        head.next = previous
        previous = head
        head = following
    return previous


def merge_sorted(first, second):
    dummy = Node(None)
    tail = dummy
    while first is not None and second is not None:
        if first.value <= second.value:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next
        tail = tail.next

    tail.next = first if first is not None else second
    return dummy.next


def merge_sort(head):
    if head is None or head.next is None:
        return head

    slow, fast = head, head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None

    return merge_sorted(merge_sort(head), merge_sort(second))


if __name__ == "__main__":
    head = from_values([4, 2, 7, 2, 1])
    print("Початковий список:", to_values(head))
    head = reverse(head)
    print("Реверс:", to_values(head))
    head = merge_sort(head)
    print("Сортування:", to_values(head))
    second = from_values([0, 3, 7, 9])
    print("Злиття:", to_values(merge_sorted(head, second)))
