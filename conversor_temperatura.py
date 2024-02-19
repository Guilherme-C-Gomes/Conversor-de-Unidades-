#apresentação do conversor
print("__________________________________________")
print("__Bem vindo ao conversor de temperatura__")
print("__________________________________________")


#entrada de valor
while True:
    print("1 = kelvin (K)")
    print("2 = Celsius (C)")
    print("3 = Fahrenhet (F)")

    valor1 = input ("Primeira unidade: ")
    valor2 = input ("converter para: ")

    if valor1 == 1 or 2 or 3:
        break
    elif valor2 == 1 or 2 or 3:
        break
    else:
        print("______________________")
        print("____valor invalido____")
        print("______________________")