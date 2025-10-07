def my_func(data: str, lvl: int):  
    if lvl == 1:  
        print("Пожалуйста, выберете желаемый метод (upper, lower, capitalize):", end=' ')  
        action1 = str(input())  
        if action1 == "upper":  
            return data.upper()  
        elif action1 == "lower":  
            return data.lower()  
        else:  
            return data.capitalize()  
    elif lvl == 2:  
        print("Пожалуйста, выберете желаемый метод (find, replace, count):", end=' ')  
        action2 = str(input())  
        if action2 == "find":  
            print("Пожалуйста, введите слово, которое первое вхождение, которого вы хотите найти:", end=' ')  
            word = str(input())  
            ans = data.find(input())  
            return ans  
        elif action2 == "replace":  
            print("Пожалуйста, введите слово, которое хотите ЗАМЕНИТЬ:", end=' ')  
            word1 = str(input())  
            print("Пожалуйста, введите слово, НА которое вы хотите ЗАМЕНИТЬ:", end=' ')  
            word2 = str(input())  
            ans = data.replace(word1, word2)  
            return ans  
        elif action2 == "count":  
            print("Пожалуйста, введите то, что хотите ПОСЧИТАТЬ:", end=' ')  
            word = input()  
            ans = data.count(word)  
            return ans  
    elif lvl == 3:  
        print("Пожалуйста, выберете желаемый метод (split, join):", end=' ')  
        action3 = input()  
        if action3 == "split":  
            print("Пожалуйста, введите желаемый разделитель:", end=' ')  
            return data.split(input())  
        elif action3 == "join":  
            print("Пожалуйста, введите желаемый разделитель:", end=' ')  
            return data.join(input())  
    elif lvl == 4:  
        print("Пожалуйста, выберете желаемый метод (isdigit, isalpha):", end=' ')  
        action4 = input()  
        if action4 == "isdigit":  
            return data.isdigit()  
        elif action4 == "isalpha":  
            return data.isalpha()  
    elif lvl == 5:  
        text = "   pYthon;is;AWesome;   "  
        data = data.replace(" ", "")  
        data = data.split(";")  
        data = ' '.join(data)  
        data = data.capitalize()  
        return data  
  
  
print("Пожалуйста, желаемый уровень:")  
lvl = int(input())  
print("Пожалуйста, введите вашу строку:")  
data = str(input())  
print(my_func(data, lvl))
