"""
8-12 code
划算还是不划算？
"""
from stone.tool import *
import stone.tool as tool

l1 = 0
l3 = 0
l4 = 0
l6 = 0


while l6 == 0:
    l1 = l1_count(l1)
    if l1 % (l1_to_l3_stone + l3_to_l4_stone):
        l3 = l1_to_l3(l1, l3)
        # output = l1_to_l3(l1, l3)
        # l1 = output[0]
        # l3 = output[1]
    else:
        continue
    output = l3_to_l4(l1, l3, l4)
    l1 = output[0]
    l3 = output[1]
    l4 = output[2]
    # print(l1)
    # print(l3)
    # print(l4)
    output = l4_to_l6(l4, l6)
    l4 = output[0]
    l6 = output[1]
    # print(tool.gold)


gold = tool.gold + tool.diamond * diamond_to_gold + tool.vit * vit_to_gold
print(gold)





















