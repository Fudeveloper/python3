class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        """往队列中添加一个元素"""
        self.__list.append(item)
    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)
    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []
    def qsize(self):
        return len(self.__list)