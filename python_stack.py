#-------------------------------------------------------
# class to implement stack
#-------------------------------------------------------
class Stack:
    # initialize an empty list (stack)
    def __init__(self):
        self.mStack = []

    # function to check if the stack is empty
    def isEmpty(self):
        return self.mStack == []

    # function to push (insert) item into the stack
    def push(self, item):
        self.mStack.append(item)
        print "Inserted item: {}".format(item)

    # function to pop (remove) item out of the stack
    def pop(self):
        if self.isEmpty() == False:
            item = self.mStack.pop()
            print "Removed item : {}".format(item)
        else:
            print "No item in stack"

    # function to view the items in the stack
    def view(self):
        if self.isEmpty() == False:
            for item in self.mStack:
                print item
        else:
            print "No item in stack"

    # function to get the length of stack
    def size(self):
        return len(self.mStack)

    # function to get the top item in stack
    def top(self):
        if self.isEmpty() == False:
            return self.mStack[len(self.mStack)-1]
        else:
            return "No item in stack"

#-------------------------------------------------------
# MAIN function
#-------------------------------------------------------
if __name__ == "__main__":
    # create an instance of the stack class
    mStack = Stack()

    print "---------------------------------"
    print "Implementation of Stack in Python"
    print "---------------------------------"

    print "Menu items"
    print "1. View the stack"
    print "2. Push item into stack"
    print "3. Pop item out of stack"
    print "4. Get the size of stack"
    print "5. Get the top item in stack"
    print "6. Quit the program"

    # keep looping until the user quits the program
    while True:
        # get the user input
        user_input = int(raw_input("Enter the option: "))

        # based on user input, perform any of the operation accordingly
        if user_input == 1:
            mStack.view()
        elif user_input == 2:
            item = (raw_input("Enter the item to be inserted: "))
            mStack.push(item)
        elif user_input == 3:
            mStack.pop()
        elif user_input == 4:
            print mStack.size()
        elif user_input == 5:
            print mStack.top()
        elif user_input == 6:
            break
