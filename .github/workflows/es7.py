import random as r

# Numero di biglie con cui giocare
quantity = r.randint(10, 100)
print(f'Ci sono {quantity} biglie con cui giocare')

# Scelta per chi inizia il turno
start = r.randint(0, 1)
if start == 1:
    print('Inizi TU a giocare.')
else:
    print('Il computer inizia per primo.')

# Scelta intelligenza del computer
intel = r.randint(0, 1)
if intel == 1:
    print('Il computer gioca in modalità intelligente\n')
else:
    print('Il computer gioca in modalità stupida\n')

# Inizializzazione variabili per numero di biglie scelte da computer e utente
playerpick = 0
compick = 0

# Inizio del gioco
while quantity > 0:
    # Caso 1: inizia il giocatore e PC 'stupido'
    if start == 1:
        if intel == 0:
            # Round del giocatore
            if quantity == 1:
                print('Hai perso')
                break
            print(f'Ci sono {quantity} biglie rimaste.')           
            while True:
                playerpick = int(input('Scegli quante biglie prendere: '))
                if playerpick <= quantity / 2:
                    break
                else:
                    print('Usa un altro numero compreso tra 1 e la metà di biglie rimaste')
            quantity = quantity - playerpick
            input(f'Sono rimaste {quantity} biglie. Premi invio per passare il turno')

            # Round del computer
            if quantity == 1:
                print('Hai vinto')
                break
            if quantity % 2 == 0:
                compick = r.randint(1, quantity/2)
            else:
                compick = r.randint(1, (quantity - 1) / 2)
            quantity = quantity - compick
            print(f'Il computer ha preso {compick} biglie, ora ne rimangono {quantity}')            
            input('Premi invio per iniziare il turno')
            
        # Caso 2: inizia il giocatore e computer intelligente
        elif intel == 1:
            # Round del computer
            if quantity == 1:
                print('Hai perso')
                break
            print(f'Ci sono {quantity} biglie rimaste.')
            while True:
                playerpick = int(input('Scegli quante biglie prendere: '))
                if playerpick <= quantity / 2:
                    break
                else:
                    print('Usa un altro numero compreso tra 1 e la metà di biglie rimaste')
            quantity = quantity - playerpick
            input(f'Sono rimaste {quantity} biglie. Premi invio per passare il turno')

            # Round del giocatore
            if quantity == 1:
                print('Hai vinto')
                break
            alg = [3, 7, 15, 31, 63]
            while True:
                check = r.choice(alg)
                if check <= quantity / 2:
                    break
            compick = quantity - check
            quantity = quantity - compick    
            print(f'Il computer ha preso {compick} biglie, ora ne rimangono {quantity}')            
            input('Premi invio per iniziare il turno')
    
    # Caso 3: Inizia il computer 'stupido'
    if start == 0:
        if intel == 0:
            # Round del computer
            if quantity == 1:
                print('Hai vinto')
                break
            if quantity % 2 == 0:
                compick = r.randint(1, quantity/2)
            else:
                compick = r.randint(1, (quantity - 1) / 2)
            quantity = quantity - compick
            print(f'Il computer ha preso {compick} biglie, ora ne rimangono {quantity}')            
            input('Premi invio per iniziare il turno')

            # Round del giocatore
            if quantity == 1:
                print('Hai perso')
                break
            print(f'Ci sono {quantity} biglie rimaste.')
            while True:
                playerpick = int(input('Scegli quante biglie prendere: '))
                if playerpick <= quantity / 2:
                    break
                else:
                    print('Usa un altro numero compreso tra 1 e la metà di biglie rimaste')
            quantity = quantity - playerpick
            input(f'Sono rimaste {quantity} biglie. Premi invio per passare il turno')

        # Caso 4: inizia il computer intelligente
        elif intel == 1:
            # Round del computer
            if quantity == 1:
                print('Hai vinto')
                break
            alg = [3, 7, 15, 31, 63]
            while True:
                check = r.choice(alg)
                if check <= quantity / 2:
                    break
            compick = quantity - check
            quantity = quantity - compick    
            print(f'Il computer ha preso {compick} biglie, ora ne rimangono {quantity}')            
            input('Premi invio per iniziare il turno')

            # Round del giocatore
            if quantity == 1:
                print('Hai perso')
                break
            print(f'Ci sono {quantity} biglie rimaste.')
            while True:
                playerpick = int(input('Scegli quante biglie prendere: '))
                if playerpick <= quantity / 2:
                    break
                else:
                    print('Usa un altro numero compreso tra 1 e la metà di biglie rimaste')
            quantity = quantity - playerpick
            input(f'Sono rimaste {quantity} biglie. Premi invio per passare il turno')  
