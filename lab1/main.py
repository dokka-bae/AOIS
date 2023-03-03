class binary_number:
    def __init__(self):
        self.__number: str = ""
        self.__view = 0  # 0 - direct, 1 - reversed, 2 - addictional
        self.__sign = True

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, view):
        self.__view = view

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, view):
        self.__sign = view

    def __str__(self):
        return self.__number

    def __copy__(self, object):
        self.__sign = object.__sign
        self.__number = object.__number
        self.__view = object.__view

    def reverse(self):
        number = ["1" if bit == "0" else "0" for bit in self.__number]
        self.__number = "".join(number)
        self.__view = 1

    def additional(self):
        self.reverse()
        temp = binary_number()
        temp.decimal_to_bin(1)
        self.__number = self.bin_sum(temp).__number
        self.__view = 2

    def abs(self):
        temp = binary_number()
        temp.__copy__(self)
        if not temp.__sign:
            temp.__sign = self.__sign
            temp.additional()
            temp.__view = 0
        return temp

    def circular_shift_left(self):
        temp = ""
        for bit in self.__number[2:]:
            temp += bit
        temp = self.__number[0] + temp + "0"
        self.__number = temp

    def circular_shift_right(self):
        temp = ""
        for bit in self.__number[:1]:
            temp += bit
        temp = "0" + temp
        self.__number = temp

    def decimal_to_bin(self, number):
        self.__sign = number >= 0
        number = abs(number)
        self.__number = ""
        while number > 0:
            self.__number += str(number % 2)
            number //= 2
        self.__number = self.__number[::-1].zfill(16)
        if not self.__sign:
            self.additional()

    def bin_to_decimal(self):
        if not self.__sign:
            self.additional()
        number = 0
        for i in range(1, len(self.__number)):
            number += int(self.__number[-i]) * 2 ** (i - 1)
        if not self.__sign:
            self.additional()
            return -number
        return number

    def bin_sum(self, object):
        result = binary_number()
        carry = 0
        self.__number = self.__number.zfill(16)
        object.__number = object.__number.zfill(16)
        for i in range(1, 16):
            sum = carry + int(self.__number[-i]) + int(object.__number[-i])
            if sum == 0:
                result.__number += "0"
            elif sum == 1:
                result.__number += "1"
                carry = 0
            elif sum == 2:
                result.__number += "0"
                carry = 1
            elif sum == 3:
                result.__number += "1"
        result.__number = result.__number[::-1]
        if result.__number[0] == "1":
            result.__sign = False
        return result

    def bin_dif(self, object):
        object.__sign = not object.__sign
        object.additional()
        result = self.bin_sum(object)
        object.__sign = not object.__sign
        object.additional()
        return result

    def bin_mul(self, object):
        number_1 = self.abs()
        number_2 = object.abs()
        counter = binary_number()
        result = binary_number()
        i = binary_number()
        i.decimal_to_bin(1)
        counter.decimal_to_bin(0)
        result.decimal_to_bin(0)
        while counter.__number != number_2.__number:
            result = result.bin_sum(number_1)
            counter = counter.bin_sum(i)
        if number_1.__sign ^ number_2.__sign:
            result.__sign = False
            result.additional()
        return result

    def div_assist_function(self, object):  # определение количества битов для сдвига
        for i in range(1, 16):
            if self.__number[-i] == "1":
                return 15 + i
        return 0

    def bin_div(self, object):
        number_1 = self.abs()
        number_2 = object.abs()
        result = binary_number()
        i = binary_number()
        i.decimal_to_bin(1)
        result.decimal_to_bin(0)
        while True:
            number_1 = number_1.bin_dif(number_2)
            if number_1.__sign:
                result = result.bin_sum(i)
            else:
                if self.__sign ^ object.__sign:
                    result.__sign = False
                    result.additional()
                return result


