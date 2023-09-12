#Adição
print(1 + 1)
>>> 2

#Subtração
print(2 - 1)
>>> 1

#Multiplicação
print(2 * 3)
>>> 6

#Divisão com ponto flutuante
print(10 / 2)
>>> 5.0

#Divisão inteira
print(10 // 2)
>>> 5

#Módulo (A sobra de uma divisão)
print(10 % 3)
>>> 1

#Exponenciação
print(2 ** 3)
>>> 8

#Precedência Numérica
#Segue as regras da matemática básica;
print(10 - 5 * 2) #Executa primeiro a multiplicação;
>>> 0

print((10 - 5) * 2 ) #Executa primeiro o conteúdo dos parêntesis;
>>> 10

print(10 ** 2 * 2) #Executa primeiro a exponenciação;
>>> 200

print(10 ** (2 * 2)) #Mesma regra dos parêntesis;
>>> 10000

print(10 / 2 * 4) #Como os dois tÊm precedência igual, o código executa da esquerda para a direita e ainda resulta em um valor com ponto flutuante;
>>> 20.0
