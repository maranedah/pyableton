from xml.etree import ElementTree

from .AbletonComponent import AbletonComponent


class ViewStates(AbletonComponent):
    session_IO: int
    session_sends: int
    session_returns: int
    session_mixer: int
    session_track_delay: int
    session_cross_fade: int
    session_show_over_view: int
    arranger_IO: int
    arranger_returns: int
    arranger_mixer: int
    arranger_track_delay: int
    arranger_show_over_view: int

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class AutomationTransformViewState(AbletonComponent):
    is_transform_pending: bool
    # time_and_value_transforms: None

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)
