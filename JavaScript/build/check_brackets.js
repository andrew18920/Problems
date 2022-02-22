const checkBrackets = (s) => {
    const brackets = new Map([
        [']', '['],
        ['}', '{'],
        [')', '('],
        ['>', '<'],
    ]);
    const found = [];
    for (let i = 0; i < s.length; i += 1) {
        const ch = s[i];
        if (Array.from(brackets.values()).includes(ch)) {
            found.push(ch);
        }
        else if (brackets.has(ch)) {
            if (found.length === 0 || brackets.get(ch) !== found.pop()) {
                return false;
            }
        }
        else {
            return false;
        }
    }
    return found.length === 0;
};
['<()>', '[', '()[]{}<>', '(]', '([)]'].forEach((s) => {
    console.log(`checkBrackets('${s}') = ${checkBrackets(s)}`);
});
