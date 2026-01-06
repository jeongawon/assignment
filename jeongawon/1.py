def is_balanced_parentheses(s: str) -> bool:
    stack = []

    for ch in s:
        if ch == "(":
            stack.append(ch)   # 여는 괄호 → push
        elif ch == ")":
            if not stack:      # 꺼낼 게 없는데 닫힘
                return False
            stack.pop()        # 짝 맞는 여는 괄호 제거

    return not stack           # 끝났을 때 비어있으면 True...


print(is_balanced_parentheses("(()())"))  # True
print(is_balanced_parentheses("(()"))     # False
print(is_balanced_parentheses("())"))     # False
print(is_balanced_parentheses("(hello(world))"))     # True
print(is_balanced_parentheses(")(abc("))     # False