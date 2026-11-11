# CLM5⁃FATES 模式对中国长白山针阔混交林分布的模拟

隋 月 1，2 ，杨 传 玉 1

1. 中国地质大学（武汉）环境学院，湖北武汉 430078  
2. 中国气象局‒中国地质大学（武汉）极端天气气候与水文地质灾害研究中心，湖北武汉 430078

摘 要：长白山阔叶红松林是全球为数不多的大面积原始针阔混交林，对其开展模拟研究尤为必要 . 本研究基于植 被 功 能 性 状 的 新 一 代 动 态 全 球 植 被 模 式 CLM5-FATES（Community Land Model version 5-Functionally AssembledTerrestrial Ecosystem Simulator），选 取 25 ℃ 时 最 大 羧 化 速 率 、比 叶 面 积 和 叶 寿 命 三 个 叶 片 特 性 参 数 ，对 长 白 山 针 阔混交林分布进行模拟，探讨模式中长白山针阔混交林分布的参数敏感性，检验模式对长白山针阔混交林分布的模 拟 能 力 . 研 究 表 明，不 同 的 性 状 参 数 组 合 显 著 影 响 该 地 区 两 种 植 被 类 型 分 布 的 模 拟 结 果，且 25 ℃时 最 大 羧 化 速率和比叶面积的影响大于叶寿命 . 适当的性状参数组合下，模式能再现观测结果中的长白山针阔混交林分布 . 本研究验证了该模式在长白山针阔混交林的适用性，可为进一步的气候植被相互作用研究提供重要支持 .

关键词：性状；动态全球植被模型；常绿针叶林；落叶阔叶林；气候学；生态系统.

中图分类号：P46

文章编号：1000-2383(2025)09-3357-12 收稿日期：2024-12-25

# Simulation of Mixed Needleleaf and Broadleaf Forest Distribution in Changbai Mountain of China Using CLM5⁃FATES Model

Sui Yue1，2 ， Yang Chuanyu1

1. School of Environmental Studies， China University of Geosciences （Wuhan）， Wuhan 430078， China  
2. CMA⁃CUG Center for Severe Weather and Climate and Hydro⁃Geological Hazards， Wuhan 430078， China

Abstract: The broadleaved Korean pine forest in Changbai Mountain is one of the few large-area primary mixed needleleaf and broadleaf forest in the world, so it is particularly necessary to conduct simulation research on it. This study is based on the new generation dynamic vegetation model CLM5-FATES (Community Land Model version 5-Functionally Assembled Terrestrial Ecosystem Simulator), by selecting the maximum carboxylation rate at 25 ℃, specific leaf area, and leaf longevity to simulate the distribution of mixed needleleaf and broadleaf forest in Changbai Mountain. This paper explores the parameter sensitivity of the distribution of mixed needleleaf and broadleaf forest in the model, and investigates the model’s ability to simulate the distribution of these forests. The study finds that different combinations of trait parameters significantly affect the distribution of vegetation types in the region. The maximum carboxylation rate at 25 ℃ and specific leaf area have a greater impact compared to leaf longevity. Under an appropriate combination of trait parameters, the model can reproduce the observed distribution of mixed needleleaf and broadleaf forest in Changbai Mountain. This study validates the applicability of the model to the mixed needleleaf and broadleaf forest in Changbai Mountain, providing crucial support for further research on climate-vegetation interactions.

Key words: traits; dynamic global vegetation model; evergreen needleleaf forest; deciduous broadleaf forest; climatology;   
ecosystems.

# 0 引 言

植 被 作 为 陆 地 生 物 圈 的 主 体，与 大 气 之 间 存在 着 复 杂 的 相 互 作 用（Bonan，2008）. 一 方 面 ，从植物个体的生长发育到植被的地理分布和演变，均 受 到 气 候 要 素 及 气 候 变 迁 的 显 著 影 响（Piao etal.，2019）. 另一方面，植被通过生物地球物理过程 和 生 物 地 球 化 学 过 程，调 节 着 陆 地 与 大 气 之 间的能量和物质交换，进而对气候系统产生重要影响（赵东升等，2023；Sui et al.，2025）. 因此，深入研究植 被 与 大 气 的 相 互 作 用 具 有 重 要 的 科 学 意 义 .

长白山阔叶红松林作为我国东北地区的地带 性 顶 极 群 落，是 全 球 为 数 不 多 的 大 面 积 原 始 针阔 混 交 林，具 有 独 特 的 建 群 种 和 丰 富 的 物 种 多 样性，在 全 球 生 物 多 样 性 保 护、国 家 碳 汇 及 全 球 碳循 环 中 占 据 重 要 地 位（郝 占 庆 等 ，2008）. 其 群 落 结构演替不仅受到气候等环境因素的影响，还与植被自身 的 特 性 密 切 相 关 .而 数 值 模 拟 是 研 究 植 被 与大 气 相 互 作 用 以 及 植 被 群 落 演 替 的 重 要 手 段 .

从早期的生物地理模型、生物物理模型、生物地球化学模型，到现今的动态全球植被模型（Dynamic Global Vegetation Models， 简 称DGVMs），这些模型在适用性和模拟能力上均取得了显著进展（谢馨瑶等，2018；李新等，2021）.DGVMs不仅整合了生物地球物理学、水文过程、生 物 地 球 化 学 循 环 、植 被 动 态 ，还 考 虑 了 自 然 干扰和人类活动等主要过程（彭书时等，2020）. 目前，DGVMs已成为陆面模式的重要组成部分，可与 地 球 系 统 模 式 中 的 其 他 模 块（如 大 气 、海 洋 等子 模 块）耦 合 ，被 广 泛 应 用 于 模 拟 不 同 时 空 尺 度的 植 被 分 布，以 及 估 算 陆 地 碳 水 通 量 和 土 地 利 用变 化 对 其 的 影 响 等（张 仲 石 等 ，2022；李 思 其 等 ，2024）. 然 而，将 DGVM 的 发 展 与 长 白 山 针 阔 叶 混交 林 群 落 结 构 演 替 联 系 起 来 的 研 究 还 相 对 不 足 .

当前一代的DGVMs仍缺失植物演替和群落组织 这 些 生 态 学 中 的 核 心 过 程（Bonan et al.，2024）.通常，DGVMs 采用每种植物功能型（plant function‐al type，简称PFT）在每个气候网格单元中的单一区域平均代表植物群落.这种简化虽然提高了模型的计 算 效 率，使 其 在 地 球 系 统 模 式 中 得 以 广 泛 应 用，但也存在显著局限（Argles et al.，2022）. 例如，这些功能型的特征参数（多为性状）固定，且竞争模拟基于植物功能型而非个体.这种假设忽略了植被个体之间的差异及其效应，严重影响了模型对生态系统结构和功能的模拟精度，导致模拟结果的不确定 性较 大（Bonan and Doney，2018；鲍 艳 等 ，2023；王丹 云 等 ，2024）. 这 种 植 物 功 能 型 框 架 已 成 为DGVMs 发 展 的 主 要 障 碍（杨 延 征 等 ，2018）.

