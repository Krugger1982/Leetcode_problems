num2 = ['12345', '12345', '12345', '12345', '12345']
count = 5
Summa = 0
Rezult = []
for num in num2:
    for i in range(count - 1, -1, -1):
        Summa += int(num[i])

    Rezult.append(str(Summa%10))
    Summa = Summa // 10
if Summa > 0:
    Rezult.append(str(Summa))
Rezult.reverse()
Rezult = ''.join(Rezult)
print(Rezult)
