print("Пожалуйста, введите первое число:")  
num_1 = int(input())  
print("Пожалуйста, введите второе число:")  
num_2 = int(input())  
print("Пожалуйста, введите желаемую операцию:")  
op = str(input())  
print("Результат:")  
  
  
def calc(n1: int, n2: int, o: str) -> float:  
    if o == "+":  
        return n1 + n2  
    elif o == "-":  
        return n1 - n2  
    elif o == "*":  
        return n1 * n2  
    else:  
        return n1/n2  
  
  
print(calc(num_1, num_2, op))
