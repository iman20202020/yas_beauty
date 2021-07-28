from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile


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
