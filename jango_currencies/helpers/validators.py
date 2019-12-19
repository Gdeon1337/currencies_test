from rest_framework.exceptions import ValidationError


def raise_if_empty(*args, error: str = 'Missing data.'):
    for arg in args:
        if arg is None:
            raise ValidationError(error)


def raise_if_not_numeric(*args, error: str = 'Incorrect data.'):
    for arg in args:
        if not str(arg).isdigit():
            raise ValidationError(error)
