print("Welcome to tic-tac-toe")

zones = {
    "a1": "-",
    "b1": "-",
    "c1": "-",
    "a2": "-",
    "b2": "-",
    "c2": "-",
    "a3": "-",
    "b3": "-",
    "c3": "-"
}

winner = False
turn = 1


def play_game(available, group):
    pos = input(f"Where would you like to play {group}\n")
    if pos in available:
        zones[pos] = group
    else:
        print("That is not a valid zone please try again\n")
        play_game(available, group)


def check_list(lst):
    return all(i == lst[0] for i in lst)


def check_winner():
    # Check rows
    for i in range(1, 4):
        if check_list([zones[f'a{i}'], zones[f'b{i}'], zones[f'c{i}']]) and zones[f'a{i}'] != "-":
            return zones[f'a{i}']

    # Check columns
    for j in ['a', 'b', 'c']:
        if check_list([zones[f'{j}1'], zones[f'{j}2'], zones[f'{j}3']]) and zones[f'{j}1'] != "-":
            return zones[f'{j}1']

    # Check diagonals
    if check_list([zones['a1'], zones['b2'], zones['c3']]) and zones['a1'] != "-":
        return zones['a1']
    if check_list([zones['a3'], zones['b2'], zones['c1']]) and zones['a3'] != "-":
        return zones['a3']

    return None


while not winner:
    interface = f'''
       a     b     c
          |     |     
    1  {zones["a1"]}  |  {zones["b1"]}  |  {zones["c1"]}  
     _____|_____|_____
          |     |     
    2  {zones["a2"]}  |  {zones["b2"]}  |  {zones["c2"]}  
     _____|_____|_____
          |     |     
    3  {zones["a3"]}  |  {zones["b3"]}  |  {zones["c3"]}  
          |     |     
    '''
    print(interface)
    available_zones = [a for a in zones.keys() if zones.get(a) == "-"]

    if turn % 2 == 1:
        play_game(available_zones, "X")
    else:
        play_game(available_zones, "O")

    turn += 1

    # Check for a winner after each turn
    winner_symbol = check_winner()
    if winner_symbol:
        print(interface)
        print(f"{winner_symbol} wins!")
        winner = True
    elif turn > 9:  # Check for a draw
        print(interface)
        print("It's a draw!")
        winner = True