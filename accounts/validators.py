from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.core.validators import validate_email


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
def email_validate(email):


    try:
        # Validate.
        valid = validate_email(email)

        # Update with the normalized form.
        email = valid.email
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))