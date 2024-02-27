while True:
    try:
        #entrada de dados
        print("Bem vindo ao conversor de medidas!")
        print("1 = conversor de temperatura")
        print("2 = conversor de altura")
        print("3 = conversor de peso")
        print("4 = conversor de distancia")

        entrada = float(input ("qual conversor irá usar?"))

        #redirecionamento a partir da entrada
        if entrada == 1:
            exec(open("conversor_temperatura.py").read())
            break
        elif entrada == 2:
            exec(open("conversor_de_altura.py").read())
            break
        elif entrada == 3:
            exec(open("conversor_de_peso.py").read())
            break
        elif entrada == 4:
            exec(open("conversor_de_distancia.py").read())
            break
        else:
            print("______________________")
            print("____valor invalido____")
            print("______________________")
    except ValueError:
        print("_______________________________________")
        print("Erro: Por favor, insira apenas números.")
        print("_______________________________________")


