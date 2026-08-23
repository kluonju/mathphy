# 第8章 数值方法

解析手段不够用时——高次代数/超越方程、无原函数的积分、表格数据、常微分方程初值——需要数值算法。本章按问题类型组织：

1. [零点求解](01-finding-zeros.md)：二分、牛顿、割线与收敛阶
2. [数值积分](02-integration.md)：梯形、Simpson、Romberg
3. [插值](03-interpolation.md)：Lagrange / Newton 均差、Runge 现象与样条
4. [ODE 数值解](04-ode.md)：Euler、改进 Euler、RK4 与刚性简介

配套插图由 `scripts/generate_numerical_figures.py` 生成；ODE 示例亦可参考 `scripts/ch06_ode_solver.py`。
