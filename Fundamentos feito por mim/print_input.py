nome = input("Informe seu nome: ") #cCria a variável nome e solicita do usuário alguma entrada do teclado;
idade = input("Informe a sua idade: ") #Mesma coisa feita na linha 1, porém com outra variável;
sexo = input("Informe seu sexo: ")

print(nome, idade) #Mostra na tela as informações solicitadas;
print(nome, idade, end = "... \n") #Adiciona no final o que estiver escrito entre as aspas;
print(nome, idade, sep = "#", end= "... \n") #Adiciona Separação entre as variáveis e qualquer coisa que estiver entre as aspas com a função end;
print(nome, idade, sexo, sep = "#") #Adiciona separação entre as variáveis; Funciona com mais de duas variáveis;