# Valori da inserire nella tabella del tris
table = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Controlla se uno dei due giocatori ha vinto
def check_win(): 
    for i in range(3):
        # file orizzontali
        if (table[i][0] == table [i][1] and table[i][1] == table [i][2]): 
            if table[i][0] == 'X':
                print('Player 1 Wins')
                return True
                
            elif table[i][0] == 'O':
                print('Player 2 Wins')
                return True
        #file diagonali
        if (table[0][0] == table [1][1] and table [1][1] == table [2][2]) or (table[0][2] == table [1][1] and table [1][1] == table [2][0]):
            if table[1][1] == 'X':
                print('Player 1 Wins')
                return True
                
            elif table[1][1] == 'O':
                print('Player 2 Wins')
                return True
            

def main():
    print(table[0][0] + ' | ' + table[0][1]+ ' | '+ table[0][2])
    print('--+---+--')
    print(table[1][0] + ' | ' + table[1][1]+ ' | '+ table[1][2])
    print('--+---+--')
    print(table[2][0] + ' | ' + table[2][1]+ ' | '+ table[2][2])
    while True:
        
        # Turno giocatore 1
        p1 = True
        p2 = False
        x = int(input('Giocatore 1 (x), rigo: '))
        y = int(input('Giocatore 1 (x), colonna: '))
        table[x-1][y-1] = 'X'

        print(table[0][0] + ' | ' + table[0][1]+ ' | '+ table[0][2])
        print('--+---+--')
        print(table[1][0] + ' | ' + table[1][1]+ ' | '+ table[1][2])
        print('--+---+--')
        print(table[2][0] + ' | ' + table[2][1]+ ' | '+ table[2][2])

        if check_win():
            break

        # Turno giocatore 2
        p2 = True
        p1 = False
        x = int(input('Giocatore 2 (O), rigo: '))
        y = int(input('Giocatore 2 (O), colonna: '))
        table[x-1][y-1] = 'O'
        print(table[0][0] + ' | ' + table[0][1]+ ' | '+ table[0][2])
        print('--+---+--')
        print(table[1][0] + ' | ' + table[1][1]+ ' | '+ table[1][2])
        print('--+---+--')
        print(table[2][0] + ' | ' + table[2][1]+ ' | '+ table[2][2])

        if check_win():
            break
main()
