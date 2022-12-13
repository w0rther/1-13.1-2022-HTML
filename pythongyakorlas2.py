def fv(a):
    r = True # Alapértelmezésben  a > 150
    if (a <= 150):
        r = False

    return r

cim = input("Add meg a könyv címét! ")
lapok = int(input("Add meg az oldalainak számát! "))

if (fv(lapok)):
    sz1 = "hosszú"
else:
    sz1 = "rövid"
print(f"{cim} {sz1} terjedelmű könyv")