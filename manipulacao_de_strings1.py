nome = "DIEgO PErEIrA"

print (nome.upper())#Deixa a string toda em letras Maiúsculas;
print (nome.lower())#Deixa a string toda em letras Minúsculas;
print(nome.title())#Deixa apenas a primeira de cada palavra da string em letra Maiúscula;

texto = "   Congratulations     "

print(texto + ".")#Adiciona o parâmetro passado entre as aspas no final da string;
print(texto.strip() + ".")#Retira todos os espaçamentos da string;
print(texto.rstrip() + ".")#"r -> Right" tira os espaçamentos da direita;
print(texto.lstrip() + ".")#"l -> Left" tira os espaçamentos da esquerda;

menu = "Opções"

print("####" + menu + "####")#Maneira manual de adicionar o que você quer na string;
print(menu.center(14))#Centraliza a string e adiciona espaços em brancos; (Conta os caracteres da string e o que passar é adicionado em branco); 
print(menu.center(14, "#"))#Adiciona o que estiver entre as aspas nos lugares que ficariam em branco;
print("-".join(menu))#Adiciona entre as letras da string o que estiver entre as aspas;



