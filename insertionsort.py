



def insertionsort(lista):
    n = len(lista)
    i = 1
    for i in range(1, n):
        chave = lista [i]
        j = i - 1
        while j >= 0 and  lista[j] > chave:
            lista [j+1] = lista [j]
            j = j - 1

        lista [j+1] = chave
        print (lista)






num = array = [1, 89, 55, 53, 29, 31, 77, 21, 31, 33, 3, 11, 5, 9, 7, 113, 15, 19, 99, 101, 59, 71, 23, 65, 89, 91 , 81,103, 27, 49  ]
insertionsort(num)