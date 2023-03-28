from mazelib import Maze
from mazelib.generate.Prims import Prims
from mazelib.transmute.CuldeSacFiller import CuldeSacFiller


m = Maze()
m.generator = Prims(12,24)
m.transmuters = [CuldeSacFiller()]

m.generate()
m.generate_entrances(start_outer=False, end_outer=False)
m.transmute()


with open('maze.txt', 'w') as f:
    f.write(str(m))
    f.close()
