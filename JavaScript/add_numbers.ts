class ListNode {
    val: number;
    next: ListNode;

    constructor(val = 0, next: ListNode = null) {
        this.val = val;
        this.next = next;
    }

    printList() {
        var out = [];
        var curr: ListNode = this;
        while (curr != null) {
            out.push(curr.val);
            curr = curr.next;
        }
        return out.toString();
    }
}

var listToLinkedList = (li: number[]) => {
    const start = new ListNode(li[0]);
    let c = start;
    li.slice(1).forEach(v => {
        c.next = new ListNode(v)
        c = c.next
    });
    return start
}

var addTwoNumbers = (l1: ListNode, l2: ListNode) => {
    const start = new ListNode(0);
    let [p, q, curr] = [l1, l2, start];
    let carry = 0;
    while (p !== null || q !== null) {
        let x = (p !== null ? p.val : 0);
        let y = (q !== null ? q.val : 0);
        let addition = x + y + carry;
        carry = Math.floor(addition / 10);
        curr.next = new ListNode(addition % 10);
        curr = curr.next;
        if (p != null) {
            p = p.next;
        }
        if (q != null) {
            q = q.next;
        }
    }

    if (carry > 0) {
        curr.next = new ListNode(carry);
    }

    return start.next;
};

const a = listToLinkedList([9, 9, 9, 9, 9, 9, 9])
const b = listToLinkedList([9, 9, 9, 9])
console.log(addTwoNumbers(a, b).printList());