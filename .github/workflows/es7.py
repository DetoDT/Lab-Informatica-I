import random as r
quantity = r.randint(10, 100)
print(f'Ci sono {quantity} biglie con cui giocare')

start = r.randint(0, 1)

if start == 1:
    print('Inizi TU a giocare.')
else:
    print('Il computer inizia per primo.')

intel = r.randint(0, 1)

if intel == 1:
    print('Il computer gioca in modalità intelligente\n')
else:
    print('Il computer gioca in modalità stupida\n')

playerpick = 0
compick = 0

while quantity > 0:
    if start == 1:
        if intel == 0:
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

        elif intel == 1:
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

            if quantity == 1:
                print('Hai vinto')
                break
            alg = [3, 7, 15, 31, 63]
            while True:
                check = quantity - r.choice(alg)
                if check > 0:
                    break
            compick = check
            quantity = quantity - compick    
            print(f'Il computer ha preso {compick} biglie, ora ne rimangono {quantity}')            
            input('Premi invio per iniziare il turno')
    
    if start == 0:
        if intel == 0:
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

        elif intel == 1:
            if quantity == 1:
                print('Hai vinto')
                break
            alg = [3, 7, 15, 31, 63]
            while True:
                check = quantity - r.choice(alg)
                if check > 0:
                    break
            compick = check
            quantity = quantity - compick    
            print(f'Il computer ha preso {compick} biglie, ora ne rimangono {quantity}')            
            input('Premi invio per iniziare il turno')

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

