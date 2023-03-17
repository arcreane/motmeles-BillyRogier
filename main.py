import grid

def showMenu():
    print(
        "1. Facile : grille 10 x 5, les mots font moins de 4 lettres \n"
        "2. Moyen : grille 15 x 7, les mots font entre 4 et 6 lettres \n"
        "3. Difficile : grille 30 x 15, les mots font entre 6 et 9 lettres \n"
    )


def showDirection():
    print(
        "1. Horizontal \n"
        "2. Vertical"
    )


def menuChoice():
    choice = int(input("Choississez une difficulté de jeu : "))
    if choice == 1:
        return 10, 5, grid.getWords(0, 4, 4)
    elif choice == 2:
        return 15, 7, grid.getWords(4, 6, 7)
    elif choice == 3:
        return 30, 15, grid.getWords(6, 9, 14)
    else:
        print("Le choix n'est pas valide\n")
        choice = menuChoice()


def getColumn(grid):
    col = int(input(f"Select column: "))
    if col > len(grid[0]):
        print("Sorry column doesn't exist")
        col = getColumn(grid)
    return col


def getRow(grid):
    row = int(input(f"Select line: "))
    if row > len(grid):
        print("Sorry row doesn't exist")
        row = getRow(grid)
    return row


def getDirection():
    direction = int(input(f"Select direction: "))
    if direction > 2:
        print("Sorry direction doesn't exist")
        direction = getDirection()
    return direction


def getPlayerInput(grid):
    col = getColumn(grid)
    row = getRow(grid)
    showDirection()
    direction = getDirection()
    return col, row, direction


def guessWords(word, grid):
    found = False
    print("Word to check : " + word)
    while not found:
        col, row, direction = getPlayerInput(grid)
        found_word = ''
        for i in range(len(word)):
            if direction == 1:
                if grid[row - 1][col - 1 + i] == word[i]:
                    found_word += grid[row - 1][col - 1 + i]
                else:
                    break
            elif direction == 2:
                if grid[row - 1 + i][col - 1] == word[i]:
                    found_word += grid[row - 1 + i][col - 1]
                else:
                    break
        if found_word == word:
            print(f"Congratulations! You found {word}.\n")
            found = True
            return col, row, direction
        else:
            print("Sorry, that's not the correct starting coordinate for the word.\n")


def gameStart():
    showMenu()
    row, col, words = menuChoice()
    grid_var = grid.createGrid(row, col)
    grid_var = grid.hideWords(grid_var, words, row, col)
    find_words = []
    for i in words:
        grid.showGrid(grid_var, words, find_words)
        col, row, direction = guessWords(i, grid_var)
        find_words.append([i, [col - 1, row - 1, direction]])

gameStart()