import pandas as pd
from helpers import get_case_files, get_pandas_solution, get_polars_solution


def main(views: str) -> pd.DataFrame:
    df = pd.read_csv(views)
    return (
        df[df.author_id == df.viewer_id][["author_id"]]
        .rename(columns={"author_id": "id"})
        .drop_duplicates()
        .sort_values(by=["id"])
    )


if __name__ == "__main__":
    for case in get_case_files(__file__):
        print("****************************************")
        print("inputs:")
        print(get_polars_solution(case.inputs.views))
        print("****************************************")
        print("return value:")
        print(main(case.inputs.views))
        print("****************************************")
        print("solution value:")
        print(get_pandas_solution(case.solution_file))
        print("****************************************")
