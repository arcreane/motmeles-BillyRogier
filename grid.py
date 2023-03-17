import random


def getWords(lmin, lmax, nbr):
    dico = open('dico.txt', 'r')
    dico = dico.read().split()
    words = []
    for w in dico:
        if lmin <= len(w) <= lmax:
            words.append(w)
    words = random.sample(words, nbr)
    return words


def getLetters():
    letters = []
    for l in range(97, 123):
        letters.append(chr(l))
    return letters


def hide_word_horizontal(grid, word, row, col, placed_words):
    len_words = len(word)
    row_position = random.randint(0, row - 1)
    col_position = random.randint(0, col - len_words)
    placed = False
    list = []
    for i in range(len_words):
        for p in placed_words:
            if [col_position + i, row_position] in p:
                placed = True
        if not placed:
            try:
                grid[col_position + i][row_position]
            except NameError:
                hide_word_horizontal(grid, word, row, col, placed_words)
            else:
                grid[col_position + i][row_position] = word[i]
                list.append([col_position + i, row_position])

    return list


def hide_word_vertical(grid, word, row, col, placed_words):
    len_words = len(word)
    row_position = random.randint(0, row - len_words)
    col_position = random.randint(0, col - 1)
    placed = False
    list = []
    for i in range(len_words):
        for p in placed_words:
            if [col_position, row_position + i] in p:
                placed = True
        if not placed:
            try:
                grid[col_position][row_position + i]
            except NameError:
                hide_word_vertical(grid, word, row, col, placed_words)
            else:
                grid[col_position][row_position + i] = word[i]
                list.append([col_position, row_position + i])
    return list


def hideWords(grid, words, row, col):
    placed_words = []
    for word in words:
        placed = False
        direction = random.choice([hide_word_horizontal, hide_word_vertical])
        direction = direction(grid, word, row, col, placed_words)
        if direction:
            placed_words.append(direction)
            placed = True
    return grid


def createGrid(column, row):
    grid = []
    for r in range(row):
        row_list = []
        for c in range(column):
            letter = random.choice(getLetters())
            row_list.append(letter)
        grid.append(row_list)
    return grid


def showGrid(grid, words, find_words):
    for w in find_words:
        for x in range(len(w[0])):
            if w[1][2] == 1:
                grid[w[1][1]][w[1][0] + x] = '\033[1;4;33;43m' + '\033[31m' + grid[w[1][1]][w[1][0] + x] + '\033[0m'
            else:
                grid[w[1][1] + x][w[1][0]] = '\033[1;4;33;43m' + '\033[31m' + grid[w[1][1] + x][w[1][0]] + '\033[0m'
        if w[0] not in words:
            words.append(w[0])
        words.remove(w[0])

    print(4*" " + "|" + " ".join([f" {i+1}" if i < 9 else f"{i+1}" for i in range(len(grid[0]))]) + " |\t" + words[0] if len(words) > 0 else find_words[0][0])
    print("_"*5 + "_" * (len(grid[0])*3) + "|\t" + words[1] if len(words) > 1 else find_words[1][0])

    for i, row in enumerate(grid):
        if i+2 < len(words):
            print(f" {i + 1}" if i < 9 else f"{i + 1}", f" | {'  '.join(row)} |\t" + words[i + 2])
        elif i+1 < len(words):
            print(f" {i + 1}" if i < 9 else f"{i + 1}", f" | {'  '.join(row)} ")
        elif len(find_words) > 0 and i+1 < len(words)+len(find_words):
            print(f" {i + 1}" if i < 9 else f"{i + 1}", f" | {'  '.join(row)} |\t" + '\033[1;3;33;43m' + '\033[31m' + find_words[i+1-len(words)][0] + '\033[0m')
        else:
            print(f" {i + 1}" if i < 9 else f"{i + 1}", f" | {'  '.join(row)} ")
