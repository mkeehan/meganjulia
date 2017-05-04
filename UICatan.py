from Tkinter import *
import random
import tkFont
import time

# Creates the board and adds the tiles to the board
def createBoard(canvas, root):
    board = canvas.create_polygon(738,112, 462,112, 325,350, 463,588, 737,588, 875,350, fill='blue')
    
    # We want to place the tiles in a spiral pattern. To do this, each element 
    # in the array represents the direction we will place tiles and the number
    # of tiles that'll be placed in this direction. r = right, l = left,
    # d = down, u = up
    order = [[2, 'r'], [2, 'rd'], [2, 'ld'], [2, 'l'], [2, 'ul'], [1, 'ur'], \
             [2, 'r'], [1, 'rd'], [1, 'ld'], [1, 'l'], [1, 'ul'], [1, 'r']]
    
    
    # The amount to shift the x and/or y value of each successive tile
    right = 79
    down = 68
    dRight = 39.5
    
    
    # The starting coordinates of the upper left tile
    xval = [600-79, 561-79, 561-79, 600-79, 639-79, 639-79, 639-79]
    yval = [305-136, 328-136, 373-136, 395-136, 373-136, 328-136]
    canvas.after(300, None)
    tile1 = canvas.create_polygon(xval[0], yval[0], xval[1], yval[1], xval[2], yval[2], xval[3], yval[3], xval[4], yval[4], xval[5], yval[5], fill='red', outline = 'AntiqueWhite1') 
    root.update()
    canvas.after(300, None)
    
    for element in order:
        count = element[0]
        direction = element[1]
        
        while count > 0:
            if direction == 'r':
                xval[:] = [x + right for x in xval]
            if direction == 'rd':
                xval[:] = [x + dRight for x in xval]
                yval[:] = [y + down for y in yval]
            if direction == 'ld':
                xval[:] = [x - dRight for x in xval]
                yval[:] = [y + down for y in yval]
            if direction == 'l':
                xval[:] = [x - right for x in xval]
            if direction == 'ul':
                yval[:] = [y - down for y in yval]
                xval[:] = [x - dRight for x in xval]
            if direction == 'ur':
                yval[:] = [y - down for y in yval]
                xval[:] = [x + dRight for x in xval]
            
            tile1 = canvas.create_polygon(xval[0], yval[0], xval[1], yval[1], xval[2], yval[2], xval[3], yval[3], xval[4], yval[4], xval[5], yval[5], fill='red', outline = 'AntiqueWhite1') 
            root.update()
            canvas.after(300, None)
            count -= 1           




if __name__ == '__main__':
    root = Tk()
    root.geometry('1200x700')
    canvas = Canvas(root, width=1200, height=700)
    canvas.configure(background='AntiqueWhite1')
    canvas.pack()
    createBoard(canvas, root)
    root.mainloop()