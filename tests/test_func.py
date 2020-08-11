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
        self.test_func = func.get_lower_betwin_two_upper
        
    def test_zero_input(self):
        """Проверка на пустую входную строчку
        Ожидается пустая строка

        """
        result = self.test_func(ZERO_INPUT)
        self.assertEqual(len(result), 0, 'Вернулась не пустая строка')

    def test_one_input(self):
        """ На вход подается 1 тройка символов
        Ожидается один символ

        """
        result = self.test_func(ONE_INPUT)
        self.assertEqual(result, 'i', 'Ошибка 1 тройки')

    def test_between_many_input(self):
        """ На вход подается строка у которой между заглавными несколько строчных 1  обрамление
        Ожидается пустая строка

        """
        result = self.test_func(ONE_INPUT_MANY)
        self.assertEqual(len(result), 0, 'строки у которой между заглавными несколько строчных 1  обрамление')

    def test_two_input(self):
        """ На вход подается 2 тройки символов подряд
        Ожидается два символа

        """
        result = self.test_func(TWO_INPUT)
        self.assertEqual(result, 'id', 'Ошибка 2 троек')

    def test_many_first(self):
        """ На вход подается 2 обрамления символа подряд у первого обрамления несколько заглавных впереди
        Ожидается два символа

        """
        result = self.test_func(MANY_FIRST)
        self.assertEqual(result, 'id', 'несколько заглавных впереди')

    def test_many_last(self):
        """ На вход подается 2 обрамления символа подряд у последнего обрамления несколько заглавных позади
        Ожидается два символа

        """
        result = self.test_func(MANY_LAST)
        self.assertEqual(result, 'id', 'несколько заглавных позади')

    def test_many_between(self):
        """ На вход подается 2 обрамления символа подряд посередине несколько заглавных
        Ожидается два символа

        """
        result = self.test_func(MANY_BETWEEN)
        self.assertEqual(result, 'id', 'несколько заглавных между')


if __name__ == '__main__':
    unittest.main()
