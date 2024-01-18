import polars as pl
from helpers import get_case_files, get_polars_solution


def main(input: str) -> pl.DataFrame:
    q = (
        pl.scan_csv(input)
        .select(pl.col("user_id"), name=(pl.col("name").str.to_titlecase()))
        .sort("user_id")
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
