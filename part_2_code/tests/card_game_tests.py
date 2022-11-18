import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card_ace = Card("clubs", 1)
        self.card_eight = Card("hearts", 8)
        self.card_five = Card("spades", 5)

    def test_check_for_ace__with_ace__true(self):
        self.assertTrue(self.card_game.check_for_ace(self.card_ace))

    def test_check_for_ace__with_five__false(self):
        self.assertFalse(self.card_game.check_for_ace(self.card_five))

    def test_highest_card__returning_card1(self):
        highest_card = self.card_game.highest_card(self.card_eight, self.card_five)
        self.assertEqual(self.card_eight, highest_card)

    def test_highest_card__returning_card2(self):
        highest_card = self.card_game.highest_card(self.card_five, self.card_eight)
        self.assertEqual(self.card_eight, highest_card)