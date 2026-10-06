
class SessionRecord:
    def __init__(self, session_id: int, match_id: int, session_date: str, 
                 duration_minutes: int, session_status: str, notes: str):
        self.session_id = session_id
        self.match_id = match_id
        self.session_date = session_date
        self.duration_minutes = duration_minutes
        self.session_status = session_status
        self.notes = notes

    def get_session_id(self) -> int:
        return 0

    def get_duration_minutes(self) -> int:
        return 0

    def is_verified(self) -> bool:
        return False
