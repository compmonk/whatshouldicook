from datetime import datetime
import base64

from unipath import Path

from django.conf import settings

from .vision import recognize


def upload_image(encoded_image_string):
    save_to_path = Path(settings.UPLOAD_DIR, str(datetime.now().strftime('%Y%m%d%H%M%S')) + '.jpg')
    try:
        with open(save_to_path, "wb") as image:
            image.write(base64.b64decode(encoded_image_string))
        return save_to_path
    except IOError:
        return False


def recognize_image(image_encoded_string):
    image_path = upload_image(image_encoded_string)
    if not image_path:
        return "Unable to Upload Image"
    return recognize(image_path)
