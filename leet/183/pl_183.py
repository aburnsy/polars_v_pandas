import polars as pl
from helpers import get_case_files, get_polars_solution


def main(customers: str, orders: str) -> pl.DataFrame:
    orders_df = pl.read_csv(orders)
    q = (
        pl.scan_csv(customers)
        .filter(~pl.col("id").is_in(orders_df.select("customerId")))
        .select("name")
        .rename({"name": "Customers"})
    )
    return q.collect()


if __name__ == "__main__":
    for case in get_case_files(__file__):
        print("****************************************")
        print("return value:")
        print(main(case.inputs.customers, case.inputs.orders))
        print("****************************************")
        print("solution value:")
        print(get_polars_solution(case.solution_file))
        print("****************************************")
