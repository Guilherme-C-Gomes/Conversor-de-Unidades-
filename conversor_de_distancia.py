while True:
    try:
        print("1 = Kilometros")
        print("2 = Milhas")
        valor1 = float(input("Distancia de entrada: "))

        while True:
            try:
                if valor1 == 1:
                    print("_________________________")
                    kilometros_valor = float(input("Insira a distancia em Kilometros: "))
                    valor2 = 2
                    break
                else:
                    print("_________________________")
                    milhas_valor = float(input("Insira a distancia em Milhas: "))
                    valor2 = 1
                    break
            except ValueError:
                print("_______________________________________")
                print("Erro: Por favor, insira apenas números.")
                print("_______________________________________")

        if valor1 == 1:
            milhas_valor = kilometros_valor * 0.621371
            print("___________________________")
            print("Tamanho em milhas é de: {:.2f}".format(milhas_valor))
            break
        else:
            kilometros_valor = milhas_valor * 1.60934
            print("___________________________")
            print("Tamanho em kilometros é de: {:.2f}".format(kilometros_valor))
            break


    except ValueError:
        print("_______________________________________")
        print("Erro: Por favor, insira apenas números.")
        print("_______________________________________")