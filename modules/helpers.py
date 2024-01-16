from collections import namedtuple
from pathlib import Path
import os
import pandas as pd
import polars as pl


def get_case_files(str_path) -> list[namedtuple] | None:
    if Path(str_path).is_file:
        str_path = os.path.dirname(str_path)
    ReturnFiles = namedtuple("ReturnFiles", ["number", "inputs", "solution_file"])
    result = []
    solutions = Path(str_path).rglob("solution*.csv")
    for i, solution in enumerate(solutions):
        solution_file = str(solution)
        input_files = [
            str(i)
            for i in sorted(list(Path(solution.parent).glob("*[!solution]*.csv")))
        ]
        input_names = [input.split("\\")[-1].split(".", 1)[0] for input in input_files]
        InputFiles = namedtuple("InputFiles", input_names)
        input_files_ins = InputFiles(*input_files)
        result.append(ReturnFiles(i + 1, input_files_ins, solution_file))
    return result


def get_pandas_solution(solution_file):
    return pd.read_csv(solution_file)


def get_polars_solution(solution_file):
    return pl.read_csv(solution_file)