因 此，亟 需 探 索 新 的 方 法 以 克 服 这 些 局 限 性 .当前，许多模型团队正在开发适用于地球系统模拟的新一代植被群落动态模型，以期捕捉这些更精细的生态过程（Fisher et al.，2018；Argles et al.，2022；Bonan et al.，2024）. 新一代植被群落动态模型提供了对植被斑块动态的尺寸和年龄结构化表示，包括冠 层 中 垂 直 方 向 的 光 竞 争、尺 寸 依 赖 的 生 长、分 配和 死 亡 率 、竞 争 以 及 干 扰 后 的 补 充（Fisher et al.，2018）.这类模型建立在生态系统动态计算框架的基础 上，允 许 在 地 球 系 统 模 式 中 进 行 高 效 计 算，可 以模拟植物尺寸（由相同尺寸和功能类型的植物群体表 示）和 自 干 扰 以 来 的 年 龄（由 一 个 或 多 个 群 体 的斑 块 表 示）. 模 型 中 不 同 的 植 物 功 能 型 由 与 植 物 生理、对干扰的响应等其他生活史特征相关的性状定义 . 例 如 ，Fisher et al.（2015） 在 通 用 陆 面 模 式CLM4.5（Community Land Model version 4.5）中 发展 了 基 于 植 物 功 能 性 状 的 植 被 模 块（EcosystemDemography，简 称 ED），预 测 了 美 国 东 部 生 物 群 系的分布.功能性状不仅能反映植物对环境变化的响应，还与生态系统的结构和功能密切相关，因此能显著提升当前DGVMs对生态系统过程的模拟和功能预测能力（杨延征等，2018；夏建阳等，2020；刘聪聪等，2024）.然而，目前的研究大多集中在站点或区域 尺 度，特 别 是 北 美 洲 和 热 带 地 区，而 对 中 国 区 域以及针阔混交林的关注则不足（Fisher et al.，2018；Massoud et al.，2019 ；Koven et al.，2020 ；Chenget al.，2022 ；Liu et al.，2024 ；Shi et al.，2024）.

目 前，通 用 陆 面 模 式 最 新 版 本 为 CLM5（Com‐munity Land Model version 5），并 且 嵌 入 了 更 新 的ED 模块，即新一代动态全球植被模型 FATES（Functionally Assembled Terrestrial Ecosystem Sim ‐ulator）（Lawrence et al.，2019）. 因此，本研究利用最新的CLM5‐FATES模式对中国长白山针阔混交林的分布进行模拟.阔叶红松林是温带针阔混交林的典型代表，也是第四纪冰川期后保存完好的原始裸子植物群落.其主要分布在我国东北三省的东部山区及俄罗斯远东、朝鲜、日本部分地区 . 以长白山针阔混交林为研究对象，检验 CLM5‐FATES对温带针阔混交林分布的模拟能力.这不仅对基于植被性状的新一代 DGVMs 的发展具有重要意义，也对未 来 气 候 与 植 被 相 互 作 用 的 研 究 具 有 重 要 价 值 .

在 长 白 山 针 阔 叶 混 交 林 中，常 绿 针 叶 树 和 落叶 阔 叶 树 是 主 要 的 组 成 部 分，它 们 在 叶 片 构 造 策略上存在明显差异 .通常，相比于常绿树，落叶树的叶片更薄，即叶片比叶重（单位面积叶片碳含量）更 小 或 叶 片 比 叶 面 积（specific leaf area ，SLA）更大；阔叶树种的 SLA 大于针叶树种（刘可佳等，2022）. 落 叶 树 的 叶 片 仅 在 一 年 中 尚 未 脱 落 的 时期 内 进 行 光 合 作 用，而 常 绿 树 的 叶 片 可 全 年 持 续存 在 . 另 外，单 位 面 积 叶 氮 含 量 和 生 产 力 也 随 叶片 厚 度 变 化 ，因 此 ，单 位 面 积 叶 氮 含 量 与 比 叶 重及 叶 寿 命 有 关 . 虽 然 树 种 死 亡 率 、碳 分 配 等 参 数也会影响植被的模拟，但叶氮含量、比叶重和叶寿命这三个叶片参数是现有数据库中被量化较好的叶片性状参数，能够合理定义不同的叶片构造策略（Fisher et al.，2015）. 因 此 ，本 文 将 基 于 叶 氮 含量、比叶重和叶寿命这三个性状参数，探讨 CLM5‐FATES 对 长 白 山 针 阔 叶 混 交 林 分 布 的 模 拟 .

# 1 数据和方法

# 1.1 研究区域

本研究关注的区域是长白山国家级自然保护区，其位于我国吉林省东南部，地理位置为 41°41'N\~42°25'N，127°42'E\~128°16'E（朱琪等，2019）. 长白山阔叶红松林是原始森林干扰后自然演替的顶级群落，是长白山地区代表性植被类型，分布面积广（韩士杰，2012）.本研究的关键点位选在长白山阔叶红松林永久样地（郝占庆等，2008）.该样地位于长白山国家级自 然 保 护 区 北 部 ，经 度 范 围 为 128° 05'41''E\~128°05'46''E，纬度范围为 42°24'10''N\~42°24'12''N. 该样地综合观测场于1998年建立，海拔784 m，观测场面积为40 m×40 m.乔木层优势种5种，即针叶树种红松（Pinus koraiensis）以及阔叶树种水曲柳（Fraxi⁃nus mandshurica）、紫 椴（Tilia amurensis）、蒙 古 栎（Quercus mongolica）和 五 角 枫（Acer pictum）（韩 士杰 ，2012）. 动 物 活 动 主 要 为 小 型 啮 齿 类 和 鸟 类 ，偶见大型兽类脚印；人类活动轻度，无任何采伐 .

# 1.2 观测数据

为了验证 CLM5‐FATES 模式在长白山阔叶红松林永久样地的针阔混交林的参数敏感性，笔者使用了《2003-2008 年吉林长白山站植物群落 种 类 组 成 与 物 质 生 产 观 测 数 据 》（http ：//www.nesdc.org.cn/sdo/detail？id=5fec0992042ebb03d9e6e68a）中 2005 年 阔 叶 红 松 林 综 合 观 测 场 乔木 层 植 物 种 组 成 数 据（韩 士 杰，2012）.

为了评估 CLM5‐FATES 模式对长白山地区针阔混交林的模拟效果，使用了中山大学全球变化与陆地生态系统模型研究团队的中国土地利用覆盖和 变 化 数 据 集（http：//www. nesdc. org. cn/sdo/de‐tail？id=6455d00e7e28173b252d9965）. 该 数 据 集 包含了1980年至2021年逐年的中国全境土地利用覆盖和变化资料，空间分辨率为10 km.本文使用了该数据集中 1991 年至 2010 年长白山地区常绿针叶林和落叶阔叶林两种植被类型的空间分布（即植 被 类 型 的 面 积 占 格 点 总 面 积 的 百 分 比 ）.

# 1.3 模式介绍

通 用 陆 面 模 式 CLM 是 目 前 国 际 上 应 用 广 泛、发 展 较 为 完 善 的 陆 面 模 式 之 一（Dai et al.，2003）.CLM5是 CLM 的最新版本，是通用地球系统模式CESM2（Community Earth System Model version 2）的默认陆面模式（http：//www.cesm.ucar.edu/mod‐els/cesm2/）（Lawrence et al.， 2019）. CLM5 在CLM4.5的基础上显著改进了土壤和植物的水文、雪、河流、碳氮循环及其耦合等，并增加了臭氧对植物的损害、与大气耦合的火灾排放气体的模拟以及本文使用的可以模拟植被种群动态的全球植被模型 FATES 等 可 选 模 块 . 关 于 CLM5 的 详 细 描 述 可参 考 CLM5 的 技 术 手 册（http：//www. cesm. ucar.edu/models/cesm2/land/CLM50_Tech_Note.pdf）.

