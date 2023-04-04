"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current_position = 1
        current_element = self.head
        if self.head is None:
            return None
        if position == 0:
            return self.head
        while current_element:
            if current_position == position:
                return current_element

            current_element = current_element.next
            current_position += 1



    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        current_element = self.head
        current_position = 1

        if self.head is None:
            return "empty list"
        if position == 1:
            new_element.next = self.head.next
            self.head = new_element
        while current_element:
            if position-1 == current_position:
                new_element.next = current_element.next
                current_element.next = new_element

            current_position += 1
            current_element = current_element.next

    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.next
        current_value = self.head
        while current_value.next:
            if current_value.next.value == value:
                current_value.next = current_value.next.next
                return
            current_value = current_value.next

    def print_ele(self):
        if self.head is None:
            print("linked list is empty")
            return

        iterator = self.head
        lstring = ""

        while iterator:
            lstring += str(iterator.value) + "-->"
            iterator = iterator.next
        print(lstring)

    # Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)


# Test insert
ll.insert(e4, 3)
ll.print_ele()
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)
ll.print_ele()
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)