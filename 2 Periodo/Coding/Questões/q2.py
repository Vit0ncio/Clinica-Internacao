
qVogal = 0
qConsoante = 0

vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'

while True:
    letra = input("Digite uma letra (Vogal ou Consoante)").lower()
    #Conectivo "in" verifica se a letra digitada está contida na string vogais ou consoantes
    if letra == '':
        print("\nEu estava pronto para isso!!! \n")
        print("Digite apenas letras do alfabeto ou '#' para sair.")
    elif letra in vogais:
        qVogal += 1
        print("Isso é uma vogal!")
    elif letra in consoantes:
        qConsoante += 1
        print("Isso é uma consoante!")
    elif letra == '#':
        print(f"Quantidade de vogais digitadas: {qVogal}")
        print(f"Quantidade de consoantes digitadas: {qConsoante}")
        if qVogal > qConsoante:
            print("Você digitou mais vogais do que consoantes.")
        elif qConsoante > qVogal:
            print("Você digitou mais consoantes do que vogais.")
        else:
            print("Você digitou a mesma quantidade de vogais e consoantes.")
        break
        
        
    else:
        print("Digite apenas letras do alfabeto ou '#' para sair.")