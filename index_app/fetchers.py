from typing import Any
from django.conf import settings
from pathlib import Path
from numpy import uint8, dtype, ndarray
import cv2


def fetch_ip_camera_path(camera_ip: str) -> str:
    return f"rtsp://admin:@{camera_ip}:554/mode=real&idc=1&ids=1"


def fetch_binary_image(RTCP_URL: str) -> ndarray[Any, dtype[uint8]] | None:
    buffer = None
    cap = cv2.VideoCapture(RTCP_URL)
    ret, frame = cap.read()
    if ret:
        _, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
    cap.release()
    return buffer


def fetch_uploaded_files() -> list[Any]:
    path = Path(settings.MEDIA_ROOT)
    return [
        {"name": file.name, "url": f"{settings.MEDIA_URL}{file.name}"}
        for file in path.glob("*.jpg")
    ]
