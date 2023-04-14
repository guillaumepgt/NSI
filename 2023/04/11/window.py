"""Tkinter window to show optimal path on playing map.

Usable as is.
               
      Licence Creative Commons CC-BY - Jean-Marc Gervais 2021
"""

import tkinter as tk
import tkinter.font as tkFont

from param import *
from model import graph_from_file, get_path

#    ** Inheritance not used, to comply with the official NSI program **
class Fen:      
    def __init__(self, map_file, bot=None, player=None):
        # === Event handlers for keyboad ===
        # . Player moves
        def left(event):
            row, col = tuple(self.end)
            if col > 0 and self.graph[(row, col-1)]['cat'] != WALL:
                self.end[1] -= 1
                self.can_update()
                
        def right(event):
            row, col = tuple(self.end)
            if ( col < self.width - 1  and
                 self.graph[(row, col+1)]['cat'] != WALL ):
                self.end[1] += 1
                self.can_update()
                
        def up(event):
            row, col = tuple(self.end)
            if row > 0 and self.graph[(row - 1, col)]['cat'] != WALL:
                self.end[0] -= 1
                self.can_update()
                
        def down(event):
            row, col = tuple(self.end)
            if ( row < self.height - 1  and
                 self.graph[(row + 1, col)]['cat'] != WALL ):
                self.end[0] += 1
                self.can_update()
        
        # . Bot moves
        def bot_left(event):
            row, col = tuple(self.start)
            if col > 0 and self.graph[(row, col-1)]['cat'] != WALL:
                self.start[1] -= 1
                self.can_update()
                
        def bot_right(event):
            row, col = tuple(self.start)
            if ( col < self.width - 1  and 
                 self.graph[(row, col+1)]['cat'] != WALL ):
                self.start[1] += 1
                self.can_update()
                
        def bot_up(event):
            row, col = tuple(self.start)
            if row > 0 and self.graph[(row - 1, col)]['cat'] != WALL:
                self.start[0] -= 1
                self.can_update()
                
        def bot_down(event):
            row, col = tuple(self.start)
            if ( row < self.height - 1 and 
                 self.graph[(row + 1, col)]['cat'] != WALL ):
                self.start[0] += 1
                self.can_update()
        
        # . Algorithm choice
        def switch_algo(event):
            """Toggle algorithm used to find the optimal path. 
            
            This choice is just store in self.label_algo['text'].
            """
            if self.label_algo['text'] == DIJKSTRA:
                self.algo = A_STAR
            else:
                self.algo = DIJKSTRA
            self.label_algo.config(text = self.algo)
            self.can_update()
        
        # === Main (and only) window ===
        fen = tk.Tk()
        fen.title(WIN_TITLE)
        fen.resizable(False, False)
        self.fen = fen
        
        # Canvas, from file
        self.graph = graph_from_file(map_file)
        self.width = self.graph["length"] 
        self.height = self.graph["height"]
        self.can = tk.Canvas(fen, 
                             width=SIDE*self.width, 
                             height=SIDE*self.height)
        self.can.pack()
        
        # Bot, player
        if player is None:
            # Searching a valid position in bottom right area
            x, y = self.height-2, self.width-2
            xmin, ymin = (self.height - 1)  // 2, (self.width - 1 )// 2
            while self.graph[(x, y)]['cat'] == WALL:
                x -= 1
                if x < xmin:
                    x = self.width-2
                    y -= 1
                    if y < ymin: 
                        msg = "No free box found in down right quarter"
                        raise ValueError(msg)
            player = [x, y]
        self.end = list(player)
        
        if bot is None:
            # Searching a valid position in top left area
            x, y = 0, 0
            xmax, ymax = (self.height - 1)  // 2, (self.width - 1 ) // 2
            while self.graph[(x, y)]['cat'] == WALL:
                x += 1
                if x >= xmax:
                    x = 0
                    y += 1
                    if y >= ymax: 
                        msg = "No free box found in up left quarter"
                        raise ValueError(msg)
            bot = [x, y]
        self.start = list(bot)
        
        # Keyboard handling and instructions
        msg = KEYB_MSG
        self.label_keyb = tk.Label(fen, 
                                   text=msg, 
                                   font=tkFont.Font(family="Mono"))
        self.label_keyb.pack(side=tk.TOP)
        
        fen.bind("<Key-q>", bot_left) # Azerty
        fen.bind("<Key-a>", bot_left) # Qwert[yz]
        fen.bind("<Key-d>", bot_right)
        fen.bind("<Key-z>", bot_up) # Azerty
        fen.bind("<Key-w>", bot_up) # Qwert[yz]
        fen.bind("<Key-s>", bot_down)
        
        fen.bind("<Key-Left>", left)
        fen.bind("<Key-j>", left)
        fen.bind("<Key-Right>", right)
        fen.bind("<Key-l>", right)
        fen.bind("<Key-Up>", up)
        fen.bind("<Key-i>", up)
        fen.bind("<Key-Down>", down)
        fen.bind("<Key-k>", down)
        
        # Choosen algorithm
        self.label_algo = tk.Label(fen, 
                                   text=DIJKSTRA, 
                                   font=tkFont.Font(family="Mono"))
        self.label_algo.pack(side=tk.BOTTOM)
        fen.bind("<Key-t>", switch_algo)
        self.algo = DIJKSTRA
        
        # Display update then infinite loop of event handling
        self.can_update()
        fen.mainloop()
    
    
    def can_update(self):
        """Update canvas (grid) display, after moving or algo switching.
        """
        for col in range(self.graph["length"]):
            for row in range(self.graph["height"]):
                x, y = SIDE * col, SIDE * row
                xx, yy = x + SIDE, y + SIDE
                color = COLOR[self.graph[(row, col)]['cat']]
                self.can.create_rectangle(x+1, y+1, xx, yy, fill=color)
        # Player        
        row, col = tuple(self.end)
        self.can.create_text((col+0.5) * SIDE, (row+0.5)*SIDE, 
                         text=YOU_TXT,
                         font = tkFont.Font(size=int(SIDE * COEFF_FONT),
                                            family="Mono",
                                            weight="bold"))
        # Bot, aiming to reach the player
        row, col = tuple(self.start)
        self.can.create_text((col+0.5) * SIDE, (row+0.5)*SIDE,
                         text=BOT_TXT,
                         font = tkFont.Font(size=int(SIDE * COEFF_FONT),
                                            family="Mono",
                                            weight="bold"))
        
        # Path and explored boxes
        path, locked = get_path(self.graph, 
                               tuple(self.start), 
                               tuple(self.end),
                               self.algo)
        for row, col in path:
            if (row, col) not in [tuple(self.start), tuple(self.end)]:
                self.can.create_text((col+0.5) * SIDE, 
                                     (row+0.5)*SIDE, text=PATH_CHAR)
        
        for row, col in locked:
            if (row, col) not in [tuple(self.start), tuple(self.end)]:
                self.can.create_text((col+0.5) * SIDE, 
                                     (row+0.5)*SIDE, text=USED_CHAR)
        self.fen.update()

    
if __name__ == "__main__":
    Fen("propaganda_map.txt", (8,18), (10,40))
