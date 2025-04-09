print("Loja de tintas Fiap Colors\nCálculo de área x quantidade de tinta")

alt = float(input("Informe a Altura do seu cômodo (em metros): "))
comp = float(input("Informe o Comprimento do seu cômodo (em metros): "))
larg = float(input("Informe a Largura do seu cômodo (em metros): "))

area = ((alt*larg)*2) + ((alt*comp)*2) + larg*comp
litros = area / 3

print(f"A área do seu cômodo é: {area:.2f} metros quadrados.")
print(f"Você vai precisar de: {litros:.1f} de tinta.")
