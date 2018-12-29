"""
   1. In your Python program, read the data from the supplied CSV file. Store that data in an appropriate data type so that it can be used in the next task.
   2. Create logic that can iterate through all 18 players and assign them to teams such that each team has the same number of players. The number of experienced players on each team should also be the same.
   3. Finally, the program should output a text file named -- teams.txt -- that contains the league roster listing the team name, and each player on the team including the player's information: name, whether they've played soccer before and their guardians' names.

"""

import csv

FILE_IN = "soccer_players.csv"
FILE_OUT = "teams.txt"
more_xp = []
less_xp = []

def get_players():
    """
    Opens the soccer_players.csv file, then grabs the fieldnames and seperates the experienced from the non experienced players
    You would use these list items in the create_teams functions.   That is the more_xp and the less_xp lists
    """
    with open(FILE_IN) as players:
        fieldnames = ['Name', 'Height (inches)', 'Soccer Experience', 'Guardian Name(s)']
        reader = csv.DictReader(players, delimiter=",", fieldnames=fieldnames)
        rows = list(reader)
        for row in rows:
            if row['Soccer Experience'] == 'NO':
                less_xp.append([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']])
            elif row['Soccer Experience'] == 'YES':
                more_xp.append([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']])
            else:
                del row
        create_teams()


def create_teams():
    """
    Splits up the teams evenly so all teams have some with experience and
    some without experience
    """
    sharks = ''
    dragons = ''
    raptors = ''
    for player in more_xp[0:3] + less_xp[0:3]:
        sharks += ', '.join(player) + '\n'
    for player in more_xp[3:6] + less_xp[3:6]:
        dragons += ', '.join(player) + '\n'
    for player in more_xp[6:9] + less_xp[6:9]:
        raptors += ', '.join(player) + '\n'
    with open(FILE_OUT, 'w') as new_teams:
        new_teams.writelines("Sharks\n" + sharks + "\n\n\n\n\n" + "Dragons\n" + dragons + "\n\n\n\n\n" + "Raptors\n" + raptors + "\n\n\n\n\n")


if __name__ == '__main__':
    get_players()

