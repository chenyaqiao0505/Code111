# class Node(object):
#     def __init__(self,val):
#         self.Next = None
#         self.val = val
#
# class stack(object):
#     def __init__(self):
#         self.top = None
#
#     def peek(self):         #获取栈顶元素
#         if self.top != None:
#             return self.top.val
#         else:
#             return None
#
#     def push(self,n):       #添加栈内
#         n =Node(n)
#         n.next = self.top
#         self.top = n
#         return n.val
#
#     def pop(self):          #抛出栈
#         if self.top == None:
#             return None
#         else:
#             tmp = self.top.val
#             self.top = self.top.Next
#             return tmp
# if __name__ == '__main__':
#     s = stack()
#     s.push(1)
#     s.push(333)
#     s.push(22)
#
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())

# class Node(object):
#     def __init__(self,val):
#         self.val = val
#         self.next = None
# class stack(object):
#     def __init__(self):
#         self.top = None
#     def peek(self):
#         if self.top != None:
#             return self.top.val
#         else:
#             return None
#     def push(self,n):
#         n = Node(n)
#         n.next = self.top
#         self.top = n
#         return n.val
#     def pop(self):
#         if self.top == None:
#             return None
#         else:
#             tmp = self.top.val
#             self.top = self.top.next
#             return tmp
# if __name__ == '__main__':
#     s = stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())



class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
class Stack(object):
    def __init__(self):
        self.top = None
    def peek(self):
        if self.top == None:
            return None
        else:
            return self.top.val
    def push(self,n):
        n = Node(n)
        n.next = self.top
        self.top = n
        return n.val
    def pop(self):
        if self.top == None:
            return None
        else:
            tmp = self.top.val
            self.top = self.top.next
            return tmp
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())