import polars as pl
from helpers import get_case_files, get_polars_solution


def main(views: str) -> pl.DataFrame:
    q = (
        pl.scan_csv(views)
        .filter(pl.col("viewer_id") == pl.col("author_id"))
        .select("author_id")
        .unique()
        .rename({"author_id": "id"})
        .sort("id")
    )
    return q.collect()


if __name__ == "__main__":
    for case in get_case_files(__file__):
        print("****************************************")
        print("return value:")
        print(main(case.inputs.views))
        print("****************************************")
        print("solution value:")
        print(get_polars_solution(case.solution_file))
        print("****************************************")
