from random import randint

def validarCPF(cpf):
    digitos = 8
    if type(cpf[0]) == str:
      for d in range(11):
          cpf.append(int(cpf[0]))
          del cpf[0]
    for n in range(2):
        multi = 2
        soma = 0
        for i in range(digitos, -1 , -1):
          soma += cpf[i] * multi
          multi += 1
        if soma % 11 >= 2:
          digito = 11 - (soma % 11)
        else:
          digito = 0
        if digito == cpf[digitos + 1]:
            digitos += 1

    if digitos == 10:
        if opcao == 1:
            print(f"O CPF é válido")
        else:
            print(f"{cpf}")
    else:
        if opcao == 1:
            print(f"O CPF é inválido")
        else:
            gerarCPF()

def gerarCPF():
    cpf = []
    for n in range(11):
        cpf.append(randint(0,9))
    validarCPF(cpf)

opcao = 0
while opcao != 1 and opcao != 2:
  opcao = int(input("Digite 1 para validar CPF ou 2 para gerar CPF."))
if opcao == 1:
  cpf = list(input("Digite o CPF sem pontuação ou espaços"))
  validarCPF(cpf)
if opcao == 2:
  gerarCPF()