class ClosedRange:
    def __init__(self, lower_endpoint, upper_endpoint):
        self.lower_endpoint = lower_endpoint
        self.upper_endpoint = upper_endpoint

    def notation(self):
        return f"[{self.lower_endpoint},{self.upper_endpoint}]"

    def is_contains(self, num: int) -> bool:
        return self.lower_endpoint <= num <= self.upper_endpoint
