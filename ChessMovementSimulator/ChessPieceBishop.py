class Bishop(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def diagonal(self, Ox, Oy, Nx, Ny):
        if abs(Ox - Nx) == abs(Oy - Ny):
            return True
        else:
            return False

    def upNdown(self, Ox, Oy, Nx, Ny):
        if Ox == Nx or Oy == Ny:
            return True
        else:
            return False

    def moves(self, Ox, Oy, Nx, Ny):
        if self.diagonal(Ox, Oy, Nx, Ny):
            return True
        else:
            return False
