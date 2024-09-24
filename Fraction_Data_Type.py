# Create Own Data Type Using Class And Some Magic Functions
import functools as ft


class Fraction:
    def __init__(self, num1, num2):
        self.numretor = num1
        self.denominator = num2

        """
            description: 

            This class is made to provide extra features in calculation of two fraction 
            and provide answer in fraction

            input => two Fraction numbers

            output => +,-,*,/  on fraction

            developed by => Rishikesh Pandey

            created => 01/jan/2024

            modified in => jan 1, 2024

            """
# ----------------------------------------------------------------------------
# Check numerator or Denominator is 0 or not                                |
# ----------------------------------------------------------------------------

    def checkZero(self, num1, num2, num3, num4):

        #  ( if any fraction is 0 then next fraction is answer )

        if num1 == 0:
            if num4 < 0:
                temp_num = -num3
                temp_deno = -num4
            else:
                temp_num = num3
                temp_deno = num4

        elif num3 == 0:
            if num2 < 0:
                temp_num = -num1
                temp_deno = -num2
            else:
                temp_num = num1
                temp_deno = num2
        return [temp_num, temp_deno]

    def lcm(self, num):
        l = []
        if (num == 1):
            l.append(num)
            return l
        real = num
        rem = 2
        while num != 1:
            if num % rem == 0:
                num = num // rem
                l.append(rem)
                rem -= 1
            if rem == real // 2:
                break
            rem += 1
        if len(l) == 0:
            l.append(real)
        return l

# ----------------------------------------------------------------------------
# check any negative number present or not                                  |
# ----------------------------------------------------------------------------

    def checkNegative(self, num1, num2, deno1, deno2):
        if (num1 > 0 and num2 < 0) or (num1 < 0 and num2 < 0):
            num1 = -num1
            num2 = -num2
        if (deno1 > 0 and deno2 < 0) or (deno1 < 0 and deno2 < 0):
            deno1 = -deno1
            deno2 = -deno2
        return [num1, num2, deno1, deno2]


# ----------------------------------------------------------------------------
# Simplification of Fraction                                                |
# ----------------------------------------------------------------------------

    def simplification(self, num1, num2):

        # ( Simplify Then Print )
        numretor = num1
        if num1 < 0:
            num1 = - num1
        if num2 < 0:
            num2 = -num2
        l1 = self.lcm(num1)
        l2 = self.lcm(num2)

        # print(l1)
        # print(l2)

        i = j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] == l2[j]:
                l1[i] = 1
                l2[j] = 1
                i += 1
                j += 1
            elif l1[i] < l2[j]:
                i += 1
            elif l1[i] > l2[j]:
                j += 1

        # print(l1)
        # print(l2)

        temp_num = ft.reduce(lambda num1, num2: num1*num2, l1)
        temp_deno = ft.reduce(lambda num1, num2: num1*num2, l2)

        if numretor < 0:
            temp_num = -temp_num

        return "{}/{}".format(temp_num, temp_deno)

    def __str__(self):
        return "{}/{}".format(self.numretor, self.denominator)


# ----------------------------------------------------------------------------
#    Addition of Two Fractional Numbers                                     |
# ----------------------------------------------------------------------------


    def __add__(self, num):
        if self.denominator == 0 or num.denominator == 0:  # 1/0 --> infinite
            return "Infinite"
        if self.numretor == 0 and num.numretor == 0:  # 0/2 + 0/3 --> 0
            return 0
        if self.numretor == 0 or num.numretor == 0:
            res = self.checkZero(
                self.numretor, self.denominator, num.numretor, num.denominator)
            temp_num = res[0]
            temp_deno = res[1]
        else:
            list2 = self.checkNegative(
                self.numretor, self.denominator, num.numretor, num.denominator)
            temp_num = (list2[0] * list2[3]) + \
                (list2[1] * list2[2])
            temp_deno = (list2[1] * list2[3])
        return self.simplification(temp_num, temp_deno)


# ----------------------------------------------------------------------------
# Subtraction of two fractional numbers                                     |
# ----------------------------------------------------------------------------


    def __sub__(self, num):
        temp_num = (self.numretor * num.denominator) - \
            (self.denominator * num.numretor)
        temp_deno = (self.denominator * num.denominator)
        return self.simplification(temp_num, temp_deno)


# ----------------------------------------------------------------------------
# Multiplication of two fractional numbers                                  |
# ----------------------------------------------------------------------------


    def __mul__(self, num):
        temp_num = self.numretor * num.numretor
        temp_deno = self.denominator * num.denominator

        return self.simplification(temp_num, temp_deno)


# ----------------------------------------------------------------------------
# Division of Two fractional numbers                                        |
# ----------------------------------------------------------------------------

    def __truediv__(self, num):
        temp_num = self.numretor * num.denominator
        temp_deno = self.denominator * num.numretor

        return self.simplification(temp_num, temp_deno)


x = Fraction(6, 5)
print(x)
y = Fraction(2, 8)
print(y)
# print("------------------------------------------------------------------")
# # print(x, " + ", y, " => ", x+y)
# print("------------------------------------------------------------------")
# # print(x, " - ", y, " => ", x-y)
# print("------------------------------------------------------------------")
# print(x, " * ", y, " => ", x*y)
# print("------------------------------------------------------------------")
# # print(x, " / ", y, " => ", x/y)
print("-----------------------------------------------------------")
print(x, " + ", y, " => ", x+y)
