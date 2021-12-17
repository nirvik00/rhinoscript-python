import rhinoscriptsyntax as rs

class Room(object):
    def __init__(self, name, crv):
        self.name=name
        self.crv=crv
    def draw_walls(self):
        v=rs.AddLine([0,0,0], [0,0,10])
        self.walls = rs.ExtrudeCurve(self.crv, v)
        rs.DeleteObject(v)
    def draw_flr(self):
        self.flr=rs.AddPlanarSrf(self.crv)
    def draw_roof(self):
        self.roof = rs.CopyObject(self.flr, [0,0,10])

