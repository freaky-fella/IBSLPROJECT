
class Subject:
    def __init__(self, subject_id: int, subject_name: str, department: str):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.department = department

    def get_subject_id(self) -> int:
        return 0

    def get_subject_name(self) -> str:
        return ""
