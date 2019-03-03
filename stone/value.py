"""
8-12
Define variables
"""

__all__ = ['l1_gold', 'l1_diamond', 'l1_to_l3_stone', 'l1_to_l3_gold',
           'l1_to_l3_vit', 'l3_to_l4_stone', 'l3_to_l4_gold', 'l3_to_l4_vit',
           'l3_to_l4_rate', 'l4_to_l6_stone', 'l4_to_l6_gold', 'l4_to_l6_vit',
           'diamond_to_gold', 'vit_to_gold']



"""
    购买1级石头
"""
l1_gold = 0.75  # 1颗1级石头消耗0.75金
l1_diamond = 8  # 1颗1级石头同时还需要消耗8颗钻石

"""
    1级合成3级
"""
l1_to_l3_stone = 12  # 1颗1级石头变成1颗3级石头，需要消耗12颗1级石头
l1_to_l3_gold = 0.39  # 同时还需要消耗0.39金
l1_to_l3_vit = 10  # 同时还需要消耗10点体力

"""
    3级合成4级
"""
l3_to_l4_stone = 16  # 1颗3级石头变成1颗4级石头，需要消耗16个1级石头
l3_to_l4_gold = 0.897  # 1颗3级石头变成1颗4级石头，需要消耗0.897金
l3_to_l4_vit = 10
l3_to_l4_rate = 0.4878  # 1颗3级石头变成1颗4级石头成功率只有0.4878.
                        #如果失败，则金和16颗1级石头将被扣除，
                        # 但是不消耗体力。

"""
    4级合成6级
"""
l4_to_l6_stone = 12  # 1颗4级石头变成6级石头，概率100%，需要消耗12颗4级石头
l4_to_l6_gold = 19.75  # 需要消耗19.75金
l4_to_l6_vit = 10  # 需要消耗10点体力


"""
已知1颗6级石头的市场售价为750金，请问是自己合成石头划算还是直接购买划算？
其他数据：
    1颗钻石diamond卖出0.05金
    1点体力vit卖出1金
"""
diamond_to_gold = 0.05
vit_to_gold = 1

