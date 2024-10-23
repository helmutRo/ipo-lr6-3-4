s = input("введите строку") #ввод строки
x= 0 #счетчик
with open("text.txt") as file: #открывается файл
    file_text = file.read().splitlines() #записывается текст и разбивает на строки
for string in file_text: #смотрит строки
    if s in string: #если в строке есть подстрока то к счетчику +1
        print(string)
        x += 1
print(f"колво строк с подстрокой {s}: {x}") #вывод колва
print("отсортированные в порядке их динны: ", sorted(file_text, key = len)) #вывод отсортированных по длине строк
