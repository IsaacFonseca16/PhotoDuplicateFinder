from dataclasses import dataclass

@dataclass
class FileInfo:
    name: str
    path: str
    size: float
    file_type: str
    sha256: str
    width: int | None = None
    height: int | None = None
    phash: object | None = None