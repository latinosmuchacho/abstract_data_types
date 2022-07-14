from stack import Stack
from queue import Queue


# s = Stack()
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())


def revstring(mystr):
    s = Stack()
    for letter in mystr:
        s.push(letter)
    reverse_str = ""
    while not s.isEmpty():
        reverse_str += s.pop()
    return reverse_str


# my_str = 'abcdefg'
# print(revstring(my_str))


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = '([{'
    closers = ")]}"
    return opens.index(open) == closers.index(close)

# print(parChecker('{{([][])}()}'))
# print(parChecker('[{()]'))


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber //= 2

    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString

# print(divideBy2(42))


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base

    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString

# print(baseConverter(25,2))
# print(baseConverter(25,16))
# print(baseConverter(25,8))
# print(baseConverter(256,16))


def infixToPosfix(infixexpr):
    prior = {}
    prior["*"] = 3
    prior["/"] = 3
    prior["+"] = 2
    prior["-"] = 2
    prior["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prior[opStack.peek()] >= prior[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

# print(postfixEval('7 8 + 3 2 + /'))


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
        
    return simqueue.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))