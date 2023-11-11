class GameRegion():
    """Represents the region in which the robot plays.
    """
    def is_in_zone(self, zone):
        """Checks whether a person is in the given zone.

        Args:
            zone (int): a zone number (1-3)
        """
        pass

    def all_zones_empty(self):
        """Checks whether no person is in any zone.
        """
        pass

    def ensure_is_in_zone(self, desired_zone, num_tries=5, time_in_seconds_for_opponent_to_move=2):
        """Ensures that the currently focused person is in the given zone by reprimanding him to move.

        Args:
            desired_zone (int): the target zone (1-3)
            num_tries (int, optional): How many times the person should be reprimanded to move. Defaults to 5.
            time_in_seconds_for_opponent_to_move (int, optional): The time in seconds the person has to move. Defaults to 2.
        """
        pass