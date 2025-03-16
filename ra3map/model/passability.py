from enum import Enum


class PassabilityEnum(Enum):
    Passable = "Passable"
    Impassable = "Impassable"
    ImpassableToPlayers = "ImpassableToPlayers"
    ImpassableToAirUnits = "ImpassableToAirUnits"
    ExtraPassable = "ExtraPassable"