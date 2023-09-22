opcao = -1
cont = 0

while opcao != 0:
    opcao = int(input("Informe um número: "))
    cont = cont+1
    if opcao == 10:
        break

    print(opcao)

print (f"Foram digitados {cont-1} números") 


#Exemplo com FOR
for numero in range(100):
    if numero == 12:#Vai fazer a contagem, quando chegar na condicional vai pular e continuar a contagem;
        continue

    print(numero, end=" ")