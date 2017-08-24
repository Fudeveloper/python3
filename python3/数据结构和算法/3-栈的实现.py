class Stack(object):
    '''栈'''
    def __init__(self):
        self.__list = []
    def push(self, item):
        """放入元素"""
        self.__list.append(item)
    def pop(self):
        """"弹出栈顶元素"""
        return self.__list.pop(0)
    def peek(self):
        """返回栈顶元素"""
        return self.__list[0]
    def is_empty(self):
        return self.__list ==[]

    def size(self):
        return len(self.__list)