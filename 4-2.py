# Задайте натуральное число N.
# Напишите программу, которая
# составит список простых множителей числа N
num = int(input ("Введите число "))
print (f"Простые множители числа {num}:")
i=2;
a = {}
while num >1:
    while True:
        if num%i == 0:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
            num=num/i
        else:
            break
    i+=1
if num !=1:
    a[int(num)] = 1
for i in a.keys ():
     if a[i] != 0:
         print (f"{i} в степени {a[i]}")
