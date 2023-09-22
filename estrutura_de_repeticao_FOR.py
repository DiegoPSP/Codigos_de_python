texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#Exemplo utilizando um iterável;
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print() #Adiciona quebra de linha;



#Exemplo utilizando a função built-in range (Faixa integrada);
for numero in range(0, 51, 5):#Start, Stop e Step. Início, Fim e Etapa (Divisor);
    print(numero, end=" ")#Adicionando "end= " "" faz com que fique em apenas uma linha;
