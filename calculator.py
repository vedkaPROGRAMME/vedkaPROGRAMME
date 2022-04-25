def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2
def sem(n1,n2):
    return n1 % n2


operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "%": sem
}

num1 = int(input("what is the first number?"))
num2 = int(input("what is the second number?"))

for symbol in operation:
    print(symbol)
operation_symbol = input("pick an operation from the above:")
calculation_function = operation%[operation_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")




