class User:
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, role: str):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role

    def get_user_id(self) -> int:
        return 0

    def get_full_name(self) -> str:
        return ""

    def get_role(self) -> str:
        return ""
