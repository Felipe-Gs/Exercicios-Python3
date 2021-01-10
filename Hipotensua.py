import math

cat1 = float(input("digite o cateto oposto:"))
cat2 = float(input("digite o cateto adjacente:"))
hip = math.hypot(cat1, cat2)
print(f"o valor da hipotenusa é {hip}")