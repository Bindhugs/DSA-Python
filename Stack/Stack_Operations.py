stack = [None]*5
top = -1

while True:
    print("\nMenu\n")
    print("1. Push\n")
    print("2. Pop\n")
    print("3. Display\n")
    print("4. Exit \n")
    choice = input("Enter your choice: ")
    
    #Push    
    if choice == "1":
        if top == len(stack)-1:
            print("Stack Overflow")
            # Stack is full
        else:
            value = input("Enter elements: \n")
            top = top + 1
            stack[top] = value
            print("Element entered into stack:", value)
            #inserts element to stack
    
    #Pop
    elif choice == "2":
        if top == -1:
            print("Stack Underflow")
            #Stack is empty
        else:
            value = stack[top]
            top = top-1
            print("Popped Element from the stack is: ",value)
            #Popping element from the stack
    
    #Display
    elif choice == "3":
        if top == -1:
            print("Stack is empty. Enter some elements into the stack first: \n")
            #Stack is empty 
        else:
            print("Stack elements: \n")
            for i in range(top,-1,-1):
                print(stack[i])
                #prints all the element in the stack
    
    #Exit
    elif choice == "4":
        print("Program ending: ")
        break

    #Wrong choice
    else:
        print("INVALID CHOICE!!")
