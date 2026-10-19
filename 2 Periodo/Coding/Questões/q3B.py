#Fibonacci
while True:
    seq = int(input("Digite um número inteiro positivo para gerar a sequência de Fibonacci "))
    elementoAnterior = 1
    elementoAtual = 1
    contador = 0
    while contador < seq:
        if elementoAnterior < seq:
            print(elementoAnterior)
        elementoProximo = elementoAnterior + elementoAtual
        elementoAnterior = elementoAtual
        elementoAtual = elementoProximo
        contador += 1
