usd = 432 #45
rub = 6 #80

money = int(input("Введи сумму для обмена : "))
code = int(input("Укажите код валюты : "))

if code == 45 :
    if money >= 10000:
         result = round(money/usd, 2)
         #print("ok")
    else :
         result = round(money/(usd+3), 2)
         #print("not ok")
    print("Валюта в долларах США")
elif code == 80:
    result = round(money/rub, 2)
    print("Валюта в рублях")
else :
    result = 0
    print("Такой валюты нет в наличии")

print("К получению:", result)