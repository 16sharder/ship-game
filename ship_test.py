import unittest
import ShipGame


class TestShipGame(unittest.TestCase):
    def test_ship(self):
        """Tests ships coordinates are correct"""
        ship_1 = ShipGame.Ship(3, ["G", 7], "R")
        coord = ship_1.calculate_coordinates()
        ship_2 = ShipGame.Ship(2, ["A", 1], "C")
        coord_2 = ship_2.calculate_coordinates()
        self.assertEqual(coord, [["G", 7], ["G", 8], ["G", 9]])
        self.assertEqual(coord_2, [["A", 1], ["B", 1]])

    def test_add_horizontal(self):
        """Tests ship exits horizontally off grid"""
        ship = ShipGame.Ship(5, ["G", 7], "R")
        grid = ShipGame.ShipGrid()
        try:
            grid.add_ship(ship)
        except ShipGame.Overlap:
            add = False
        else:
            add = True
        self.assertEqual(add, False)
        self.assertEqual(grid.get_grid(), {
            "A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "B": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "C": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "D": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "E": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "F": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "G": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "H": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "I": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "J": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        })

    def test_add_vertical(self):
        """Tests ship exits vertically off grid"""
        ship = ShipGame.Ship(5, ["G", 7], "C")
        grid = ShipGame.ShipGrid()
        try:
            grid.add_ship(ship)
        except KeyError:
            add = False
        else:
            add = True
        self.assertEqual(add, False)
        self.assertEqual(grid.get_ships_list(), [])

    def test_add_overlap(self):
        """Tests ship overlaps with other ship"""
        ship_1 = ShipGame.Ship(2, ["C", 2], "R")
        grid = ShipGame.ShipGrid()
        ship_2 = ShipGame.Ship(3, ["A", 2], "C")
        grid.add_ship(ship_1)
        try:
            grid.add_ship(ship_2)
        except ShipGame.Overlap:
            add = False
        else:
            add = True
        self.assertEqual(add, False)
        self.assertEqual(grid.get_grid(), {
            "A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "B": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "C": [1, 4, 5, 6, 7, 8, 9, 10],
            "D": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "E": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "F": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "G": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "H": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "I": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "J": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        })

    def test_add_successful_grid(self):
        """Tests ship is added correctly to grid"""
        ship_1 = ShipGame.Ship(2, ["C", 2], "R")
        grid = ShipGame.ShipGrid()
        ship_2 = ShipGame.Ship(3, ["G", 2], "C")
        grid.add_ship(ship_1)
        try:
            grid.add_ship(ship_2)
        except ShipGame.Overlap:
            add = False
        else:
            add = True
        self.assertEqual(add, True)
        self.assertEqual(grid.get_grid(), {
            "A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "B": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "C": [1, 4, 5, 6, 7, 8, 9, 10],
            "D": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "E": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "F": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "G": [1, 3, 4, 5, 6, 7, 8, 9, 10],
            "H": [1, 3, 4, 5, 6, 7, 8, 9, 10],
            "I": [1, 3, 4, 5, 6, 7, 8, 9, 10],
            "J": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        })

    def test_add_successful_list(self):
        """Tests ship is added correctly to the ship list"""
        ship_1 = ShipGame.Ship(2, ["C", 2], "R")
        grid = ShipGame.ShipGrid()
        ship_2 = ShipGame.Ship(3, ["G", 2], "C")
        grid.add_ship(ship_1)
        try:
            grid.add_ship(ship_2)
        except ShipGame.Overlap:
            add = False
        else:
            add = True
        self.assertEqual(add, True)
        self.assertEqual(grid.get_ships_list(), [ship_1, ship_2])

    def test_place_vertical(self):
        """Tests ship exits vertically off grid"""
        game = ShipGame.ShipGame()
        test = game.place_ship("first", 5, "G7", "C")
        self.assertEqual(test, False)

    def test_place_horizontal(self):
        """Tests ship exits horizontally off grid"""
        game = ShipGame.ShipGame()
        test = game.place_ship("first", 5, "G7", "R")
        self.assertEqual(test, False)

    def test_place_overlap(self):
        """Tests ship overlaps with other ship"""
        game = ShipGame.ShipGame()
        game.place_ship("first", 2, "C2", "R")
        test = game.place_ship("first", 3, "A2", "C")
        self.assertEqual(test, False)

    def test_place_short(self):
        """Tests short ship placement"""
        game = ShipGame.ShipGame()
        test = game.place_ship("first", 1, "A2", "C")
        self.assertEqual(test, False)

    def test_place_successful(self):
        """Tests successful ship placement"""
        game = ShipGame.ShipGame()
        test = game.place_ship("first", 3, "A10", "C")
        self.assertEqual(test, True)
        self.assertEqual(game._first_grid.get_grid(), {
            "A": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "B": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "C": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "D": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "E": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "F": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "G": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "H": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "I": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "J": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        })

    def test_place_two_player(self):
        """Tests that player boards are different"""
        game = ShipGame.ShipGame()
        test_1 = game.place_ship("first", 2, "C2", "R")
        test_2 = game.place_ship("second", 3, "A2", "C")
        self.assertEqual(True, test_1)
        self.assertEqual(test_1, test_2)
        game.place_ship("first", 6, "E3", "R")
        game.place_ship("second", 6, "E3", "R")
        self.assertNotEqual(game._first_grid.get_grid(), game._second_grid.get_grid())

    def place_ships(self):
        """Places ships beforehand"""
        game = ShipGame.ShipGame()
        game.place_ship("first", 6, "E3", "R")
        game.place_ship("second", 6, "E3", "R")
        game.place_ship("first", 2, "C2", "R")
        game.place_ship("second", 3, "A10", "C")
        return game

    def test_fire_torpedo_not_turn(self):
        """Tests unsuccessful hit if not player turn, and player turn remains previous player"""
        game = self.place_ships()
        test = game.fire_torpedo("second", "E3")
        self.assertEqual(test, False)

    def test_fire_torpedo_successful(self):
        """Tests that a function returns true upon successful fire"""
        game = self.place_ships()
        test = game.fire_torpedo("first", "F3")
        self.assertEqual(test, True)
        self.assertEqual(game._second_grid.get_grid(), {
            "A": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "B": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "C": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "D": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "E": [1, 2, 9, 10],
            "F": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "G": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "H": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "I": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "J": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        })

    def test_fire_torpedo_grid_update(self):
        """Tests that the grid is updated if the torpedo hits"""
        game = self.place_ships()
        test = game.fire_torpedo("first", "B10")
        self.assertEqual(test, True)
        self.assertEqual(game._second_grid.get_grid(), {
            "A": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "B": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "C": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "D": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "E": [1, 2, 9, 10],
            "F": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "G": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "H": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "I": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "J": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        })

    def test_fire_torpedo_multiple_coord(self):
        """Tests that a player can fire successfully on the same coordinate more than once"""
        game = self.place_ships()
        game.fire_torpedo("first", "E3")
        game.fire_torpedo("second", "E4")
        test = game.fire_torpedo("first", "E3")
        self.assertEqual(test, True)

    def test_fire_torpedo_game_won(self):
        """Tests unsuccessful fire if game is already won"""
        game = ShipGame.ShipGame()
        game.place_ship("first", 6, "E3", "R")
        game.place_ship("second", 3, "E3", "R")
        game.fire_torpedo("first", "E3")
        game.fire_torpedo("second", "E4")
        game.fire_torpedo("first", "E4")
        game.fire_torpedo("second", "E4")
        game.fire_torpedo("first", "E5")
        test = game.fire_torpedo("second", "E4")
        self.assertEqual(test, False)

    def test_current_state_unfinished(self):
        """Tests that the game is unfinished at a few points"""
        game = ShipGame.ShipGame()
        state_1 = game.get_current_state()
        self.assertEqual(state_1, "UNFINISHED")
        game.place_ship("first", 6, "E3", "R")
        game.place_ship("second", 6, "E3", "R")
        game.place_ship("first", 2, "C2", "R")
        game.place_ship("second", 3, "A2", "C")
        state_2 = game.get_current_state()
        self.assertEqual(state_2, "UNFINISHED")
        game.fire_torpedo("first", "E3")
        game.fire_torpedo("second", "E4")
        state_3 = game.get_current_state()
        self.assertEqual(state_3, "UNFINISHED")

    def test_current_state_one_won(self):
        """Tests that player one has won"""
        game = ShipGame.ShipGame()
        game.place_ship("first", 6, "E3", "R")
        game.place_ship("second", 3, "F3", "R")
        game.fire_torpedo("first", "F3")
        game.fire_torpedo("second", "E4")
        state_1 = game.get_current_state()
        self.assertEqual(state_1, "UNFINISHED")
        game.fire_torpedo("first", "F4")
        game.fire_torpedo("second", "E4")
        game.fire_torpedo("first", "F5")
        state_2 = game.get_current_state()
        self.assertEqual(state_2, "FIRST_WON")

    def test_current_state_two_won(self):
        """Tests that player two has won"""
        game = ShipGame.ShipGame()
        game.place_ship("first", 3, "F3", "R")
        game.place_ship("second", 6, "E3", "R")
        game.fire_torpedo("first", "E3")
        game.fire_torpedo("second", "F3")
        state_1 = game.get_current_state()
        self.assertEqual(state_1, "UNFINISHED")
        game.fire_torpedo("first", "E4")
        game.fire_torpedo("second", "F4")
        game.fire_torpedo("first", "E5")
        game.fire_torpedo("second", "F5")
        state_2 = game.get_current_state()
        self.assertEqual(state_2, "SECOND_WON")

    def test_num_ships_1(self):
        """Tests that player 1 loses a ship"""
        game = self.place_ships()
        game.fire_torpedo("first", "E3")
        game.fire_torpedo("second", "C2")
        num_1 = game.get_num_ships_remaining("first")
        self.assertEqual(num_1, 2)
        game.fire_torpedo("first", "E4")
        game.fire_torpedo("second", "C1")
        game.fire_torpedo("first", "E5")
        game.fire_torpedo("second", "C3")
        num_2 = game.get_num_ships_remaining("first")
        self.assertEqual(num_2, 1)

    def test_num_ships_2(self):
        """Tests that player 2 still has both ships"""
        game = self.place_ships()
        game.fire_torpedo("first", "E3")
        game.fire_torpedo("second", "C2")
        num_1 = game.get_num_ships_remaining("second")
        self.assertEqual(num_1, 2)
        game.fire_torpedo("first", "E4")
        game.fire_torpedo("second", "C1")
        game.fire_torpedo("first", "E5")
        game.fire_torpedo("second", "C3")
        num_2 = game.get_num_ships_remaining("second")
        self.assertEqual(num_2, 2)


if __name__ == '__main__':
    unittest.main(exit=False)
