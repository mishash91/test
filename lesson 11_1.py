class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        if self.denominator == 0:
            raise ZeroDivisionError

    def get(self):
        return self.numerator / self.denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            other = Fraction(other.numerator, other.denominator)
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            other = Fraction(other.numerator, other.denominator)
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __sub__(self, other):
        if isinstance(other, Fraction):
            other = Fraction(other.numerator, other.denominator)
        return Fraction(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            other = Fraction(other.numerator, other.denominator)
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def __eq__(self, other):
        return self.get() == other.get()

    def __ne__(self, other):
        return self.get() != other.get()

    def __lt__(self, other):
        return self.get() < other.get()

    def __le__(self, other):
        return self.get() <= other.get()

    def __gt__(self, other):
        return self.get() > other.get()

    def __ge__(self, other):
        return self.get() >= other.get()


c1 = Fraction(1, 10)
c2 = Fraction(1, 100)
c3 = Fraction(1, 1000)
c4 = Fraction(1, 10)
print(c1 >= c4 >= c2)
print((c1 + c2 + c3).get())
print((c1 - c2 - c3).get())
print((c1 * c2 * c3).get())
print((c1 / c2 / c3).get())
print(c1 == c3)
print(c1 >= c3)
print(c2 <= c3)
print(c2 != c3)
sp = sorted([c1, c2, c3], reverse=True)
print([i.get() for i in sp])
sp.sort(reverse=False)
print([i.get() for i in sp])
