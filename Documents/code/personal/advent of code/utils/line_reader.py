from typing import Iterator


def read_lines(file_path: str) -> Iterator[str]:
    """
    Read lines from a file and yield each line without the trailing newline character.

    Args:
        file_path (str): The path to the file.

    Yields:
        str: The lines from the file without the trailing newline character.
    """
    with open(file_path, "r") as file:
        for line in file:
            yield line.rstrip("\n")
