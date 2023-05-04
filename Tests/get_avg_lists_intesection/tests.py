import unittest

from get_avg_lists_intersection import get_avg_lists_intersection


class TestGetAvg(unittest.TestCase):
    """Тестируем get_avg_lists_intersection."""

    def test_mixed_numbers(self):
        result = get_avg_lists_intersection([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
        expected = 3.5
        self.assertEqual(result, expected, 'Функция должна возвращать среднее арифметическое')

    def test_equal_numbers(self):
        result = get_avg_lists_intersection([1, 2, 3], [1, 2, 3])
        expected = 2.0
        self.assertEqual(result, expected, 'Функция должна возвращать среднее арифметическое')

    def test_empty(self):
        result = get_avg_lists_intersection([1, 2, 3], [4, 5, 6])
        expected = 0
        self.assertEqual(result, expected, 'Функция должна возвращать 0 для пустого списка')


if __name__ == '__main__':
    unittest.main()
