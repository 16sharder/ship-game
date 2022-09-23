# Author: Sara Harder
# GitHub username: 16sharder
# Date: 2/22/22
# Description: A battle ship game is created with the class ShipGame, and executed through various other classes. A
#              player can place ships on a grid, and then fire at opponent ships in an attempt to sink them.

class Overlap(Exception):
    """Creates an exception for when a player tries to place a ship that overlaps with an already placed ship, or the
    ship goes off the grid horizontally"""
    pass


class Node:
    """Represents a node in a linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A linked list with specific values stored to maintain the order of turns. Composes from class Node to create
    nodes in the linked list"""
    def __init__(self):
        """Initializes the head to a node for the first player, and its next value as a node for the second player.
        The second player's next value is the first player (the head). Takes no parameters and returns nothing"""
        self._head = Node("first")
        self._head.next = Node("second")
        self._head.next.next = self._head

    def get_head(self):
        """Returns the head of the linked list (always the Node with value "first")"""
        return self._head


class EmptyGrid:
    """Represents an empty battleship grid"""
    def __init__(self):
        """Doesn't take any parameters. Creates a dictionary to represent a grid with row letters as keys, lists of
        column numbers as values"""
        self._grid = {
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
        }

    def get_grid(self):
        """Returns the grid in its current state"""
        return self._grid


class Ship:
    """Represents a ship object, which occupies specific coordinates, calculated based on the user input"""
    def __init__(self, length, coordinate, direction):
        """Takes a ship length, initial coordinate, and direction as parameters, and initializes them as data members.
        Also initializes an empty list for all of the ship's coordinates, and 2 dictionaries for conversion from letters
        to numbers and vice versa"""
        self._start_coordinate = coordinate
        self._length = length
        self._direction = direction
        self._ship_coordinates = []
        self._letters_to_nums = {  # used to calculate coordinates with integers
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10
        }
        self._nums_to_letters = {  # used to convert the calculated integers back to coordinates
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J"
        }

    def calculate_coordinates(self):
        """Determines the coordinates that the ship occupies"""
        if self._direction == "R":  # if the ship is horizontal (row)
            for num in range(self._start_coordinate[1], self._start_coordinate[1] + self._length):
                coordinate = [self._start_coordinate[0], num]  # calculates each coordinate based on length
                self._ship_coordinates.append(coordinate)  # adds the coordinate to the ship's coordinates
        elif self._direction == "C":  # if the ship is vertical (column)
            for num in range(self._letters_to_nums[self._start_coordinate[0]],  # calculates coordinate based on length
                             self._letters_to_nums[self._start_coordinate[0]] + self._length):
                coordinate = [self._nums_to_letters[num], self._start_coordinate[1]]
                self._ship_coordinates.append(coordinate)  # adds the coordinates to the ship's coordinates
        return self._ship_coordinates

    def get_coordinates(self):
        """Returns the coordinates of the ship"""
        return self._ship_coordinates


class ShipGrid(EmptyGrid):
    """Represents a specific player's game board with all of their ships, inheriting the grid from class EmptyGrid.
    Includes methods to add ships to the grid and the list of ships, and remove ships from the list of ships."""
    def __init__(self):
        """Takes no parameters, but initializes a grid data member inherited from EmptyGrid, and initializes an empty
        list of ships on the board"""
        super().__init__()  # inherits data member "grid" from EmptyGrid
        self._ships_list = []

    def add_ship(self, ship):
        """'Adds' a ship object (taken as a parameter) to the player's grid by removing all coordinates of that ship
        from the player's grid, then adds the ship object to the list of ships"""
        coordinates_list = ship.calculate_coordinates()  # retrieves the coordinates of the ship object
        backup_counter = 0
        for coordinate in coordinates_list:  # for each coordinate
            column_numbers = self._grid[coordinate[0]]  # retrieves the list of nums for that letter
            if coordinate[1] in column_numbers:
                column_numbers.remove(coordinate[1])  # deletes the coordinate number for that letter
                backup_counter += 1
            else:  # if the space is already occupied
                for num in range(0, backup_counter):  # re-adds any coordinates already removed for that ship
                    prev_coord = coordinates_list[num]
                    column_numbers = self._grid[prev_coord[0]]
                    column_numbers.append(prev_coord[1])
                    column_numbers.sort()  # ensures the original list for each letter is in the same order
                raise Overlap   # does not add the ship, raises an error instead
        self._ships_list.append(ship)  # adds the ship object to the list of ships

    def remove_ships(self):
        """'Removes' a ship from the player's list of ships by determining if its coordinates have been added back to
        the player's grid"""
        ship_copy = list(self._ships_list)  # a copy of the ship's list for iteration
        for ship in ship_copy:  # analyzes each ship in the player's list
            coordinates_list = ship.get_coordinates()  # gets the list of coordinates the ship occupies
            coordinate_copy = list(coordinates_list)  # copies the list of coordinates
            for coordinate in coordinates_list:  # for each coordinate in the list
                column_numbers = self._grid[coordinate[0]]  # gets the list of numbers for the coordinate's row letter
                if coordinate[1] in column_numbers:  # if the coordinate's number is in the list
                    coordinate_copy.remove(coordinate)  # deletes the coordinate from the list of coordinates copy
            if coordinate_copy == list():  # if the list is empty (all coordinates have been fired at)
                self._ships_list.remove(ship)  # the ship is sunk and removed from the list of ships

    def get_ships_list(self):
        """Returns the updated ships list for specified player"""
        self.remove_ships()  # calls remove ships to update whether a ship has been sunk or not
        return self._ships_list


