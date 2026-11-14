from fastapi import FastAPI
from fastapi.responses import Response

from entities.qrcode import QRCode
from scripts.generate import generate_qr


app = FastAPI()


@app.get("/")
def check() -> dict[str, str]:
    return {"status": "200 OK"} 


@app.post("/qrcode")
def generate_qrcode(qrcode: QRCode):
    buf, media_type = generate_qr(
        data=qrcode.data,
        format=qrcode.format
    )

    return Response(content=buf.getvalue(), media_type=media_type)