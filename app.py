import qrcode
import datetime

from typing import Dict
from settings import URL_PATH


def create_code(link: Dict):
    try:
        return make_qr_code(link)
    except Exception as ex:
        print(ex)


def make_qr_code(data: Dict):
    try:
        qr = qrcode.QRCode(version=1, box_size=100, border=1)
        qr.add_data(data['link'])
        qr.make(fit=True)

        if save_qr_code(qr, data):
            return {'status': 'success'}
    except Exception as ex:
        print(ex)


def save_qr_code(qr, data):
    try:
        img = qr.make_image(fill='black', back_color='white')
        nome = data["nome"].lower().replace(" ", "_")
        time_now = f"{datetime.datetime.now():%Y-%m-%d}"
        img.save(f'{URL_PATH}/{nome}-{time_now}.png')
        return True
    except Exception as ex:
        print(ex)
        return False
