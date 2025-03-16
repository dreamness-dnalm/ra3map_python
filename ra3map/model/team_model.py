
class TeamModel:
    def __init__(self):
        raise NotImplementedError()

    @property
    def team_name(self) -> str:
        """
        Get the team name
        :return:
        """
        raise NotImplementedError()

    @team_name.setter
    def team_name(self, value: str):
        """
        Set the team name
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def belong_to_player_name(self) -> str:
        """
        Get the player name
        :return:
        """
        raise NotImplementedError()

    @belong_to_player_name.setter
    def belong_to_player_name(self, value: str):
        """
        Set the player name
        :param value:
        :return:
        """
        raise NotImplementedError()