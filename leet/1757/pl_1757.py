import polars as pl
from helpers import get_case_files, get_polars_solution


def main(input_file: str) -> pl.DataFrame:
    q = (
        pl.scan_csv(input_file)
        .filter((pl.col("low_fats") == "Y") & (pl.col("recyclable") == "Y"))
        .select("product_id")
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
