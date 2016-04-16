import sys


def main():
    teams = {}
    for line in sys.stdin:
        team_name = line[:line.find(':')]
        team_score = 0

        try:
            for c in line[line.find(':')+2:].split():
                team_score += int(c)
        except:
            continue

        teams[team_name] = team_score

    for team in sorted(teams.items(), key=lambda x: x[1], reverse=True):
        print(team[0]+': '+str(team[1])+' points')

if __name__ == '__main__':
    main()
