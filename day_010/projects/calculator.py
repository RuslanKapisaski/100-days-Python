logo = ''' 
__________
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|    
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------"  '''


def add(n_1,n_2):
    return n_1 + n_2

def subtract(n_1, n_2):
    return n_1 - n_2

def multiply(n_1,n_2):
    return n_1 * n_2

def divide(n_1,n_2):
    return n_1 / n_2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
answer = 0
first_num = float(input("What is your first number? "))
def calculator():
    global answer
    global first_num
    while True:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        second_num = float(input("What is the next number?: "))
        answer = operations[operation](first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {answer}")

        command = input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation: ")

        if command.lower() == 'n':
          break
        elif command.lower() != 'y':
             print("Unknown command. Please try again later.")
        else:
            first_num = answer
            print(f"\n * 20")
            calculator()

calculator()






