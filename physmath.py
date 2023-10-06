from numpy import array


class PM:
    G = 6.6743 * 10 ** (-11)

    def force(self, a, b):
        r = self.ro(a, b)
        if r < a.r + b.r:
            return 0
        else:
            return 10000000000 * self.G * a.m * b.m /\
                   (self.ro(a, b) ** 2)

    def edvec(self, a, b):
        r = array([b.x - a.x, b.y - a.y])
        x = self.ro(a, b)
        if x == 0:
            return array([0, 0])
        else:
            return r / x

    @staticmethod
    def proj(a, b):
        return (a[0] * b[0] + a[1] * b[1]) /\
               ((b[0] ** 2 + b[1] ** 2) ** 0.5)

    @staticmethod
    def ro(a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
