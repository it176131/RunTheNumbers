from pytest_cases.case_parametrizer_new import parametrize_with_cases

from rtn.materials.interior.carpentry import trim as trim_


class TestTrim:
    """Tests for :class:``Trim``."""

    @parametrize_with_cases(argnames="cost_per_foot", prefix="cost_")
    @parametrize_with_cases(argnames="linear_footage", prefix="len_")
    def test_total_cost(
        self, linear_footage: float, cost_per_foot: float
    ) -> None:
        """Test :method:``Trim.total_cost``.

        :method:``Trim.total_cost`` takes no arguments and should
        return the total materials cost for trim of length
        ``linear_footage``.
        """
        trim = trim_.Trim(
            cost_per_foot=cost_per_foot,
            brand="",
            house_square_footage=0,
            linear_footage=linear_footage,
            width=0,
            color="",
            trim_type=trim_.TrimType.Baseboard,
            molding_use=trim_.MoldingUse.Floor,
            material=trim_.MoldingMaterial.Wood,
            finish_type=trim_.FinishType.Primed,
            installation_type=trim_.InstallationType.Nail,
            durability=trim_.Durability.NotApplicable,
        )
        assert trim.total_cost in (0.97, 9.215, 1.03, 9.785)
