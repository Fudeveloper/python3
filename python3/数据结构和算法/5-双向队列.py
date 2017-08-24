class Deque:
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        """往队列中添加一个元素"""
        self.__list.insert(0,item)

    def add_read(self, item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)
    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []
    def qsize(self):
        return len(self.__list)