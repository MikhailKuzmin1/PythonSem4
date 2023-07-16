'''В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.'''

import random

bush = int(input('Введите колличество кустов: '))
harvest = [random.randint(0,10) for i in range(0, bush)]
print(f'{harvest} - ягод на кустах')
i = 0
sum_berry = 0
end = 3
res = []
j = 1
while i < bush:
    if end < bush + 1:
        sum_berry = sum(harvest[i:end])
        i += 1
        end += 1
        res.append(sum_berry)
    else:
        sum_berry = sum(harvest[i:]) + sum(harvest[:j])
        i += 1
        j += 1
        res.append(sum_berry)
print(f'За один заход можно собрать ягод: {max(res)}')
