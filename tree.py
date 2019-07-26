class Tree:
    def __init__(self):
        self.root=None
    def insert(self,info):
       
        if isinstance(self,Tree):
            if self.root==None:
                temp1=Node(info)
                self.root=temp1
                return
            else:
                self.balinsert(self.root,info)
    def balinsert(self,root,info):
        if root==None:
            
            root=Node(info)
            return root
            
        if info>root.data:
           
            root.right=self.balinsert(root.right,info)
        else:
            
            root.left=self.balinsert(root.left,info)
           
        root.height=max(self.getheight(root.left),self.getheight(root.right))+1
        bf=self.balancedft(root)
        
        if bf>1 and info<root.left.data:
            print(root.data)
            if self.root is root:
                self.root=self.rightRotate(root)
                root=self.root
            else:
                root=self.rightRotate(root)
        if bf<-1 and info>root.right.data:
            if self.root is root:    
                self.root=self.leftRotate(root)
                root=self.root
            else:
                root=self.leftRotate(root)
        if bf>1 and info>root.left.data:
            root.left = self.leftRotate(root.left)
            if self.root is root:
                self.root=self.rightRotate(root)
                root=self.root
            else:
                root=self.rightRotate(root)
        if bf<-1 and info<root.right.data:
            root.right=self.rightRotate(root.right)
            if self.root is root:
                self.root=self.leftRotate(root)
                root=self.root
            else:
                root=self.leftRotate(root)
        return root
        
    def rightRotate(self,root):
        temp=root.left
        tmp=temp.right
        temp.right=root
        root.left=tmp
        root.height=max(self.getheight(root.left),self.getheight(root.right))+1
        temp.height=max(self.getheight(temp.left),self.getheight(temp.right))+1
        return temp
        
    def leftRotate(self,root):
        temp=root.right
        tmp=temp.left
        temp.left=root
        root.right=tmp
        root.height=max(self.getheight(root.left),self.getheight(root.right))+1
        temp.height=max(self.getheight(temp.left),self.getheight(root.right))+1
        return temp
        
    def getheight(self,temp):
        if temp!=None:
            return temp.height
        return 0
        
    def balancedft(self,root):
       if root!=None:
           return(self.getheight(root.left)-self.getheight(root.right))
       return 0
    
    

    def traversing(self,choice='preorder'):
        if choice=='preoder':
            self.preorder()
        elif choice=='postorder':
            self.postorder()
        elif choice=='inorder':
            self.inorder()
        else:
            print("Wrong Enter")
            
            
    def preorder(self):
        ans=[]
        left=[]
        right=[]
        if self==None:
            return
        if self.root:
            self=self.root
        ans.append(self.data)
        if self.left:
            left=self.left.preorder()
        if self.right:
            right=self.right.preorder()
        return ans+left+right
        
        
    def postorder(self):
        ans=[]
        left=[]
        right=[]
        if self==None:
            return
        if self.root:
            self=self.root
        if self.left:
           left= self.left.preorder()
        if self.right:
            right=self.right.preorder()
        ans.append(self.data)
        return ans+right+left
       

    def inorder(self):
        ans=[]
        left=[]
        right=[]
        if self==None:
            return
        if self.root:
            self=self.root
        if self.left:
            left=self.left.preorder()
        ans.append(self.data)
        if self.right:
            right=self.right.preorder()
        return ans+left+right
    def levelorder(self):
        ans=[]
        queue=[]
        queue.append(self.root)
        while len(queue)!=0:
            temp=queue.pop(0)
            ans.append(temp.data)
            if temp.left!=None:
                queue.append(temp.left)
            if temp.right!=None:
                queue.append(temp.right)
        return ans
        
class Node(Tree):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.root=None
        self.height=1





            
