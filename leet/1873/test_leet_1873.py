import pytest
import pandas as pd
import polars.testing as pt
import pd_1873
import pl_1873
from helpers import get_case_files, get_pandas_solution, get_polars_solution

cases_info = get_case_files(__file__)
cases_ids = [f"Case {x.number}" for x in cases_info]


@pytest.mark.parametrize("number,inputs,solution_file", cases_info, ids=cases_ids)
def test_pandas(number, inputs, solution_file):
    pd.testing.assert_frame_equal(
        pd_1873.main(inputs.input).reset_index(drop=True),
        get_pandas_solution(solution_file),
    )


@pytest.mark.parametrize("number,inputs,solution_file", cases_info, ids=cases_ids)
def test_polars(number, inputs, solution_file):
    pt.assert_frame_equal(
        pl_1873.main(inputs.input),
        get_polars_solution(solution_file),
    )
