import polars as pl
from helpers import get_case_files, get_polars_solution


def main(input: str) -> pl.DataFrame:
    q = (
        pl.scan_csv(input)
        .select(pl.col("content"))
        .with_columns(
            [
                pl.col("content").str.contains(" bull ").alias("bull"),
                pl.col("content").str.contains(" bear ").alias("bear"),
            ]
        )
        .drop("content")
        .sum()
        .melt(value_vars=["bull", "bear"], variable_name="word", value_name="count")
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
