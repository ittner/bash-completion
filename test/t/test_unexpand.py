import pytest


class Test(object):

    @pytest.mark.complete("unexpand --",
                          skipif="! unexpand --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list