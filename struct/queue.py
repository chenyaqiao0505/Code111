# class Node(object):
#     def __init__(self,val):
#         self.next = None
#         self.val = val
# class queue(object):
#     def __init__(self):
#         self.first = None
#         self.last = None
#
#     def enter(self,n):
#         n = Node(n)
#         if self.first == None:
#             self.first = n
#             self.last = self.first
#         else:
#             self.last.next = n
#             self.last = n
#
#     def quit(self):
#         if self.first == None:
#             return None
#         else:
#             tem = self.first.val
#             self.first = self.first.next
#         return tem
#
#     def quitall(self):
#         lists = []
#         while self.first != None:
#             lists.append(self.first.val)
#             self.first = self.first.next
#         return lists
# if __name__ == '__main__':
#     q = queue()
#     q.enter(1)
#     q.enter(2)
#     q.enter(3)
#     q.enter(4)
#     q.enter(5)
#     q.enter(6)
#
#     print(q.quitall())


class Node(object):
    def __init__(self,val):
        self.next = None
        self.val = val
class queue(object):
    def __init__(self):
        self.first = None
        self.last = None
    def enter(self,n):
        n = Node(n)
        if self.first == None:
            self.first = n
            self.last = self.first
        else:
            self.last.next = n
            self.last = n
    def quit(self):
        if self.first == None:
            return None
        else:
            tmp = self.first.val
            self.first = self.first.next
            return tmp
    def quitAll(self):
        if self.first == None:
            return None
        else:
            list = []
            while self.first != None:
                list.append(self.first.val)
                self.first = self.first.next
            return list
if __name__ == '__main__':
    q = queue()
    q.enter(1)
    q.enter(2)
    q.enter(3)
    q.enter(4)
    q.enter(5)
    q.enter(6)

    print(q.quitAll())