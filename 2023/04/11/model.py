"""Modelization of a playground (a simple rectangular grid) by a graph.

This GRAPH is modelized has a `dict`:
. Keys are vertices coordinates, as a 2-tuple (x, y) of integers,
   from 0 to height - 1 for x (row index) and 
   from 0 to width - 1 for y (column index).
. Values are given as a `dict`:
   - `cat` key is for the category: WALL, FREE, or SLOW,
   - `neighb` stands for the `list` of neighbours' coordinates.
------------------------------------------------------------------------   
E.g. graph = {(0,0) : {'cat':WALL, 'neighb": [(0,1), (1,1), (1,0)], ...}
------------------------------------------------------------------------   

It is build upon a TEXT FILE where each character symbolize a box on 
the grid :
   - a space character means FREE, a normal, easy to cross box,
   - '.' means SLOW, a difficult to cross box,
   - any other indicates a WALL, a forbidden box.

THE GOAL of `get_path` function is to build an optimal path from a 
`start` box to an `end` one, using Dijkstra or (if possible) A* algo.
This function has to return as a 2-tuple the coordinates of path boxes, 
and of other boxes by the algorithm, in order to provide later a 
graphical representation of thoses boxes (see window.py).

              *** YOUR MISSION IF YOU ACCEPT IT  ***
               Implement this `get_path` function !
               
      Licence Creative Commons CC-BY - Jean-Marc Gervais 2021
"""
from math import sqrt

# Constants for preferences
from param import *

# This function is ready to use as is
def graph_from_file(filename):
    """Return the graph, as a dict, build from the named file.
    
    The file has to include a final empty line, and before this, 
    every lines have to have the same size.
     - A ' ' character is translated into FREE, 
     - a '.' into SLOW and 
     - any others into WALL.
    
    In this dict, the keys are box coordinates, as tuples of 2 int.
    In addition, two particular keys are added to store the dimensions 
    of the grid, 'length' and 'height'.
    """
    read_length = True
    height = 0
    graph = dict()
    
    # Nodes and their category, from the text file
    with open(filename, encoding='utf-8') as f:
        while 1:
            line = f.readline()
            if not line:
                break
            ll = len(line) - 1  # Without final carriage return
            if read_length:
                graph['length'] = ll 
                read_length = False
            elif ll != 1:       # Last (empty) line
                assert ll == graph['length'],\
                       (f"Length of line #{height+1} : " +
                        f"{ll} != {graph['length']}")
                        
            # Parse line except final character (carriage return)
            for col, car in enumerate(line[:-1]):
                if car == ' ':
                    categ = FREE
                elif car == '.':
                    categ = SLOW
                else:
                    categ = WALL
                graph[(height, col)] = {'cat':categ}
                
            height += 1
            
    graph['height'] = height
    
    # Add neighbours (!= WALL) of each node != WALL
    for row in range(height):
        for col in range(ll):
            # Neighbours are useless for WALLs 
            if graph[(row, col)]['cat'] == WALL:
                continue
            graph[(row, col)]["neighb"] = []
            for dr, dc in [ (-1, -1), (-1, 0), (-1, 1), 
                            (0, -1),           (0, 1),
                            (1, -1),  (1, 0),  (1, 1)  ] :
                rowdr, coldc = row + dr, col + dc
                if ( (rowdr, coldc) in graph 
                    and graph[(rowdr, coldc)]['cat'] != WALL ):
                      graph[(row, col)]["neighb"].append((rowdr, coldc))
    
    return graph


# This function is ready to use as is
def extra_cost(graph, pt, pt2):
    """Return the cost of the move from 1st to 2nd box* on the grid.
    
    (*) These boxes must have an common edge or vertex, 
        and must be different from WALL.
    
    This cost represents the "duration" of the move. It is calculated 
    from an approximative euclidian distance between boxes centers, 
    multiplied by a "speed coefficient" based on 1st box category.
    
    It aims to be added to the previous cost, hence the name of 
    the function.
    """
    x, y = pt
    xx, yy = pt2
    assert abs(x - xx) < 2 and abs(y - yy) < 2, "Non adjacents points"
    assert graph[pt]['cat'] != WALL and graph[pt2]['cat'] != WALL,\
           "'WALL' point"
    
    if x == xx or y == yy:
        d = 1.
    else:
        d = 1.41421356  # sqrt(2)
        
    coeff = 1 if graph[(x, y)]['cat'] == FREE else COEFF_SLOW
    
    return d * coeff

# ===== TO BE IMPLEMENTED. FUNNIEST PART OF THE JOB ! ==================
def get_path(graph, start, end, algo=DIJKSTRA):
    """Return an path and the "locked" vertices, from `start` to `end`.
    
    `graph` is a dict like the return value of `graph_from_file` func.,
    `start` and `end` are the coordinates of 2 boxes on the grid, 
    obviously, the returned path is from `start` to `end`.

    Return value is a 2-tuple of lists (of tuples as boxes coordinates):
     - Its first item provides ordered coordinates of path boxes.
     - The second one indicates "locked" vertices (no specific order 
       is expected here), which means they have got their final cost.
    """
    # EMPTY LISTS FOR NOW :-(
    path, locked = [], []
    
    return path, locked
# ======================================================================


if __name__ == "__main__":
    # Example with the smallest playground given
    graph = graph_from_file("test_map.txt")
    #print(graph, '\n')
    print(f"Dimensions L×h = {graph['length']}×{graph['height']}")
    print(get_path(graph, (1,2), (3,5)))
