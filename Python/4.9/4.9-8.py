import math

def kor_terulet(r):
    return r*r*math.pi
r = int(input("Sugár: "))
print(f"Területe: {kor_terulet(r)}")