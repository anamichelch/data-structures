class Node: #node is an element is the list
    def __init__(self, data=None, next=None, prev=None):
        #data can be an integer
        #next is a pointer for the next element
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        #head of the linkes list
        self.head = None

    def insert_at_begining(self, data):
        #create an element "node"
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        iterator = self.head
        lstring = ""

        while iterator:
            lstring += str(iterator.data) + "-->"
            iterator = iterator.next
        print(lstring)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head # to start at the beggining of the items
        while itr.next: #while itr next is not Null, will keep iterating
            itr = itr.next #sets Iterator into the next element
        itr.next = Node(data,None, None) #when there is no next element, will create this element with last data enetered in fucntion and set as latest element

    def insert_values(self, values):
        self.head = None #wiping all current values to insert new ones
        for value in values:
            self.insert_at_end(value) #add with previous method

    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_lenght():
            raise Exception ("invalid index")
        if index == 0: #if want to remove head, just set it as next element
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1: #i am looking for the previous element so i can use itr.next and land on the precise leement i need
                itr.next = itr.next.next #itr.next would be the element on the index, and i am converting to be the next element
                break

            itr = itr.next
            count += 1

    def insert_at(self, data, index):
        if index<0 or index > self.get_lenght():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1: #i am looking for the previous element so i can use itr.next and land on the precise leement i need
                node = Node(data, itr.next)
                itr.next = node #itr.next would be the element on the index, and i am converting to be the input data
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, value_after, data):
        if self.head is None:
            return

        if self.head.data == value_after:
            new_node = Node(data,self.head.next)
            self.head.next = new_node


        current_node = self.head

        while current_node:
            if current_node.data == value_after:
                new_node = Node(data,current_node.next)
                current_node.next = new_node
                break

            current_node = current_node.next

    def remove_by_value(self, value_after):
        if self.head is None:
            return

        if self.head.data == value_after:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data == value_after:
                current_node.next = current_node.next.next
                break

            current_node = current_node.next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            return print("Linked list is empty")

        current_node = self.head
        llstr = ""

        while current_node:
            llstr += str(current_node.data) + "-->"
            current_node = current_node.next
        print(llstr)
    # This method prints list in forward direction. Use node.next

    def print_backward(self):
        if self.head is None:
            return print("Linked List is empty")

        last_node = self.get_last_node()
        current_node = last_node
        llstr = ""
        while current_node:
            llstr += current_node.data + "<--"

            current_node = current_node.prev
        print(f"{llstr}")

    def get_last_node(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    def get_lenght(self):
        if self.head is None:
            return print("Empty Linked List")
        index = 0
        current_node = self.head
        while current_node.next:
            index += 1
            current_node = current_node.next

        return index+1

    def insert_at_begining(self, value):
        new_node = Node(value, self.head, None)
        self.head = new_node

    def insert_values(self, values):
        self.head = None #wipe clean all elements
        for value in values:
            self.insert_at_end(value)

    def insert_at_end(self,value):
        if self.head is None:
            self.head = Node(value,None,None)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value, None, current_node)



    def insert_at(self, index, value):
        if self.head is None:
            self.insert_at_begining()
        if index<0 or int(index) > int(self.get_lenght()):
            raise Exception ("invalid Index")
        if index == 0:
            self.insert_at_begining(value)
        current_index = 0
        current_node = self.head
        while current_node.next:
            current_index += 1

            if index == current_index:
                new_node = Node(value,current_node.next,current_node)
                current_node.next = new_node
                break
            current_node = current_node.next


    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
        if index<0 or index > self.get_lenght():
            raise Exception("Invalid Index")

        current_index = 0
        current_node = self.head
        while current_node.next:
            if index == current_index+1:
                current_node.next = current_node.next.next
                break
            current_index += 1
            current_node = current_node.next


if __name__=='__main__':
    ll = LinkedList()

ll = DoublyLinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.get_lenght()
ll.print_forward()
ll.print_backward()
ll.insert_at_end("figs")
ll.print_forward()
ll.insert_at(0, "jackfruit")
ll.print_forward()
ll.insert_at(6, "dates")
ll.print_forward()
ll.insert_at(2, "kiwi")
ll.print_forward()
ll.remove_at(2)
ll.print_forward()