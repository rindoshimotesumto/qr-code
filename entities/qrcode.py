from enum import Enum
from pydantic import BaseModel, Field


class QRCodeTypes(str, Enum):
    png = "PNG"
    svg = "SVG"


class QRCode(BaseModel):
    """
    Сущность для qrcode.
    """

    data: str = Field(..., min_length=1, max_length=2048)
    format: QRCodeTypes = QRCodeTypes.png
