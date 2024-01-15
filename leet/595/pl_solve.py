import polars as pl


def main(input_file: str) -> pl.DataFrame:
    q = (
        pl.scan_csv(input_file)
        .filter((pl.col("area") >= 3000000) | (pl.col("population") >= 25000000))
        .select(pl.col("name", "population", "area"))
    )
    return q.collect()


if __name__ == "__main__":
    print(main("leet\\595\\case1\\input.csv"))
