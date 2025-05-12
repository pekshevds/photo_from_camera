from typing import Any
from django.conf import settings
from pathlib import Path
from numpy import uint8, dtype, ndarray


def handle_uploaded_file(photo_name: str, file: Any) -> None:
    path = settings.MEDIA_ROOT
    with open(Path(path) / photo_name, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def save_image(photo_name: str, binary_image: ndarray[Any, dtype[uint8]]) -> None:
    path = settings.MEDIA_ROOT
    with open(Path(path) / photo_name, mode="wb+") as destination:
        destination.write(binary_image.tobytes())
