"""
Functions
"""
from stone.value import *
import random

"""
    Initialise variables
"""
gold = 0
diamond = 0
vit = 0

"""
    Random pick in a certain probability
"""
def random_pick(seq, probabilities):
    x = random.uniform(0, 1)  # 首先随机生成一个0，1之间的随机数
    cumulative_probability = 0.0
    for item, item_probability in zip(seq, probabilities):  # seq代表待输入的字符串，prob代表各自字符串对应的概率
        cumulative_probability += item_probability  # 只有当累加的概率比刚才随机生成的随机数大时候，才跳出，并输出此时对应的字符串
        if x < cumulative_probability:
            break
    return item


"""
    0: failed to update
    1: sec
"""
def l3_to_l4_trials():
    trials = [0, 1]
    probabilities = [1-l3_to_l4_rate, l3_to_l4_rate]
    result = random_pick(trials, probabilities)
    return result


def l1_count(l1):
    l1 += 1
    global gold
    gold = gold + l1_gold
    global diamond
    diamond = diamond + l1_diamond
    return l1


def l1_to_l3(l1_num, l3_num):
    if l1_num % l1_to_l3_stone == 0:
        # l1 = 0
        l3 = l3_num + 1
        global gold
        gold = gold + l1_to_l3_gold
        global vit
        vit = vit + l1_to_l3_vit
        return l3
    else:
        return l3_num


def l3_to_l4(l1_num, l3_num, l4_num):
    if l3_num == 1 and l1_num == l3_to_l4_stone:
        if l3_to_l4_trials():
            l1 = 0
            l3 = 0
            l4 = l4_num + 1
            global gold
            gold = gold + l3_to_l4_gold
            global vit
            vit = vit + l3_to_l4_vit
            return l1, l3, l4
        else:
            l1 = l1_num - l3_to_l4_stone
            l3 = l3_num
            l4 = 0
            gold = gold + l3_to_l4_gold
            return l1, l3, l4
    else:
        return l1_num, l3_num, l4_num


def l4_to_l6(l4_num, l6_num):
    if l4_num == l4_to_l6_stone:
        l4 = 0
        l6 = l6_num + 1
        global gold
        gold = gold + l4_to_l6_gold
        global vit
        vit = vit + l4_to_l6_vit
        return l4, l6
    else:
        return l4_num, l6_num




