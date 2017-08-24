class  SingleNode(object):
    '''节点'''
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self, node = None):
        self.__head = node
    def is_empty(self):
        '链表是否为空'
        return self.__head == None
    def length(self):
        '链表长度'
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count计数器
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '遍历整个链表'
        cur = self.__head
        while cur != None:
            print(cur.item,end='')
            cur = cur.next

    def add(self, item):
        '链表头部添加元素'
        node = SingleNode(item)
        # node.next = self.__head
        # cur = self.__head
        node.next, self.__head = self.__head, node

    def append(self,item):
        '链表尾部添加元素'
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '指定位置添加元素'
        if pos <= 0:
            self.add(item)
        elif pos >= self.length()-1:
            self.append(item)
        else:
            node = SingleNode(item)
            pre = self.__head
            for i in range(pos - 1):
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '删除节点'
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                # 先判断此节点是否是头节点，如果是，移动__head
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next




    def serach(self, item):
        '查找节点是否存在'
        cur = self.__head
        for i in range(self.length()):
            if cur.item == item:
                return i
            cur = cur.next
        return -1

sl = SingleLinkList()
sl.add(1)
sl.add(2)
sl.add(3)
sl.add(4)
sl.remove(4)
sl.travel()
