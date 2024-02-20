#apresentação do conversor
print("__________________________________________")
print("__Bem vindo ao conversor de temperatura__")
print("__________________________________________")

while True:
    #primeiro valor de entrada de valor
    while True:
        #cabeçalho de entrada
        print("1 = kelvin (K)")
        print("2 = Celsius (C)")
        print("3 = Fahrenhet (F)")

        #entrda
        valor1 = input ("Primeira unidade: ")
        
        #verificação de numero valido
        if valor1 == 1 or 2 or 3:
            break
        else:
            print("______________________")
            print("____valor invalido____")
            print("______________________")

        #entrada do valor de medida
        if valor1 == "1":
            kelvin_valor = input("Valor de Kelvin:")
        elif valor1  == "2":
            celsius_valor = input("Valor de Celsius")
        elif valor1 == "3":
            fahrenhet_valor = input("Valor de Fahrenhet")


    #segundo valor de entrada de valor
    while True:
        #cabeçalho de entrada
        print("1 = kelvin (K)")
        print("2 = Celsius (C)")
        print("3 = Fahrenhet (F)")

        #entrda
        valor2 = input ("converter para: ")


        #verificação de numero valido
        if valor2 == 1 or 2 or 3:
            break
        else:
            print("______________________")
            print("____valor invalido____")
            print("______________________")

        #entrada do valor de medida
        if valor1 == "1":
            kelvin_valor = input("Valor de Kelvin:")
        elif valor1  == "2":
            celsius_valor = input("Valor de Celsius")
        elif valor1 == "3":
            fahrenhet_valor = input("Valor de Fahrenhet")    

    #comparando se os parametros são diferentes
    if valor1 == valor2:
        print("_______________________________________________")
        print("os parametros de conversão não podem ser iguais")
        print("_______________________________________________")
    else:
        break