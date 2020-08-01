from closed_range import ClosedRange


def test_下端点3と上端点8を渡したら文字列を返す():
    cr = ClosedRange(3, 8)
    assert cr.notation() == "[3,8]"

def test_下端点3と上端点8の閉区間に5が含まれている():
    cr = ClosedRange(3, 8)
    assert cr.is_contains(5) == True