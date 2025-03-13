
from Ra3MapBridge import Ra3MapWrap
from MapCoreLib.Core.Util import PathUtil

class Ra3Map:
    def __init__(self, original_map_obj):
        self._map = original_map_obj

    @staticmethod
    def new_map(width:int, height:int, border:int, map_name:str, output_path:str=None, default_texture='Dirt_Yucatan03') -> Ra3Map:
        if output_path is None:
            output_path = Ra3Map.get_default_map_path()
        return Ra3Map(Ra3MapWrap.NewMap(output_path, map_name, width, height, border, default_texture))

    @staticmethod
    def load_map(map_name: str, parent_path: str=None) -> Ra3Map:
        if parent_path is None:
            parent_path = Ra3Map.get_default_map_path()
        return Ra3Map(Ra3MapWrap.Open(parent_path, map_name))

    @staticmethod
    def get_default_map_path() -> str:
        return PathUtil.RA3MapFolder

    def save(self):
        self._map.Save()

    def save_as(self, map_name: str, output_path: str=None):
        if output_path is None:
            output_path = self.get_default_map_path()
        self._map.SaveAs(output_path, map_name)

    def set_height(self, x:int, y:int, height:float):
        self._map.SetHeight(x, y, height)

    def get_height(self, x:int, y:int):
        return self._map.GetHeight(x, y)

    def set_tile_texture(self, x:int, y:int, texture:str):
        self._map.SetTileTexture(x, y, texture)

    def get_tile_texture(self, x:int, y:int, texture:str):
        return self._map.GetTileTexture(x, y, texture)

    def set_passability(self, x:int, y:int, passability:str):
        self._map.SetPassability(x, y, passability)

    def get_passability(self, x:int, y:int):
        return self._map.GetPassability(x, y)

    def get_objs(self):
        return self._map.GetObjects()

    def add_obj(self, type_name:str, x:float, y:float, z:float, angle:float, obj_name=""):
        self._map.AddObject(type_name, x, y, z, angle, obj_name)

    def get_waypoints(self):
        return self._map.GetWaypoints()

    def add_waypoint(self, x:float, y:float, z:float, waypoint_name:str):
        self._map.AddWaypoint(x, y, z, waypoint_name)

    def get_map_width(self) -> int:
        return self._map.Width

    def get_map_height(self) -> int:
        return self._map.Height
