from typing import Iterator

def read_file(filepath: str, encoding='utf-8') -> str:
    """Loads a file into memory as a string."""
    with open(filepath, mode='r', encoding=encoding) as f:
        return f.read()

def stream_file(filepath: str, encoding='utf-8') -> Iterator[str]:
    """Loads a file into memory line-by-line."""
    with open(filepath, mode='r', encoding=encoding) as f:
        for line in f.readlines():
            yield line
