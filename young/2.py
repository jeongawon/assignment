def is_balanced_brackets(s: str) -> bool:
    pair = {')': '(', ']': '[', '}': '{'}
    opens = set(pair.values())
    stack = []

    for ch in s:
        if ch in opens:
            stack.append(ch)
        elif ch in pair:  # 닫는 괄호
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_balanced_brackets("{[()()]}"))  # True
print(is_balanced_brackets("{[(])}"))    # False
print(is_balanced_brackets("([)]"))      # False
print(is_balanced_brackets('''{
  "id": "user-001",
  "name": "Jinyoung Choi",
  "active": true,
  "createdAt": "2026-01-03T10:30:00Z",
  "projects": [
    {
      "projectId": "p-100",
      "title": "Cloud Migration",
      "status": "in-progress"
    },
    {
      "projectId": "p-200",
      "title": "DevOps Automation",
      "status": "completed"
    }
  ]
}
'''))     # False