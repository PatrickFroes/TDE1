import math

cat1 = float(input("Digite o valor do primeiro cateto:"))
cat2 = float(input("Digite o valor do segundo cateto:"))

hip = math.sqrt((cat2**2)+(cat1**2))

print("A hipotenusa do seu triangulo vale:", hip)