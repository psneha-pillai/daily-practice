class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def createlinkedlist(arr):
    head = None
    temp = None
    for data in arr:
        if head is None:
            head = Node(data)
            temp = head
        else:
            temp.next = Node(data)
            temp = temp.next
    return head

def printlinkedlist(head):
    temp = head
    while temp:
        print(str(temp.val), end=" --> ")
        temp = temp.next
    print("None")

# Driver code
arr = list(map(int, input("Enter elements of the linked list: ").split()))
head = createlinkedlist(arr)
printlinkedlist(head)

 
        
                    
            
