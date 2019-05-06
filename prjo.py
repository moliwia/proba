def zmieniacz_x(ciag):
    lista = list(ciag)
    count = 0
    for i in lista:
        count+=1
        if i == 'a':
            index = int(count)
            lista[index] = "X"
    ciag="".join(lista)
    return ciag

znak = input("Proszę wpisać słowo do zmiany: ")
print(zmieniacz_x(znak))

print("Zmiany. Zmiany. Zmiany.")
