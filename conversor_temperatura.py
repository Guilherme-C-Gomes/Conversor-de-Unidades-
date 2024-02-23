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
        while True:
            try:
                valor1 = float(input ("Primeira unidade:"))
                break
            except ValueError:
                print("_______________________________________")
                print("Erro: Por favor, insira apenas números.")
                print("_______________________________________")

        #entrada do valor de medida   
        while True:          
            try:
                if valor1 == 1:
                    print("_____________________________________")
                    kelvin_valor = float(input("Insira valor de Kelvin:"))
                    break
                elif valor1  == 2:
                    print("_____________________________________")
                    celsius_valor = float(input("Insira valor de Celsius:"))
                    break
                elif valor1 == 3:
                    print("_____________________________________")
                    fahrenhet_valor = float(input("Insira valor de Fahrenhet:"))
                    break
            except ValueError:
                print("_______________________________________")
                print("Erro: Por favor, insira apenas números.")
                print("_______________________________________")
    

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
        while True:
            try:
                valor2 = float(input ("converter para:"))
                break
            except ValueError:
                print("_______________________________________")
                print("Erro: Por favor, insira apenas números.")
                print("_______________________________________")


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

#_________Formulas de conversão_________
if valor1 == 1 and valor2 == 2:
    Temperatura = kelvin_valor - 273.15
    print("_______________________________________________")
    print("A temperatura em Celsius é de:{:.2f}".format(Temperatura))
    print("_______________________________________________")
elif valor1 == 2 and valor2 == 1:
    Temperatura = celsius_valor +273.15
    print("_______________________________________________")
    print("A temperatura em Kelvin é de: {:.2f}".format(Temperatura))
    print("_______________________________________________")

if valor1 == 1 and valor2 == 3:
    Temperatura = kelvin_valor * 9/5 - 453.67
    print("_______________________________________________")
    print("A temperatura em Fahrenhet é de:{:.2f}".format(Temperatura))
    print("_______________________________________________")

elif valor1 == 3 and valor2 == 1:
    Temperatura = (fahrenhet_valor + 459.67) * 5/9
    print("_______________________________________________")
    print("A temperatura em Kelvin é de: {:.2f}".format(Temperatura))
    print("_______________________________________________")

if valor1 == 2 and valor2 ==3:
    Temperatura = celsius_valor * 9/5 + 32
    print("_______________________________________________")
    print("A temperatura em Fahrenhet e de: {:.2f}".format(Temperatura))
    print("_______________________________________________")
if valor1 == 3 and valor2 ==2:
    Temperatura = (fahrenhet_valor - 32) * 5/9
    print("_______________________________________________")
    print("A temperatura em Celsius e de: {:.2f}".format(Temperatura))
    print("_______________________________________________")