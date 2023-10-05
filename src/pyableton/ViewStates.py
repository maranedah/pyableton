from xml.etree import ElementTree


class ViewStates:
    session_io: int
    session_sends: int
    session_returns: int
    session_mixer: int
    session_track_delay: int
    session_cross_fade: int
    session_show_over_view: int
    arranger_io: int
    arranger_returns: int
    arranger_mixer: int
    arranger_track_delay: int
    arranger_show_over_view: int

    def __init__(self, root: ElementTree.Element):
        int(root.find("SessionIO").attrib["Value"])
        int(root.find("SessionSends").attrib["Value"])
        int(root.find("SessionReturns").attrib["Value"])
        int(root.find("SessionMixer").attrib["Value"])
        int(root.find("SessionTrackDelay").attrib["Value"])
        int(root.find("SessionCrossFade").attrib["Value"])
        int(root.find("SessionShowOverView").attrib["Value"])
        int(root.find("ArrangerIO").attrib["Value"])
        int(root.find("ArrangerReturns").attrib["Value"])
        int(root.find("ArrangerMixer").attrib["Value"])
        int(root.find("ArrangerTrackDelay").attrib["Value"])
        int(root.find("ArrangerShowOverView").attrib["Value"])
        return None
