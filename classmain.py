import rhinoscriptsyntax as rs

from person import Person
from room import Room

p = Person(12, "a")
q = Person(14, "b")
print(p.age, q.age)

p.increment_age()
print(p.age, p.name)



C=rs.GetObject("pick")
r = Room("a", C)
r.draw_walls()
r.draw_flr()
r.draw_roof()

