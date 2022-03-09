from main import Stack

stack = Stack()


def brackets_balance(some_string):
    brackets_list = ['(', ')', '[', ']', '{', '}']
    brackets_dict = {')': '(', '}': '{', ']': '['}

    if len(some_string) % 2 != 0:
        print('Несбалансированно1')
        return False

    for char in some_string:
        if char in brackets_list:
            if stack.isEmpty():
                stack.push(char)
            else:
                if stack.peek() == brackets_dict.get(char):
                    stack.pop()
                else:
                    stack.push(char)

    if stack.size() == 0:
        print('Сбалансированно')
        return True
    else:
        print('Несбалансированно2')
        return False


if __name__ == '__main__':
    brackets_balance('[[{())}]')