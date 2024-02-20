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
        valor1 = float(input ("Primeira unidade: "))
        
        #entrada do valor de medida
        if valor1 == 1:
            kelvin_valor = float(input("Valor de Kelvin:"))
        elif valor1  == 2:
            celsius_valor = float(input("Valor de Celsius"))
        elif valor1 == 3:
            fahrenhet_valor = float(input("Valor de Fahrenhet"))

        #verificação de numero valido
        if valor1 == 1 or 2 or 3:
            break
        else:
            print("______________________")
            print("____valor invalido____")
            print("______________________")


    #segundo valor de entrada de valor
    while True:
        #cabeçalho de entrada
        print("1 = kelvin (K)")
        print("2 = Celsius (C)")
        print("3 = Fahrenhet (F)")

        #entrda
        valor2 = float(input ("converter para: "))

        #verificação de numero valido
        if valor2 == 1 or 2 or 3:
            break
        else:
            print("______________________")
            print("____valor invalido____")
            print("______________________")    

    #comparando se os parametros são diferentes
    if valor1 == valor2:
        print("_______________________________________________")
        print("os parametros de conversão não podem ser iguais")
        print("_______________________________________________")
    else:
        break

if valor1 == 1 and valor2 == 2:
    Temperatura = kelvin_valor - 273.15
    print("Valor em celsius:{:.2f}".format(Temperatura))
