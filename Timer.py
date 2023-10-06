from tkinter import *
import time


class StopWatch(Frame):
    def __init__(self, board, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.board = board
        self._timeelapsed = 0.0
        self._start = 0.0
        self._run = 0
        self.timestr = StringVar()
        self.makewidgets()

    def makewidgets(self):
        lab = Label(self,
                    textvariable=self.timestr,
                    font="Arial 20")
        self._settime(self._timeelapsed)
        lab.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self):
        self._timeelapsed = time.time() - self._start
        self._settime(self._timeelapsed)
        self._timer = self.after(50, self._update)

    def _settime(self, elap):
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds)
                       * 100)
        self.timestr.set('%02d:%02d:%02d' %
                         (minutes, seconds, hseconds))

    def start(self):
        if not self._run:
            self._start = time.time() - self._timeelapsed
            self._update()
            self._run = 1
            self.board.startsim()

    def stop(self):
        if self._run:
            self.after_cancel(self._timer)
            self._timeelapsed = time.time() - self._start
            self._settime(self._timeelapsed)
            self._run = 0
            self.board.stopsim()

    def reset(self):
        self._start = time.time()
        self._timeelapsed = 0.0
        self._settime(self._timeelapsed)
        self.board.resetsim()


class Timer(Frame):
    def __init__(self, board, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.timelabel = Label(parent, text="\nВремя симуляции\n",
                               font='Arial 18', bg='green')
        self.sw = StopWatch(board, parent)
        self.btnlabel = Label(parent,
                              text="\nУправление симуляцией\n",
                              font='Arial 14', bg='green')
        self.btnstart = Button(parent, text='Start',
                               font='Arial 18', command=self.sw.start)
        self.btnstop = Button(parent, text='Stop',
                              font='Arial 18', command=self.sw.stop)
        self.btnreset = Button(parent, text='Reset',
                               font='Arial 18', command=self.sw.reset)
        self.placeall()

    def placeall(self):
        self.timelabel.grid(row=0, column=0, columnspan=3)
        self.sw.grid(row=1, column=0, columnspan=3)
        self.btnlabel.grid(row=2, column=0, columnspan=3)
        self.btnstart.grid(row=3, column=0)
        self.btnstop.grid(row=3, column=1)
        self.btnreset.grid(row=3, column=2)
