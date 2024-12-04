import Back
from Back import dis_calc

try:
 file = open("Back.py", encoding= 'utf-8')
 s = file.readlines()
 print("Файл существует")
file.close()
a = int(input("Введите первый аргумент: "))
b = int(input("Введите второй аргумент: "))
c = int(input("Введите третий аргумент: "))

d = dis_calc(a,b,c)
print("Ответ:", d)

except FileNotFoundedError:
print("Невозможно открыть файл")
