class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

def eval_postfix(expr):
    flag = ""
    flags = ""
    import re
    
    token_list = re.split("([^0-9])",expr)
    stack = Stack()
    i=0
    for token in token_list:
        if  token == '' or token == ' ':
            continue
        if token == '+':
           flag = 'sum1'
        stack.push(token)
        if i==2 and flag == 'sum1':
            res=int(stack.pop())+ int(stack.pop())
            stack.push(res)

        if token == '*':
           flags = 'mul1'
        if i==2 and flags == 'mul1':
            res=int(stack.pop())* int(stack.pop())
            stack.push(res)
        i = i + 1
    return stack.pop()
