"""
@version:01.00.00
@Author:Shenglong
@Structure:单链表
#链表基本操作：
(1)isEmpty() 链表为空，返回True
(2)length()  返回链表长度
(3)traver()  遍历打印整个列表
(4)append(node)  尾部添加数据
(5)add(node)     头部添加数据
(6)insert(index,node)  指定位置添加数据
(7)remove(node)  删除数据节点
(8)search(node)  查找数据节点是否存在
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkListOneDir(object):
    def __init__(self, node = None):
        self.__head = node


    def __len__(self):
        cur = self.__head
        count = 0

        while cur:
            count += 1
            cur = cur.next
        return count

    def length(self):
        return len(self)

    def isEmpty(self) -> bool:
        return  self.__head == None


    def traver(self):
        cur = self.__head
        while cur:
            print(cur.value)
            cur = cur.next


    def append(self, value):
        '''
        尾插法

        遍历至为尾节点
        将尾节点的next指向新节点
        :param value:
        :return:
        '''

        node = Node(value)
        cur = self.__head
        if self.isEmpty():
            self.__head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node


    def add(self, value):
        '''
        头插法
        将头结点指向新节点的next
        然后将头结点指向新节点
        :param value:
        :return:
        '''
        node = Node(value)
        node.next = self.__head
        self.__head = node


    def insert(self, index, value):
        '''
        定点插入
        新节点
        将新节点的next 指向当前节点的next
        当前节点的next 指向新节点。
        :param index:
        :param value:
        :return:
        '''
        if index < 0:
            self.add(value)
        elif index > self.__len__() - 1:
            self.append(value)
        else:
            node = Node(value)
            count = 0
            cur = self.__head
            while count < index - 1:
                cur = cur.next
                count += 1
            node .next = cur.next
            cur.next = node


    def remove(self,value):

        '''
        等值移除（移除第一个等值节点）
        注意处理与头结点相等
        记录当前节点与上一节点
        遍历链表，直至等值出现
        将上一节点的next指向当前节点的next
        :param value:
        :return:
        '''
        cur = self.__head
        preNode = None

        while cur:

            if cur.value == value:
                if self.__head == cur:
                    self.__head = cur.next
                else:
                    preNode.next = cur.next
                break
            else:
                preNode = cur
                cur = cur.next


    def search(self, value) -> bool :
        cur = self.__head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False



def main():
    node = LinkListOneDir()

    print("######################")
    node.append(0)
    node.traver()

    print("######################")
    node.add(1)
    node.traver()
    print("size is %d" % node.length())

    print("######################")
    node.insert(1,5)
    node.traver()

    print("######################")
    print(node.isEmpty())

    print("######################")
    node.remove(5)
    node.traver()

    print("######################")
    print(node.search(1))
    print(node.search(5))

if __name__ == '__main__':
    main()