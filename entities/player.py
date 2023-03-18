import dataclasses
from typing import List


@dataclasses.dataclass
class Player:
    name: str
    total_score: float
    score_array: List
    atp_ranking: int
    credits_needed: int
