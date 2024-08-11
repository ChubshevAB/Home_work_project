import pytest

from src.decorators import func


def test_log_success_stdout(capsys):
    """Тест выполнения функции без ошибки и вывод результата в консоль"""

    func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_error(capsys):
    """Тест выполнения функции с ошибкой и вывод результата в консоль"""
    func(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: ZeroDivisionError. Inputs: (1, 0), {}\n"


# def test_log_good_file_log():
#     """Тестирует запись в файл после успешного выполнения"""
#     file_path = Path('d:\Python\Projects\Home_work_project\src\log.txt')
#
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         file_path = tmp_file.name
#
#     @log(filename='log.txt')
#     def func(x, y):
#         return x + y
#
#     func(1, 2)
#
#     with open(file_path, 'r', encoding='utf-8') as file:
#         logs = file.read()
#
#     assert "my_function ok" in logs
