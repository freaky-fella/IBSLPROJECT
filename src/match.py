
class Match:
    def __init__(self, match_id: int, tutor_id: int, tutee_id: int, subject_id: int, match_status: str):
        self.match_id = match_id
        self.tutor_id = tutor_id
        self.tutee_id = tutee_id
        self.subject_id = subject_id
        self.match_status = match_status

    def get_match_id(self) -> int:
        return 0

    def is_active(self) -> bool:
        return False
