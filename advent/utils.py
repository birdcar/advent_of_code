from pathlib import Path
from typing import Generator, Callable, Any


ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
DATA_DIR = ROOT_DIR / "data"
PASS_FN = lambda item: item


def gen_inputs(
    file_path: Path, map_fn: Callable = PASS_FN, *, strip: bool = True
) -> Generator[Any, None, None]:
    """
    Gather input data from a file and yield each line, passing the line through
    an optionally specified map function for processing.

    Each line also can optionally be stripped of leading and trailing
    whitespace using the strip kwarg (True by default)
    """
    with open(file_path) as data_file:
        if strip:
            yield from (map_fn(line.strip()) for line in data_file)
        else:
            yield from (map_fn(line) for line in data_file)
