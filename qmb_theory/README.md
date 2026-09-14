# 量子多体理论讲义

本目录为研究生课程 **B113C004 量子多体理论** 的讲义，结构仿照 `lecture_new`。

## 目录结构

- `main.tex`：主文件
- `frontmatter/`：前言等前置内容
- `chapters/`：各章独立目录与子节
- `refs/Shi_Junren_QTMPS.pdf`：施均仁《多体系统的量子理论》讲义副本（参考）

## 编译全书

```bash
latexmk -xelatex main.tex
```

或：

```bash
xelatex main.tex
```

## 只编译部分章节

在 `main.tex` 中取消注释并修改：

```tex
\includeonly{chapters/ch01/ch01,chapters/ch02/ch02}
```

## 章节与来源

| 章 | 内容 | 主要依据 |
|----|------|----------|
| 1 绪论 | 多体问题概述、理论发展 | 课程大纲 |
| 2 二次量子化 | 全同粒子、平移不变 $H$、密度算符、声子、Fröhlich | GV + Gross Ch1–6,12 |
| 3 格林函数 | GML、Goldstone、$W$/顶点、GMB、骨架、有限温 | Gross Ch14–29 + Mahan |
| 4 HF 与 DFT | RHF/UHF 困境、交换自能、Slater/OEP、KS/LDA | Gross Ch7–10 + GV |
| 5 线性响应 | 经典/量子等离、Lindhard/RPA/STLS、Kubo 电导 | Gross Ch11 + GV + Mahan |
| 6 泛函积分 | 路径积分、虚时、相干态泛函积分 | 施均仁 Ch3 |
| 7 有效作用量 | Landau 平衡/输运、微观极限、Kondo | Gross Ch30–34 + GV Ch8 |
| 8 相变与 SSB | Landau、BEC、声子 $V_{\mathrm{eff}}$、Cooper/BCS | Gross Ch13 + 施均仁 + Mahan |

教材：Fabrizio, *A course in quantum many-body theory*, Springer, 2022.
