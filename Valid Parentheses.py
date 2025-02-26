def isValidParenthesis(s):
    stack = []
    valid_para = {')': '(', '}': '{', ']': '['}
    for i in s:
        if i in valid_para:
            if stack and stack[-1] == valid_para[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return not stack

isValidParenthesis('()')
