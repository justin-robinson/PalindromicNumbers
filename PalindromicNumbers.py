class PalindromicNumbers:

    def __init__(self, decimal_number):
        self.decimal_number = decimal_number

    def _convert_decimal_to_base_recursion(self, quotient, base, based_array):
        """Algorithm to convert decimal to base by dividing quotient by base and collecting remainder recursively."""
        quotient, remainder = divmod(quotient, base)
        # insert into beginning to prevent reversing array later
        based_array.insert(0, int(remainder))
        if quotient == 0:
            return 1
        self._convert_decimal_to_base_recursion(quotient, base, based_array)

    def convert_decimal_to_base(self, base):
        """Set up recursion to convert a decimal to the given base format."""
        # TODO change array to a string which would prevent having to convert array to string later?
        based_array = []
        self._convert_decimal_to_base_recursion(self.decimal_number, base, based_array)
        return ''.join(map(str, based_array))

    def _is_palindrome(self, based_value):
        """Return whether or not the converted based value is equal to it's reversed self."""
        if based_value == based_value[::-1]:
            return True

    def execute(self):
        """Increments base by 1 until the converted base value is a palindrome."""
        # TODO add a time out to prevent infinite loops? -- look into possibility
        base = 2
        while True:
            based_value = self.convert_decimal_to_base(base)
            if self._is_palindrome(based_value):
                return base
            base += 1
