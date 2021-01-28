sospetti = open('sospetti.txt', 'r')
presenze = open('presenze.txt', 'r')
dizionario = {}
for line in presenze:
    persona = line.strip('\n').split(',')
    dizionario[persona[0]] = (int(persona[2]), int(persona[3]), persona[1])
print(dizionario)
for s in sospetti:
    l = []
    s = s.strip('\n')
    if s in dizionario.keys():        
        for key in dizionario:
            if (key != s) and (dizionario[s][0] in range(dizionario[key][0], dizionario[key][1]+1) or (dizionario[key][0] in range(dizionario[s][0], dizionario[s][1]+1))):
                l.append(key)
    print(f'Contatti del cliente {s}: ')
    if len(l) > 0:
        for i in sorted(l):
            print(f'    {i}, {dizionario[i][2]}')
    else:
        print('    Il cliente non ha contatti')
sospetti.close()
presenze.close()