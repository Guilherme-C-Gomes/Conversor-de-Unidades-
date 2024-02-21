#apresentação do conversor
print("__________________________________")
print("__Bem vindo ao conversor de peso__")
print("__________________________________")

while True:
    try:
        #entrada de dados
        print("1 = Kilos")
        print("2 = Libras")
        valor1 = float(input("Medida de entrada: "))

        while True:
            try:
                if valor1 == 1:
                    print("_________________________")
                    kilos_valor = float(input("Insira o valor de Kilos: "))
                    valor2 = 2
                    break
                elif valor1 == 2:
                    print("_________________________")
                    libras_valor = float(input("Insira o valor de Libras"))
                    valor2 = 1
                    break
            except ValueError:
                print("_______________________________________")
                print("Erro: Por favor, insira apenas números.")
                print("_______________________________________")

        if valor1 == 1:
            kilos_valor = kilos_valor * 2.205
            print("___________________________")
            print("Valor em Libras e de: {:.2f}".format(kilos_valor))
            break
        else:
            libras_valor = libras_valor * 0.453592
            print("___________________________")
            print("Valor em Kilos e de: {:.2f}".format(libras_valor))
            break

        
    except ValueError:
        print("_______________________________________")
        print("Erro: Por favor, insira apenas números.")
        print("_______________________________________")