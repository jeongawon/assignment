def is_balanced_parentheses(s: str) -> bool:
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)      # push
        elif ch == ')':
            if not stack:         # pop할 게 없음
                return False
            stack.pop()           # pop
    return len(stack) == 0        # 남아있으면 '('가 남은 것

print(is_balanced_parentheses("(()())"))  # True
print(is_balanced_parentheses("((()"))     # False
print(is_balanced_parentheses("())"))     # False
print(is_balanced_parentheses("(hello(world))"))     # True
print(is_balanced_parentheses(")(abc("))     # False