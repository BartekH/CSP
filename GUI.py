import threading
import DataProvider
import SudokuSolver
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM, LEFT


class App(threading.Thread):

    def __init__(self, frame):
        self.frame = frame
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.frame.quit()

    def run(self):
        self.frame.mainloop()

class SudokuUI(Frame):

    global MARGIN
    global SIDE
    global WIDTH
    global HEIGHT

    def __init__(self, parent, grid):
        self.game = grid
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0
        self.MARGIN = 2
        self.SIDE = 50
        self.WIDTH = 480
        self.HEIGHT = 480


        self.__initUI(grid)

    def __initUI(self, grid):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=self.WIDTH,
                             height=self.HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Clear answers" )
        solve_button = Button(self, text="Solve!", command=self.__solve)
        solve_button.pack(side=LEFT)
        clear_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle(grid)

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __solve(self):
        SudokuSolver.solve9x9ForwardCheckingGUI(DataProvider.sudoku9x9Normal, self)

    def __cell_clicked(self, event):
        pass

    def __key_pressed(self, event):
        pass

    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        WIDTH = 455
        HEIGHT = 455
        for i in xrange(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = self.MARGIN + i * self.SIDE
            y0 = self.MARGIN
            x1 = self.MARGIN + i * self.SIDE
            y1 = HEIGHT - self.MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = self.MARGIN
            y0 = self.MARGIN + i * self.SIDE
            x1 = WIDTH - self.MARGIN
            y1 = self.MARGIN + i * self.SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self, game):

        self.canvas.delete("numbers")
        for i in xrange(9):
            for j in xrange(9):
                answer = game[i][j]
                if answer != 0:
                    x = self.MARGIN + j * self.SIDE + self.SIDE / 2
                    y = self.MARGIN + i * self.SIDE + self.SIDE / 2
                    color = "black" if answer == 0 else "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )
    def dodaj(self, grid):
        self.canvas.delete("numbers")
        for i in xrange(9):
            for j in xrange(9):
                answer = grid[i][j]
                if answer != 0:
                    x = self.MARGIN + j * self.SIDE + self.SIDE / 2
                    y = self.MARGIN + i * self.SIDE + self.SIDE / 2
                    color = "black" if answer == 0 else "sea green"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )



sudoku9x9 = DataProvider.sudoku9x9Normal
root = Tk()
frame = SudokuUI(root, sudoku9x9)
app = App(frame)
