print("Пожалуйста, введите первое число:")  
num_1 = int(input())  
print("Пожалуйста, введите второе число:")  
num_2 = int(input())  
print("Пожалуйста, введите желаемую операцию:")  
op = str(input())  
print("Результат:")  
  
if op == '+':  
    print(num_1 + num_2)  
elif op == '-':  
    print(num_1 - num_2)  
elif op == '*':  
    print(num_1 * num_2)  
elif op == '/':  
    print(num_1 / num_2)
