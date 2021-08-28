from enum import Enum


class Colorr(tuple, Enum):
    WHITE = (255, 255, 255)
    YELLOW = (223, 225, 0)
    ORANGE = (255, 191, 0)
    GREEN = (159, 226, 191)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    SILVER = (192, 192, 192)
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)