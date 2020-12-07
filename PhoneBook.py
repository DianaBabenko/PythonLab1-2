import json


class PhoneBook(object):
    phoneBookList = []

    def __init__(self):
        """Constructor"""
        self.setCountRecord()

    def __del__(self):
        """Destructor"""
        print("Викликано метод __del__()")

    def setCountRecord(self):
        print('Write count of new record: ')
        self.countRecord = int(input())

    def setAllData(self):
        for i in range(self.countRecord):
            arr = {"id": i + 1}

            print('Name: ')
            arr["name"] = input()

            print('Surname: ')
            arr["surname"] = input()

            print('Middlename: ')
            arr["middlename"] = input()

            print('Personal phone: ')
            arr["personalPhone"] = input()

            print('Phone: ')
            arr["phone"] = input()

            print('Additional info: ')
            arr["additionalInfo"] = input()

            self.setPhoneBookList(arr)

    def setPhoneBookList(self, arr):
        self.phoneBookList.append(arr)

    def getAllData(self):
        print(json.dumps(self.phoneBookList))

    def exportData(self):
        file = open('phoneBook.json', 'w')
        file.write(json.dumps(self.phoneBookList))
        file.close()
