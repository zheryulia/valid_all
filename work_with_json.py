import json
import sys
from jsonschema import validate, ValidationError
from validate_email import validate_email


class InputParameterVerificationError(Exception):
    """Исключение возникает из-за ошибки во входных данных."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return "Ошбика данных! " + str(self.message)


def input_validation() -> None:
    """Функция, считывающая данные из JSON и проверяющая их."""
    try:
        with open('goods.schema.json', 'r', encoding='utf-8') as f1:
            goods_schema = json.load(f1)

        with open('goods.data.json', 'r', encoding='utf-8') as f2:
            goods_data = json.load(f2)
    except json.decoder.JSONDecodeError:
        raise InputParameterVerificationError("Неправильно заполнена схема.")
        sys.exit()
    try:
        validate(goods_data, goods_schema)
    except ValidationError:
        raise InputParameterVerificationError("Схемы отличаются.")
        sys.exit()


def result_validation(email) -> bool:
    """Функция, проверяющая корректный ввод email."""
    email_check = str(email)
    return validate_email(email_check)
