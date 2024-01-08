from .AbletonComponent import AbletonComponent


class Grid(AbletonComponent):
    """
    Grid Class

    Represents the grid settings in Ableton Live.

    Attributes
    ----------
    fixed_numerator : int
        The fixed numerator value for the grid in Ableton Live.
    fixed_denominator : int
        The fixed denominator value for the grid in Ableton Live.
    grid_interval_pixel : int
        The pixel value for the grid interval in Ableton Live.
    ntoles : int
        The number of toles for the grid in Ableton Live.
    snap_to_grid : bool
        Flag indicating whether snapping to the grid is enabled in Ableton Live.
    fixed : bool
        Flag indicating whether the grid is fixed in Ableton Live.

    """

    fixed_numerator: int
    fixed_denominator: int
    grid_interval_pixel: int
    ntoles: int
    snap_to_grid: bool
    fixed: bool
