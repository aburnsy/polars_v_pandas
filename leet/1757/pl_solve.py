import polars as pl


def main(input_file: str) -> pl.DataFrame:
    q = (
        pl.scan_csv(input_file)
        .filter((pl.col("low_fats") == "Y") & (pl.col("recyclable") == "Y"))
        .select("product_id")
    )
    return q.collect()


if __name__ == "__main__":
    print(main("leet\\1757\\case1\\input.csv"))
