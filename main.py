s = input("введите строку") #ввод строки
x= 0 
with open("text.txt") as file:
    file_text = file.read().splitlines()
for string in file_text:
    if s in string:
        print(string)
        x += 1
print(f"колво строк с подстрокой {s}: {x}")
