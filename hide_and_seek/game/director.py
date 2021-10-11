from game.console import Console
from game.seeker import Seeker
from game.hider import Hider


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        seeker (Seeker): An instance of the class of objects known as Seeker.
        hider (Hider): An instance of the class of objects known as Hider.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.seeker = Seeker()
        self.keep_playing = True
        self.hider = Hider()

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        message = self.seeker.get_message()
        self.console.write(message)
        location = self.console.read_number("Enter a location [1-1000]: ")
        self.seeker.move(location)

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """
        self.hider.watch(self.seeker.location)

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the hider provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        hint = self.hider.get_hint()
        self.console.write(hint)
        self.keep_playing = (self.hider.distance[-1] != 0)
