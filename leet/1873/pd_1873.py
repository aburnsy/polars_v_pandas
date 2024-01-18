import pandas as pd
from helpers import get_case_files, get_pandas_solution, get_polars_solution
import numpy as np


def main(input: str) -> pd.DataFrame:
    employees = pd.read_csv(input)
    employees["bonus"] = np.where(
        (~employees["name"].str.startswith("M")) & (employees["employee_id"] % 2 == 1),
        employees["salary"],
        0,
    )
    return employees[["employee_id", "bonus"]].sort_values(["employee_id"])


if __name__ == "__main__":
    for case in get_case_files(__file__):
        print("****************************************")
        print("inputs:")
        print(get_polars_solution(case.inputs.input))
        print("****************************************")
        print("return value:")
        print(main(case.inputs.input))
        print("****************************************")
        print("solution value:")
        print(get_pandas_solution(case.solution_file))
        print("****************************************")
