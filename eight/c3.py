"""
8-3 code
"""


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 + 2 + 10
    return damage1, damage2


dam = damage(3, 6)
print(type(dam[0]))

# skill1_dam, skill2_dam = damage(3, 6)
# print(skill1_dam, skill2_dam)


