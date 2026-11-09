import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    # print("Oliot:")
    # for player in players:
    #     print(player)

    print_finnish_players(players)

def print_finnish_players(players):
    print("FINNISHERS FROM FINLAND:")
    for player in players:
        if player.nationality == "FIN":
            print(f"{player.name:20} - TEAM: {player.team:18} - GOALS: {player.goals:3} - ASSISTS: {player.assists:3}")

if __name__ == "__main__":
    main()
