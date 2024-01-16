import pandas as pd
from helpers import get_case_files, get_pandas_solution


def main(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file)
    return df[(df.area >= 3000000) | (df.population >= 25000000)][
        ["name", "population", "area"]
    ]


if __name__ == "__main__":
    for case in get_case_files(__file__):
        print("****************************************")
        print("return value:")
        print(main(case.inputs.input))
        print("****************************************")
        print("solution value:")
        print(get_pandas_solution(case.solution_file))
        print("****************************************")
