h = input("輸入身高(CM)")
w = input("輸入體重(KG)")

bmi = int(w) / ((float(h)/100) ** 2)
print(" bmi值 %d " %bmi)
