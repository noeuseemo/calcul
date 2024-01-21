print("здравствуйте, вас приветствует калькулятор!")

num = input("выберите действие, которое вы желаете выполнить (+,-,/,*,**, но если хотите сразу всё, то напишите all)  - ")

a = int(input("ваше первое число - "))
b = int(input("ваше второе число - "))

if num == "+":
    print(f'{a} + {b} = {a+b}')

elif num == "-":
    print (f'{a} - {b}= {a-b}')

elif num == "/":
    print (f'{a} / {b}= {a/b}')

elif num == "*":
    print (f'{a} * {b}= {a*b}')

elif num == "**":
    print(f'{a} в степени {b} будет {a**b}')

elif num == "all":
    print(f'{a} + {b} = {a+b}')
    print (f'{a} - {b}={a-b}')
    print (f'{a} / {b}= {a/b}')
    print (f'{a} * {b}={a*b}')
    print(f'{a} в степени {b} будет {a**b}')
else:
    print("похоже вы написали что-то не то, попробуйте другое")

