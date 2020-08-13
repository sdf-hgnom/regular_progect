import unittest
import func

ZERO_INPUT = ''
ONE_INPUT = 'AiA'
ONE_INPUT_MANY = 'AiiA'
TWO_INPUT = 'AiAdA'
MANY_FIRST = 'AAiAdS'
MANY_LAST = 'AiAdSSS'
MANY_BETWEEN = 'AiASSdA'


class MyTestFunc(unittest.TestCase):

    def setUp(self) -> None:
        self.test_func_base = func.get_lower_betwin_two_upper
        self.test_func_regular = func.get_lower_betwin_two_upper_re

    def test_zero_input(self):
        """Проверка на пустую входную строчку
        Ожидается пустая строка

        """
        result1 = self.test_func_base(ZERO_INPUT)
        result2 = self.test_func_regular(ZERO_INPUT)
        self.assertEqual(result1, result2, 'Ошибка пустой строки')

    def test_one_input(self):
        """ На вход подается 1 тройка символов
        Ожидается один символ

        """
        result1 = self.test_func_base(ONE_INPUT)
        result2 = self.test_func_regular(ONE_INPUT)
        self.assertEqual(result1, result2, 'Ошибка 1 тройки')

    def test_between_many_input(self):
        """ На вход подается строка у которой между заглавными несколько строчных 1  обрамление
        Ожидается пустая строка

        """
        result1 = self.test_func_base(ONE_INPUT_MANY)
        result2 = self.test_func_regular(ONE_INPUT_MANY)
        self.assertEqual(result1, result2, 'строки у которой между заглавными несколько строчных 1  обрамление')

    def test_two_input(self):
        """ На вход подается 2 тройки символов подряд
        Ожидается два символа

        """
        result1 = self.test_func_base(TWO_INPUT)
        result2 = self.test_func_regular(TWO_INPUT)
        self.assertEqual(result1, result2, 'Ошибка 2 троек')

    def test_many_first(self):
        """ На вход подается 2 обрамления символа подряд у первого обрамления несколько заглавных впереди
        Ожидается два символа

        """
        result1 = self.test_func_base(MANY_FIRST)
        result2 = self.test_func_regular(MANY_FIRST)
        self.assertEqual(result1, result2, 'несколько заглавных впереди')

    def test_many_last(self):
        """ На вход подается 2 обрамления символа подряд у последнего обрамления несколько заглавных позади
        Ожидается два символа

        """
        result1 = self.test_func_base(MANY_LAST)
        result2 = self.test_func_regular(MANY_LAST)
        self.assertEqual(result1, result2, 'несколько заглавных позади')

    def test_many_between(self):
        """ На вход подается 2 обрамления символа подряд посередине несколько заглавных
        Ожидается два символа

        """
        result1 = self.test_func_base(MANY_BETWEEN)
        result2 = self.test_func_regular(MANY_BETWEEN)
        self.assertEqual(result1, result2, 'несколько заглавных между')


if __name__ == '__main__':
    unittest.main()
