class TutorSubject:
    def __init__(self, tutor_id: int, subject_id: int, proficiency_level: str):
        self.tutor_id = tutor_id
        self.subject_id = subject_id
        self.proficiency_level = proficiency_level

    def get_tutor_id(self) -> int:
        return 0

    def get_subject_id(self) -> int:
        return 0

    def get_proficiency_level(self) -> str:
        return ""
