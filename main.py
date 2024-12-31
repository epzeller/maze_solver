from graphics import Window
from cell import cell

def main():
    win = Window(800, 600)
    cell1 = cell(50, 50, 100, 100, True, False, True, False, win)
    cell2 = cell(150, 150, 200, 175, False, True, True, False, win)
    cell1.draw()
    cell2.draw()

    win.wait_for_close()


main()