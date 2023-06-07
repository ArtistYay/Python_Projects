def commaCode(): # defined a function
    items = [] #created an empty list for input.
    while True: # while loop will always be true thus continuing. 
        print("Enter an Item" + "(or enter nothing to stop:)") # tells the user the input random words.
        name = input() # user has the option to input.
        if name == "": # if the user doesn't input anything.
            break # the program will stop and continue.
        items = items + [name] # added the user inputs to the empty list.
    print("Items are: ") # letting the user know what items they picked.
    for name in items: 
        print(", " .join(items[0:-1]) + ", and " + items[-1]) # the join() method returns the list as a string. 
commaCode()