# {'name': 'Rafael Harvey-Pinard', 'nationality': 'CAN', 'assists': 0, 'goals': 0, 'team': 'MTL', 'games': 1, 'id': 8481093}, 
# {'name': 'Klim Kostin', 'nationality': 'RUS', 'assists': 6, 'goals': 1, 'team': 'SJS', 'games': 35, 'id': 8480011}, 
# {'name': 'Ilya Mikheyev', 'nationality': 'RUS', 'assists': 14, 'goals': 20, 'team': 'CHI', 'games': 80, 'id': 8481624},

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']

    

    def __str__(self):
        return self.name
