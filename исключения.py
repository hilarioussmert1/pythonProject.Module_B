class NonPositiveDigitException(ValueError):
    pass

class Square:
    def ask(self, a):
        a = int(input('gggggg:'))
        print(a)
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('uncorrectly long!')
s = Square(0)
s.ask(0)
s.__init__(0)

