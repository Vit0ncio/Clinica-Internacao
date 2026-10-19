#Fibonacci
while True:
    seq = int(input("Digite um número inteiro positivo para gerar uma posição da sequência de Fibonacci "))
    elementoAnterior = 0
    elementoAtual = 1
    contador = 0
    while contador < seq:

        elementoProximo = elementoAnterior + elementoAtual
        elementoAnterior = elementoAtual
        elementoAtual = elementoProximo
        contador += 1
        if contador == seq:
            print(elementoAnterior)
