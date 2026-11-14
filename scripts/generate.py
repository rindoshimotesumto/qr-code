import io
import qrcode

from functools import lru_cache

from qrcode.image.pure import PyPNGImage
from qrcode.image.svg import SvgPathImage
from qrcode.constants import ERROR_CORRECT_L

from entities.qrcode import QRCodeTypes


@lru_cache(maxsize=1024)
def generate_qr(
    data: str,
    format: QRCodeTypes = QRCodeTypes.png,
) -> tuple[bytes, str]:
    
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    if format == QRCodeTypes.png:
        image_factory = PyPNGImage
        media_type = "image/png"
    else:
        image_factory = SvgPathImage
        media_type = "image/svg+xml"
    
    img = qr.make_image(image_factory=image_factory)    
    buf = io.BytesIO()

    img.save(buf)

    return buf.getvalue(), media_type