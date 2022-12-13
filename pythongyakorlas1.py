a = int(input("Adj meg egy számot!: "))
b = int(input("Add meg a második számot!: "))
msg = ""

if a <0 and b <0:
    msg = "A mind két szám negatív"
elif a < 0:
    msg = "Az első szám negatív"
elif b < 0:
    msg = "A második szám negatív"
else:
    msg = "Mindkét szám pozitiv"

print(msg)