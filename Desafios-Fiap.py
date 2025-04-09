letra = input("Digite uma letra minuscula: ")
match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("É uma vogal! Parabéns")
    case _:
        print("É uma consoante.")





