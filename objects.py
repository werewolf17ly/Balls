from physmath import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getcoords(self):
        return self.x, self.y

    def setcoords(self, x, y):
        self.x = x
        self.y = y


class Entity(Point, PM):
    def __init__(self, name, x, y, mass, vel, k):
        super().__init__(x, y)
        self.name = name
        self.m = mass
        self.v = vel
        self.k = k

    def move(self):
        self.x = self.x + self.v[0]
        self.y = self.y + self.v[1]

    def acc(self, b):
        a = self.edvec(self, b) *\
            self.force(self, b) / self.m
        self.v = self.v + a

    def setvel(self, x, y):
        self.v = array([0. + x, 0. + y])

    def getphys(self):
        return self.m, self.v, self.k

    def setphys(self, mass, vel, k):
        self.m = mass
        self.v = vel
        self.k = k

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name


class Ball(Entity, PM):
    def __init__(self, name):
        super().__init__(name, 10, 10, 10, array([0., 0.]), 1)
        self.r = 10
        self.col = "salmon"

    def resetprop(self, name, x, y, mass, vel, k, rad, col):
        self.setname(name)
        self.setcoords(x, y)
        self.setphys(mass, vel, k)
        self.setgeom(rad, col)

    def bum(self, b):
        n, v = self.edvec(self, b), self.v
        vn = n * self.proj(v, n) * self.k
        v -= 2 * vn
        self.v = v

    def merge(self, b):
        return self.ro(self, b) < self.r + b.r

    def getgeom(self):
        return self.r, self.col

    def setgeom(self, rad, col):
        self.r = rad
        self.col = col
