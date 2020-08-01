from closed_range import ClosedRange


class FixtureClass:
    def setup(self):
        self.cr = ClosedRange(3, 8)


class TestClosedRange(FixtureClass):
    def test_下端点3と上端点8を渡したら文字列を返す(self):
        assert self.cr.notation() == "[3,8]"

    class Test指定した整数で判定(FixtureClass):
        def setup(self):
            self.cr = ClosedRange(3, 8)

        def test_下端点3と上端点8の閉区間に5が含まれていること(self):
            assert self.cr.is_contains(5) is True

        def test_下端点3と上端点8の閉区間に2が含まれていないこと(self):
            assert self.cr.is_contains(2) is False

        def test_下端点3と上端点8の閉区間に9が含まれていないこと(self):
            assert self.cr.is_contains(9) is False

    class Test別の閉区間と判定(FixtureClass):

        def test_下端点3と上端点8の閉区間と別の下端点3と上端点8が等価であること(self):
            assert self.cr == ClosedRange(3, 8)

        def test_下端点3と上端点8の閉区間と別の下端点4と上端点10が等価でないこと(self):
            assert self.cr != ClosedRange(4, 10)

        def test_下端点3と上端点8の閉区間が別の下端点4と上端点10が(self):
            pass
            # # TODO: どっち目線かどうか
            # assert self.ClosedRange(3,8).is_includse(ClosedRange(4,10)) is True

            # a include b
            # include(a, b)

            # TODO:どっちも入れろ。まず、書いてみる。