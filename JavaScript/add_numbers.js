class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }

    printList() {
        var out = [];
        var curr = this;
        while (curr != null) {
            out.push(curr.val);
            curr = curr.next;
        }
        return out.toString();
    }
}

var listToLinkedList = function (li) {
    var start = new ListNode(li[0]);
    c = start;
    li.slice(1).forEach(v => {
        c.next = new ListNode(v)
        c = c.next
    });
    return start
}

var addTwoNumbers = function (l1, l2) {
    var start = new ListNode(0);
    var [p, q, curr] = [l1, l2, start];
    var carry = 0;
    while (p !== null || q !== null) {
        var x = (p !== null ? p.val : 0);
        var y = (q !== null ? q.val : 0);
        var addition = x + y + carry;
        var carry = Math.floor(addition / 10);
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