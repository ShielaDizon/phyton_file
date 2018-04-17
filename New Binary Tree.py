#SHIELA B. DIZON
#Binary Tree
#github.com/ShielaDizon
#shiela.dizon1231@gmail.com

class binary_tree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = binary_tree(newNode)
        else:
            tree = binary_tree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = binary_tree(newNode)
        else:
            tree = binary_tree(newNode)
            tree.left = self.left
            self.left = tree


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())


if __name__ == "__main__":
    ela = binary_tree("Panda")
    ela.insertLeft("Peppa Pig")
    ela.insertLeft("Minion")
    ela.setNodeValue("Mr. Bean")
    ela.insertRight("Doraemon")
    ela.insertRight("Spongebob")
    ela.insertLeft("Phineas")
    ela.insertRight("Ferb")
    
    print "Welcome to Binary Tree"
    printTree(ela)
    print "\n THE NODE VALUE IS: ",ela.getNodeValue()
