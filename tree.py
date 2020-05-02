class node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def setleft(self, left):
        self.left=left

    def setright(self, right):
        self.right=right
p1=node('A')
root=p1
p2=node('B')
p3=node('C')
p4=node('D')
p5=node('E')
p7=node('F')
p1.setleft(p2)
p1.setright(p3)
p2.setleft(p4)
p2.setright(p5)
p3.setright(p7)
def preorder(d):
    if d:
        print(d.value,' ',end='')
        preorder(d.left)
        preorder(d.right)
def inorder(d):
    if d:
        inorder(d.left)
        print(d.value,' ',end='')
        inorder(d.right)
def postorder(d):
    if d:
        postorder(d.left)
        postorder(d.right)
        print(d.value,' ',end='')

print(preorder(root))
print(inorder(root))
print(postorder(root))


