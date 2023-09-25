nome = "Diego Pereira"

#Quando queremos mostrar uma mensagem muito longa ou criar um menu;
#podemos usar três aspas duplas ou simples, o python vai preservar os espaçamentos;
mensagem = f"""
    Olá meu é {nome},
Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print (mensagem)


print(
    """
    ========== MENU ==========

    1 - Depositar
    2 - Sacar
    0 - Sair

    ==========================

            Obrigado por usar nosso sistema!!!!
    """
)