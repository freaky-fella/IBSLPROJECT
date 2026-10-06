from users import User

class Tutee(User):
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, role: str, 
                 tutee_id: int, grade_level: int):
        super().__init__(user_id, first_name, last_name, email, role)
        self.tutee_id = tutee_id
        self.grade_level = grade_level

    def get_tutee_id(self) -> int:
        return 0

    def get_grade_level(self) -> int:
        return 0
