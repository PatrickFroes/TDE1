preco = float(input("Digite o preco do produto:"))


par2 = preco/2
par3 = (preco+((preco*5)/100))/3
vista = preco-((preco*5)/100)

print("O preco a vista será:",vista)
print("O preco em duas parcelas será:", par2, "por mês")
print("O preco em três parcelas será:", par3, "por mês")