import polars as pl
from helpers import get_case_files, get_polars_solution


def main(input: str) -> pl.DataFrame:
    q = (
        pl.scan_csv(input)
        .select(
            pl.col("employee_id"),
            bonus=(
                pl.when(
                    (~pl.col("name").str.starts_with("M"))
                    & (pl.col("employee_id") % 2 == 1)
                )
                .then(pl.col("salary"))
                .otherwise(0)
            ),
        )
        .sort("employee_id")
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
