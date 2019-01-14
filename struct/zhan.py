'''
栈作为一种数据结构，是一种只能在一端进行插入和删除操作。
它按照先进后出的原则存储数据，先进入的数据被压入栈底，最后的数据在栈顶，需要读数据的时候从栈顶开始弹出数据（最后一个数据被第一个读出来）

在桟的设计中，我们需要定义一个实例属性top。三个实例方法：获取栈顶元素peek()；出桟pop()；入栈push()
'''
#给一个点，我们能够根据这个点知道一些内容
class Node(object):
    def __init__(self,val): #定位的点的值和一个指向
        self.val=val    #指向元素的值,原队列第二元素
        self.next=None   #指向的指针

class stack(object):
    def __init__(self):
        self.top=None #初始化最开始的位置

    def peek(self):  #获取栈顶的元素
        if self.top!=None:  #如果栈顶不为空
            return self.top.val  #返回栈顶元素的值
        else:
            return None

    def push(self,n):#添加到栈中
        n=Node(n)  #实例化节点
        n.next=self.top  #顶端元素传值给一个指针
        self.top=n
        return n.val

    def pop(self):  #退出栈
        if self.top == None:
            return None
        else:
            tmp=self.top.val
            self.top=self.top.next  #下移一位，进行
            return tmp

if __name__=="__main__":
    s=stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print (s.pop())
    print (s.pop())
    print (s.pop())
