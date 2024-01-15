import pytest
import pandas as pd
import polars as pl
import polars.testing as pt
import os
from pathlib import Path
import pd_solve
import pl_solve

CASES = [
    val
    for val in range(
        1,
        len(
            list((Path(os.path.dirname(os.path.realpath(__file__))).rglob("input.csv")))
        )
        + 1,
    )
]


@pytest.mark.parametrize("number", CASES)
def test_pandas_case_x(number):
    pd.testing.assert_frame_equal(
        pd_solve.main(f"leet\\595\\case{number}\\input.csv").reset_index(drop=True),
        pd.read_csv(f"leet\\595\\case{number}\\solution.csv"),
    )


@pytest.mark.parametrize("number", CASES)
def test_polars_case_x(number):
    pt.assert_frame_equal(
        pl_solve.main(f"leet\\595\\case{number}\\input.csv"),
        pl.read_csv(f"leet\\595\\case{number}\\solution.csv"),
    )
