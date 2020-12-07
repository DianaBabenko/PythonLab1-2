class CustomString:
    welcome_str = "Welcome to"
    name_str = 'University'
    number = 123
    number_str = '456'

    def concat(self, first_str, second_str):
        return first_str + ' ' + second_str

    def int(self, str):
        return print(int(str))

    def str(self, str):
        return print(str(str))

    def repr(self, str):
        return print(repr(str))

    def float(self, str):
        return print(float(str))

    def calcStrToInt(self, firstParam, secondParam):
        return print(int(firstParam) + int(secondParam))

    def calcIntToStr(self, firstParam, secondParam):
        return print(str(firstParam) + str(secondParam))