FATES是一个植被竞争与共存的种群动态植被模型.该模型结构的具体特征包括：（1）灵活的植物功能型参数化，（2）从生态系统种群概念推导出的 植 物 种 群 统 计 和 演 替 表 示，（3）基 于 完 美 可 塑 性近 似（perfect plasticity approximation ，简 称 PPA）

表 1 25 ℃时最大羧化速率（Vc,max,25）、比叶面积（SLA）和叶寿命（L）l 三个属性的参数组合  
Table 1 Parameter combinations for the maximum carboxylation rate at 25 ℃ ( Vc, max, 25 ), specific leaf area (SLA) and leaf longevity ( L l )   

<table><tr><td rowspan="2">参数组合序号</td><td colspan="2">25℃时最大羧化速率（Vc,max,25） (μmolCO2 m-2.s-1)</td><td colspan="2">比叶面积(SLA) (m2·g·C-1)</td><td colspan="2">叶寿命(L) （年）</td></tr><tr><td>常绿针叶</td><td>落叶阔叶</td><td>常绿针叶</td><td>落叶阔叶</td><td>常绿针叶</td><td>落叶阔叶</td></tr><tr><td>0</td><td>65</td><td>58</td><td>0.010</td><td>0.030</td><td>4.000 0</td><td>1.000 0</td></tr><tr><td>1</td><td>84</td><td>68</td><td>0.002</td><td>0.010</td><td>2.062 6</td><td>0.3258</td></tr><tr><td>2</td><td>44</td><td>74</td><td>0.004</td><td>0.008</td><td>2.382 4</td><td>0.535 7</td></tr><tr><td>3</td><td>34</td><td>42</td><td>0.006</td><td>0.014</td><td>0.758 5</td><td>0.642 7</td></tr><tr><td>4</td><td>49</td><td>47</td><td>0.003</td><td>0.017</td><td>4.115 5</td><td>0.149 8</td></tr><tr><td>5</td><td>71</td><td>69</td><td>0.003</td><td>0.010</td><td>1.367 8</td><td>0.424 1</td></tr><tr><td>6</td><td>47</td><td>61</td><td>0.006</td><td>0.021</td><td>3.170 4</td><td>0.299 4</td></tr><tr><td>7</td><td>108</td><td>49</td><td>0.002</td><td>0.017</td><td>1.967 1</td><td>0.2019</td></tr><tr><td>8</td><td>65</td><td>97</td><td>0.003</td><td>0.006</td><td>2.202 5</td><td>0.303 5</td></tr><tr><td>9</td><td>101</td><td>58</td><td>0.003</td><td>0.021</td><td>5.384 2</td><td>0.322 2</td></tr><tr><td>10</td><td>47</td><td>79</td><td>0.004</td><td>0.010</td><td>1.640 3</td><td>0.395 2</td></tr><tr><td>11</td><td>17</td><td>38</td><td>0.006</td><td>0.024</td><td>3.993 2</td><td>0.266 6</td></tr><tr><td>12</td><td>87</td><td>79</td><td>0.003</td><td>0.010</td><td>2.7613</td><td>0.538 4</td></tr><tr><td>13</td><td>80</td><td>32</td><td>0.002</td><td>0.013</td><td>3.824 9</td><td>0.458 6</td></tr><tr><td>14</td><td>1</td><td>42</td><td>0.004</td><td>0.018</td><td>1.469 7</td><td>0.321 4</td></tr><tr><td>15</td><td>103</td><td>43</td><td>0.002</td><td>0.016</td><td>0.683 9</td><td>0.2761</td></tr></table>

注：参数组合序号 0 为 CLM5-FATES 模式原始参数，1\~15 依据 Fisher et al.（2015）的参数计算得到 .

模型的植物自组织冠层，（4）在较高的时间分辨率（即半小时）和垂直分辨率下处理冠层过程，以及（5）在同一垂直光谱中表示多种不同的植物 类 型 的 能 力（Fisher et al.，2015 ；Lawrence etal.，2019）. 这使得 FATES 可以直接通过植物生理 特 征 的 竞 争 交 互 作 用 预 测 生 物 群 系 ，并 且 包括了可选的火模块、模块化的异速生长和分配方 案 、交 互 式 伐 木 以 及 植 物 水 动 力 学 过 程（Law‐rence et al.，2019）.FATES 的 快 速 时 间 尺 度 生 理过 程 基 于 CLM5，但 对 高 度 结 构 化 和 多 PFT 冠 层进行了解析 .代码库的开放源代码开发和应用正在 进 行 中（https ：//github.com/NGEET/fates）.

# 1.4 性状参数

本 文 重 点 关 注 的 是 温 带 地 区 常 绿 针 叶 树和 落 叶 阔 叶 树 的 叶 片 构 造 策 略 问 题 . 基 于GLOPNET（Global Plant Trait Network）全 球 叶性 状 数 据 库（Wright et al. ，2004），考 虑 了 比叶 重（M ）、单 位 面 积 叶 氮 含 量（N ）及 叶 寿命（L ）三 个 性 状 之 间 权 衡 的 方 向 和 保 真 度 ，根 据 物 候 习 性（即 常 绿 或 阔 叶），Fisher et al.（2015）构 建 了 常 绿 针 叶 林 和 落 叶 阔 叶 林 的三 维 协 方 差 矩 阵 ；然 后 使 用 多 变 量 正 态 分 布采 样 程 序（MATLAB 中 的 mvnrnd 函 数）采 样得 到 了 两 种 植 被 类 型 的 15 组 参 数 组 合 .

本文使用的常绿针叶林和落叶阔叶林的性状参数见表1.序号0代表CLM5‐FATES模式自带的Vc，max，25、SLA 和 Ll 三 个 属 性 参 数 组 合 . 序 号 1\~15则根据 Fisher et al（. 2015）采样的 M 、N 及 L 三个性状的15组参数组合计算得到.具体而言，考虑到常绿针叶林和落叶阔叶林的光合能力与N 的关系存 在 差 异 ，因 此 ，序 号 1\~15 的 Vc，max，25 由 Narea 根 据公 式（1）和（2）计 算 得 到（Kattge et al.，2009），公 式中 N 的 单 位 为 g/m2 ，V ， ， 的 单 位 为μmol CO 2 m-2 ⋅ s -1 ；SLA 由 M a 的 倒 数 计 算 得 到 . L l则直接使用 Fisher et al.（2015）采样的参数数据 .

落叶阔叶林：Vc，max，25 = 33.79Narea，常绿针叶林：Vc，max，25 = 20.72Narea.

# 1.5 试验设计

在本研究中，CLM5‐FATES模式的模拟首先设定在中国东北长白山阔叶红松林永久样地中心（42° 24'11'' N、128° 05'44'' E），网格大小为 0.1° × 0.1°.气象驱动数据采用全球土壤湿度计划强迫数据集

表 2 仅用表 1 的第 6 组或第 9 组中的 Vc,max,25、SLA 或 Ll参数替换 CLM5⁃FATES 原始参数的参数组合  
able 2 Parameter combinations replacing the original parameters of CLM5-FATES with Vc, max, 25, SLA or Ll from Set 6 or Set 9 in Table 1   

