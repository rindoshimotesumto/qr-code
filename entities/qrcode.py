from enum import Enum
from pydantic import BaseModel


class QRCodeTypes(Enum):
    png = "PNG"
    svg = "SVG"


class QRCodeSizes(Enum):
    small = 10
    medium = 20
    large = 30


class QRCodeAccuracy(Enum):
    low = 7
    medium = 15
    high = 25
    max = 30


class QRCode(BaseModel):
    """
    Сущность для qrcode.
    """

    data: str
    format: QRCodeTypes
    size: QRCodeSizes
    accuracy: QRCodeAccuracy
    