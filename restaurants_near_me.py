def merge_list(x,y): #O(len(x)+len(y))
    result=[]
    i=0
    j=0
    while i < len(x) and j < len(y) :
        if x[i] < y[j]:
            result.append(x[i])
            i+=1
        elif x[i] > y[j]:
            result.append(y[j])
            j+=1
        else:
            result.append(x[i])
            result.append(y[j])

    while i < len(x):
        result.append(x[i])
        i+=1

    while j < len(y):
        result.append(y[j])
        j+=1

    return result


def insert(p,x): # O(len(p)) = O(n)
    m=[]
    m.append(x)
    n=merge_list(p,m)
    return n

class Node:
    def __init__(self,value,parent,left,right):
        self.value=value
        self.parent=parent
        self.left=left
        self.right=right
        self.bst_y=None
        self.bst_y_inorder=None
        
def extremes(p,cord,a,b):
    if a < p[0][cord] and b < p[0][cord] :
        return None,None

    elif a<p[0][cord] and b>p[-1][cord]:
        return p[0],p[-1]
    elif a < p[0][cord] and b >= p[0][cord] and b <= p[-1][cord] :
        c=0
        d=len(p)
        while c<d:
            mid = (c+d)//2
            if b < p[mid][cord]:
                d = mid 
            elif b > p[mid][cord]:
                c = mid + 1
            elif b == p[mid][cord]:
                c = mid
                break

        if b != p[c]:
            right_extreme = p[c-1]
        else:
            right_extreme = p[c]
        return p[0],right_extreme

    elif b > p[-1][cord] and a > p[-1][cord] :
        return None,None
    elif b > p[-1][cord] and a <= p[-1][cord] and a >= p[0][cord]:
        x=0
        y=len(p)
        while x<y:
            mid = (x+y)//2
            if a < p[mid][cord]:
                y = mid 
            elif a > p[mid][cord]:
                x = mid + 1
            elif a == p[mid][cord]:
                x = mid
                break

        left_extreme = p[x]
        return left_extreme,p[-1]

    elif a >= p[0][cord] and a<=p[-1][cord] and b <= p[-1][cord] and b >= p[0][cord]:
        x=0
        y=len(p)
        while x<y:
            mid = (x+y)//2
            if a < p[mid][cord]:
                y = mid 
            elif a > p[mid][cord]:
                x = mid + 1
            elif a == p[mid][cord]:
                x = mid
                break

        left_extreme = p[x]


        c=0
        d=len(p)
        while c<d:
            mid = (c+d)//2
            if b < p[mid][cord]:
                d = mid 
            elif b > p[mid][cord]:
                c = mid + 1
            elif b == p[mid][cord]:
                c = mid
                break

        if b != p[c]:
            right_extreme = p[c-1]
        else:
            right_extreme = p[c]
        if not(left_extreme[cord]>b) and not(right_extreme[cord]<a):
            return left_extreme, right_extreme
        else:
            return None,None


def extremes_index(p,cord,a,b):
    if a < p[0][cord] and b < p[0][cord] :
        return None,None

    elif a<p[0][cord] and b>p[-1][cord]:
        return 0,len(p)-1
    elif a < p[0][cord] and b >= p[0][cord] and b <= p[-1][cord] :
        c=0
        d=len(p)
        while c<d:
            mid = (c+d)//2
            if b < p[mid][cord]:
                d = mid 
            elif b > p[mid][cord]:
                c = mid + 1
            elif b == p[mid][cord]:
                c = mid
                break

        if b != p[c][cord]:
            right_extreme = c-1
        else:
            right_extreme = c
        return 0,right_extreme

    elif b > p[-1][cord] and a > p[-1][cord] :
        return None,None
    elif b > p[-1][cord] and a <= p[-1][cord] and a >= p[0][cord]:
        x=0
        y=len(p)
        while x<y:
            mid = (x+y)//2
            if a < p[mid][cord]:
                y = mid 
            elif a > p[mid][cord]:
                x = mid + 1
            elif a == p[mid][cord]:
                x = mid
                break

        left_extreme = x
        return left_extreme,len(p)-1

    elif a >= p[0][cord] and a<=p[-1][cord] and b <= p[-1][cord] and b >= p[0][cord]:
        x=0
        y=len(p)
        while x<y:
            mid = (x+y)//2
            if a < p[mid][cord]:
                y = mid 
            elif a > p[mid][cord]:
                x = mid + 1
            elif a == p[mid][cord]:
                x = mid
                break

        left_extreme = x


        c=0
        d=len(p)
        while c<d:
            mid = (c+d)//2
            if b < p[mid][cord]:
                d = mid 
            elif b > p[mid][cord]:
                c = mid + 1
            elif b == p[mid][cord]:
                c = mid
                break

        if b != p[c][cord]:
            right_extreme = c-1
        else:
            right_extreme = c
        if not(p[left_extreme][cord]>b) and not(p[right_extreme][cord]<a):
            return left_extreme, right_extreme
        else:
            return None,None



