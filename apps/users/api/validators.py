import re

from rest_framework.exceptions import ValidationError


def secure_password(value):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$"
    if re.search(regex, value) is None:
        raise ValidationError('La contraseña debe contener al menos 1 mayúscula, 1 minúscula y 1 número')
