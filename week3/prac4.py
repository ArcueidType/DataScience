class Node:
    def __init__(self, x) -> None:
        self.Value = x
        self.Next = None
        
class LinkList:
    def __init__(self) -> None:
        self.Head = None
        
    def add(self, value):
        node = Node(value)
        if self.Head == None:
            self.Head = node
        else:
            tmp = self.Head
            while tmp.Next is not None:
                tmp = tmp.Next
            tmp.Next = node
            
    def delete(self, value):
        pre = None
        cur = self.Head
        while cur is not None:
            if cur.Value == value:
                if pre == None:
                    self.Head = cur.Next
                    cur = self.Head
                else:
                    pre.Next = cur.Next
                    cur = pre.Next
            else:
                pre = cur
                cur = cur.Next
        
    def replace(self, origin, new):
        cur = self.Head
        while cur is not None:
            if cur.Value == origin:
                cur.Value = new
            else:
                cur = cur.Next
                
    def find(self, target):
        cnt = 0
        cur = self.Head
        while cur is not None:
            if cur.Value == target:
                return cnt
            else:
                cnt += 1
                cur = cur.Next
        return -1
    
    def showList(self):
        cur = self.Head
        while cur is not None:
            print(cur.Value, end=" ")
            cur = cur.Next
        print("")
        
    
if __name__ == "__main__":
    ll = LinkList()
    ll.add(3)
    ll.add(5)
    ll.add(1)
    ll.showList()
    ll.replace(5, 1)
    ll.showList()
    ll.delete(1)
    ll.showList()
    print(ll.find(3))
    print(ll.find(10))
    
        