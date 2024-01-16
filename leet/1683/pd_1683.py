import pandas as pd
from helpers import get_case_files, get_pandas_solution, get_polars_solution


def main(input: str) -> pd.DataFrame:
    tweets = pd.read_csv(input)
    return tweets[tweets.content.str.len() > 15][["tweet_id"]]


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
