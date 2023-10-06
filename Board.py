from tkinter import *
from Settings import *
from objects import *


class Board(Canvas, Settings):
    def __init__(self, frame):
        super().__init__(frame,
                         width=800*(self.SimX-2*self.Border),
                         height=600*(self.SimY-2*self.Border))
        self.lis = []
#        self.addobj("first")
#        self.setobj("first",400,200,10,array([1.,0.]),1,10,"green")
#        self.addobj("second")
#        self.setobj("second",400,400,1000,array([0.,0.]),1,10,"red")
        self.insim = False
        self.ontimer()

    def ontimer(self):
        if self.insim:
            self.accmove()
            self.drawall()
            self.after(self.GameSpeed, self.ontimer)

    def startsim(self):
        self.insim = True
        self.after(self.GameSpeed, self.ontimer)

    def stopsim(self):
        self.insim = False

    def resetsim(self):
        for i in self.lis:
            i[0].setvel(0, 0)

    def findobj(self, name):
        for i in self.lis:
            if i[0].getname() == name:
                return i

    def addobj(self, name):
        x = Ball(name)
        r, col = x.getgeom()
        self.lis.append([x, self.create_oval(0, 0, 20, 20,
                                             fill=col)])
        self.drawall()

    def setobj(self, name, newname, x, y, mass, vel, k, rad, col):
        ob = self.findobj(name)
        ob[0].resetprop(newname, x, y, mass, vel, k, rad, col)
        self.delete(ob[1])
        ob[1] = self.create_oval(x - rad, y - rad, x + rad, y + rad,
                                 fill=col)
        self.drawall()

    def delobj(self, name):
        x = self.findobj(name)
        self.delete(x[1])
        self.lis.remove(x)
        self.drawall()

    def accmove(self):
        for ball in self.lis:
            for ballt in self.lis:
                if ball[0].merge(ballt[0]) and (ball[0] != ballt[0]):
                    ball[0].bum(ballt[0])
                ball[0].acc(ballt[0])
        for ball in self.lis:
            ball[0].move()
        self.drawall()

    def drawall(self):
        for ball in self.lis:
            x, y = ball[0].getcoords()
            r, col = ball[0].getgeom()
            self.coords(ball[1],
                        x - r, y - r,
                        x + r, y + r)

    def getlist(self):
        return self.lis

    def setlist(self, newlist):
        self.lis = newlist
