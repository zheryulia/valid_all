from work_with_json import input_validation, result_validation
from typing import Any, Callable


class ResultVerificationError(Exception):
    """Исключение возникает из-за ошибки в проверке параметров."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return "Ошбика в проверке! " + str(self.message)


def default_function() -> None:
    """"Функция-заглушка"""
    print('Сосиска!')
    print('Если видишь сосиску, то код сработал!')


def valid_all(in_validation: Callable, res_validation: Callable,
              on_fail_repeat_times: int, default_behavior: Callable = None) -> Any:
    """Функция-декоратор, валидирующая входные и выходные данные."""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Вложенная функция-обёртка."""
            in_validation()
            k = 0  # переменная-счётчик
            if on_fail_repeat_times == 0:
                raise ResultVerificationError('Провал валидации!')
            cycle = True  # переменная для количества повторений функции
            while cycle and (on_fail_repeat_times < 0
                             or (k < on_fail_repeat_times and on_fail_repeat_times > 0)):
                k += 1
                result = func(*args, **kwargs)
                res_validation(result)

                if default_behavior is not None:
                    default_behavior(*args, **kwargs)
                else:
                    return result

        return wrapper

    return decorator


@valid_all(input_validation, result_validation,
           on_fail_repeat_times=1, default_behavior=default_function)
def func_email() -> str:
    """Функция, демонстрирующая работу декоратора."""
    mail = 'ex@mail.com'
    return mail


if __name__ == "__main__":
    func_email()


