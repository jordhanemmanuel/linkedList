# Treinamento para fazer Lista Encadeada em Python

class Node:
    def __init__(self, identification, description, next = None):
        self.id = identification
        self.description = description
        self.next = next
		
class LinkedList:
    def __init__(self):
        self.head = None

    # Inclui novo node
    def includeNode(self, identification, description):
        if (self.searchNode(identification)):
            print("ID already exists! ID: "+str(identification))
            return
        newNode = Node(identification, description)
        if(self.head):
            selected = self.head
            while(selected.next):
                selected = selected.next
            selected.next = newNode     
        else:
            self.head = newNode  

    # Imprime node informado
    def printNode(self, data):
        print("ID: "+str(data.id)+"; Description: "+data.description+";")

    # Imprime primeiro node
    def printHead(self):
        data = self.head
        self.printNode(data)

    # Imprime todos os nodes
    def listNodes(self):
        selected = self.head
        while(selected):
            self.printNode(selected)
            selected = selected.next
    
    # Procura node pelo ID
    def searchNode(self, identification):
        selected = self.head
        while(selected):
            if (selected.id == identification):
                return True
            else:
                selected = selected.next
        return False     

    # Atualiza descrição do node informado
    def updateNode(self, identification, description):    
        if (not self.searchNode(identification)):
            print("ID don't exists! ID: "+str(identification))
            return       
        selected = self.head
        while(selected):
            if (selected.id == identification):
                selected.description = description
            selected = selected.next     

    # Remove node pelo ID
    def removeNode(self, identification):
        selected = self.head

        if (selected.id == identification):
            self.head = selected.next
            selected = None
            return

        flag = False
        while (selected):
            if (selected.id == identification): 
                flag = True
                break   
            previous = selected
            selected = selected.next

        if (flag):
            previous.next = selected.next
            selected = None		
			
ll = LinkedList()
ll.includeNode(1, "item 1")            
ll.includeNode(2, "item 2")            
ll.includeNode(3, "item 3")  
ll.listNodes()     
ll.includeNode(2, "updated")
ll.listNodes()			