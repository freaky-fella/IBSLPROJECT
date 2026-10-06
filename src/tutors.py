from users import User

class Tutor(User):
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, role: str, 
                 tutor_id: int, max_weekly_hours: int, status: str):
        super().__init__(user_id, first_name, last_name, email, role)
        self.tutor_id = tutor_id
        self.max_weekly_hours = max_weekly_hours
        self.status = status

    def get_tutor_id(self) -> int:
        return 0

    def is_available(self) -> bool:
        return False

    def get_max_weekly_hours(self) -> int:
        return 0
