
from Ra3MapBridge import Ra3MapWrap

class Ra3Map:
    def __init__(self, original_map_obj):
        self._map = original_map_obj

    @staticmethod
    def new_map(output_path, map_name, width, height, border, default_texture='Dirt_Yucatan03') -> Ra3Map:
        return Ra3Map(Ra3MapWrap.NewMap(output_path, map_name, width, height, border, default_texture))

    @staticmethod
    def load_map(parent_path: str, map_name: str) -> Ra3Map:
        return Ra3Map(Ra3MapWrap.Open(parent_path, map_name))

    def save(self):
        self._map.Save()

    def save_as(self, output_path: str, map_name: str):
        self._map.SaveAs(output_path, map_name)

    def set_height(self, x, y, height):
        self._map.SetHeight(x, y, height)

    def get_height(self, x, y):
        return self._map.GetHeight(x, y)

    def set_tile_texture(self, x, y, texture):
        self._map.SetTileTexture(x, y, texture)

    def get_tile_texture(self, x, y, texture):
        return self._map.GetTileTexture(x, y, texture)

    def set_passability(self, x, y, passability):
        self._map.SetPassability(x, y, passability)

    def get_passability(self, x, y, passability):
        return self._map.GetPassability(x, y, passability)

    def get_objs(self):
        return self._map.GetObjects()

    def add_obj(self, type_name, x, y, z, angle, obj_name):
        self._map.AddObject(type_name, x, y, z, angle, obj_name)

    def get_waypoints(self):
        return self._map.GetWaypoints()

    def add_waypoint(self, x, y, z, waypoint_name):
        self._map.AddWaypoint(x, y, z, waypoint_name)

    def get_map_width(self):
        return self._map.Width

    def get_map_height(self):
        return self._map.Height
