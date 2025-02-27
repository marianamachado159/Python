def inverter_lista(numero):
    n = 1

    for i in range(1, numero + 1):
        print(i, end=' ')

resultado  = inverter_lista(1, 2, 3, 4, 5)
print(resultado [::-1])