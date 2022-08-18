hora = float(input("Informe a hora vigente:"))
min = float(input("Informe os minutos vigentes:"))
sec = float(input("Informe os segundos vigentes:"))

mintot = (hora*60)+min+(sec/60)
sectot = ((hora*60)*60)+(min*60)+sec

print("Se passaram:", mintot,"minutos desde o inicio do dia")
print("se passaram:", sectot, "desde o inicio do dia")
