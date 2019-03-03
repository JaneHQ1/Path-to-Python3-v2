"""
8-8 code
"""


# def squsum(*param):
#     sum = 0
#     for i in param:
#         sum += i*i
#     print(sum)
#
#
# squsum(1, 2, 3)


def city_temp(**param):
    for key,value in param.items():
        print(key, ':', value)


# city_temp(bj='32c', xm='23c', sh='31c')

a = {'bj': '32c', 'xm': '23c', 'sh': '31c'}
city_temp(**a)