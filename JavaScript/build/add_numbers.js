class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
    printList() {
        const out = [];
        let curr = this;
        while (curr != null) {
            out.push(curr.val);
            curr = curr.next;
        }
        return out.toString();
    }
}
const listToLinkedList = (li) => {
    const start = new ListNode(li[0]);
    let c = start;
    li.slice(1).forEach((v) => {
        c.next = new ListNode(v);
        c = c.next;
    });
    return start;
};
const addTwoNumbers = (l1, l2) => {
    const start = new ListNode(0);
    let [p, q, curr] = [l1, l2, start];
    let carry = 0;
    while (p !== null || q !== null) {
        const x = p !== null ? p.val : 0;
        const y = q !== null ? q.val : 0;
        const addition = x + y + carry;
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
const a = listToLinkedList([9, 9, 9, 9, 9, 9, 9]);
const b = listToLinkedList([9, 9, 9, 9]);
console.log(addTwoNumbers(a, b).printList());
