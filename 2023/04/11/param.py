"""Preferences expressed as "constants", used in other modules.
               
      Licence Creative Commons CC-BY - Jean-Marc Gervais 2021
"""
# Abstract graph parameters
INF = 1_000_000 # "Infinite" in algorithms
FREE, SLOW, WALL = 0, 1, 9  # Enumeration, values are not used
COEFF_SLOW = 3  # Speed divided by this factor when outing SLOW boxes

# Multiplier of euclidian distance for heuristic 
# (Choose it < 1 if you don't have any reason to do anything else)
COEFF_HEURISTIC = 0.9  

# Tkinter window
SIDE = 30       # Size in pixel of any boxes on the grid
COLOR = {FREE:"#FFF", SLOW:"#FAA", WALL:"#11A"}
COEFF_FONT = 0.29   # SIDE * COEFF_FONT = font size, for bot and player

USED_CHAR = '*' # To illustrate evaluated (locked) boxes
PATH_CHAR = "●" # To illustrate path's boxes

BOT_TXT = "BOT" # Messages displayed on boxes, for bot and player
YOU_TXT = "YOU"

WIN_TITLE = "Optimal path demo, with Dijkstra or A*"

# Next two are used for message content AND to store the choosen algo.
DIJKSTRA = "\n[T] key to Toggle ALGORITHM : Dijkstra\n"
A_STAR =   "\n[T] key to Toggle ALGORITHM :     A*  \n"

KEYB_MSG = '\nMOVE THE PLAYER with I-J-K-L or Arrow Keys\nMOVE '
KEYB_MSG += 'THE BOT with Z-Q-S-D (/Azerty) or W-A-S-D (/Qwert[yz])'
