
# #HW:
# написать валидацию на Номера Транспартов
# будет класс ValidCarNumber —> будет метод is_valid(self, number)
# который принимает 1 аргумент number и проверяет на валидность то есть:
# Input:

#     01KG777BMW
#     hhh777hhh

# Output:

#     Номер валидный!
#     Номер не валидный!

# ExtraTask:

# Дан массив целых чисел nums, отсортированных в порядке возрастания, и целое число target, напишите функцию для поиска target в nums. Если target существует, верните его индекс. В противном случае возвращайтесь -1.

# class ValidCarNumber:
#     def __init__(self,number):
#         self.number = number



num = [1,3,4,6,7,9,10,66,89]

target = int(input('enter num:'))
for i in num:
    if target in num:
        print(num.index(target))
    elif target not in num:
        print('-1')
    else:
        print('please enter num')        





import re

class ValidCarNumber:
    def __init__(self, number):
        self.number = number

    def is_valid(self):
        self.is_valid = re.search(r"([0-9]{2})([A-Z]{2})([0-9]{3})([A-Z]{3})",self.number)
        if self.is_valid:
            print('Номер валидный!')
        else:
            print('Номер не валидный!')
valid = ValidCarNumber(input('Enter: '))
valid.is_valid()