print("| Especificação   | Código |   Preço  |")
print("  Cachorro quente |   100  |  R$13.20 |")
print("  Hamburguer      |   101  |  R$19.90 |")
print("  Cheeseburguer   |   102  |  R$21.90 |")
print("  Suco Natural    |   103  |  R$7.00  |")
print("  Refrigerante    |   104  |  R$6.50  |")

cod = int(input("informe o código do produto: "))
quant = int(input("Informe a quantidade do produto: "))
match cod:
    case 100:
        print(f"O valor do Cachorro-Quente foi de: {quant*13.2:.2f} ")
    case 101:
        print(f"O valor do hamburguer foi de: {quant*19.9:.2f} ")
    case 102:
        print(f"O valor do chesseburguer foi de: {quant*21.9:.2f}")
    case 103:
        print(f"O valor do suco natural foi de: {quant*7.0:.2f}")
    case 104:
        print(f"O valor do Refrigerante foi de: {quant*6.5:.2f}")
    case _:
        print("Código Inválido.")


