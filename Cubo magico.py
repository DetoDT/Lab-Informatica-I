tab = []

for i in range(4):
    lista = []
    for j in range(4):
        num = int(input('Inserire numero: '))
        lista.append(num)
    tab.append(lista)

listaSomme = []
for i in tab:
    somma = 0
    for j in i:
        somma = somma + j
    if somma not in listaSomme:
        listaSomme.append(somma)

sommaDiagonale1 = tab[0][0] + tab[1][1] + tab[2][2] + tab[3][3] 
sommaDiagonale2 = tab[0][3] + tab[1][2] + tab[2][1] + tab[3][0] 

if sommaDiagonale1 and sommaDiagonale2 not in listaSomme:
    listaSomme.append(sommaDiagonale1)

for i in range(4):
    somma = 0
    for j in range(4):
        somma += tab[j][i]
    if somma not in listaSomme:
        listaSomme.append(somma)

if len(listaSomme) == 1:
    print("E' un cubo magico")
else:
    print('Non è un cubo magico')
    
