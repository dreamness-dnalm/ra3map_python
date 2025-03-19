from enum import Enum


class ObjectModel:
    def __init__(self):
        raise NotImplementedError()

    @property
    def angle(self) -> float:
        """
        Get the angle of the object
        :return:
        """
        raise NotImplementedError()

    @angle.setter
    def angle(self, value: float):
        """
        Set the angle of the object, default 0f
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def x(self):
        """
        Get the x position of the object
        :return:
        """
        raise NotImplementedError()

    @x.setter
    def x(self, value):
        """
        Set the x position of the object
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def y(self):
        """
        Get the y position of the object
        :return:
        """
        raise NotImplementedError()

    @y.setter
    def y(self, value):
        """
        Set the y position of the object
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def unique_id(self) -> str:
        """
        Get the unique id of the object
        :return:
        """
        raise NotImplementedError()

    @property
    def type_name(self) -> str:
        """
        Get the type name of the object
        :return:
        """
        raise NotImplementedError()

    @type_name.setter
    def type_name(self, value: str):
        """
        Set the type name of the object
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def belong_to_team_full_name(self) -> str:
        """
        Get the team name of the object
        :return:
        """
        raise NotImplementedError()

    @belong_to_team_full_name.setter
    def belong_to_team_full_name(self, value: str):
        """
        Set the team name of the object
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def object_name(self) -> str:
        """
        Get the object name of the object
        :return:
        """
        raise NotImplementedError()

    @object_name.setter
    def object_name(self, value: str):
        """
        Set the object name of the object
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def initial_health(self) -> int:
        """
        Get the initial health percentage of the object, default 100
        :return:
        """
        raise NotImplementedError()

    @initial_health.setter
    def initial_health(self, value: int):
        """
        Set the initial health percentage of the object, default 100
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def enable(self) -> bool:
        """
        Get the enable status of the object, default True
        :return:
        """
        raise NotImplementedError()

    @enable.setter
    def enable(self, value: bool):
        """
        Set the enable status of the object, default True
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def indestructible(self) -> bool:
        """
        Get the indestructible status of the object, default False
        :return:
        """
        raise NotImplementedError()

    @indestructible.setter
    def indestructible(self, value: bool):
        """
        Set the indestructible status of the object, default False
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def unsellable(self) -> bool:
        """
        Get the unsellable status of the object, default False
        :return:
        """
        raise NotImplementedError()

    @unsellable.setter
    def unsellable(self, value: bool):
        """
        Set the unsellable status of the object, default False
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def powered(self) -> bool:
        """
        Get the powered status of the object, default True
        :return:
        """
        raise NotImplementedError()

    @powered.setter
    def powered(self, value: bool):
        """
        Set the powered status of the object, default True
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def recruitable_ai(self):
        """
        Get the recruitable ai of the object, default True
        :return:
        """
        raise NotImplementedError()

    @recruitable_ai.setter
    def recruitable_ai(self, value):
        """
        Set the recruitable ai of the object, default True
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def targetable(self) -> bool:
        """
        Get the targetable status of the object, default False
        :return:
        """
        raise NotImplementedError()

    @targetable.setter
    def targetable(self, value: bool):
        """
        Set the targetable status of the object, default False
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def sleeping(self) -> bool:
        """
        Get the sleeping status of the object, default False
        :return:
        """
        raise NotImplementedError()

    @sleeping.setter
    def sleeping(self, value: bool):
        """
        Set the sleeping status of the object, default False
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def stance(self) -> str:
        """
        Get the stance of the object, default GUARD
        options: GUARD / AGGRESSIVE / HOLD_POSITION / HOLD_FIRE
        :return:
        """
        raise NotImplementedError()

    @stance.setter
    def stance(self, value: str):
        """
        Set the stance of the object, default GUARD
        options: GUARD / AGGRESSIVE / HOLD_POSITION / HOLD_FIRE
        :param value:
        :return:
        """
        raise NotImplementedError()

    @property
    def experience_level(self) -> int:
        """
        Get the experience level of the object, default 1
        range: [1, 4]
        :return:
        """
        raise NotImplementedError()

    @experience_level.setter
    def experience_level(self, value: int):
        """
        Set the experience level of the object, default 1
        range: [1, 4]
        :param value:
        :return:
        """
        raise NotImplementedError()