class ShipGame:
    """Represents a game of battleship, where players can place ships on a grid at the beginning, then fire at each
    others ships to sink them. Composes a turn order from the class LinkedList and player grids from the class ShipGrid.
    Uses class Ship to create ships that are added to a player's grid in the place_ship method. Includes a method that
    represents a player's turn, used to let players attempt to fire on their opponent's ships, removing those ships from
    the grid"""
    def __init__(self):
        """Takes no parameters. Initializes each player's game board. Sets the current state of the game to unfinished.
        Initializes the current player to the first player through a linked list (initialized as player order)."""
        self._first_grid = ShipGrid()
        self._second_grid = ShipGrid()
        self._current_state = "UNFINISHED"
        self._player_order = LinkedList()
        self._current_player = self._player_order.get_head()
        self._first_num = 5
        self._second_num = 5

    def place_ship(self, player, length, coordinate, direction):
        """Takes as parameters the first or second player, the length of a ship that player is trying to place, the
        ship's coordinate closest to A1, and the direction of the ship (vertical or horizontal). Runs tests to make sure
        the ship is of length 2 or longer, the ship does not go outside of the player's grid, and the ship does not
        overlap any previously placed ships. If any of these tests fail, the function returns false. Otherwise, the ship
        is added to the player's grid, and the function returns true."""
        coordinate = [coordinate[0], int(coordinate[1:])]  # converts the string input to list with a letter and a num
        if length < 2:
            return False
        ship = Ship(length, coordinate, direction)  # creates a ship object with the input
        if player == "first":  # determines which player grid the ship should be added to
            player_grid = self._first_grid
        else:
            player_grid = self._second_grid
        try:
            player_grid.add_ship(ship)  # adds the ship to the grid
        except KeyError:  # raised when the ship is out of the board's range
            return False
        except Overlap:  # raised when the ship overlaps with another already placed ship
            return False
        return True

    def get_current_state(self):
        """Returns the current state of the game"""
        return self._current_state

    def fire_torpedo(self, player, coordinate):
        """Takes as parameters a player and the coordinate they would like to hit. Runs tests to determine the move is
        valid, then updates the opponent's grid if the torpedo has hit a ship. If the move is valid, the current state
        of the game is updated, the turn moves to the next player, and the func returns true. Else returns false"""
        if self._current_state != "UNFINISHED":  # if the game has ended
            return False
        if player != self._current_player.data:  # if the wrong player tries to make a move
            return False
        coordinate = [coordinate[0], int(coordinate[1:])]  # converts the string input to a list with letter and num
        if player == "first":  # determines which player grid is retrieved
            player_grid = self._second_grid  # opposite grid is retrieved since player is firing towards opponent
        else:
            player_grid = self._first_grid
        grid_dict = player_grid.get_grid()  # retrieves the grid itself
        if coordinate[1] not in grid_dict[coordinate[0]]:  # if the ship is on the coordinate, the torpedo hits
            grid_dict[coordinate[0]].append(coordinate[1])  # the coordinate is added back into the grid
            grid_dict[coordinate[0]].sort()
            print("Torpedo hit!")
        else:
            print("Torpedo missed.")
        if player == "first":
            num = self.get_num_ships_remaining("second")
            if num < self._second_num:
                print("Ship sunk!")
                self._second_num = num
        else:
            num = self.get_num_ships_remaining("first")
            if num < self._first_num:
                print("Ship sunk!")
                self._first_num = num
        player_grid.remove_ships()  # updates the opponent's ship list
        empty_grid = EmptyGrid()  # initializes an empty grid for comparison
        if player_grid.get_grid() == empty_grid.get_grid():  # if the opponent's grid is the same as a base grid
            self._current_state = player.upper() + "_WON"  # the player has won, all ships have been sunk
        self._current_player = self._current_player.next  # it becomes the next player's turn
        return True

    def get_num_ships_remaining(self, player):
        """Takes as a parameter a player, then retrieves that player's ShipGrid, and their list of ships. Returns the
        length of the list of ships."""
        if player == "first":  # determines which player grid is retrieved
            player_grid = self._first_grid
        else:
            player_grid = self._second_grid
        ships_list = player_grid.get_ships_list()  # retrieves the ship list from their grid
        return len(ships_list)
