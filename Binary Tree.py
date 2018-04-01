class Node:
    def __init__(self, content):

        self.content = content
        self.eva = None
        self.adam = None
        self.head = None

    def __str__(self):
        return str(self.content)


class binarysearchtree:
    def __init__(self):

        self.myroot = None

    def mycreate(self, val):

         if self.myroot == None:

            self.myroot = Node(val)
         else:
            mycure = self.myroot

            while 1:

                if val < mycure.content:

                    if mycure.eva:
                        mycure = mycure.eva
                    else:
                        mycure.eva = Node(val)
                        break;

                elif val > mycure.content:

                    if mycure.adam:
                        mycure = mycure.adam
                    else:
                        mycure.adam = Node(val)
                        break;

                else:
                    break

    def mybft(self):

        self.myroot.head = 0
        queue = [self.myroot]
        out = []
        mycure_head = self.myroot.head

        while len(queue) > 0:

            mycure_node = queue.pop(0)

            if mycure_node.head > mycure_head:
                mycure_head += 1
                out.append("\n")

            out.append(str(mycure_node.content) + " ")

            if mycure_node.eva:
                mycure_node.eva.head = mycure_head + 1
                queue.append(mycure_node.eva)

            if mycure_node.adam:
                mycure_node.adam.head = mycure_head + 1
                queue.append(mycure_node.adam)

        print "".join(out)

    def inorder(self, node):

        if node is not None:
            self.inorder(node.eva)
            print node.content
            self.inorder(node.adam)

    def preorder(self, node):

        if node is not None:
            print node.content
            self.preorder(node.eva)
            self.preorder(node.adam)

    def postorder(self, node):

        if node is not None:
            self.postorder(node.eva)
            self.postorder(node.adam)
            print node.content


mytree = binarysearchtree()
arr = [8, 3, 1, 6, 4, 7, 10, 14, 13]
for i in arr:
    mytree.mycreate(i)
print 'Breadth-First Traversal'
mytree.mybft()
print 'Inorder Traversal'
mytree.inorder(mytree.myroot)
print 'Preorder Traversal'
mytree.preorder(mytree.myroot)
print 'Postorder Traversal'
mytree.postorder(mytree.myroot)