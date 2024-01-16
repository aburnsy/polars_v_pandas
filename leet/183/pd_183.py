import pandas as pd
from helpers import get_case_files, get_pandas_solution, get_polars_solution


def main(customers: str, orders: str) -> pd.DataFrame:
    customers = pd.read_csv(customers)
    orders = pd.read_csv(orders)
    return customers[~customers["id"].isin(orders["customerId"])][["name"]].rename(
        columns={"name": "Customers"}
    )


if __name__ == "__main__":
    for case in get_case_files(__file__):
        print("****************************************")
        print("inputs:")
        print(get_polars_solution(case.inputs.customers))
        print(get_polars_solution(case.inputs.orders))
        print("****************************************")
        print("return value:")
        print(main(case.inputs.customers, case.inputs.orders))
        print("****************************************")
        print("solution value:")
        print(get_pandas_solution(case.solution_file))
        print("****************************************")
