import pytest
from pytest_cases.case_parametrizer_new import parametrize_with_cases

from rtn.materials.interior.framing import Wall


class TestWall:
    """Tests for :class:``Wall``."""

    @pytest.mark.xfail()
    @parametrize_with_cases(argnames=["length", "expected"], prefix="studs_")
    def test_number_of_studs(self, length: float, expected: float) -> None:
        """Test :method:``Wall.number_of_studs``.

        :method:``Wall.number_of_studs`` takes no arguments and should
        return the number of studs required to build a :class:``Wall``.
        """
        wall = Wall(length=length)
        assert hasattr(wall, "number_of_studs")
        assert wall.number_of_studs == expected
