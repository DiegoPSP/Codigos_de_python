print(int(1.0)) #Vai apresentar o numero descartando os números depois da vírgula (ponto flutuante);

print(int("10")) #Conversão para string

print(float("10.10")) #Variável do tipo float e do tipo string

print(float(100)) #Variável do tipo float apenas.

valor = 10 #valor é do tipo inteiro;
valor_str = str(valor) #A variável valor passa a ser uma string;
print(type(valor)) #Antes da conversão;
print(type(valor_str)) #Depois da conversão;

print(100 / 2) #Vai retornar até os numeros que tiverem apóa a vírgula, mesmo a operação resultando em um número inteiro;
print(100 // 2) #Vai retornar apenas o valor inteiro da operação;