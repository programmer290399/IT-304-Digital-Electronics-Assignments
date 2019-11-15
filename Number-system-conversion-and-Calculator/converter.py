from math import modf


class NumberSystemConverter:

    """
    A simple class to convert a number in a given base to another.

    :param int input_base: The base of the input_num
    :param int/float input_num: Number to be converted to other base
    :param int target_base: Base in which input_num is to be converted


    Algorithm :

        Step 0 . Check whether the number has a fractional part or not , if it has no fractional part then use the
            following algorithm (otherwise go to Step 1) :

            Step 0.1 . Convert input number to decimal using the following algorithm :

                Step 0.1.1 − Determine the column (positional) value of each digit (this depends on the position of the
                        digit and the base of the number system).

                Step 0.1.2 − Multiply the obtained column values (in Step 1) by the digits in the corresponding columns.

                Step 0.1.3 − Sum the products calculated in Step 2. The total is the equivalent value in decimal.


            Step 0.2 . Convert the decimal number to required base using the following algorithm :

                Step 0.2.1 − Divide the decimal number to be converted by the value of the new base.

                Step 0.2.2 − Get the remainder from Step 1 as the rightmost digit (least significant digit) of new base
                    number.

                Step 0.2.3 − Divide the quotient of the previous divide by the new base.

                Step 0.2.4 − Record the remainder from Step 3 as the next digit (to the left) of the new base number.

                Repeat Steps 0.2.3 and 0.2.4, getting remainders from right to left, until the quotient becomes zero in
                Step 3.
                The last remainder thus obtained will be the Most Significant Digit (MSD) of the new base number.

        Step 1 . Follow the same algorithm as above to convert the integer part of the number to desired base and to
            convert the fractional part use following algorithm :

            Step 1.1 - Convert the fractional part to it's decimal equivalent fraction by using Steps 0.1.1.- 0.1.3

            Step 1.2 - Multiply the decimal equivalent of the fractional part with target base

            Step 1.3 - Append the whole part of the product obtained to target base fractional part and reassign decimal
                equivalent of the fractional part to be the fractional part of the product obtained in the step above

            Repeat steps 1.2 and 1.3 until the fractional part of decimal equivalent becomes zero or the iteration limit
            (here 10) is exceeded.
        
    """

    def __init__(self, input_base, input_num, target_base):

        self.input_base = input_base
        self.input_num = input_num
        self.target_base = target_base
        self.hex_table = {
                         10: 'A',
                         11: 'B',
                         12: 'C',
                         13: 'D',
                         14: 'E',
                         15: 'F',
                        }

    def convert(self):
        """
        :return: input_num's equivalent in target_base
        :rtype: str
        """

        if float(self.input_num).is_integer():

            # converting number to decimal base
            digits = [int(digit) for digit in str(self.input_num)]
            decimal_equivalent = sum([digit*(self.input_base**i) for i, digit in enumerate(digits[::-1])])

            # converting the obtained decimal_equivalent to the desired base
            target_num = list()

            while True:

                if decimal_equivalent == 0:
                    if self.target_base == 16 :
                        target_num = ''.join(map(lambda num: str(self.hex_table[num]) if num in range(10, 16) else str(num), target_num[::-1]))
                    else:
                        target_num = ''.join(map(str, target_num[::-1]))
                    return target_num

                current_remainder = decimal_equivalent % self.target_base
                current_quotient = decimal_equivalent // self.target_base
                target_num.append(current_remainder)
                decimal_equivalent = current_quotient

        else:

            int_digits, frac_digits = map(lambda part: [int(digit) for digit in part], str(self.input_num).split('.'))
            decimal_equivalent_int, decimal_equivalent_frac = map(lambda lst: sum(lst), [
                                                                                            [digit * (self.input_base ** i) for i, digit in enumerate(int_digits[::-1])],
                                                                                            [digit*(self.input_base ** (-1 * (i+1))) for i, digit in enumerate(frac_digits)],
                                                                                        ])

            # Converting integer part to desired base
            target_num_int = list()

            while True:

                if decimal_equivalent_int == 0:
                    if self.target_base == 16:
                        target_num_int = ''.join(map(lambda num: str(self.hex_table[num]) if num in range(10, 16) else str(num), target_num_int[::-1]))
                    else:
                        target_num_int = ''.join(map(str, target_num_int[::-1]))
                    break

                current_remainder = decimal_equivalent_int % self.target_base
                current_quotient = decimal_equivalent_int // self.target_base
                target_num_int.append(current_remainder)
                decimal_equivalent_int = current_quotient

            # Converting fractional part to desired base
            target_num_frac = list()
            iteration_count = 0
            while True:

                if any([iteration_count >= 10, float(decimal_equivalent_frac).is_integer()]):
                    if self.target_base == 16:
                        target_num_frac = ''.join(map(lambda num: str(self.hex_table[num]) if num in range(10, 16) else str(num), target_num_frac))
                    else:
                        target_num_frac = ''.join(map(str, target_num_frac))
                    break

                decimal_equivalent_frac *= self.target_base
                fraction, whole = modf(decimal_equivalent_frac)
                target_num_frac.append(int(whole))
                decimal_equivalent_frac = fraction
                iteration_count += 1

            return target_num_int + '.' + target_num_frac


if __name__ == '__main__':
    test = NumberSystemConverter(8, 25.37, 2)
    print(test.convert())
