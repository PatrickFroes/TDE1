import math

alt = float(input("Digite a altura do cilindro:"))
raio = float(input("Digite o raio do cilindro:"))

area = (2*math.pi*raio*alt)+(2*(math.pi*(raio**2)))
litros = area/3
latas = math.ceil(litros/5)
custo = latas*50

print("você precisará de:", latas, "latas")
print("o custo total será de:", custo, "reais")