class BinaryStree:
    def __init__(self,pointlist,r):
        
        pointlist.sort(key = lambda m : m[r]) #O(nlog(n)) , n=len(pointlist)
        self.root=Node(pointlist[len(pointlist)//2],None,None,None)



    
        
    def bst(self,P,r): #O(nlog(n))
        P.sort(key = lambda m : m[r]) #O(nlog(n))
        def construct_bst(l1=0,r1=(len(P)//2) ,l2=(len(P)//2) + 1,r2=len(P),parent=self.root):
            if l1 < r1:
                parent.left = Node(P[(l1+r1)//2],parent,None,None)
                construct_bst(l1,((l1+r1)//2),((l1+r1)//2)+1,r1,parent.left)

            if l2 < r2 :
                parent.right = Node(P[(l2+r2)//2],parent,None,None)
                construct_bst(l2,((l2+r2)//2),((l2+r2)//2)+1,r2,parent.right)

            
            
        
        construct_bst(l1=0,r1=(len(P)//2) ,l2=(len(P)//2) + 1,r2=len(P),parent=self.root)

    def get_bst_y(self, node = 1):
        if node == 1:
            node = self.root

        if node.left == None and node.right == None :
            x = node.value
            y=[]
            y.append(x) #O(1)
            w=BinaryStree(y,1) #O(1)
            w.bst(y,1)         #O(1)
            node.bst_y = w 
            node.bst_y_inorder = w.inorder(w.root)     
            return node.bst_y

        elif node.left == None and node.right != None:
            a = self.get_bst_y(node.right)
            b = a.inorder(a.root)
            c = insert(b,node.value)
            d = BinaryStree(c,1)
            d.bst(c,1)
            node.bst_y = d
            node.bst_y_inorder = d.inorder(d.root)   
            return node.bst_y

        elif node.left != None and node.right == None:
            a = self.get_bst_y(node.left)
            b = a.inorder(a.root)
            c = insert(b,node.value)
            d = BinaryStree(c,1)
            d.bst(c,1)
            node.bst_y = d 
            node.bst_y_inorder = d.inorder(d.root)   
            return node.bst_y

        elif node.left != None and node.right != None:
            a=self.get_bst_y(node.left)
            b=self.get_bst_y(node.right)
            c = a.inorder(a.root)
            d = b.inorder(b.root)
            e = merge_list(c,d)
            f = insert(e,node.value)
            g=BinaryStree(f,1)
            g.bst(f,1)
            node.bst_y = g
            node.bst_y_inorder = g.inorder(g.root)   
            return node.bst_y          

    def inorder(self,node): #O(n) , n=no. of keys of subtress rooted at 'node'
        inorder_list=[]
        def inordering(x):
            if x != None:
                inordering(x.left)
                inorder_list.append(x.value)
                inordering(x.right)
        inordering(node)
        return inorder_list


    def get_node(self,x , node = 1):
        if node == 1:
            node = self.root
        if node != None and node.value == x:
           return node
        elif node != None and node.value > x:
            return self.get_node(x,node.left)
        elif node != None and node.value < x:
            return self.get_node(x,node.right)
        elif node == None:
            return None

    
    def ancestor(self,root1,root2):
        node=self.root
        while not((root1.value < node.value and node.value < root2.value) or (root2.value < node.value and node.value < root1.value) or (node == root1) or (node == root2)) :
            if root1.value < node.value and root2.value < node.value :
                node = node.left
            elif root2.value > node.value and root2.value > node.value :
                node = node.right
            elif node.value == root1.value:
                node = root1
            elif node.value == root2.value:
                node = root2
        else:
            return node

    def x_allowed(self,left_root,right_root):
        f=self.ancestor(self.get_node(left_root.value),self.get_node(right_root.value))
        node_l=[]
        subtree_node=[]
        if f != self.get_node(left_root.value) and f != self.get_node(right_root.value):
            node=left_root
            node_l.append(node)
            if node.right != None:
                subtree_node.append(node.right)
            while node.parent != f and node != f:
                if node.parent.left == node :
                    node_l.append(node.parent)
                    if node.parent.right != None:
                        subtree_node.append(node.parent.right)
                    node=node.parent
                elif node.parent.right == node :
                    node=node.parent

            node = right_root
            node_l.append(node)
            if node.left != None:
                subtree_node.append(node.left)
            while node.parent != f and node != f:
                if node.parent.right == node :
                    node_l.append(node.parent)
                    if node.parent.left != None:
                        subtree_node.append(node.parent.left)
                    node=node.parent
                elif node.parent.left == node :
                    node=node.parent
            node_l.append(f)

        elif f == self.get_node(left_root.value) and f != self.get_node(right_root.value):
            node = right_root
            node_l.append(node)
            if node.left != None:
                subtree_node.append(node.left)
            while node.parent != f and node != f:
                if node.parent.right == node :
                    node_l.append(node.parent)
                    if node.parent.left != None:
                        subtree_node.append(node.parent.left)
                    node=node.parent
                elif node.parent.left == node :
                    node=node.parent
            node_l.append(f)
        elif f != self.get_node(left_root.value) and f == self.get_node(right_root.value):
            node=left_root
            node_l.append(node)
            if node.right != None:
                subtree_node.append(node.right)
            while node.parent != f and node != f:
                if node.parent.left == node :
                    node_l.append(node.parent)
                    if node.parent.right != None:
                        subtree_node.append(node.parent.right)
                    node=node.parent
                elif node.parent.right == node :
                    node=node.parent
            node_l.append(f)


        return node_l,subtree_node
      
    def smallest_node(self):
        node = self.root
        while node.left != None:
            node = node.left
        else:
            return node

    def greatest_node(self):
        node = self.root
        while node.right != None:
            node = node.right
        else:
            return node        

    def left_terminal(self,value,node=1):
        if node == 1:
            node = self.root
        if node.value == value :
            return node
        elif node.value > value :
            self.left_terminal(value,node.left)
        elif node.value < value :
            self.left_terminal(value,node.right)

class PointDatabase:
    def __init__(self,pointlist):
        if len(pointlist) != 0 :
            self.size = True
            self.bs_tree=BinaryStree(pointlist,0)
            self.bs_tree.bst(pointlist,0)
            self.bs_tree.get_bst_y()
            pointlist.sort(key = lambda m : m[0])
            self.sorted_x = pointlist
            pointlist_y=[]
            for i in range(len(pointlist)):
                pointlist_y.append(pointlist[i])
            pointlist_y.sort(key = lambda m : m[1])
            self.sorted_y = pointlist_y
        else:
            self.size = False




    def searchNearby(self,c,d):
        if self.size == True :

            n=(c[0],c[1])
            x1,x2 = extremes(self.sorted_x,0,c[0]-d,c[0]+d)
            y1,y2 = extremes(self.sorted_y,1,c[1]-d,c[1]+d)
            ans=[]
            if (x1,x2) != (None,None) and (y1,y2) != (None,None) and (x1 != x2) and (y1 != y2):
                w1,w2 = self.bs_tree.get_node(x1),self.bs_tree.get_node(x2)
                nod,subtree = self.bs_tree.x_allowed(w1,w2)
            
                for i in range(len(nod)):
                    if abs((nod[i].value[1])-(c[1])) < d :
                        ans.append(nod[i].value)

                for j in range(len(subtree)):
                    p1=subtree[j].bst_y_inorder
                    z1,z2 = extremes_index(p1,1,y1[1],y2[1])

                    if z1 == None and z2 == None:
                        continue
                    elif z1 != None and z2 != None:
                        for jack in range(z1,z2+1):
                            ans.append(p1[jack])
                    

            elif (x1,x2) != (None,None) and (y1,y2) != (None,None) and (x1==x2):
                if max (abs(c[0]-x1[0]),abs(c[1]-x1[1])) < d :
                    ans.append(x1)
            elif (x1,x2) != (None,None) and (y1,y2) != (None,None) and (y1==y2):
                if max (abs(c[0]-y1[0]),abs(c[1]-y1[1])) < d :
                    ans.append(x1)
            else:
                pass
        else:
            ans=[]   

        return ans
                








    




