from unittest import TestCase

from PalindromicNumbers import PalindromicNumbers


class TestPalindromicNumbers(TestCase):

    def test_convert_decimal_to_base_recursion(self):
        converted_base = []
        PalindromicNumbers(10)._convert_decimal_to_base_recursion(10, 3, converted_base)
        converted_base = ''.join(map(str, converted_base))
        self.assertNotEqual(converted_base, '10')

        converted_base = []
        PalindromicNumbers(11)._convert_decimal_to_base_recursion(11, 2, converted_base)
        converted_base = ''.join(map(str, converted_base))
        self.assertEqual(converted_base, '1011')

        with self.assertRaises(TypeError):
            PalindromicNumbers('10')._convert_decimal_to_base_recursion('10', 3, converted_base)

    def test_convert_decimal_to_base(self):
        base = PalindromicNumbers(7).convert_decimal_to_base(3)
        self.assertNotEqual(base, '2')

        base = PalindromicNumbers(18).convert_decimal_to_base(3)
        self.assertEqual(base, '200')

        with self.assertRaises(TypeError):
            PalindromicNumbers('10').convert_decimal_to_base('10')

    def test_is_palindrome(self):
        self.assertTrue(PalindromicNumbers(5)._is_palindrome('101'))
        self.assertFalse(PalindromicNumbers(11)._is_palindrome('1011'))

    def test_execute(self):
        base = PalindromicNumbers(5).execute()
        self.assertEqual(base, 2)

        base = PalindromicNumbers(19).execute()
        self.assertEqual(base, 18)
