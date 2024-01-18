import pandas as pd
from helpers import get_case_files, get_pandas_solution


def main(input: str) -> pd.DataFrame:
    patients = pd.read_csv(input)
    return patients[patients["conditions"].str.contains(r"\bDIAB1", na=False)]


if __name__ == "__main__":
    for case in get_case_files(__file__):
        print("****************************************")
        print("return value:")
        print(main(case.inputs.input))
        print("****************************************")
        print("solution value:")
        print(get_pandas_solution(case.solution_file))
        print("****************************************")
