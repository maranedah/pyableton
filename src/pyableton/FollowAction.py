from .AbletonComponent import AbletonComponent


class FollowAction(AbletonComponent):
    """
    FollowAction Class

    Represents the follow action settings in Ableton Live.

    Attributes
    ----------
    follow_time : int
        The time value for the follow action in Ableton Live.
    is_linked : bool
        Flag indicating whether the follow action is linked in Ableton Live.
    loop_iterations : int
        The number of loop iterations for the follow action in Ableton Live.
    follow_action_a : int
        The follow action for branch A in Ableton Live.
    follow_action_b : int
        The follow action for branch B in Ableton Live.
    follow_chance_a : int
        The follow chance for branch A in Ableton Live.
    follow_chance_b : int
        The follow chance for branch B in Ableton Live.
    jump_index_a : int
        The jump index for branch A in Ableton Live.
    jump_index_b : int
        The jump index for branch B in Ableton Live.
    follow_action_enabled : bool
        Flag indicating whether the follow action is enabled in Ableton Live.

    """

    follow_time: int
    is_linked: bool
    loop_iterations: int
    follow_action_a: int
    follow_action_b: int
    follow_chance_a: int
    follow_chance_b: int
    jump_index_a: int
    jump_index_b: int
    follow_action_enabled: bool
