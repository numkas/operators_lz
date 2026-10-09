s = 0
#Задаем переменную 
n = int(input ("Введите число "))
if 1<=n<=25:
      if n !=1:
            for i in range(2,n):
                  if n % i == 0:
                        s += 1
            if s >= 1:
                  print("N")
            else:
                  print("Y")
      else:
            print("N")
else:
            print("Ошибка")