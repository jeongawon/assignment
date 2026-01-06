def is_balanced_brackets(s: str) -> bool:
    stack=[]

    #닫는 괄호 -> 여는 괄호 매핑
    pair = {
        ')': '(',
        ']': '[' ,
        '}': '{'
    }
    for ch in s:
        #여는 괄호면 stack에 push
        if ch in "([{":
            stack.append(ch)
        #닫는 괄호면
        elif ch in ")]}":
            # stack에 비어있으면 False 
            if not stack:
                return False
            # 가장 최근 여는 괄호 꺼내기
            top = stack.pop()  # 맨 끝 즉, 가장 최근에 들어간 것을 꺼내서  top이라는 변수에 저장 그리고 나서 그 꺼낸 괄호가 짝이 맞는 지를 확인

            #짝이 맞는지 확인
            if pair[ch] !=top: # 짝이 같지 않으면 False  
                return False
    # 끝났을 때 stack에 비어있으면 성공임
    return not stack

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
'''))                                     # True