class float_bin_number:
    def __init__(self):
        self.__float_number = ""

    @property
    def float_number(self):
        return self.__float_number

    @float_number.setter
    def float_number(self, __float_number):
        self.__float_number = __float_number

    def __str__(self) -> str:
        return self.__float_number

    def get_int_part(self, number):
        result = ""
        while number > 0:
            result += str(number % 2)
            number //= 2
        return result[::-1]

    def get_real_part(self, number):
        result = ""
        for i in range(0, 64):
            number *= 2
            result += str(int(number))
            number -= int(number)
        return result

    def bin_sim(self, number_1, number_2, shift):
        result = ""
        carry = 0
        if shift == 0:
            number_1 = "1" + number_1
            number_2 = "0" + number_2
        elif shift == 1:
            number_1 = "0" + number_1
            number_2 = "1" + number_2
        elif shift == 2:
            number_1 = "1" + number_1
            number_2 = "0" + number_2
        for i in range(1, len(number_1) + 1):
            sum = carry + int(number_1[-i]) + int(number_2[-i])
            if sum == 0:
                result += "0"
            elif sum == 1:
                result += "1"
                carry = 0
            elif sum == 2:
                result += "0"
                carry = 1
            elif sum == 3:
                result += "1"
        result = result[::-1]
        if carry == 1:
            return True, result
        return False, result

    def bin_to_decimal(self):  # way - True = exponent way - False = mantiss
        number = self.__float_number[1:9]
        exponent = 0
        for i in range(0, len(number)):
            exponent += int(number[i]) * 2 ** (7 - i)
        mantiss = 0.0
        number = self.__float_number[9:]
        for i in range(1, len(number)):
            mantiss += int(number[i - 1]) * 2 ** (-i)
        return (
            ((-1) ** int(self.__float_number[0]))
            * (1 + mantiss)
            * 2 ** (exponent - 127)
        )

    def get_mantiss(self, intPart, realPart):
        result = ""
        if intPart.find("1") != -1:
            pos = intPart.find("1")
            result = intPart[pos + 1 :] + realPart
            result = result[:23]
            return (len(intPart) - pos - 1), result
        else:
            pos = realPart.find("1")
            result = realPart[pos + 1 :]
            result = result[:23]
            return -(pos + 1), result

    def get_exponent(self, number):
        exponent = binary_number()
        exponent.decimal_to_bin(127)
        shift = binary_number()
        shift.decimal_to_bin(number)
        exponentShift = exponent.bin_sum(shift)
        result = exponentShift.number[7:]
        return result

    def get_float_number(self, intPart, realPart):
        exponentShift, result = self.get_mantiss(intPart, realPart)
        exponent = self.get_exponent(exponentShift)
        return exponent + result

    def decimal_to_float_bin(self, number):
        sign = "1"
        if number > 0:
            sign = "0"
        number = abs(number)
        intPart = self.get_int_part(int(number))
        realPart = self.get_real_part(number - int(number))
        self.__float_number = sign + self.get_float_number(intPart, realPart)
        return self.__float_number

    def float_bin_to_decimal(self):
        print(self.bin_to_decimal())

    def first_exponent_greater(self, object, exponent_1, exponent_2):
        sign = self.__float_number[0]
        exponent__1 = self.__float_number[1:9]
        mantiss__1 = self.__float_number[9:]
        mantiss__2 = object.__float_number[9:]
        _range = exponent_1 - exponent_2
        mantiss__2 = "1" + mantiss__2[:-1]
        shift = ""
        for i in range(0, _range - 1):
            shift += "0"
        if _range > 1:
            mantiss__2 = shift + mantiss__2[: -(_range - 1)]
        shifted, mantiss__2 = self.bin_sim(mantiss__1, mantiss__2, 2)
        if shifted:
            exponent_1 += 1
            temp_exponent = binary_number()
            temp_exponent.decimal_to_bin(exponent_1)
            return sign + temp_exponent.number[8:] + "0" + mantiss__2[1:]
        return sign + exponent__1 + mantiss__2[1:]

    def second_exponent_greater(self, object, exponent_1, exponent_2):
        sign = self.__float_number[0]
        exponent__2 = self.__float_number[1:9]
        mantiss__2 = self.__float_number[9:]
        mantiss__1 = object.__float_number[9:]
        _range = exponent_2 - exponent_1
        mantiss__1 = "1" + mantiss__1[:-1]
        shift = ""
        for i in range(0, _range - 1):
            shift += "0"
        if _range > 1:
            mantiss__1 = shift + mantiss__1[: -(_range - 1)]
        shifted, mantiss__1 = self.bin_sim(mantiss__2, mantiss__1, 1)
        if shifted:
            exponent_2 += 1
            temp_exponent = binary_number()
            temp_exponent.decimal_to_bin(exponent_2)
            return sign + temp_exponent.number[8:] + "0" + mantiss__1[1:]
        return sign + exponent__2 + mantiss__1

    def exponents_equals(self, object, exponent_1, exponent_2):
        sign = self.__float_number[0]
        mantiss__2 = self.__float_number[9:]
        mantiss__1 = object.__float_number[9:]
        exponent__1 = self.__float_number[1:9]
        shifted, mantiss__1 = self.bin_sim(mantiss__2, mantiss__1, 0)
        temp_exponent__1 = binary_number()
        temp_exponent__1.decimal_to_bin(exponent_1 + 1)
        temp_exponent_1 = temp_exponent__1.number[8:]
        if shifted:
            return sign + temp_exponent_1 + "1" + mantiss__1[1:]
        else:
            return sign + temp_exponent_1 + "0" + mantiss__1[1:]

    def float_bin_sum(self, object):
        exponent__1 = self.__float_number[1:9]
        exponent__2 = object.__float_number[1:9]
        exponent_1 = 0
        for i in range(0, len(exponent__1)):
            exponent_1 += int(exponent__1[i]) * 2 ** (7 - i)
        exponent_2 = 0
        for i in range(0, len(exponent__2)):
            exponent_2 += int(exponent__2[i]) * 2 ** (7 - i)
        if exponent_1 > exponent_2:
            return self.first_exponent_greater(object, exponent_1, exponent_2)
        elif exponent_2 > exponent_1:
            return self.second_exponent_greater(object, exponent_1, exponent_2)
        else:
            return self.exponents_equals(object, exponent_1, exponent_2)


number_1 = binary_number()
number_1.decimal_to_bin(11)
number_2 = binary_number()
number_2.decimal_to_bin(2)

print(number_1)
print(number_1.bin_to_decimal())

print(number_2)
print(number_2.bin_to_decimal())

print(number_1.bin_sum(number_2))
print(number_1.bin_sum(number_2).bin_to_decimal())

print(number_1.bin_dif(number_2))
print(number_1.bin_dif(number_2).bin_to_decimal())

print(number_1.bin_mul(number_2))
print(number_1.bin_mul(number_2).bin_to_decimal())

print(number_1.bin_div(number_2))
print(number_1.bin_div(number_2).bin_to_decimal())
float_1 = float_bin_number()
float_2 = float_bin_number()
print(float_1.decimal_to_float_bin(6.125))
print(float_2.decimal_to_float_bin(5.25))
print(float_1.float_bin_to_decimal())
print(float_2.float_bin_to_decimal())
float_3 = float_bin_number()
float_3.float_number = float_1.float_bin_sum(float_2)
print(float_3.float_bin_to_decimal())
