import os
import base64
import errno
from mimetypes import guess_type, guess_extension
from datetime import datetime

from .models import File


def handle_file(file_id, file):
    filename = download_file(file)

    with open(filename, "r") as fp:
        lines = len(fp.readlines())

    File.objects.filter(id=file_id).update(lines_count=lines)


def download_file(file):
    header, content = file.split(",")
    file_extension = guess_extension(guess_type(header + ",")[0])
    content = base64.b64decode(content)
    filename = get_filename(file_extension)
    create_dirs_if_not_exist(filename)
    with open(filename, "wb") as fp:
        fp.write(content)
    return filename


def get_filename(extension):
    return "uploads/" + datetime.now().strftime("%Y/%m/%d/%H-%M-%S") + "." + extension


def create_dirs_if_not_exist(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
