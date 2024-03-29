from math import modf


class NumberSystemConverter:

    """
    A simple class to convert a number in a given base to another.

    :param int input_base: The base of the input_num
    :param int/float input_num: Number to be converted to other base
    :param int target_base: Base in which input_num is to be converted
    """

    def __init__(self, input_base, input_num, target_base):

        self.input_base = input_base
        self.input_num = input_num
        self.target_base = target_base
        self.hex_table = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    def convert(self):
        """
        :return: input_num's equivalent in target_base
        :rtype: str
        """

        if float(self.input_num).is_integer():

            # converting number to decimal base
            digits = [int(digit) for digit in str(self.input_num)]
            decimal_equivalent = sum(
                [digit * (self.input_base ** i) for i, digit in enumerate(digits[::-1])]
            )

            # converting the obtained decimal_equivalent to the desired base
            target_num = list()

            while True:

                if decimal_equivalent == 0:
                    if self.target_base == 16:
                        target_num = "".join(
                            map(
                                lambda num: str(self.hex_table[num])
                                if num in range(10, 16)
                                else str(num),
                                target_num[::-1],
                            )
                        )
                    else:
                        target_num = "".join(map(str, target_num[::-1]))
                    return target_num

                current_remainder = decimal_equivalent % self.target_base
                current_quotient = decimal_equivalent // self.target_base
                target_num.append(current_remainder)
                decimal_equivalent = current_quotient

        else:

            int_digits, frac_digits = map(
                lambda part: [int(digit) for digit in part],
                str(self.input_num).split("."),
            )
            decimal_equivalent_int, decimal_equivalent_frac = map(
                lambda lst: sum(lst),
                [
                    [
                        digit * (self.input_base ** i)
                        for i, digit in enumerate(int_digits[::-1])
                    ],
                    [
                        digit * (self.input_base ** (-1 * (i + 1)))
                        for i, digit in enumerate(frac_digits)
                    ],
                ],
            )

            # Converting integer part to desired base
            target_num_int = list()

            while True:

                if decimal_equivalent_int == 0:
                    if self.target_base == 16:
                        target_num_int = "".join(
                            map(
                                lambda num: str(self.hex_table[num])
                                if num in range(10, 16)
                                else str(num),
                                target_num_int[::-1],
                            )
                        )
                    else:
                        target_num_int = "".join(map(str, target_num_int[::-1]))
                    break

                current_remainder = decimal_equivalent_int % self.target_base
                current_quotient = decimal_equivalent_int // self.target_base
                target_num_int.append(current_remainder)
                decimal_equivalent_int = current_quotient

            # Converting fractional part to desired base
            target_num_frac = list()
            iteration_count = 0
            while True:

                if any(
                    [iteration_count >= 10, float(decimal_equivalent_frac).is_integer()]
                ):
                    if self.target_base == 16:
                        target_num_frac = "".join(
                            map(
                                lambda num: str(self.hex_table[num])
                                if num in range(10, 16)
                                else str(num),
                                target_num_frac,
                            )
                        )
                    else:
                        target_num_frac = "".join(map(str, target_num_frac))
                    break

                decimal_equivalent_frac *= self.target_base
                fraction, whole = modf(decimal_equivalent_frac)
                target_num_frac.append(int(whole))
                decimal_equivalent_frac = fraction
                iteration_count += 1

            return target_num_int + "." + target_num_frac


if __name__ == "__main__":
    test = NumberSystemConverter(8, 25.37, 2)
    print(test.convert())
