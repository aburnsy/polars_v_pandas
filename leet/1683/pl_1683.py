import polars as pl
from helpers import get_case_files, get_polars_solution


def main(input: str) -> pl.DataFrame:
    q = (
        pl.scan_csv(input)
        .filter(pl.col("content").str.len_chars() > 15)
        .select(pl.col("tweet_id"))
    )
    return q.collect()


if __name__ == "__main__":
    for case in get_case_files(__file__):
        print("****************************************")
        print("return value:")
        print(main(case.inputs.input))
        print("****************************************")
        print("solution value:")
        print(get_polars_solution(case.solution_file))
        print("****************************************")
