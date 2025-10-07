class Calculator:  
    def __init__(self, n1: int, n2: int, op: str):  
        self.n1 = n1  
        self.n2 = n2  
        self.op = op  
  
    def calc(self):  
        if op == "+":  
            return self.n1 + self.n2  
        elif op == "-":  
            return self.n1 - self.n2  
        elif op == "*":  
            return self.n1 * self.n2  
        elif op == "/":  
            return self.n1 // self.n2  
  
    def eng_calc(self):  
        print("Ведется разработка")  
  
  
print("Пожалуйста, введите первое число:")  
num_1 = int(input())  
print("Пожалуйста, введите второе число:")  
num_2 = int(input())  
print("Пожалуйста, введите желаемую операцию:")  
op = str(input())  
print("Результат:")  
calc_e = Calculator(num_1, num_2, op)  
print(calc_e.calc())
