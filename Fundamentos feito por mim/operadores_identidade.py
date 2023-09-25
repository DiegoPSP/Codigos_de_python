#Essa verificação é bem simples mas pode ser muito útil
#para saber se determinadas variáveis ocupam o mesmo espaço na memória;
saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)

#Operadores de associação

frutas = ["limao", "uva", "laranja"]
curso = "Curso de Python"

print("laranja" in frutas)
print("limao" not in frutas)
print("Python" in curso)