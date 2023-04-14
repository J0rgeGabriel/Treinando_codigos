print("Olá, vamos pegar alguns dos seus dados!")
diaNascimento = int(input("Digite o dia do seu nascimento: "))
mesNascimento = int(input("Digite o mês do seu nascimento: "))
anoNascimento = int(input("Digite o ano do seu nascimento: "))
dataNascimento = print(f"Essa é a data de nascimento informada: {diaNascimento}/{mesNascimento}/{anoNascimento}")
infoCorreta = input("Essas informações estão corretas? (sim/não)")

if infoCorreta.lower() == "sim":
    print("Ótimo, vamos continuar!")
elif infoCorreta.lower() == "nao":
    print("Por favor, digite novamente as informações corretas.")
    diaNascimento = int(input("Digite o dia do seu nascimento: "))
    mesNascimento = int(input("Digite o mês do seu nascimento: "))
    anoNascimento = int(input("Digite o ano do seu nascimento: "))
else:
    print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

cpf = int(input("DIgite o seu CPF (somente os números!!!"))
