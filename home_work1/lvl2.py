print("Пожалуйста, введите первое число:")  
num_1 = int(input())  
print("Пожалуйста, введите второе число:")  
num_2 = int(input())  
print("Пожалуйста, введите желаемую операцию:")  
op = str(input())  
print("Результат:")  
  
  
def add(n1: int, n2: int) -> int:  
    return num_1 + num_2  
  
  
def sub(n1: int, n2: int) -> int:  
    return num_1 - num_2  
  
  
def mul(n1: int, n2: int) -> int:  
    return n1 * n2  
  
  
def div(n1: int, n2: int) -> float:  
    return n1 / n2  
  
  
if op == '+':  
    print(add(num_1, num_2))  
elif op == '-':  
    print(sub(num_1, num_2))  
elif op == '*':  
    print(mul(num_1, num_2))  
elif op == '/':  
    print(div(num_1, num_2))
