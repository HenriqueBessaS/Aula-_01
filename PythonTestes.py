# Crie um código que o usuário digite seu salário, seu nome e faço um calculo de bonus.

nome_valido = False
salario_valido = False
bonus_valido = False


#Solicitar ao usuário que informe seu nomer
while nome_valido is not True:
    try:
        nome_usuario = input("Digite seu nome: ")

        #Verificando se o nome está vazio
        if len(nome_usuario) == 0:
                raise ValueError("O nome não pode estar vazio.")
        #Verificar se há números no nome
        elif any(char.isdigit() for char in nome_usuario):
             raise ValueError("O nome não deve conter números.")
        else:
             nome_valido = True
             print("Nome válido.", nome_usuario)
    except ValueError as e:
        print(e)


#Solicita ao usuário que digite seu salário e há converta para float
while salario_valido is not True:
    try:
        salario_usuario = float(input("Digite seu salário: "))
        if salario_usuario <= 0:
             print("Por favor, digite um número válido.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada invalida, por favor digite um número.")


#Solicite o usuário que digite o valor do bonus, converter para float
while bonus_valido is not True:
    try:
        bonus_salário = float(input("Digite o valor do bonus recebido"))
        if bonus_salário < 0:
            print("Por favor, digite um valor positivo.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada invalida para o bônus, por favor, digite um número.")


bonus_recebido =  salario_usuario * bonus_salário #Exemplo simple de KPI.


#Imprimir as informações para o usuário
print(f"{nome_usuario}, seu salário é R${salario_usuario:.2f} e seu bonus final é R${bonus_recebido:.2f}.")














        
        
         



