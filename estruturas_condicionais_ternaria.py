saldo = 2000
saque = 5000
#Essa condicional é composta por 3 partes;
# 1- a variável e a mensagem a ser exibida caso for verdadeiro;
# 2- a condição lógica, nesse caso saldo ser maior ou igual a saque;
# 3- a segunda mensagem caso retorne falso;
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")