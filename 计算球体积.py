'''
输入半径，计算球的体积。球体积公式是 

输入格式:
输入半径，可以是小数。

输出格式:
输出球的体积，结果保留3位小数，π使用math库的常量。
'''
import math
r = float(input())
v = 4/3*math.pi*r**3
print(f"v={v:.3f}")
'''
错误分析
1.不会用π，math.pi  !!!一定加math
2.不会计算r的三次幂，r**3
'''
