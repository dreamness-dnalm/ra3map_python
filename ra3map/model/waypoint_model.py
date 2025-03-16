class WaypointModel:
    def __init__(self):
        raise NotImplementedError()

    @property
    def x(self) -> float:
        """
        Get the x position of the waypoint
        :return:
        """
        raise NotImplementedError()

    @x.setter
    def x(self, value: float):
        """
        Set the x position of the waypoint
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def y(self) -> float:
        """
        Get the y position of the waypoint
        :return:
        """
        raise NotImplementedError()

    @y.setter
    def y(self, value: float):
        """
        Set the y position of the waypoint
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def unique_id(self) -> str:
        """
        Get the unique id of the waypoint
        :return:
        """
        raise NotImplementedError()

    @unique_id.setter
    def unique_id(self, value: str):
        """
        Set the unique id of the waypoint
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def waypoint_name(self) -> str:
        """
        Get the name of the waypoint
        :return:
        """
        raise NotImplementedError()

    @waypoint_name.setter
    def waypoint_name(self, value: str):
        """
        Set the name of the waypoint
        :param value:
        :return:
        """
        raise NotImplementedError()