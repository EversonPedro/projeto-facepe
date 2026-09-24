
#validação de CPF
def validar_cpf(cpf):
    # Remove pontos e traço
    cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")

    # Verifica se possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os números são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calculando o primeiro dígito
    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Compara com o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        return False

    # Calculando o segundo dígito
    soma = 0

    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Compara com o segundo dígito verificador
    if digito2 != int(cpf[10]):
        return False

    return True

#validação de CNPJ

def validar_cnpj(cnpj):

    # Remove pontuação
    cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "").replace(" ", "")

    # Verifica se possui 14 dígitos
    if len(cnpj) != 14:
        return False

    # Impede CNPJs com todos os números iguais
    if cnpj == cnpj[0] * 14:
        return False

    # Pesos para calcular o primeiro dígito
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma = 0

    for i in range(12):
        soma += int(cnpj[i]) * pesos1[i]

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Verifica o primeiro dígito
    if digito1 != int(cnpj[12]):
        return False

    # Pesos para calcular o segundo dígito
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma = 0

    for i in range(13):
        soma += int(cnpj[i]) * pesos2[i]

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verifica o segundo dígito
    if digito2 != int(cnpj[13]):
        return False

    return True

#decisão inicial do cliente
print(20*"-")
print("     VALIDAÇÃO     ")
print(20*"-")
print("1-CPF")
print("2-CNPJ")

opcao = input('Esconha uma opçção pra validar')

if opcao == '1':
    cpf = input('Digite seu CPF:')

    if validar_cpf(cpf):

        print('CPF valido!')
    else:
        print("CPF invalido!")

elif opcao =="2":
    cnpj = input('Digite o su CNPJ:')

    if validar_cnpj(cnpj):
        print("CNPJ valido!")
    else:
        print("CNPJ invalido!")

else:
    print('Opção invalida!')

