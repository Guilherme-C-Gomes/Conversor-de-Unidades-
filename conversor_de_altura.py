while True:
    try:
        print("1 = Metros")
        print("2 = Pés")
        valor1 = float(input("Medida de entrada: "))

        while True:
            try:
                if valor1 == 1:
                    print("_________________________")
                    metros_valor = float(input("Insira a altura em metros: "))
                    valor2 = 2
                    break
                else:
                    print("_________________________")
                    pes_valor = float(input("Insira a altura em pés: "))
                    valor2 = 1
                    break
            except ValueError:
                print("_______________________________________")
                print("Erro: Por favor, insira apenas números.")
                print("_______________________________________")

        if valor1 == 1:
            pes_valor = metros_valor * 3.28084
            print("___________________________")
            print("Tamanho em Pés é de: {:.2f}".format(pes_valor))
            break
        else:
            metros_valor = pes_valor * 0.3048
            print("___________________________")
            print("Tamanho em Metros é de: {:.2f}".format(metros_valor))
            break


    except ValueError:
        print("_______________________________________")
        print("Erro: Por favor, insira apenas números.")
        print("_______________________________________")
