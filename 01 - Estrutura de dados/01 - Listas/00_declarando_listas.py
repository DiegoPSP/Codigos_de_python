frutas = ["laranja", "maca", "uva"]#Posso declarar com objetos já pré-definidos;
print(frutas)

frutas = []#Posso declarar uma lista vazia;
print(frutas)

letras = list("python")#Posso declarar utilizando a função list, mas se fizer dessa maneira aí cada letra será um objeto diferente;
print(letras)#O programa entende que "p" é um objeto, "y" é outro objeto e assim por diante;

numeros = list(range(10))#Posso declarar com o range que é um "contador", ele cria elementos de acordo com o número que você declarou;
print(numeros)#Essa é a função build-in, vai criar um elemento para cada elemento retornado pela função range;

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]#Posso declarar com vários objetos, idependente do seu tipo;
print(carro)
