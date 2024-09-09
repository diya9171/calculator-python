def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
def modulus(x,y):
    return x%y
def exponantial(x,y):
    return x**y
def floor_division(x,y):
    return x//y
a=int(input("enter first number: "))
b=int(input("enter second number: ")) 
operators=input("choose any operator: (+ , - , * , / , % ,** , //): ")
match operators:
    case '+':
        print(f"{a} + {b} = {addition(a,b)}")
    case '-':
        print(f"{a} - {b} = {subtraction(a,b)}")
    case '*':
        print(f"{a} * {b} = {multiplication(a,b)}")
    case '/':
        print(f"{a} / {b} = {division(a,b)}")
    case '%':
        print(f"{a} % {b} = {modulus(a,b)}")
    case '**':
        print(f"{a} ** {b} = {exponantial(a,b)}")
    case '//':
        print(f"{a} // {b} = {floor_division(a,b)}")
    case _:
        print("invalid operator")