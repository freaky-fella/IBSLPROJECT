class AvailabilitySlot:
    def __init__(self, slot_id: int, user_id: int, day_of_week: str, period_number: int):
        self.slot_id = slot_id
        self.user_id = user_id
        self.day_of_week = day_of_week
        self.period_number = period_number

    def get_slot_id(self) -> int:
        return 0

    def overlaps_with(self, other: "AvailabilitySlot") -> bool:
        return False
