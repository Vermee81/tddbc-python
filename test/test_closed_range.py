from closed_range import ClosedRange


def test_下端点3と上端点8を渡したら文字列を返す():
    cr = ClosedRange(3, 8)
    assert cr.notation() == "[3,8]"


def test_下端点3と上端点8の閉区間に5が含まれていること():
    cr = ClosedRange(3, 8)
    # PEPでは注意されているが、仕様のわかりやすさのために==Trueとする
    assert cr.is_contains(5) == True


def test_下端点3と上端点8の閉区間に2が含まれていないこと():
    cr = ClosedRange(3, 8)
    # PEPでは注意されているが、仕様のわかりやすさのために==Falseとする
    assert cr.is_contains(2) == False


def test_下端点3と上端点8の閉区間に9が含まれていないこと():
    cr = ClosedRange(3, 8)
    # PEPでは注意されているが、仕様のわかりやすさのために==Falseとする
    assert cr.is_contains(9) == False
