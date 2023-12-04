from xml.etree import ElementTree

from .AbletonComponent import AbletonComponent
from .FollowAction import FollowAction


class Scene(AbletonComponent):
    id: int
    follow_action: FollowAction
    name: str
    annotation: str
    color: int
    tempo: int
    is_tempo_enabled: bool
    time_signature_id: int
    is_time_signature_enabled: bool
    lom_id: int
    clip_slots_list_wrapper: int

    def __init__(self, root: ElementTree.Element):
        super().__init__(root)


class ScenesListWrapper(AbletonComponent):
    def __init__(self, root: ElementTree.Element):
        return None
