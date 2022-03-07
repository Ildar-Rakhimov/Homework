class Stack:
    def __init__(self, some_list=[]):
        self.some_list = some_list

    def isEmpty(self):
        if len(self.some_list) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.some_list.append(element)

    def pop(self):
        if not self.isEmpty():
            self.some_list.pop()
            return self.some_list[-1]
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.some_list[-1]
        else:
            return None

    def size(self):
        return len(self.some_list)

