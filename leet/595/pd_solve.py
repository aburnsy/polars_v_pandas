import pandas as pd


def main(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file)
    return df[(df.area >= 3000000) | (df.population >= 25000000)][
        ["name", "population", "area"]
    ]


if __name__ == "__main__":
    print(main("leet\\595\\case1\\input.csv"))
