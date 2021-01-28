file = open('nazioni.txt', 'r')
nazioni_punteggi = {}
for line in file:
    l = line.strip('\n').split(' ')
    if int(l[3]) == 3:
        p = 0.05
    elif int(l[3]) == 2:
        p = 0.10
    elif int(l[3]) == 1:
        p = 1.00
    else:
        p = 0

    if l[2] not in nazioni_punteggi:
        nazioni_punteggi[l[2]] = p
    else:
        nazioni_punteggi[l[2]] += p
for key in nazioni_punteggi:
    print(f'{key} : {nazioni_punteggi[key]:.2f}')
values = nazioni_punteggi.values()
values = sorted(values, reverse=True)
minimo = values[2]
top = {}
for nazione in nazioni_punteggi:
    if nazioni_punteggi[nazione] == values[0]:
        top['primo'] = nazione
    elif nazioni_punteggi[nazione] == values[1]:
        top['secondo'] = nazione
    elif nazioni_punteggi[nazione] == values[2] and len(top) <= 3:
        top['terzo'] = nazione
print('Top 3 Nazioni\n')
print(f"Primo posto: {top['primo']}, medaglie equivalenti: {nazioni_punteggi[top['primo']]}")  
print(f"Secondo posto: {top['secondo']}, medaglie equivalenti: {nazioni_punteggi[top['secondo']]}")        
print(f"Terzo posto: {top['terzo']}, medaglie equivalenti: {nazioni_punteggi[top['terzo']]}")
file.close()
