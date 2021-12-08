class Line:
    def __init__(self, x1, y1, x2, y2, diagonal=False):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.diagonal = diagonal

    def __repr__(self) -> str:
        return f'x1: {self.x1}, y1: {self.y1}, x2: {self.x2}, y2:{self.y2}'