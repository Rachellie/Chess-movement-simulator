class King(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moves(self, Ox, Oy, Nx, Ny):
        if abs(Ox - Nx) <= 1 and abs(Oy - Ny) <= 1:
            return True
        else:
            return False
