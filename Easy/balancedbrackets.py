def isBalanced(s):
    stack=[]
    pairs={"{":"}","(":")","[":"]"}
    for i in s:
        if not stack:
            stack.append(i)
        if i==pairs.get(stack[-1]):
            stack.pop()
        else:
            stack.append(i)
    return "NO" if stack else "NO"
print(isBalanced("}][}}(}][))]"))