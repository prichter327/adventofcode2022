from pathlib import Path

games = []
score = 0
cardsA = ['A', 'B', 'C']
cardsB = ['X', 'Y', 'Z']
winGames = [2, 3, 1]
loseGames = [3, 1, 2]

path = Path(__file__).with_name('data.txt')

f = open(path, "r")
for x in f:
    games.append(x[:-1].split())

for game in games:
    if game[1] == 'X': #lose
        score += loseGames[cardsA.index(game[0])]

    if game[1] == 'Y': #draw
        score += (cardsA.index(game[0]) + 1) + 3
    
    if game[1] == 'Z': #win
        score += winGames[cardsA.index(game[0])] + 6


print(score)