<table><tr><td rowspan="2">参数组合序号</td><td colspan="2">Vc, max,25(μmol CO2 m−2.s-1)</td><td colspan="2">SLA(m2·g·C-1)</td><td colspan="2">L(年）</td></tr><tr><td>常绿针叶</td><td>落叶阔叶</td><td>常绿针叶</td><td>落叶阔叶</td><td>常绿针叶</td><td>落叶阔叶</td></tr><tr><td>0</td><td>65</td><td>58</td><td>0.010</td><td>0.030</td><td>4.000 0</td><td>1.000 0</td></tr><tr><td>6</td><td>47</td><td>61</td><td>0.006</td><td>0.021</td><td>3.170 4</td><td>0.299 4</td></tr><tr><td>61</td><td>47</td><td>61</td><td>0.010</td><td>0.030</td><td>4.000 0</td><td>1.000 0</td></tr><tr><td>62</td><td>65</td><td>58</td><td>0.006</td><td>0.021</td><td>4.000 0</td><td>1.000 0</td></tr><tr><td>63</td><td>65</td><td>58</td><td>0.010</td><td>0.030</td><td>3.170 4</td><td>0.299 4</td></tr><tr><td>9</td><td>101</td><td>58</td><td>0.003</td><td>0.021</td><td>5.384 2</td><td>0.322 2</td></tr><tr><td>91</td><td>101</td><td>58</td><td>0.010</td><td>0.030</td><td>4.000 0</td><td>1.000 0</td></tr><tr><td>92</td><td>65</td><td>58</td><td>0.003</td><td>0.021</td><td>4.000 0</td><td>1.000 0</td></tr><tr><td>93</td><td>65</td><td>58</td><td>0.010</td><td>0.030</td><td>5.384 2</td><td>0.322 2</td></tr></table>

GSWP3v1（Global Soil Wetness Project phase 3version 1）的 1991 年 至 2010 年 的 气 象 数 据（https：//doi.org/10.20783/DIAS.501），并 在 模 拟中 进 行 循 环 .CO 浓 度 设 定 为 367.0×10-6 . 由 于FATES 目 前 尚 未 考 虑 营 养 限 制 ，因 此 不 模 拟 氮循环过程 . 暂不考虑火灾干扰，因此火灾组件被关 闭 . 每 组 试 验 均 从 裸 土 开 始 初 始 化 ，均 匀 播 种相 同 数 量 的 常 绿 针 叶 树 和 落 叶 阔 叶 树 的 种 子 .基于表 1 中的 16 组参数，测试长白山阔叶红松林永久样地的针阔混交林对模式参数值的依赖性 .因此，仅运行模式直到植被分布趋于稳定，即 40年 .

其 次 ，为 了 进 一 步 对 比 V ， ， 、SLA 和 L这 三 个 参 数 对 长 白 山 针 阔 混 交 林 分 布 的 影响 ，基 于 模 式 自 带 参 数 ，分 别 只 使 用 表 1 中 第6 组 或 第 9 组 参 数 中 的 一 组 参 数 进 行 替 换 ，然后 进 行 40 年 的 模 拟 . 具 体 参 数 见 表 2. 选 择 第6 组 和 第 9 组 参 数 进 行 替 换 的 原 因 主 要 是 这两 组 参 数 下 模 式 能 够 再 现 该 地 区 针 阔 混 交 林的 分 布 ，且 阔 叶 林 数 量 多 于 针 叶 林（具 体 请 参考 结 果 分 析 中 的 2.1 小 节）.

目 前 ，长 白 山 地 区 的 林 龄 多 在 60\~100 年（Cheng et al.，2024）. 因 此 ，与 上 述 试 验 设 计 相同，但 仅 将 上 述 16 个 参 数 中 在 长 白 山 阔 叶 红 松林 永 久 样 地 模 拟 较 好 的 参 数 组 合 应 用 于 长 白 山地 区，进 行 100 年 的 模 拟 . 模 拟 的 长 白 山 地 区 以42°N、128°E 为中心，网格范围为 1° × 1°，分辨率为 0.1° × 0.1°. 驱动数据除了使用上述 GSWP3v1，还 使 用 了 CRUNCEPv7（Climatic Research Unit

National Centers for Environmental Prediction ver‐sion 7）中 1991 年 至 2010 年 的 气 象 数 据（Viovy ，2018）. 这 两 套 气 象 驱 动 数 据 是 陆 面 模 式 的 常 用强迫数据资料（彭静漫等，2020）.

# 2 结果分析

# 2.1 长白山阔叶红松林永久样地的针阔混交林分布对CLM5⁃FATES模式参数的依赖性

图 1为基于表 1中 0\~15组参数 CLM5‐FATES模式模拟的 40年中国东北长白山阔叶红松林永久样 地 的 常 绿 针 叶 林 和 落 叶 阔 叶 林 每 平 方 米 个 体 数量的逐月变化.根据长白山阔叶红松林永久样地观测场内的观测结果，2005 年红松（常绿针叶树）每平方米0.016株，其他落叶阔叶树（紫椴、水曲柳等）每平方米 0.152株 .模拟结果显示，第 1、3、4、13、14和15组试验下，40年后长白山阔叶红松林永久样地不存 在 这 两 种 植 被 类 型（图 1b、1d\~1e 和 1n\~1p）. 第2、5、8和10组试验下，40年后长白山阔叶红松林永久样地仅存在少量常绿针叶林，每平方米个体数量为 0.002\~0.020 株（图 1c、1f、1i 和 1k）. 第 12 组 试 验下，40年后也仅为常绿针叶林，每平方米为0.647株（图1m）.第11组试验下，40年后长白山阔叶红松林永久样地仅存在落叶阔叶林，每平方米个体数量为0.350株（图 1l）.第 0、6、7和 9组试验下模拟范围内在第40年时仍为针阔混交林，其中常绿针叶林分别为每平方米 0.471 株、0.016 株、0.027 株和 0.071 株，落叶阔叶林分别为每平方米 0.001 株、0.530 株、

![](images/190877e0d4b90137459f09adbbce2a7d80c9b26e5261d0eb6c0dfac395b1dfad.jpg)  
图1　基于表1中0\~15组参数，GSWP3v1驱动CLM5-FATES模拟的40年中国东北长白山阔叶红松林永久样地的常绿针叶林和落叶阔叶林每平方米个体数量的逐月变化（单位：株/m2）  
Fig.1 Monthly variations in the number of individuals per square meter of evergreen needleleaf and deciduous broadleaf forests at the permanent sample plot of the broadleaved Korean pine forest in Northeast China’s Changbai Mountain over 40 years, simulated by CLM5-FATES driven by GSWP3v1, based on parameter sets 0 to 15 from Table 1 (units: individuals/m2 )

0.020 株 和 0.528 株（图 1a 、1g\~1h 和 1j）. 第 0 组和 第 7 组 下，虽 然 长 白 山 阔 叶 红 松 林 永 久 样 地也 是 针 阔 混 交 林，但 两 组 试 验 结 果 中 阔 叶 林 模拟偏少 . 第 6 组和第 9 组能够再现该地区针阔混交林的分布，且阔叶林数量多于针叶林 .

为 了 进 一 步 比 较 Vc，max，25 、SLA 和 Ll 三 个 属性参数对长白山阔叶红松林永久样地针阔混交林分布的影响，相对于 CLM5‐FATES 模式原始参数，笔者仅使用表 1 中第 6 组或第 9 组的一组参数进行替换，具体参数组合见表 2，40 年的模拟 结 果 见 图 2. 选 择 第 6 组 和 第 9 组 参 数 的 原 因主 要 是 这 两 组 参 数 下 模 式 能 够 再 现 该 地 区 针阔混交林的分布，且阔叶林数量多于针叶林 .

首先，63 试验使用了第 6 组常绿针叶林和落叶阔叶林的叶寿命参数 3.170 4 年和 0.299 4 年，替 换 原 始 参 数 4.000 0 年 和 1.000 0 年 .93 试 验 则使用了第 9 组常绿针叶林和落叶阔叶林的叶寿命 参 数 5.384 2 年 和 0.322 2 年 替 换 原 始 参 数 . 对 比第 0组试验，63和 93试验下两种植被类型每平方米 个 体 数 量 随 时 间 的 演 变 特 征 与 第 0 组 试 验 的 结果 大 体 一 致（图 2a、2d 和 2g），即 叶 寿 命 对 两 种 植被 类 型 分 布 的 影 响 弱 于 其 他 两 个 参 数（图 2）.

其次来看25 ℃时最大羧化速率对两种植被类型分布的影响.相对于第0组试验，61和91试验分别使用常绿针叶林和落叶阔叶林的第6组25 ℃时最大羧化速率参数 47 μmol CO m-2 ⋅ s -1 和 61 μmol CO m-2 ⋅ s -1以 及 第 9 组 25 ℃ 时 最 大 羧 化 速 率 参 数101 μmol CO m-2 ⋅ s-1 和 58 μmol CO m-2 ⋅ s-1 替 换原始参数 65 μmol CO2 m-2 ⋅ s -1 和 58 μmol CO2 m-2 ⋅s-1.相比于第0组试验，61试验下常绿针叶林25 ℃时最

![](images/e292410aa81d1246d3329cdf3810d510132b8e42f39ee1a0cc1acddd22e7d451.jpg)  
图2 GSWP3v1驱动CLM5-FATES模拟的40年中国东北长白山阔叶红松林永久样地的常绿针叶林和落叶阔叶林每平方米个体数量的逐月变化（单位：株/m2）  
Fig.2 Monthly variations in the number of individuals per square meter of evergreen needleleaf and deciduous broadleaf forests at a permanent sample plot of the broadleaved Korean pine forest in Northeast China’s Changbai Mountain over 40 years, simulated by CLM5-FATES driven by GSWP3v1 (units: individuals/m2 )

a. 表 1 中 第 0 组 参 数 组 合 ； b. 第 6 组 的 V c，max，25 替 换 原 始 参 数 ；c. 第 6 组 的 SLA 替 换 原 始 参 数 ；d. 第 6 组 的 L l 替 换 原 始 参 数 ；e. 第 9组 的 V 替 换 原 始 参 数；f. 第 9 组 的 SLA 替 换 原 始 参 数；g. 第 9 组 的 L 替 换 原 始 参 数

大羧化速率减弱，落叶阔叶林 25 ℃时最大羧化速率略有增强 .这使得相比于 0试验，61试验下常绿针叶林在演替初期的光合能力弱，进而竞争能力弱，有利于落叶阔叶林生长（图 2a 和 2b）. 类 似地 ，相 比 于 第 0 组 试 验 ，91 试 验 下 常 绿 针 叶 林25 ℃时最大羧化速率增强，光合能力强，更 早地 显 现 出 更 强 的 竞 争 能 力（图 2a 和 2e）.

然后，笔者探讨了比叶面积对两种植被类型分布的影响 .相对于第 0组试验，62和 92试验分别使用常绿针叶林和落叶阔叶林的第6组比叶面积参数0.006 m2 ⋅ g ⋅ C-1 和 0.021 m2 ⋅ g ⋅ C-1 以及第 9 组比叶面 积 参 数 0.003 m 2 ⋅ g ⋅ C-1 和 0.021 m 2 ⋅ g ⋅ C-1 替 换原 始 参 数 0.01 m 2 ⋅ g ⋅ C-1 和 0.03 m 2 ⋅ g ⋅ C-1 . 0、62 和

92试验下常绿针叶林的比叶面积逐渐减小，即同样的光合能力下叶片单位面积碳含量越来越高，使得演替初期常绿针叶林的竞争力越来越弱（图 2a、2c和 2f）.

总体上，在长白山阔叶红松林永久样地的两种植被类型演替初期，25 ℃时最大羧化速率和比叶面积两个参数的作用强于叶寿命 .演替初期，通常光合能力越弱、比叶面积越小，其竞争能力越弱.类似地，表 1 中第 1、7、13、15 组参数试验下，拥有最小比叶面积（0.002 m2 ⋅ g ⋅ C-1）的常绿针叶林均不能很好生 长（图 1b、1h、1n 和 1p）. 即 使 25 ℃ 时 最 大 羧 化 速率最大的第 7组试验下，常绿针叶林也只能少量生长（图1h）.第3、11、14组试验下，虽然常绿针叶林的比叶面积略大（0.004\~0.006 m2 ⋅ g ⋅ C-1），但其 25 ℃时最大羧化速率较小（1\~34 μmol CO m-2 ⋅ s-1），也使其不能很好生长（图1d、1l和1o）.同样地，在常绿针叶林比叶面积小于 0.010 m2 ⋅g⋅C-1 的情况下，落叶 阔 叶 林 仅 在 比 叶 面 积 达 到 0.021 m2 ⋅ g ⋅ C-1 的 第6、9和11组试验下才能生长（图1g、1j和1l）.

![](images/0a641a3537dceb92e467cbc5f912a56c6a6eb17739f158f514496b99d78247d2.jpg)  
图 　基于第 （）、（ ）、（）、（ ）和 （）组参数，使用 和 驱动 - 模式在长白山阔叶红松林永久样地模拟100年的常绿针叶林和落叶阔叶林的逐年变化（单位：株/m2）  
Fig.3 Yearly variations in the number of individuals of evergreen needleleaf and deciduous broadleaf forests at the permanent sam ‐ ple plot of broadleaved Korean pine forest in Changbai Mountain over 100 years, simulated by the CLM5-FATES model driven by GSWP3v1 and CRUNCEPv7, based on the parameters from Set 0 (a), 6 (b), 7 (c), 9 (d), and 11 (e) in Table 1 (units: individuals/m 2 )

# 2.2 CLM5⁃FATES模式对长白山地区针阔混交林分布的模拟

观测结果中，长白山阔叶红松林永久样地2005年落叶阔叶林数量（0.152株 /m2）多于常绿针叶林（0.016株 /m2）.然而，上述试验中，仅第 0、6、7、9和11组参数下长白山阔叶红松林永久样地在第40年时仍存在落叶阔叶林.因此，基于这5组参数，使用

GSWP3v1 和 CRUNCEPv7 驱动 CLM5‐FATES 模式在长白山阔叶红松林永久样地继续模拟至100年（图3）.首先，5组参数下，模拟前期（第1\~25年）长白 山 阔 叶 红 松 林 永 久 样 地 两 种 植 被 类 型 的 个 体 数量 变 化 较 大；模 拟 中 后 期（第 25\~100 年 间）两 种 植被类型的个体数量变化趋势不明显，以年际和年代际 波 动 为 主（图 3）. 其 次，同 种 参 数 下，两 种 气 象 驱动 数 据 下 模 拟 的 两 种 植 被 类 型 分 布 的 变 化 趋 势 大致相同，但存在年际和年代际差异（图3）.例如，第0组 参 数 下 ，使 用 GSWP3v1 和 CRUNCEPv7 驱 动CLM5‐FATES 模拟的长白山阔叶红松林永久样地两种植被类型的演变趋势基本一致，在模拟的最后蓝色区域为长白山国家级自然保护区

![](images/91b6d6d976fb5a23ed76c0cc68bda8f8fe3a00f9b7bf70ecf50be36722fd58c9.jpg)  
图4　基于观测资料1991年至2010年平均的长白山地区的常绿针叶林（ENF）和落叶阔叶林（DBF）面积百分比（单位：%）（a）.第 0、6、7、9 和 11 组参数下，使用 GSWP3v1（b\~f）和 CRUNCEPv7（g\~k）驱动 CLM5-FATES 模式模拟的长白山地区第81\~100年平均的常绿针叶林和落叶阔叶林的空间分布（单位：株/m2）  
Fig.4 Percentage of forest area (a) covered by evergreen needleleaf forest (ENF) and deciduous broadleaf forest (DBF) in the Changbai Mountain region based on observation averaged over the period from 1991 to 2010 (units: %). The simulated spa‐ tial distribution of evergreen needleleaf forests and deciduous broadleaf forests in the Changbai Mountain region averaged over years 81 to 100, using CLM5-FATES model driven by GSWP3v1 (b‒f) and CRUNCEPv7 (g‒k) based on parame‐ ters from Set 0, 6, 7, 9, and 11 (units: individuals/m2 )

20年都仅为常绿针叶林，每平方米分别为 0.554株和 0.631 株（图 3a）. 第 11 组 参 数 下，使 用 GSWP3v1和 CRUNCEPv7驱动模式模拟的长白山阔叶红松林永久样地两种植被类型的演变趋势也类似，最后都仅存落叶阔叶林；但两种驱动数据下落叶阔叶林数量有差别，最后 20年每平方米分别为 0.379株和0.580 株（图 3e）. 第 6 组 和 第 7 组 参 数 下 ，使 用GSWP3v1 和 CRUNCEPv7 驱动模式模拟的长白山阔 叶 红 松 林 永 久 样 地 在 模 拟 后 期 以 落 叶 阔 叶 林 为主，常绿针叶林较少；且第6组参数下的落叶阔叶林多于第7组参数下的结果（图3b和3c）.另外，第7组参数下，相比于 GSWP3v1，CRUNCEPv7 驱动下的落叶阔叶林数量变化幅度更大（图 3c）. 第 9 组参数下，使 用 GSWP3v1 和 CRUNCEPv7 驱 动 模 式 模 拟的长白山阔叶红松林永久样地均为针阔混交林，在最后20年落叶阔叶林分别为每平米0.571株和0.562株 ，常 绿 针 叶 林 分 别 为 每 平 方 米 0.129 株 和 0.130株（图 3d）.总的来说，长白山阔叶红松林永久样地的 两 种 植 被 类 型 分 布 的 模 拟 主 要 取 决 于 性 状 参 数的影响，同时也受不同气象驱动数据的调节（图3）.

基 于 第 0、6、7、9 和 11 组 参 数 ，使 用 GSWP3v1和 CRUNCEPv7 驱 动 CLM5‐FATES 对 长 白 山 地区的针阔混交林进行 100 年的模拟，最后 20 年的常绿针叶林和落叶阔叶林的空间分布见图 4.

观测资料显示，1991 年 至 2010 年长白山地区、长白山以南和以东的地区主要以常绿针叶林为主；长白山以北和以西的地区以落叶阔叶林为主（图4a）.基于 CLM5‐FATES原始参数下的模拟显示，长白山及周边地区在模拟的第81\~100年仅为常绿针叶林（图 4b 和 4g）. 第 7 组 参 数 下 CLM5‐FATES模 拟 显 示，模 拟 的 第 81\~100 年 仅 落 叶 阔 叶 林 分 布在 长 白 山 西 北 部 和 长 白 山 以 西 的 地 区（图 4d 和4i）.第 11 组参数下 CLM5‐FATES 模拟显示，模拟的 第 81\~100 年 落 叶 阔 叶 林 分 布 在 长 白 山 及 其 周边 地 区（图 4f和 4k）.第 6组 参 数 下，常 绿 针 叶 林 主要分布在长白山南部及其以南地区，其他地区主要 以 落 叶 阔 叶 林 为 主（图 4c 和 4h）. 对 比 来 看 ，第 9组 参 数 下 模 拟 的 长 白 山 地 区 两 种 植 被 类 型 的 分 布与 观 测 资 料 最 接 近，即 长 白 山 及 其 以 东 和 以 南 的地区以常绿针叶林为主，长白山以西和以北的地区 以 落 叶 阔 叶 林 为 主（图 4e 和 4j）. 总 的 来 说 ，CLM5‐FATES 模式对长白山及其周边地区的两种 植 被 类 型 分 布 的 模 拟 也 主 要 取 决 于 性 状 参 数的影响，同时受不同气象驱动数据的调节（图 4）.

# 3 讨论与结论

基于全球叶性状数据库所定义的参数空间，笔者首先探讨了CLM5‐FATES模式中长白山针阔混交林分布对25 ℃时最大羧化速率、比叶面积和叶寿命三个叶片特性参数的敏感性，然后从植物生理特性及其竞争相互作用中模拟长白山针阔混交林的分布.

（1）CLM5‐FATES 模 式 模 拟 长 白 山 阔 叶 红松林分布时，不同的性状参数组合显著影响两种植被类型分布的模拟结果，且 25 ℃时最大羧化速率和比叶面积对植被分布的影响大于叶寿命 .

（2）第 0、6、7、9组参数下在第 40年时能再现长 白 山 阔 叶 红 松 林 永 久 样 地 的 针 阔 混 交 分 布，但仅第 6 组和第 9 组参数下能够模拟出与观测一致的 混 交 分 布 ，即 落 叶 阔 叶 林 数 量 多 于 常 绿 针 叶林 .100 年 的 模 拟 下 ，仅 第 9 组 参 数 下 能 再 现 长 白山 阔 叶 红 松 林 永 久 样 地 的 针 阔 混 交 林 分 布 .

（3）区 域 上，与 观 测 资 料 一 致，第 9 组 参 数下 CLM5‐FATES 模 式 能 再 现 长 白 山 地 区 针 阔混 交 林 的 空 间 分 布 特 征 ：长 白 山 及 其 以 东 和以 南 的 地 区 以 常 绿 针 叶 林 为 主 ，长 白 山 以 西和以北的地区以落叶阔叶林为主 .

根据刘可佳等（2022）的调查，中国东北部温带红松针阔叶混交林的落叶林或阔叶林的比叶面积约 0.025 m2 ⋅ g ⋅ C-1 ，常绿林或针叶林的比叶面积约为 0.006\~0.007 m2 ⋅ g ⋅ C-1 . 本研究中模拟较好的第6 组和第 9 组的常绿针叶林的比叶面积分别为0.006 m 2 ⋅ g ⋅ C-1 和 0.003 m 2 ⋅ g ⋅ C-1 ，落 叶 阔 叶 林 的比叶面积都为 0.021 m2 ⋅ g ⋅ C-1 . 这与刘可佳等（2022）在中国温带森林的比叶面积调查结果类似 .CLM5‐FATES中默认的常绿针叶林和落叶阔叶林比叶面积分别为 0.01 m2 ⋅ g ⋅ C-1 和 0.03 m2 ⋅ g ⋅ C-1 ；这比刘可佳等（2022）研究中的两种植被类型的比叶面积大.第6组和第9组参数下常绿针叶林25 ℃最大羧化效率分别为47 μmol CO m-2 ⋅ s-1 和 101 μmol CO m-2 ⋅ s-1 ，与CLM5‐FATES模式默认值（61 μmol CO m-2 ⋅s-1）和Aboelyazeed et al.（2023） 机 器 学 习 方 法 的 估 值（61 μmol CO m-2 ⋅ s -1）差异大 . 第 6 组和第 9 组参数下 落 叶 阔 叶 林 25 ℃ 最 大 羧 化 效 率 分 别 为61 μmol CO m-2 ⋅ s-1 和 58 μmol CO m-2 ⋅ s-1 ，这 与CLM5 ‐ FATES 模式默认的 58 μmol CO m-2 ⋅ s -1 相近，但大于机器学习方法的估值（45 μmol CO m-2 ⋅ s -1）（Aboelyazeed et al.，2023）.另外，虽然第 9 组参数组合下，CLM5‐FATES 能够再现类似观测的针阔混交林分布特征，但模式模拟的两种植被类型单位面积的个体数量与观测仍有差异 .CLM5‐FATES 模式中，影响该地区针阔混交林分布模拟的参数较多 . 未来应 该 对 这 些 参 数 进 行 敏 感 性 分 析，并 优 化 关 键参数，提升对该地区针阔混交林分布的模拟能力 .

总的来说，本研究通过不同性状参数组合的 模 拟 ，验 证 了 CLM5‐FATES 模 式 对 长 白 山地 区 针 阔 混 交 林 分 布 的 模 拟 能 力 .CLM5‐FATES 对 长 白 山 针 阔 混 交 林 分 布 的 模 拟 主 要受 不 同 性 状 参 数 的 影 响 ，并 受 气 象 驱 动 要 素 的调 节 . 本 研 究 通 过 模 拟 验 证 了 CLM5‐FATES模 式 在 长 白 山 地 区 的 适 用 性 ，为 进 一 步 的 气 候和植被相互作用研究提供了重要的科学支持 .

致 谢 ：长 白 山 阔 叶 红 松 林 观 测 数 据 源 自 国家 科 技 基 础 条 件 平 台 ‒ 国 家 生 态 科 学 数 据 中 心（http ：//www.nesdc.org.cn）！

# References

Aboelyazeed, D., Xu, C. G., Hoffman, F. M., et al., 2023. A Differentiable, Physics ‐ Informed Ecosystem Model‐ ing and Learning Framework for Large ‐ Scale Inverse Problems: Demonstration with Photosynthesis Simula‐ tions. Biogeosciences, 20(13): 2671-2692. https://doi. org/10.5194/bg‐20‐2671‐2023   
Argles, A. P. K., Moore, J. R., Cox, P. M., 2022. Dynam ‐ ic Global Vegetation Models: Searching for the Balance between Demographic Process Representation and Com ‐ putational Tractability. PLOS Climate, 1(9): e0000068. https://doi.org/10.1371/journal.pclm.0000068   
Bao, Y., Wang, Y. Q., Nan, S. L., et al., 2023. Evaluation of Vegetation Characteristics over Qinghai ‐ Xizang Pla‐ teau Simulated by a Vegetation Dynamic Model. Pla⁃ teau Meteorology, 42(2): 333-343 (in Chinese with English abstract).   
Bonan, G. B., 2008. Forests and Climate Change: Forcings, Feedbacks, and the Climate Benefits of Forests. Sci⁃ ence, 320(5882): 1444-1449. https://doi.org/10.1126/ science.1155121   
Bonan, G. B., Doney, S. C., 2018. Climate, Ecosystems, and Planetary Futures: The Challenge to Predict Life in Earth System Models. Science, 359(6375): eaam8328. https://doi.org/10.1126/science.aam8328   
Bonan, G. B., Lucier, O., Coen, D. R., et al., 2024. Rei‐ magining Earth in the Earth System. Journal of Advanc⁃ es in Modeling Earth Systems, 16(8): e2023MS004017. https://doi.org/10.1029/2023MS004017   
Cheng, K., Chen, Y. L., Xiang, T. Y., et al., 2024. A 2020 Forest Age Map for China with 30 m Resolution. Earth System Science Data, 16(2): 803-819. https:// doi.org/10.5194/essd‐16‐803‐2024   
Cheng, Y. Y., Leung, L. R., Huang, M. Y., et al., 2022. Modeling the Joint Effects of Vegetation Characteristics and Soil Properties on Ecosystem Dynamics in a Panama Tropical Forest. Journal of Advances in Modeling Earth Systems, 14(1): e2021MS002603. https://doi. org/10.1029/2021MS002603   
Dai, Y. J., Zeng, X. B., Dickinson, R. E., et al., 2003. The Common Land Model. Bulletin of the American Meteo⁃ rological Society, 84(8): 1013-1024. https://doi. org/ 10.1175/bams‐84‐8‐1013   
Fisher, R. A., Koven, C. D., Anderegg, W. R. L., et al., 2018. Vegetation Demographics in Earth System Models: A Review of Progress and Priorities. Global Change Biol⁃ ogy, 24(1): 35-54. https://doi.org/10.1111/gcb.13910   
Fisher, R. A., Muszala, S., Verteinstein, M., et al., 2015. Taking off the Training Wheels: The Properties of a Dy‐ namic Vegetation Model without Climate Envelopes, CLM4.5(ED). Geoscientific Model Development, 8(11): 3593-3619. https://doi.org/10.5194/gmd‐8‐3593‐2015   
Han, S. J., 2012. China Ecosystem Location Observation and Research Dataset, Forest Ecosystem Volume: Changbaishan Station from 2001 to 2008, Jilin. China Agriculture Press, Beijing (in Chinese).   
Hao, Z. Q., Li, B. H., Zhang, J., et al., 2008. Broad ‐ Leaved Korean Pine (Pinus Koraiensis) Mixed Forest Plot in Changbaishan (CBS) of China: Community Com ‐ position and Structure. Journal of Plant Ecology, 32(2): 238-250 (in Chinese with English abstract).   
Kattge, J., Knorr, W., Raddatz, T., et al., 2009. Quantify‐ ing Photosynthetic Capacity and Its Relationship to Leaf Nitrogen Content for Global‐Scale Terrestrial Biosphere Models. Global Change Biology, 15(4): 976-991. https://doi.org/10.1111/j.1365‐2486.2008.01744.x   
Koven, C. D., Knox, R. G., Fisher, R. A., et al., 2020. Benchmarking and Parameter Sensitivity of Physiologi‐ cal and Vegetation Dynamics Using the Functionally As‐ sembled Terrestrial Ecosystem Simulator (FATES) at Barro Colorado Island, Panama. Biogeosciences, 17(11): 3017−3044. https://doi.org/10.5194/bg‐17‐3017‐2020   
Lawrence, D. M., Fisher, R. A., Koven, C. D., et al., 2019. The Community Land Model Version 5: Descrip‐ tion of New Features, Benchmarking, and Impact of Forcing Uncertainty. Journal of Advances in Modeling Earth Systems, 11(12): 4245-4287. https://doi. org/ 10.1029/2018MS001583   
Li, S. Q., Zhang, X., Lu, Z. Y., et al., 2024. Progress of Vegetation Modelling and Future Research Prospects. Science China Earth Sciences, 54(9): 2762-2782 (in Chinese).   
Li, X., Ma, H. Q., Ran, Y. H., et al., 2021. Terrestrial Carbon Cycle Model ‐ Data Fusion: Progress and Chal‐ lenges. Science China Earth Sciences, 51(10): 1650- 1663 (in Chinese).   
Liu, C. C., He, N. P., Li, Y., et al., 2024. Current and Fu‐ ture Trends of Plant Functional Traits in Macro ‐ Ecolo‐ gy. Chinese Journal of Plant Ecology, 48(1): 21-40 (in Chinese with English abstract).   
Liu, K. J., He, N. P., Hou, J. H., 2022. Spatial Patterns and Influencing Factors of Specific Leaf Area in Typical Temperate Forests. Acta Ecologica Sinica, 42(3): 872- 883 (in Chinese with English abstract).   
Liu, Y. L., Holm, J. A., Koven, C. D., et al., 2024. Large Divergence of Projected High Latitude Vegetation Com ‐ position and Productivity Due to Functional Trait Uncer‐ tainty. Earth ’s Future, 12(8): e2024EF004563. https:// doi.org/10.1029/2024EF004563   
Massoud, E. C., Xu, C. G., Fisher, R. A., et al., 2019. Identification of Key Parameters Controlling Demographi‐ cally Structured Vegetation Dynamics in a Land Surface Model: CLM4.5(FATES). Geoscientific Model Develop⁃ ment, 12(9): 4133-4164. https://doi.org/10.5194/gmd‐ 12‐4133‐2019   
Peng, J. M., Liu, S. F., Dai, Y. J., et al., 2020. Evaluation of Common Land Model Based on International Land Model Benchmarking System. Climatic and Environ⁃ mental Research, 25(6): 649-666 (in Chinese with English abstract).   
Peng, S. S., Yue, C., Chang, J. F., 2020. Developments and Applications of Terrestrial Biosphere Model. Chinese Journal of Plant Ecology, 44(4): 436-448 (in Chinese with English abstract).   
Piao, S. L., Liu, Q., Chen, A. P., et al., 2019. Plant Phe‐ nology and Global Climate Change: Current Progresses and Challenges. Global Change Biology, 25(6): 1922- 1940. https://doi.org/10.1111/gcb.14619   
Shi, M. J., Keller, M., Bomfim, B., et al., 2024. Functional‐ ly Assembled Terrestrial Ecosystem Simulator (FATES) for Hurricane Disturbance and Recovery. Journal of Ad⁃ vances in Modeling Earth Systems, 16(1): e2023MS0036 79. https://doi.org/10.1029/2023MS003679   
Sui, Y., Wei, M., Liu, B., 2025. Biophysical Impacts of Glob‐ al Deforestation on Near‐Surface Air Temperature in Chi‐ na: Results from Land Use Model Intercomparison Project Simulations. Advances in Atmospheric Sciences, 42(6): 1141-1155. https://doi.org/10.1007/s00376‐024‐4149‐z   
Viovy, N., 2018. CRUNCEP Version 7— Atmospheric Forcing Data for the Community Land Model. Research data Archive at the National Center for Atmospheric Re‐ search, Computational and Information Systems Labora‐ tory, Boulder, CO. https://doi.org/10.5065/PZ8F‐F017   
Wang, D. Y., Zeng, X. D., Song, X., 2024. Evaluation of CMIP6 Models in Simulating the Sensitivity of Leaf Ar‐ ea Index to Temperature and Precipitation Changes over China. Chinese Journal of Atmospheric Sciences, 48(5): 1961−1977 (in Chinese with English abstract).   
Wright, I. J., Reich, P. B., Westoby, M., et al., 2004. The Worldwide Leaf Economics Spectrum. Nature, 428 (6985): 821-827. https://doi.org/10.1038/nature02403   
Xia, J. Y., Lu, R. L., Zhu, C., et al., 2020. Response and Adaptation of Terrestrial Ecosystem Processes to Cli‐ mate Warming. Chinese Journal of Plant Ecology, 44 (5): 494-514 (in Chinese with English abstract).   
Xie, X. Y., Li, A. N., Jin, H. A., 2018. The Simulation Models of the Forest Carbon Cycle on a Large Scale: A Review. Acta Ecologica Sinica, 38(1): 41-54 (in Chinese with English abstract).   
Yang, Y. Z., Wang, H., Zhu, Q. A., et al., 2018. Research Progresses in Improving Dynamic Global Vegetation Models (DGVMS) with Plant Functional Traits. Chinese Science Bulletin, 63(25): 2599-2611 (in Chinese with English abstract).   
Zhang, Z. S., Li, S. L., Wang, H. J., et al., 2022. Introduc‐ tion of Crossing Disciplines between Geology and Atmo‐ spheric Science. Earth Science, 47(10): 3569-3579 (in Chinese with English abstract).   
Zhao, D. S., Wang, K., Cui, Y. P., 2023. Feedback Mecha‐ nisms and Regulatory Effects of Vegetation Change on Climate. Acta Ecologica Sinica, 43(19): 7830− 7840 (in Chinese with English abstract).   
Zhu, Q., Zhou, W. M., Jia, X., et al., 2019. Ecological Vulnerability Assessment on Changbai Mountain Nation‐

al Nature Reserve and Its Surrounding Areas, Northeast China. Chinese Journal of Applied Ecology, 30(5): 1633-1641 (in Chinese with English abstract).

# 中文参考文献

鲍艳, 王玉琦, 南素兰, 等, 2023. 动态植被模型对青藏高原植被的模拟检验 . 高原气象, 42(2): 333-343.  
韩士杰, 2012. 中国生态系统定位观测与研究数据集, 森林生 态 系 统 卷 : 吉 林 长 白 山 站（2001-2008）. 北 京 : 中 国农业出版社.  
郝占庆, 李步杭, 张健, 等, 2008. 长白山阔叶红松林样地(CBS): 群 落 组 成 与 结 构 . 植 物 生 态 学 报 , 32(2):238-250.  
李思其, 张旭, 陆正遥, 等, 2024. 植被模型研究进展与展望 . 中国科学: 地球科学, 54(9): 2762-2782.  
李新, 马瀚青, 冉有华, 等, 2021. 陆地碳循环模型‒数据融合 : 前 沿 与 挑 战 . 中 国 科 学 : 地 球 科 学 , 51(10):1650-1663.  
刘聪聪, 何念鹏, 李颖, 等, 2024. 宏观生态学中的植物功能性状研究: 历史与发展趋势 . 植物生态学报, 48(1):21-40.  
刘可佳, 何念鹏, 侯继华, 2022. 中国温带典型森林植物比叶 面 积 的 空 间 格 局 及 其 影 响 因 素 . 生 态 学 报 , 42(3):872-883.  
彭静漫, 刘少锋, 戴永久, 等, 2020. 基于陆面模式基准平台ILAMB 对 陆 面 模 式 CoLM 的 评 估 . 气 候 与 环 境 研 究,25(6): 649-666.  
彭书时, 岳超, 常锦峰, 2020. 陆地生物圈模型的发展与应用 . 植物生态学报, 44(4): 436-448.  
王丹云, 曾晓东, 宋翔, 2024. CMIP6模式关于中国叶面积指数对温度和降水变化敏感性的模拟能力评估 . 大气科学, 48(5): 1961−1977.  
夏建阳, 鲁芮伶, 朱辰, 等, 2020. 陆地生态系统过程对气候变暖的响应与适应 . 植物生态学报, 44(5): 494-514.  
谢馨瑶, 李爱农, 靳华安, 2018. 大尺度森林碳循环过程模拟模型综述 . 生态学报, 38(1): 41-54.  
杨延征, 王焓, 朱求安, 等, 2018. 植物功能性状对动态全球植 被 模 型 改 进 研 究 进 展 . 科 学 通 报 , 63(25):2599-2611.  
张仲石, 李双林, 王会军, 等, 2022. 浅谈大气科学与地质学的学科交叉 . 地球科学, 47(10): 3569-3579.  
赵东升, 王珂, 崔耀平, 2023. 植被变化对气候的反馈机制及调节效应 . 生态学报, 43(19): 7830−7840.  
朱琪, 周旺明, 贾翔, 等, 2019. 长白山国家自然保护区及其周 边 地 区 生 态 脆 弱 性 评 估 . 应 用 生 态 学 报 , 30(5):1633-1641.