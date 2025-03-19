from typing import List

from Ra3MapBridge import Ra3MapWrap
from MapCoreLibMod.Core.Util import PathUtil

from ra3map.enums.passability_enum import PassabilityEnum
from ra3map.enums.texture_enum import TextureEnum

from ra3map.models.player_model import PlayerModel
from ra3map.models.object_model import ObjectModel
from ra3map.models.team_model import TeamModel
from ra3map.models.waypoint_model import WaypointModel


class Ra3Map:
    def __init__(self, original_map_obj):
        self._map = original_map_obj

    # ---------  IO ----------


    @staticmethod
    def get_default_map_path() -> str:
        """
        Get the default map path
        :return:
        """
        return PathUtil.RA3MapFolder

    @staticmethod
    def new_map(playable_width: int, playable_height: int, border_with: int, map_name: str,
                init_player_start_waypoint_cnt=2,
                output_path: str = None,
                default_texture: TextureEnum=TextureEnum.Dirt_Yucatan03):
        """
        Create a new map
        :param playable_width: map width
        :param playable_height: map height
        :param border_with: map border width
        :param map_name: map name
        :param output_path: the parent path of the map, if None, use the default path
        :param default_texture: default texture
        :return:
        """
        if output_path is None:
            output_path = Ra3Map.get_default_map_path()

        return Ra3Map(Ra3MapWrap.NewMap(output_path, map_name, playable_width, playable_height, border_with, init_player_start_waypoint_cnt,default_texture.value))

    @staticmethod
    def load_map(map_name: str, parent_path: str = None):
        """
        Load a map
        :param map_name: map name
        :param parent_path: the parent path of the map, if None, use the default path
        :return:
        """
        if parent_path is None:
            parent_path = Ra3Map.get_default_map_path()
        return Ra3Map(Ra3MapWrap.Open(parent_path, map_name))

    def save(self):
        """
        Save the map
        :return:
        """
        self._map.Save()

    def save_as(self, map_name: str, output_path: str = None):
        """
        Save the map as a new map
        :param map_name: map name
        :param output_path: the parent path of the map, if None, use the default path
        :return:
        """
        if output_path is None:
            output_path = Ra3Map.get_default_map_path()
        self._map.SaveAs(output_path, map_name)

    # --------- camera ----------

    @property
    def camera_ground_min_height(self) -> float:
        """
        Get the minimum height limit of the camera
        :return:
        """
        return self._map.CameraGroundMinHeight

    @camera_ground_min_height.setter
    def camera_ground_min_height(self, value: float):
        """
        Set the minimum height limit of the camera
        :param value:
        :return:
        """
        self._map.CameraGroundMinHeight = value

    @property
    def camera_ground_max_height(self) -> float:
        """
        Get the maximum height limit of the camera
        :return:
        """
        return self._map.CameraGroundMaxHeight

    @camera_ground_max_height.setter
    def camera_ground_max_height(self, value: float):
        """
        Set the maximum height limit of the camera
        :param value:
        :return:
        """
        self._map.CameraGroundMaxHeight = value

    @property
    def camera_min_height(self) -> float:
        """
        Get the minimum height of the camera
        :return:
        """
        return self._map.CameraMinHeight

    @camera_min_height.setter
    def camera_min_height(self, value: float):
        """
        Set the minimum height of the camera
        :param value:
        :return:
        """
        self._map.CameraMinHeight = value

    @property
    def camera_max_height(self) -> float:
        """
        Get the maximum height of the camera
        :return:
        """
        return self._map.CameraMaxHeight

    @camera_max_height.setter
    def camera_max_height(self, value: float):
        """
        Set the maximum height of the camera
        :param value:
        :return:
        """
        self._map.CameraMaxHeight = value

    # ---------  texture ----------

    def set_tile_texture(self, x: int, y: int, texture: TextureEnum):
        """
        Set the texture of the tile
        :param x:
        :param y:
        :param texture:
        :return:
        """
        self._map.SetTileTexture(x, y, texture.value)

    def get_tile_texture(self, x: int, y: int) -> TextureEnum:
        """
        Get the texture of the tile
        :param x:
        :param y:
        :return:
        """
        return TextureEnum(self._map.GetTileTexture(x, y))

    # ---------  terrain ----------

    def set_terrain_passability(self, x: int, y: int, passability: PassabilityEnum):
        """
        Set the passability of the terrain
        :param x:
        :param y:
        :param passability:
        :return:
        """
        self._map.SetPassability(x, y, passability.value)

    def get_terrain_passability(self, x: int, y: int):
        """
        Get the passability of the terrain
        :param x:
        :param y:
        :return:
        """
        return PassabilityEnum(self._map.GetPassability(x, y))

    def update_terrain_passability(self):
        """
        Update the passability of the terrain automatically.
        Suggestions: call this function after you have set the passability of the terrain.
        :return:
        """
        self._map.UpdatePassabilityMap()

    def set_terrain_height(self, x: int, y: int, height: float):
        """
        Set the height of the terrain
        :param x:
        :param y:
        :param height:
        :return:
        """
        self._map.SetTerrainHeight(x, y, height)

    def get_terrain_height(self, x: int, y: int):
        """
        Get the height of the terrain
        :param x:
        :param y:
        :return:
        """
        return self._map.GetTerrainHeight(x, y)


    # ---------  team ----------

    def get_teams(self) -> List[TeamModel]:
        """
        Get the teams
        :return:
        """
        return self._map.GetTeams()

    def add_team(self, team_name: str, belong_to_player_name: str) -> TeamModel:
        """
        Add a team
        :param team_name:
        :param belong_to_player_name:
        :return:
        """
        return self._map.AddTeam(team_name, belong_to_player_name)

    def remove_team(self, team_name: str, belong_to_player_name: str) -> bool:
        """
        Remove a team
        :param team_name:
        :return: is success
        """
        return self._map.RemoveTeam(team_name, belong_to_player_name)


    # ---------  object ----------

    def get_objects(self) -> List[ObjectModel]:
        """
        Get the objects
        :return:
        """
        return self._map.GetObjects()

    def add_object(self, object_name: str, x: float, y: float) -> ObjectModel:
        """
        Add an object
        :param object_name:
        :param x:
        :param y:
        :return:
        """
        return self._map.AddObject(object_name, x, y)

    def remove_object(self, unique_id: str) -> bool:
        """
        Remove an object
        :param unique_id:
        :return: is success
        """
        return self._map.RemoveObjectOrWaypoint(unique_id)

    # ---------  waypoint ----------

    def get_waypoints(self) -> List[WaypointModel]:
        """
        Get the waypoints
        :return:
        """
        return self._map.GetWaypoints()

    def add_waypoint(self, waypoint_name: str, x: float, y: float) -> WaypointModel:
        """
        Add a waypoint
        Attention: Unlike the map width/height, x or y are 10 times of width/height, and the type of x and y is float.
        :param waypoint_name:
        :param x:
        :param y:
        :return:
        """
        return self._map.AddWaypoint(waypoint_name, x, y)

    def remove_waypoint(self, waypoint_name: str) -> bool:
        """
        Remove a waypoint
        :param waypoint_name:
        :return:
        """
        return self._map.RemoveWaypoint(waypoint_name)

    def add_player_start_waypoint(self, player_index: int, x: float, y: float) -> WaypointModel:
        """
        Add a player start waypoint
        :return:
        """
        return self._map.AddPlayerStartWaypoint(player_index, x, y)

    def get_waypoint(self, waypoint_name) -> WaypointModel:
        """
        Get a waypoint by name
        :param waypoint_name:
        :return:
        """
        return self._map.GetWaypoint(waypoint_name)

    # ---------  basic info ----------

    @property
    def map_width(self) -> int:
        """
        Get the map width
        :return:
        """
        return self._map.MapWidth

    @property
    def map_height(self) -> int:
        """
        Get the map height
        :return:
        """
        return self._map.MapHeight

    @property
    def map_border_width(self) -> int:
        """
        Get the map border width
        :return:
        """
        return self._map.MapBorderWidth

    @property
    def map_playable_width(self):
        """
        Get the map playable width
        :return:
        """
        return self._map.MapPlayableWidth

    @property
    def map_playable_height(self):
        """
        Get the map playable height
        :return:
        """
        return self._map.MapPlayableHeight


    # --- player ----

    def get_players(self) -> List[PlayerModel]:
        """
        Get the players
        :return:
        """
        return self._map.GetPlayers()





