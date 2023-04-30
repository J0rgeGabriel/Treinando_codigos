while True:
    real = float(input("Digite quantos reais você gostaria de converter: R$").replace(',','.'))
    
    while real <= 0:
            real = float(input("Não é possivel converter zero!! Digite quantos reais você gostaria de converter: R$").replace(',', '.'))

    opcao = input("Para qual moeda você gostaria de converter? Escolha uma opção a seguir: \n"
                "1 - Dólar Americano\n"
                "2 - Dolar Australiano\n"
                "3 - Dólar Canadense\n"
                "4 - Euro\n"
                "5 - Libra\n"
                "6 - Iene\n"
                "0 - Parar de converter\n"
                "Para qual moeda gostaria de converter? ")
    print()

    while opcao not in ["0", "1", "2", "3", "4", "5", "6"]:
        opcao = input("Para qual moeda você gostaria de converter? Escolha uma opção a seguir: \n"
                    "1 - Dólar Americano\n"
                    "2 - Dolar Australiano\n"
                    "3 - Dólar Canadense\n"
                    "4 - Euro\n"
                    "5 - Libra\n"
                    "6 - Iene\n"
                    "0 - Parar de converter\n"
                    "Para qual moeda gostaria de converter? ")
        print()

    if opcao == "1":
        dolar = round(real * 0.20, 2)
        print(f"R${real} são {dolar} dolares")

    elif opcao == "2":
        dolarAustraliano = round(real * 0.30, 2)
        print(f"R${real} são {dolarAustraliano} dolares australianos")

    elif opcao == "3":
        dolarCanadense = round(real * 0.27, 2)
        print(f"R${real} são {dolarCanadense} dolares canadenses")

    elif opcao == "4":
        euro = round(real * 0.18, 2)
        print(f"R${real} são {euro} euros")

    elif opcao == "5":
        libra = round(real * 0.16, 2)
        print(f"R${real} são {libra} libras")

    elif opcao == "6":
        iene = round(real * 27.33, 2)
        print(f"R${real} são {iene} ienes")

    elif opcao == "0":
        print("Conversões encerradas")
        
        
    continuar = input("Você deseja continuar realizando conversões? [S/N]").upper()
    if continuar == "S":
        continue
    else:
        print("Encerrando as conversões")
        break