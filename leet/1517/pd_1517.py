import pandas as pd
from helpers import get_case_files, get_pandas_solution


def main(input: str) -> pd.DataFrame:
    df = pd.read_csv(input)
    return df[df["mail"].str.fullmatch(r"^[a-zA-z]+[a-zA-z0-9.\-_]*@leetcode.com")]


if __name__ == "__main__":
    for case in get_case_files(__file__):
        print("****************************************")
        print("return value:")
        print(main(case.inputs.input))
        print("****************************************")
        print("solution value:")
        print(get_pandas_solution(case.solution_file))
        print("****************************************")
