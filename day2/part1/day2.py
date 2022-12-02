from pathlib import Path

games = []
score = 0
cardsA = ['A', 'B', 'C']
cardsB = ['X', 'Y', 'Z']
winGames = [['C', 'X'], ['A', 'Y'], ['B', 'Z']]

path = Path(__file__).with_name('data.txt')

f = open(path, "r")
for x in f:
    games.append(x[:-1].split())

for game in games:
    score += cardsB.index(game[1]) + 1

    if cardsA.index(game[0]) == cardsB.index(game[1]):
        score += 3

    if game in winGames:
        score += 6


print(score)