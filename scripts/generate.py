import io
import qrcode

from qrcode.image.pure import PyPNGImage
from qrcode.image.svg import SvgPathImage
from qrcode.constants import ERROR_CORRECT_L

from entities.qrcode import QRCodeTypes


def generate_qr(
    data: str,
    format: QRCodeTypes = QRCodeTypes.png,
) -> tuple[io.BytesIO, str]:
    
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    if format == QRCodeTypes.png:
        _image_factory = PyPNGImage
    else:
        _image_factory = SvgPathImage
    
    img = qr.make_image(image_factory=_image_factory)    
    buf = io.BytesIO()

    img.save(buf)
    buf.seek(0)

    return buf, f"image/{format.value}"