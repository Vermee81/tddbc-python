from src.calculate import add


class ClosedRange:
    def __init__(self, lower_endpoint, upper_endpoint):
        self.lower_endpoint = lower_endpoint
        self.upper_endpoint = upper_endpoint

    def notation(self):
        return f"[{self.lower_endpoint},{self.upper_endpoint}]"


def test_下端点3と上端点8を渡したら文字列を返す():
    cr = ClosedRange(3, 8)
    assert cr.notation() == "[3,8]"


def test_下端点4と上端点10を渡したら文字列を返す():
    cr = ClosedRange(4, 10)
    assert cr.notation() == "[4,10]"
