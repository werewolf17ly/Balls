from Board import *
from Timer import *
from ObjList import *


class GUI(Frame, Settings):
    def __init__(self, parent):
        super().__init__()
        simarea = Frame(parent, bg=self.SimCol)
        simarea.place(relwidth=self.SimX, relheight=self.SimY)
        guiarea = Frame(parent, bg='pale green')
        guiarea.place(relx=self.SimX,
                      relwidth=1 - self.SimX, relheight=self.SimY)
        self.board = self.initboard(parent)
        self.board.pack()
        self.inittimer(parent, self.board)
        self.initlist(parent, self.board)

    def initboard(self, parent):
        frame_board = Frame(parent, bg='white')
        frame_board.place(relx=self.Border,
                          rely=self.Border,
                          relwidth=self.SimX - 2 * self.Border,
                          relheight=1 - 2 * self.Border)
        board = Board(frame_board)
        return board

    def inittimer(self, parent, board):
        frame_timer = Frame(parent, bg='green')
        frame_timer.place(relx=self.SimX + self.Border,
                          rely=self.Border,
                          relwidth=1 - self.SimX - 2 * self.Border,
                          relheight=0.5 - 2 * self.Border)
        Timer(board, frame_timer)

    def initlist(self, parent, board):
        frame_list = Frame(parent, bg='salmon')
        frame_list.place(relx=self.SimX + self.Border,
                         rely=0.5 + self.Border,
                         relwidth=1 - self.SimX - 2 * self.Border,
                         relheight=0.5 - 2 * self.Border)
        ObjList(board, frame_list)


class Window(Tk, Settings):
    def __init__(self):
        super().__init__()
        self['bg'] = self.WinColor
        self.title(self.WinTitle)
        self.geometry(self.WinScale)
        self.resizable(width=False, height=False)
