number = (int(input("Enter a number: "))) # asking for a number input.
def collatz (number): # defining a function named collatz and giving it a parameter of number.
        if number % 2 == 0: # checking to see if the number inputted is even.
            print(number // 2)
            return number // 2 
        elif number % 2 == 1: 
            result = 3 * number + 1
            print(result)
            return result
while number != 1: # if number is not eqaul to 1 the code will keep going. 
    number = collatz(int(number))