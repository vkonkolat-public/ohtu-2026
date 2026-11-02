import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_player_when_found(self):
        player = self.stats.search("Kurri")

        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_when_player_not_found(self):
        player = self.stats.search("Mikko")

        self.assertIsNone(player)

    def test_team_returns_only_players_of_given_team(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_returns_players_sorted_by_points(self):
        players = self.stats.top(2)
        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])