import re

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.core.validators import validate_email
from iran_mobile_va import mobile


def validate_video_size(value):
    file_size = value.size

    if file_size > 52428800:
        raise ValidationError("The maximum file size that can be uploaded is 50MB")
    else:
        return value

def validate_image_size(value):
    file_size = value.size

    if file_size > 5242880:
        raise ValidationError("The maximum image size that can be uploaded is 5MB")
    else:
        return value


def is_valid_iran_code(input):
    if not re.search(r'^\d{10}$', input): return False
    check = int(input[9])
    s = sum(int(input[x]) * (10 - x) for x in range(9)) % 11
    return check == s if s < 2 else check + s == 11