from .AbletonComponent import AbletonComponent


class FollowAction(AbletonComponent):
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
