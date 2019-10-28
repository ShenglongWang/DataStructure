"""
@version:01.00.00
@Author:Shenglong
#使用类实现数组
#功能：增删改查，判空。
#增：   insertHead()、 在头部插入一个数据
#       insertRear()、 在尾部插入一个数据
#       insertIndex()  在指定索引处插入一个数据，index越界则添加失败返回False

#删：
#       deleteIndex（）  删除指定索引处的数据，重新整理数组，index越界则删除失败返回False
#       deleteHead()     删除头部的数据，重新整理数组
#       deleteRear()     删除尾部的数据，重新整理数组
#       clear()          清空数组

#改
#       modifyIndex()    修改指定index处的数据值，若不超出数组大小，则修改失败并返回False

#查

        index()          返回指定index的数据值，若不存在则抛出异常。
        findAll( value ) 返回值等于value 的index 数组，若没有返回[]。
"""
class Array():
    __size__ = 0
    __array__ = []
    def __init__(self):
        self.__array__ = []
        self.__size__ = 0

    def insertHead(self,value):
        self.__array__.insert(0,value)
        self.__size__ = len(self.__array__)
        return True
    def insertRear(self,value):
        self.__array__.append(value)
        self.__size__ = len(self.__array__)
        return True

    def insertIndex(self,index,value):
        if (index > self.__size__ or index < 0):
            print("The array's length is %d, but index is %d" % (self.__size__,index))
            return False
        else:
            self.__array__.insert(index,value)
            self.__size__ = len(self.__array__)
            return True

    def deleteIndex(self,index):
        if (index > self.__size__ or index < 0):
            print("The array's length is %d, but index is %d" % (self.__size__, index))
            return False
        else:
            self.__array__.pop(index)
            self.__size__ = len(self.__array__)
            return True

    def deleteHead(self):
        return self.deleteIndex(0)

    def deleteRear(self):
        return self.deleteIndex(self.__size__ - 1)

    def clear(self):
        self.__array__ = []
        self.__size__ = len(self.__array__)
        return True


    def modifyIndex(self, index, value):
        if (index > self.__size__ or index < 0):
            print("The array's length is %d, but index is %d" % (self.__size__, index))
            return False
        else:
            self.__array__[index] = value
            self.__size__ = len(self.__array__)
            return True

    def index(self, index):
        if (index > self.__size__ or index < 0):
            print("The array's length is %d, but index is %d" % (self.__size__, index))
        else:
            return self.__array__[index]

    def findAll(self, value):
        resutl = [ x for x in self.__array__ if x == value]
        return resutl

    def __repr__(self):
        return ("The array values is %s" % str(self.__array__))

    def length(self):
        return self.__size__


def main():

    #创建Array对象
    test = Array()

    a = [ x for x in range(10)]

    for x in a:
        #向尾部添加数据
        test.insertRear(x)
    print(test)

    #向头部添加数据
    test.insertHead(11)
    print(test)

    #在index为4的地方加入22
    test.insertIndex(4,22)
    print(test)

    #在超出index的地方加入值55
    test.insertIndex(20,55)
    print(test)

    #删除index为10的值
    test.deleteIndex(10)
    print(test)

    #删除头部元素
    test.deleteHead()
    print(test)

    #删除尾部元素
    test.deleteRear()
    print(test)

    #修改index为0的值为100
    test.modifyIndex(0,100)
    print(test)


    #打印index为10的值
    print(test.index(10))

    #查找值为100

    print(test.findAll(100))


if __name__ == '__main__':
    main()