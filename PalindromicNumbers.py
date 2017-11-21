class PalindromicNumbers:

    def __init__(self, decimal_number):
        self.decimal_number = decimal_number

    def _convert_decimal_to_base_recursion(self, quotient, base, converted_base):
        """Algorithm to convert decimal to base by dividing quotient by base and collecting remainder recursively."""
        quotient, remainder = divmod(quotient, base)
        # insert into beginning to prevent reversing array later
        converted_base.insert(0, int(remainder))
        if quotient == 0:
            return 1
        self._convert_decimal_to_base_recursion(quotient, base, converted_base)

    def convert_decimal_to_base(self, base):
        """Set up recursion to convert a decimal to the given base format."""
        converted_base = []
        self._convert_decimal_to_base_recursion(self.decimal_number, base, converted_base)
        return ''.join(map(str, converted_base))

    def _is_palindrome(self, converted_base):
        """Return whether or not the converted based value is equal to its reversed self."""
        if converted_base == converted_base[::-1]:
            return True

    def execute(self):
        """Increments base by 1 until the converted base value is a palindrome."""
        base = 2
        while True:
            converted_base = self.convert_decimal_to_base(base)
            if self._is_palindrome(converted_base):
                return base
            base += 1
