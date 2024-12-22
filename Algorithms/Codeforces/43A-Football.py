n = int(input())
goals = {}

for _ in range(n):
    team = input()
    if team in goals:
        goals[team] += 1
    else:
        goals[team] = 1

max_goals = 0
winner = ''

for teams in goals:
    if goals[teams] > max_goals:
        max_goals = goals[teams]
        winner = teams

print(winner)  