from xml.etree import ElementTree

from .AbletonComponent import AbletonComponent


class Grid(AbletonComponent):
    fixed_numerator: int
    fixed_denominator: int
    grid_interval_pixel: int
    ntoles: int
    snap_to_grid: bool
    fixed: bool

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
