import unittest
import func

ZERO_INPUT = ''
ONE_INPUT = 'AiA'
ONE_INPUT_MANY = 'AiiA'
TWO_INPUT = 'AiAdA'
MANY_FIRST = 'AAiAdS'
MANY_LAST = 'AiAdSSS'
MANY_BETWEEN = 'AiASSdA'
test_func = func.get_lower_betwin_two_upper


class MyTestCase(unittest.TestCase):
    def test_zero_input(self):
        """Проверка на пустую входную строчку
        Ожидается пустая строка

        """
        result = test_func(ZERO_INPUT)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
