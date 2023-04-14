
print("Olá, vamos pegar alguns dos seus dados!")

#variaveis
diaNascimento = int(input("Digite o dia do seu nascimento: "))
mesNascimento = int(input("Digite o mês do seu nascimento: "))
anoNascimento = int(input("Digite o ano do seu nascimento: "))
dataNascimento = print(f"Essa é a data de nascimento informada: {diaNascimento}/{mesNascimento}/{anoNascimento}")
infoCorreta = input("Essas informações estão corretas? (sim/não)")

#if dos dados iniciais
if infoCorreta.lower() == "sim":
    print("Ótimo, vamos continuar!")

elif infoCorreta.lower() == "nao":
    print("Por favor, digite novamente as informações corretas.")
    diaNascimento = int(input("Digite o dia do seu nascimento: "))
    mesNascimento = int(input("Digite o mês do seu nascimento: "))
    anoNascimento = int(input("Digite o ano do seu nascimento: "))
    print("Ótimo, vamos continuar!")

else:
    print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

cpf = int(input("DIgite o seu CPF (somente os números)"))
print(f"Esse é o seu CPF {cpf}?")
cpfCorreto = input("Esse é o seu CPF? (sim/não)")

if cpfCorreto.lower() == "sim":
    print("Ótimo, vamos para a próxima etapa")

elif cpfCorreto.lower() == "nao":
    print("Digite novamente o seu CPF")
    cpf = int(input("DIgite o seu CPF (somente os números!!!"))
    print("Ótimo, vamos para a próxima etapa")

else:
    print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

#dados para login
gmail = input("Digite o seu endereço de email: ")
gmail2 = input("DIgite novamente o seu endereço de email: ")

if gmail.lower() == gmail2:
    print("Vamos definir a sua senha agora!")

elif gmail.lower() != gmail2:
    print("Digite ambos os emails iguais!")
    gmail = input("Digite o seu endereço de email: ")
    gmail2 = input("DIgite novamente o seu endereço de email: ")
    print("Vamos definir a sua senha agora!")

#senha
senha = input("Defina a sua senha: ")
senha2 = input("DIgite novamente a sua senha: ")

if senha == senha2:
    print("Senha validada")

elif senha != senha2:
    print("Senhas digitadas de formas diferentes, favor digitar novamente!!")
    senha = input("Defina a sua senha")
    senha2 = input("DIgite novamente a sua senha")
    print("Senha validada")