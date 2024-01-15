import os
from pathlib import Path
import pandas as pd
from itertools import chain


def main():
    # Loop through all folders from cwd
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # find txt files
    input_files = Path(dir_path).glob("*input*.txt")
    solution_files = Path(dir_path).glob("*solution*.txt")

    # for each txt file
    # check if there is an equivalent csv file
    # covert the file if not
    for input_file in chain(input_files, solution_files):
        file_name = str(input_file)
        csv_file_name = file_name.replace(".txt", ".csv")
        if not os.path.isfile(csv_file_name):
            print(f"Found file {file_name} with no equivalent csv file {csv_file_name}")
            convert_txt_to_csv(file_name, csv_file_name)
            os.remove(file_name)


def convert_txt_to_csv(input_file: str, output_file: str) -> None:
    df = pd.read_csv(
        input_file,
        sep=r"\s*\|\s*",
        skiprows=[1],
        skipinitialspace=True,
        engine="python",
        nrows=0,
    )
    column_count = len(df.columns) - 1
    df = pd.read_csv(
        input_file,
        sep=r"\s*\|\s*",
        skiprows=[1],
        skipinitialspace=True,
        engine="python",
        usecols=range(1, column_count),
    )
    df.to_csv(
        output_file,
        index=False,
    )


if __name__ == "__main__":
    main()
