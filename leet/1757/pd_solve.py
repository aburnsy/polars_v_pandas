import pandas as pd


def main(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file)
    return df[(df.low_fats == "Y") & (df.recyclable == "Y")][["product_id"]]


if __name__ == "__main__":
    print(main("leet\\1757\\case1\\input.csv"))
