from collections import deque
import operator


def evaluatePostfix(S):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul
    }

    st = deque()
    for ch in S:
        if ch in "+-/*":
            operand2 = int(st.pop())
            operand1 = int(st.pop())
            st.append(operators[ch](operand1, operand2))
        else:
            st.append(ch)
    return int(st[0])


def oprPrecedence(operator):
    if (operator == '+' or operator == '-'):
        return 1
    elif (operator == '*' or operator == '/'):
        return 2
    elif (operator == '^'):
        return 3
    else:
        return -1


def infixToPostfix(exp):
    st = deque()
    res = ""

    for ch in exp:
        if (ch in '+-*/^'):
            while (st and oprPrecedence(st[-1]) >= oprPrecedence(ch)):
                res += st.pop()
            st.append(ch)

        elif (ch == '('):
            st.append(ch)

        elif (ch == ')'):
            while (st and st[-1] != '('):
                res += st.pop()
            if (st):
                st.pop()

        else:
            res += ch

    while (st):
        res += st.pop()
    return res


if __name__ == '__main__':
    S = "123+*8-"
    print(evaluatePostfix(S))
