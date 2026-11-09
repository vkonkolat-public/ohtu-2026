import requests
from player import Player

class PlayerReader: 
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players

class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        nationality_players = []
        for player in self.players:
            if player.nationality == nationality:
                nationality_players.append(player)
        nationality_players.sort(key=lambda x: x.goals + x.assists, reverse=True)
        return nationality_players

    # def print_finnish_players(players):
    # print("FINNISHERS FROM FINLAND:")
    # players.sort(key=lambda x: x.goals + x.assists, reverse=True)
    # for player in players:
    #     if player.nationality == "FIN":
    #         print(f"{player.name:20} - TEAM: {player.team:18} - TEHOT: {player.goals + player.assists:4}")

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.get_players())
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

    # print("JSON-muotoinen vastaus:")
    # print(response)

    # players = []

    # for player_dict in response:
    #     player = Player(player_dict)
    #     players.append(player)

    # print("Oliot:")
    # for player in players:
    #     print(player)



if __name__ == "__main__":
    main()
