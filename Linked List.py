#SHIELA B. DIZON
#Linked List with remove duplicates
#github.com/ShielaDizon
#shiela.dizon1231@gmail.com

class Node:
    def __init__(self, contents, next = None):
        self.contents = contents
        self.next = next

    def getContents(self):
        return self.contents

    def setContents(self, val):
        self.contents = val

    def getNext(self):
        return self.next

    def setNext(self, val):
        self.next = val


class Linkedlist:
    def __init__(self, headnode = None):
        self.headnode = headnode
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, contents):
        newNode = Node (contents, self.headnode)
        self.headnode = newNode
        self.size +=1
        return True

    def printNode(self):
        ela = self.headnode
        while ela:
            print(ela.contents)
            ela = ela.getNext()

myList = Linkedlist()
print("Inserting")
print(myList.addNode(5))
print (myList.addNode(15))
print (myList.addNode(25))
print (myList.addNode(35))
print (myList.addNode(45))
print (myList.addNode(55))
print ("Printing")
myList.printNode()
print ("Size")
print (myList.getSize())