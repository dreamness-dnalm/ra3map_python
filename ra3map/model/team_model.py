
class TeamModel:
    def __init__(self):
        raise NotImplementedError()

    @property
    def team_name(self) -> str:
        raise NotImplementedError()

    @team_name.setter
    def team_name(self, value: str):
        raise NotImplementedError()

    @property
    def belong_to_player_name(self) -> str:
        raise NotImplementedError()

    @belong_to_player_name.setter
    def belong_to_player_name(self, value: str):
        raise NotImplementedError()