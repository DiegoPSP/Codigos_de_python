nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
profissao = input("Qual a sua profissão? ")
linguagem = input("Qual sua linguagem de programação que você domina? ")
saldo = float(input("Quanto de saldo você têm? "))

dados = {"nome": "Diego Pereira", "idade": 21}#Biblioteca, ainda não sei o que é mais à frente falarei sobre;

print("Nome: %s Idade: %d" % (nome, idade))#Modo que se originou com a linguagem, Não é tão utilizado hoje em dia;

print("Nome: {} Idade: {}".format(nome, idade))#Usando o format, mas desse jeito você têm que seguir a ordem que está no script;

print("Nome: {1} Idade: {0}".format(idade, nome))#Dessa maneira é atribuída as variáveis com sua representação numérica de criação;
print("Nome: {1} Idade: {0}".format(nome, idade))#Mesma maneira e em sequência;

print("Nome: {nome} Idade: {idade}". format(nome=nome, idade=idade))#Atribuição com as mesmas nomeclaturas para as variáveis;
print("Nome: {name} Idade: {age} {name} {name} {age}". format(name=nome, age=idade))#Atribuição com novas nomeclaturas para as variáveis;
print("Nome: {nome} Idade: {idade}".format(**dados))#Utilização da biblioteca que foi criada lá em cima;

print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem} Saldo: {saldo}.")#Método mais utilizado por causa de sua rapidez e fácil leitura;
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem} Saldo: {saldo:.2f}.")#Manipulação de valores com ponto flutuante;
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem} Saldo: {saldo:10.2f}.")#Adiciona espaços em branco antes de mostrar na tela;
