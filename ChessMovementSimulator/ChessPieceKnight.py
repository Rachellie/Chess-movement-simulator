class Knight(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moves(self, Ox, Oy, Nx, Ny):
        if Nx == Ox+1 and (Ny == Oy+2 or Ny == Oy-2):
            return True
        elif Nx == Ox-1 and (Ny == Oy+2 or Ny == Oy-2):
            return True
        elif  Nx == Ox+2 and(Ny == Oy+1 or Ny == Oy-1):
            return True
        elif Nx == Ox-2 and (Ny == Oy+1 or Ny == Oy-1):
            return True
        else:
            return False
