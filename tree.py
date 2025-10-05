class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

node1=Node('abe')
node2=Node('herb')
node3=Node('homer')
node4=Node('bart')
node5=Node('lisa')
node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5
