import os
from datetime import datetime

from unipath import Path

from django.conf import settings


def upload_file(file_name, file_content):
    directory_name = Path(settings.UPLOAD_DIR, str(datetime.now().strftime('%Y%m%d%H%M%S')))

    try:
        os.mkdir(directory_name)
    except OSError:
        # TODO : Add error logs
        return False

    full_filename = Path(directory_name, file_name)

    with open(full_filename, 'wb+') as file:
        for chunk in file_content.chunks():
            file.write(chunk)
        file.close()

    return full_filename
