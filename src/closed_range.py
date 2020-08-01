from dataclasses import dataclass


@dataclass(eq=True)
class ClosedRange:
    lower_endpoint: int
    upper_endpoint: int

    def notation(self):
        return f"[{self.lower_endpoint},{self.upper_endpoint}]"

    def is_contains(self, num: int) -> bool:
        return self.lower_endpoint <= num <= self.upper_endpoint
