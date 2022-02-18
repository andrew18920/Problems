class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        out = []
        curr = self
        while curr:
            out.append(curr.val)
            curr = curr.next
        return str(out)


def list_to_linkedlist(li: list):
    start = ListNode(li[0])
    c = start
    for v in li[1:]:
        c.next = ListNode(v)
        c = c.next
    return start


def add_two_numbers(l1: ListNode, l2: ListNode):
    start = ListNode(0)
    p, q, curr = l1, l2, start
    carry = 0
    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        addition = x + y + carry
        carry = addition // 10
        curr.next = ListNode(addition % 10)
        curr = curr.next
        if p:
            p = p.next
        if q:
            q = q.next

    if carry:
        curr.next = ListNode(carry)

    return start.next


def main():
    x = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
    y = list_to_linkedlist([9, 9, 9, 9])

    print(f"{add_two_numbers(x, y) = }")


if __name__ == "__main__":
    main()
