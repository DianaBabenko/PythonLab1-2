# This is a sample Python script.
# from Fraction import Fraction

from Student import Student
from PhoneBook import PhoneBook
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print_hi('Test')

# Fraction class
#
#
# print('Enter the numerator')
# numerator = input()
#
# print('Enter the denominator')
# denominator = input()
#
# fraction = Fraction(float(numerator), float(denominator))
#
# print('Sum = {numbers_sum}'.format(numbers_sum=fraction.numbers_sum()))
# print('Division = {numbers_division}'.format(numbers_division=fraction.numbers_division()))
# print('Multiplication = {numbers_multiplication}'.format(numbers_multiplication=fraction.numbers_multiplication()))
# print('Subtraction = {numbers_subtraction}'.format(numbers_subtraction=fraction.numbers_subtraction()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == '__main__':

    # --------PhoneBook Task--------
    phoneBook = PhoneBook()
    phoneBook.setAllData()
    phoneBook.getAllData()
    # # --------PhoneBook JsonTask--------
    phoneBook.exportData()
    #
    del phoneBook

    # --------User Task----------
    student = Student()
    student.setAllData()
    student.getAllData()
