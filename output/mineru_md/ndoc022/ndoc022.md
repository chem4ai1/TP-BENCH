# 延河流域生态环境质量遥感测评模型改进及其精度分析

王 丽 霞 1 ，张 信 伟 1 ，赵 蕊 1，2 ，张 晶 2 ，刘 招 3

（ 长安大学地质工程与测绘学院，西安 ； 中科星图空间技术有限公司，西安 ； 长安大学水利与环境学院，西安 710054）

摘要：生态环境是人类赖以生存和发展的基础，建立准确和高效的测评模型，对评价生态环境的稳定性和安全性具有重要的现实意义 基于遥感生态指数（ ），运用移动窗口法和熵值法建立了基于区域尺度的遥感生态环境质量指数（ - ）和改进遥感生态指数（M-RSEI），并以延河流域为例，对比分析了模型的优化效果 . 结果表明：①基于 RSEI模型，引入移动窗口法构建的- 模型，可以有效解决区域性差异问题，但无法实现批量化生产； 基于 - 模型，运用熵值法构建改进型 -模型，可以显著提高生态环境质量的测评精度，特别是指数高值区和低值区的拟合效果良好；并且可以有效解决批量监测的问题；③2000\~2020年延河流域的生态环境质量整体逐渐改善，但综合等级以“中等”为主，且空间分布上东南部优于西北部，修复重心逐渐向西北方向迁移. 模型对比结果表明，M-RSEI模型在流域或区域空间尺度上对生态环境质量的监测具有更好的评价精 度 .

关键词：生态环境质量；改进遥感生态指数（ - ）；区域尺度的遥感生态环境质量指数（ - ）；精度分析；延河流域中图分类号： X87 文献标识码： A 文章编号：0250-3301（2025）11-7186-11 DOI：10.13227/j.hjkx.202409271

# Improvement and Accuracy Analysis of Remote Sensing Evaluation Model for Yanhe River Basin Ecological Environment Quality

WANG Li-xia1 ，ZHANG Xin-wei1 ，ZHAO Rui1，2 ，ZHANG Jing2 ，LIU Zhao3（1. School of Geological Engineering and Geomatics， Chang'an University， Xi'an 710054， China； 2. Geovis Spatial Technology Co.， Ltd.， Xi'an 710005， China； 3. School of Waterand Environment， Chang'an University， Xi'an 710054， China）

Abstract：The ecological environment serves as the foundation for human survival and development， making the establishment of accurate and efficient evaluation models vital for assessing its stability and security. Based on the remote sensing ecological index （RSEI）， this study employs the moving window and entropy weight methods to develop the regional optimized remote sensing ecological index （RO-RSEI） and the modified remote sensing ecological index （M-RSEI）. Using the Yanhe River Basin as a case study， the optimization effects of the models are comparatively analyzed. The results indicate that： ① The RO-RSEI model， constructed by incorporating the moving window method into the RSEI framework， effectively addressed regional disparities but was limited in its capacity for large-scale application. ② Building upon the RO-RSEI model， the M-RSEI model， developed using the entropy weight method， significantly enhanced the evaluation accuracy of ecological environment quality， particularly in areas with high and low index values. It also enabled efficient large-scale monitoring. ③ From 2000 to 2020， the overall ecological environment quality of the Yanhe River Basin improved gradually， with most areas classified as “moderate.” Spatially， the southeastern region exhibited better quality than the northwestern region， with the focus of ecological restoration shifting progressively northwestward. Comparative analysis demonstrated that the M-RSEI model offered superior precision for monitoring ecological environment quality at basin or regional spatial scales.

Key words：ecological environment quality； modified remote sensing ecological index （M-RSEI）； regional optimized remote sensing ecological index （RO-RSEI）；accuracyanalysis； Yanhe River Basin

生态环境是人类生存、生产与生活的基本条件，是关系到社会和经济持续发展的复合生态系统［1，2］ .近几十年来，受人类活动和气候变化影响，生态系统退化、水土流失和草地退化等问题逐渐加剧，逐渐威胁到区域生态安全 . 伴随科技进步和经济快速发展，人们对生态质量的关注不断提升，因此，采用合理高效的生态环境质量评价方法，实现对区域生态状况快速、准确的监测是十分有必要的.

早期的生态环境质量评价方法主要包括压力-状态-响应模型［3］ 、人工神经网络［4］ 和生态足迹分析［5］等. 然而，以上方法受到主观因素的影响较大，且所依赖的数据多为统计数据，获取难度较高. 随着遥感（RS）和地理信息系统（GIS）技术的不断进步，部分学者分别利用植被指数［6］ 、标准化降水蒸散发指数［7］ 、地表温度指数［8］ 和土地适宜性指数［9］ 等单一指数评估生态环境质量，但单一指数仅能反映某一因素对生态环境的影响，而生态环境是受多重因素影响的复杂系统，因此，用单一指数对整体的生态环境进行评价缺乏真实性与客观性 . 近几年，生态环境评价指标 体 系 应 用 较 为 广 泛 的 是 生 态 环 境 状 况 指 数（ecological index， EI）［10］ 、生 态 环 境 质 量 指 数（environmental quality index， EQI）［11］ 和 徐 涵 秋 提 出 的遥 感 生 态 指 数（remote sensing ecological index，RSEI）［12］ . EI指数和EQI指数虽已被广泛应用，但存在数据难以获取、指标权重固定、无法逐像元分析等不足，而相比之下，RSEI不仅克服了以上不足，能够量化生态环境状况，还支持对区域生态环境的变化进行空间分析 .

自 模型提出以来，我国学者对该指数进行了大量的研究和应用. 例如，李光哲等［13］ 利用RSEI模型，对长株潭城市群的生态环境质量进行了评估；张云霞等［14］ 利用 RSEI 模型，分析了青藏高原 2000\~2020年生态质量时空变化 . 然而，在不断的尝试应用中，学者们也发现了 模型的一些不足，例如，朱冬雨等［15］ 和张亚球等［16］ 均提出，RSEI 对整个研究区进行生态环境质量计算时，未考虑自然情况下生态环境的影响具有区域性，使得评价结果缺乏生态学意义，因此他们在RSEI模型中引入了景观学中的移动窗口法，以此对模型进行改进 . 此外，RSEI 模型由于 4 项指标的特征向量方向存在差异，采用主成分分析方法所计算的结果需要根据实际情况判断是否需要进行反转，这使得RSEI模型的结果具有随机性，无法应用于批量化生产［17，18］ . 并且仅选取第一主成分构建RSEI模型无法保证较高贡献度，容易造成信息部分丢失，导致研究区生态环境质量被低估或高估［19，20］移动窗口法用来解决较远生态系统间相互影响的问题. 熵值法可以克服人为权重无法避免的随机性和臆断性问题，消除多指标变量间信息冗余［17］ . 因此，本研究在移动窗口法的基础上，用熵值法替换主成分分析法 ，构建了改进的遥感生态指数（modifiedremote sensing ecological index， M-RSEI），使 准 确 、批量评估区域生态环境质量成为可能.

延河流域位于陕北黄土丘陵沟壑区，其水土流失和土壤侵蚀等生态问题十分突出［21］ . 目前对延河流域生态环境状况的综合评价缺乏具有时效性的对比研究 . 鉴于此，本研究基于 2000 年、2005 年、2010年、2015 年和 2020 年共 5 期遥感影像，运用移动窗口法和熵值法建立了结合区域尺度优化的生态环境质量 遥 感 评 价 指 数（regional optimized remote sensingecological index， RO-RSEI）和 改 进 的 遥 感 生 态 指 数（M-RSEI），对延河流域的生态环境质量进行时空变化分析，探索准确和高效的多尺度动态监测方法 .

# 1　材料与方法

# 1.1　研究区域概况

延河发源于陕西省靖边县天赐湾乡周山（图1），是黄河的一级支流. 流域总面积7 725 km2，属于典型的大陆性季风气候区. 多年平均降水量为482 mm，年内降水分布不均，主要集中于夏季（6\~9 月）. 流域地处西北干旱半干旱地区，下垫面复杂，生态环境十分脆弱［21］ . 此外，近几十年在该地区实施了大量的水土工程，致使生态环境呈现修复与退化时空交叠的现状［22］ . 因此，构建高精度的生态环境质量评价模型，对于明确流域生态安全的时空格局和主导驱动因素，完善流域生态环境治理措施具有重要的理论和现实意义［23，24］ .

![](images/1216354f3853c7df6dc8f61c51a745b7486fa8b5ee9a990ae63fe6923d49e72a.jpg)  
图 1　研究区概况  
Fig. 1 Overview of the study area

# 1.2　数据来源

研究采用的数据源主要有影像数据和地理空间数据 . 其中遥感影像包括 Landsat TM 与 Landsat OLI，均来源于地理空间数据云（http：//www.gscloud.cn/）；数字高程模型（DEM）、土地利用数据和土壤类型等栅格数据，均来源于国家基础地理信息中心和中国科学院地球大数据科学工程数据共享服务系统（https：//data.casearth.cn/）；生态质量指数（EQI）数据源自国家科技基础条件平台-国家生态科学数据中心（http：//www.nesdc.org.cn）. 具体参数详见表 1.

表1　研究数据来源Table 1 Research data sources  

<table><tr><td>数据类型</td><td>数据来源</td><td>时间</td><td>空间分辨率/m</td></tr><tr><td rowspan="3">Landsat TM</td><td rowspan="3">地理空间数据云(http://www.gscloud.cn/)</td><td>2000年6月</td><td></td></tr><tr><td>2005年9月</td><td>30</td></tr><tr><td>2010年6月 2015年7月</td><td>30</td></tr><tr><td>Landsat OLI DEM</td><td>地理空间数据云(http://www.gscloud.cn/) 地理空间数据云(http://www.gscloud.cn/)</td><td>2020年8月 2009年</td><td>30</td></tr><tr><td>土地利用数据</td><td>国家基础地理信息中心和中国科学院地球大数据科学工程数据</td><td>2000年、2005年、2010年、2015年</td><td>30</td></tr><tr><td></td><td>共享服务系统(https://data.casearth.cn/) 国家基础地理信息中心和中国科学院地球大数据科学工程数据</td><td>和2020年</td><td></td></tr><tr><td>土壤类型数据 生态质量指数数据</td><td>共享服务系统(https://data.casearth.cn/) 国家科技基础条件平台-国家生态科学数据中心(http://www.</td><td>1995年 2000年、2005年、2010年、2015年</td><td>30 1000</td></tr></table>

# 1.3　数据处理

基于数字高程模型（ ）、土壤类型数据和土地利用数据，在 平台下运用水文分析模块提取流域边界，并利用投影变换和网格分析等方法实现多源数据融合；基于Landsat影像，在ENVI平台下进行辐射定标、大气校正、拼接裁剪等预处理，获得延河流域遥感影像；基于遥感影像，在ENVI平台中进行相关波段运算，计算RSEI模型所需的4项指标（ 、 、 和 ）

# 1.4　研究方法

# 1.4.1 RSEI 模型

RSEI 模型由干度（NDBSI）、湿 度（WET）、绿 度（ ）和热度（ ）等共 项指标构成 首先依据Landsat影像提取植被覆盖、湿度、土地退化和地表温度等图层信息，而后对各图层进行归一化处理，并通过主成分分析法，将以上信息耦合，进而逐像元计算流域生态环境质量指数［25］ . RSEI计算公式如下：

![](images/fee734d0f5e36b87af232238406c6af7d1de10b70d9f1874dd2751c109c41a47.jpg)

式中，PC1为将4项指标通过主成分转换集中到的第一主成分；式（1）为特征向量方向相反的主成分结果，即 和 特征值为负值， 和 为正值，进行正负值转置［17，26］ . 式（2）为对第一主成分结果进行归一化，RSEI 为第一主成分值，RSEI 和RSEI 分别为 RSEI 的最大和最小值［27］ . 式中的 4 项指标的计算公式如下.

# 1.4.1.1　干度获取

RSEI模型中的干度指标是用NDBSI来表示的，该指标是通过对建筑物指数（IBI）和裸土指数（SI）之和求均值得到的［28］ . 其计算公式如下 .

![](images/abeb53f54f95ccb1f97d38590a1cb7ef13e39548bad68255c6c5dda23815e80a.jpg)

![](images/ca944f526e3747549477a4ea38f597287ab2b6cebe607510e8eacdfacccb5501.jpg)

![](images/2f965e3975abc41af7b0027045a2c2785d70993eaae36837d016178818e43ef2.jpg)

式中，ρ（i=1、2、3、4、5、6）分别表示 Landsat5 TM 波段、、、、 的反射率和 波段 、、、、的反射率.

# 1.4.1.2　湿度获取

湿度选用的是Wet指数，该指数是通过缨帽变换所获得的，它不但可以反映水体湿度，还可以反映土壤以及植被的湿度，是一个能够很好反映生态环境湿度的指数［25，28］ . 其计算公式如下：

Wet ( TM) = 0.031 5ρ + 0.202 1ρ + 0.310 2 ρ +

![](images/db8a6038c8735b74a03712a1b2d3c4d6f1ce1b549165181070efba5fa30d5c76.jpg)

Wet (OLI) = 0.151 1ρ 1 + 0.197 3ρ 2 + 0.328 3ρ 3 +

![](images/10d93301dfffa77f6e35269c75ad76f6ea5f2a3b5b7920327a7b2426d4c2b9a2.jpg)

式中，ρ（i=1、2、3、4、5、6）分别表示 Landsat8 OLI 波段2、3、4、5、6、7的反射率.

# 1.4.1.3　绿度获取

绿度所反映的是研究区的植被覆盖情况，而归

一化植被指数（NDVI）能够很好的反映研究区的植被繁茂程度. 因此，选用NDVI代表绿度指标. 其计算公式如下：

![](images/a4a6310d5b67a043d28a15f18d86a1ef4d3f153a751499d78296d28a8b3778ce.jpg)

式中，RED 和 NIR 分别为红波段和近红外波段反射率 . 分别对应与 Landsat5 TM 的第 3、4 波段反射率和Landsat8 OLI 的第 4、5 波段反射率［29］ .

# 1.4.1.4　热度获取

热度指标通过地表温度来获取，本文将沿用大气校正法进行地表温度反演. 其计算公式如下：

![](images/3d0cb320dd7747d5da8eaa62a52e789ec409bfb3757dcd1edb70930c9cf2852e.jpg)

![](images/9dcb14f5f1564607adf2446a533db9c22e985fe0f8080fb29af46a16ee27c37f.jpg)

![](images/532e24d5ac0cb41580f433d660ae8621681ba0f3e9a904792d2576c4fc4e84f6.jpg)

式中，L 为Landsat热红外波段的辐射值，DN为原始的灰度值，gain和bias分别为波段增益值和偏置值，由传感器决定. T 为亮度温度，K1和K2为定标参数，在影像的元数据中记录 . γ 为 TM 影像第 6 波段的中心波长 11.5 µm 和 OLI 数据的第 10 波段中心波长 10.9µm，ρ 为常数 其值为 1.438×10−2 mK，ε 为比辐射率［30］ .

# 1.4.2　基于移动窗口的综合指标构建

在景观生态学和区域生态学领域，移动窗口法多用来解决较远生态系统间相互影响的问题，避免过远区域对目标区域的影响. 传统的RSEI模型未考虑区域尺度上各生态系统之间的相互作用，忽略了不同距离间隔对测评结果的影响，同时对整个研究区域进行主成分变换，一定程度会夸大像元的最值，致使估算结果存在偏差［15，18］ . 因此基于移动窗口法构建RO-RSEI模型，可以有效解决区域性差异问题.

原理如图2所示，以移动窗口为单元，一个像元为步长，将窗口遍历整幅图像，当窗口移动时，以窗口所覆盖的范围为评价区，采用主成分分析方法计算窗口区域的 RO-RSEI值 .

依据前人研究的成果［31，32］ ，本研究选择在流域边界外扩2 000 m作为评价单元窗口，即以每个像素为中心点向外扩展 4 000 m×4 000 m（133 px×133 px）的区域作为评价范围. 为了更好地分析生态环境的优劣，需要设定第一主成分的阈值，其中占比高的区域将具有更高的确信度.

![](images/47b83d4c53081d586ff708f5dc4396bbe17049b840170797d3f1b4928010c53d.jpg)  
图2　移动窗口法原理  
Fig. 2 Schematic of moving window method

# 1.4.3　基于熵值法的单窗口 M-RSEI计算

熵值法是一种综合评价方法，它通过计算各个指标的权重来反映评价体系中各指标所含的信息量. 在计算权重值之前，熵值法会对已归一化的指标进行非负处理，以确保所有计算出的权重值都是正数，从而避免结果产生不确定性［17］ . 为改善传统的RSEI模型使用主成分分析法所造成的指标信息丢失和不能批量生产问题，研究基于移动窗口和熵值法构建改进的生态环境质量评估模型（M-RSEI），计算公式如下：

![](images/76c162a07d126788e5aab46145edff2ed630333b45ece0fb88e25c7d2abe6358.jpg)

式中，M-RSEI为基于熵值法的遥感生态指数，NDVI、WET、NDBSI和LST分别为绿度指标、湿度指标、干度指标和地表温度［33］ . ωi为第i个指标的权重，可以利用4项指标的均值计算得到，具体公式如下：

![](images/8fdb280e38031f48f7c02719d139db29dcb11d575583e06fe013b230b9d70ae0.jpg)

![](images/25162645fa1fd2531a64c4ad08a2549d79e2c563fc485df1aea0ea1755764671.jpg)

![](images/5988f6de7ec4af52ee6342a4ae62fd4bdd5784f91fd3ad583c58dea6ba0ddf4f.jpg)

![](images/0a8d309b496712d5fca0947026fe1ae79738194e14cbdb219c8cbfe8eb46c66e.jpg)

![](images/7aeeae208d4edd22997c61640479da234126c92f7f2c3727068d76c9d5cd1962.jpg)

![](images/0dca29323e8f82f65625f9c96975ee27ff5587e250752c4921a6d2422402c3fb.jpg)

式中，H为第i个指标的熵，m为评价指标的数目，n为评价对象的数目，k=1/lnm［33］ ，NIij为第 j期的第 i 个指标的归一化值（j=1、2、3、4、5，分别对应 5个年份），I为某一像元值，I 和I 分别为最小值和最大值［17，34］ . 绿度和湿度对生态环境有正向作用，采用正向归一化公式［式（16）］计算；热度和干度对生态环境有负向作用，采用负向归一化公式［式（17）］计算［35，36］ .

# 2　结果与分析

# 2.1　测评模型改进

为探究改进方法对生态环境质量评价的精度影响，分别采用 RSEI、RO-RSEI 和 M-RSEI 模型对延河流域 2000 年、2005 年、2010 年、2015 年和 2020 年的生态环境质量进行测评和对比分析

结果如表 和表 所示 可以看出， 第一主成分的贡献率介于 71.84%\~88.49% 之间，RO-RSEI 的第一主成分贡献率介于 41.53%\~93.68% 之间，最大值和最小值相差较大. 结果表明，加入移动窗口法的改进模型会根据下垫面和各参数相关程度的不同，在进行主成分分析坐标轴旋转时，对冗余数据进行有效取舍，从而解决区域差异性问题［15，16］ ；仅选取第一主成分来替代4项指标所反映的信息，贡献率无法满足信息充分的要求，即计算结果反映的生态环境信息丰富程度不高，可能增加分区生态环境质量的评估误差 .

各年份生态因子贡献值统计（表 2）结果表明，模型在绿度、湿度、干度和热度贡献方向上存在随机性 . 例如 2000 年、2005 年、2015 年和 2020 年的绿度、湿度为正向贡献，干度、热度为负向贡献，而2010年则呈现反向贡献情况. 因此，要正确测评2010年生态环境质量，需要根据先验知识进行反转，这使得模型无法进行批量处理 而熵值法可以根据各指标对生态环境的作用情况设置归一化公式［式（16）和（17）］，使得各个指标所计算的权重均为正值，进而实现批量处理和生产 .

# 2.2　测评模型精度分析

# 2.2.1　测评精度时间差异分析

参考《生态评价技术规范》中的生态环境质量分级标准，将监测结果按照 0.2的间隔进行等级划分，得到很差（ ）、较差（ ）、中等（0.6）、良好（0.6\~0.8）和优良（0.8\~1）5 个等级 . 统计结果如表 4所示，可以看出，①RSEI模型的计算结果相比其他两模型普遍偏低，这是由于 RSEI 模型是以整个流域作为整体进行计算，未考虑流域内各生态区之间的影响，从而导致高低值计算存在偏差；②RO-RSEI 模 型 在 2005 年 、2015 年 和 2020 年 计 算结果普遍高于 RSEI模型低于 M-RSEI模型，在 2000年和 年两个生态环境质量较差的年份，计算结 果 高 于 RSEI 和 M-RSEI 模 型 ；③RSEI 和 M-RSEI均值变化趋势相符，整体呈上升趋势，仅在 2010年有小幅度下降，RO-RSEI 模型仅在 2005 年有所下降 . 其中 RSEI和 M-RSEI均值的变化趋势符合延安市政府所发布的延安市生态环境变化情况；④与其他两个模型相比，M-RSEI 模型的均值更接近于中国科学院所发布的 EQI 的均值，因此，从时间尺度来看， - 模型的测评精度优于 - 模型和 RSEI 模型 .

表2　测评年份RSEI模型各指标主成分分析 Table 2 Principal component analysis of RSEI model in each evaluation year   

<table><tr><td>年份</td><td>参数</td><td>PC1</td><td>PC2</td><td>PC3</td><td>PC4</td></tr><tr><td rowspan="6"></td><td>NDVI</td><td>0.6061</td><td>0.328 4</td><td>-0.247 1</td><td>0.6811</td></tr><tr><td>WET</td><td>0.462 4</td><td>-0.201 7</td><td>0.8633</td><td>-0.000 9</td></tr><tr><td>NDBSI</td><td>-0.561 8</td><td>-0.3088</td><td>0.229 6</td><td>0.732 2</td></tr><tr><td>LST</td><td>-0.3211</td><td>0.869 5</td><td>0.375 2</td><td>0.002 6</td></tr><tr><td>特征值</td><td>0.1151</td><td>0.0308</td><td>0.008 8</td><td>0.002 4</td></tr><tr><td>特征值贡献率/%</td><td>73.27</td><td>19.61</td><td>5.6</td><td>1.53</td></tr><tr><td rowspan="6">2005</td><td>NDVI</td><td>0.475 9</td><td>0.536 6</td><td>-0.2457</td><td>0.6521</td></tr><tr><td>WET</td><td>0.577 6</td><td>-0.390 3</td><td>0.6981</td><td>0.162 8</td></tr><tr><td>NDBSI</td><td>-0.497 4</td><td>-0.460 1</td><td>-0.0171</td><td>0.7352</td></tr><tr><td>LST</td><td>-0.438 6</td><td>0.5898</td><td>0.672 2</td><td>0.0881</td></tr><tr><td>特征值</td><td>0.1028</td><td>0.0274</td><td>0.0081</td><td>0.004 9</td></tr><tr><td>特征值贡献率/%</td><td>71.84</td><td>19.15</td><td>5.59</td><td>3.42</td></tr><tr><td rowspan="6"></td><td>NDVI</td><td>-0.574 5</td><td>-0.3031</td><td>-0.299 2</td><td>0.6988</td></tr><tr><td>WET</td><td>-0.470 2</td><td>0.0171</td><td>0.882 3</td><td>-0.001 3</td></tr><tr><td>NDBSI</td><td>0.580 3</td><td>0.244 6</td><td>0.305 5</td><td>0.7141</td></tr><tr><td>LST</td><td>0.334 6</td><td>-0.920 8</td><td>0.1961</td><td>-0.040 3</td></tr><tr><td>特征值</td><td>0.1522</td><td>0.018 9</td><td>0.008 2</td><td>0.002 8</td></tr><tr><td>特征值贡献率/%</td><td></td><td></td><td>4.54</td><td>1.58</td></tr><tr><td rowspan="6"></td><td>NDVI</td><td>83.48 0.5579</td><td>10.4 0.2928</td><td>0.6435</td><td>0.434 4</td></tr><tr><td>WET</td><td>0.479 3</td><td>-0.0938</td><td>-0.712 7</td><td>0.503 3</td></tr><tr><td>NDBSI</td><td>-0.605 7</td><td>-0.262 2</td><td>0.147 2</td><td>0.7365</td></tr><tr><td>LST</td><td>-0.3031</td><td>0.914 6</td><td>-0.236 9</td><td>0.123 7</td></tr><tr><td>特征值</td><td></td><td></td><td></td><td></td></tr><tr><td>特征值贡献率/%</td><td>0.1631</td><td>0.0142</td><td>0.005 3</td><td>0.0017</td></tr><tr><td rowspan="6"></td><td>NDVI</td><td>88.49 0.604 2</td><td>7.71 0.190 9</td><td>2.88</td><td>0.92 0.2655</td></tr><tr><td>WET</td><td></td><td></td><td>0.726 5</td><td>0.5578</td></tr><tr><td>NDBSI</td><td>0.513 -0.554 9</td><td>0.0691 -0.166 7</td><td>-0.648 7 0.218 4</td><td>0.7851</td></tr><tr><td>LST</td><td>-0.252 2</td><td>0.964 8</td><td>-0.059 5</td><td>0.0431</td></tr><tr><td>特征值</td><td>0.179 9</td><td>0.0305</td><td>0.0071</td><td>0.001 8</td></tr><tr><td>特征值贡献率/%</td><td>82.03</td><td>13.91</td><td>3.19</td><td>0.87</td></tr></table>

表3　各测评年份RO-RSEI模型第一主成分特征贡献率统计Table 3 Statistics of characteristic contribution rate of the firstprincipal component of RO-RSEI model in each evaluation year/%  

<table><tr><td>年份</td><td>最小值</td><td>最大值</td><td>均值</td></tr><tr><td>2000</td><td>44.43</td><td>86.86</td><td>73.40</td></tr><tr><td>2005</td><td>42.47</td><td>86.78</td><td>67.88</td></tr><tr><td>2010</td><td>44.72</td><td>93.68</td><td>78.20</td></tr><tr><td>2015</td><td>45.62</td><td>93.52</td><td>80.79</td></tr><tr><td>2020</td><td>41.53</td><td>89.39</td><td>73.58</td></tr></table>

此外，为了从长时间尺度上清晰的对比各个模型的计算结果，使用小提琴图和箱型图（如图3）对流域空间范围内生态环境的聚集情况进行可视化. 其中小提琴琴体在某范围内宽度越宽，表明位于该值范围内的区域越多 . 对比 RSEI、RO-RSEI和 M-RSEI 3个模型的统计结果，可以看出：①3个模型所反映出的延河流域生态环境质量情况相似，2000年生态环境质量指数集中于低值区，2005年集中于中值区，2015 年低值区分布减少，高值区分布增加，2020 年流域生态环境质量多分位于高值区； 生态指数分布形态从上窄下宽逐渐变化为上宽下窄，表明延河流域的生态环境质量逐渐优化的过程.

表 4 2000 年、2005 年、2010 年、2015 年和 2020 年不同模型计算均值统计  
Table 4 Statistics of calculated mean values of different models in， ， ， ，  

<table><tr><td>年份</td><td>项目</td><td>M-RSEI</td><td>RO-RSEI</td><td>RSEI</td><td>EQI</td></tr><tr><td rowspan="2">2000</td><td>均值</td><td>0.4817</td><td>0.503 5</td><td>0.446 5</td><td>0.521 4</td></tr><tr><td>环境等级</td><td>中等</td><td>中等</td><td>中等</td><td>中等</td></tr><tr><td rowspan="2">2005</td><td>均值</td><td>0.504 3</td><td>0.4768</td><td>0.497 3</td><td>0.533 2</td></tr><tr><td>环境等级</td><td>中等</td><td>中等</td><td>中等</td><td>中等</td></tr><tr><td rowspan="2">2010</td><td>均值</td><td>0.491 7</td><td>0.503 9</td><td>0.475 2</td><td>0.510 2</td></tr><tr><td>环境等级</td><td>中等</td><td>中等</td><td>中等</td><td>中等</td></tr><tr><td rowspan="2">2015</td><td>均值</td><td>0.537 2</td><td>0.5231</td><td>0.507 7</td><td>0.554 4</td></tr><tr><td>环境等级</td><td>中等</td><td>中等</td><td>中等</td><td>中等</td></tr><tr><td rowspan="2">2020</td><td>均值</td><td>0.608 3</td><td>0.591 6</td><td>0.597 4</td><td>0.633 2</td></tr><tr><td>环境等级</td><td>良好</td><td>中等</td><td>中等</td><td>良好</td></tr></table>

模 型 类 型 ：1.RSEI（2000 年），2.RO-RSEI（2000 年），3.M-RSEI（2000 年），4.RSEI（2005 年），5.RO-RSEI（2005 年），6.M-RSEI（2005 年），7.RSEI（2010 年），8.RO-RSEI（2010 年），9.M-RSEI（2010 年），10.RSEI（2015 年），11.RO-RSEI（2015 年），12.M-RSEI（2015 年），13.RSEI（2020 年），14.RO-RSEI（2020 年），15.M-RSEI（2020 年）

![](images/ce2168f52e67d61331c3ee1dbe11a95308b7fbbe4e9b33a10eeb664ca1466d69.jpg)  
图3　多模型长时间序列测评结果统计  
Fig. 3 Statistics of multi model long time series evaluation results

# 2.2.2　测评精度空间差异分析

图4为2010年延河流域在不同模型下的计算结果分布，可以看出，3 种模型计算结果的空间分布大致相同，主要差异出现在延河流域西北部、安塞县以及延河流域南部，在延河流域西北部，RSEI模型的计算结果明显低于其他两个模型，且在延河流域南部，RSEI模型的计算结果明显高于其他两个模型，这是因为仅选取第一主成分构建的 RSEI 模型，无法保证较高贡献度，容易造成信息部分丢失，导致研究区生态环境质量被低估或高估. 为了进一步对比模型的精度，将3个模型2010年计算结果与中国科学院所发布的EQI进行对比（如表5）. 可以看出，在极值变化较为明显的靖边县、志丹县以及安塞县， - 模型的均值与EQI均值最为接近，表明基于移动窗口法和熵值法相耦合的M-RSEI模型，可以较好地提升生态

表5 2010年延河流域各县（区）模型均值统计  
Table 5 Statistics of model mean values of counties （districts） in the Yanhe River Basin in 2010   

<table><tr><td>地区</td><td>M-RSEI</td><td>RORSEI</td><td>RSEI</td><td>EQI</td></tr><tr><td>靖边县</td><td>0.4688</td><td>0.4431</td><td>0.423 9</td><td>0.477 4</td></tr><tr><td>志丹县</td><td>0.473 4</td><td>0.4631</td><td>0.462 2</td><td>0.499 2</td></tr><tr><td>安塞县</td><td>0.502 4</td><td>0.497 9</td><td>0.472 1</td><td>0.538 9</td></tr><tr><td>宝塔区</td><td>0.5352</td><td>0.5368</td><td>0.5031</td><td>0.527 4</td></tr><tr><td>延长县</td><td>0.528 7</td><td>0.502 5</td><td>0.4863</td><td>0.508 3</td></tr></table>

![](images/6efe488b98fad3d36f2d1a7a563bd8b051da2a074f2dc35cf0d0858771edc47b.jpg)  
图4 2010年不同模型空间分布  
Fig. 4 Spatial distribution of different models in 2010

环境质量测评精度.

此外，在变化差异较小的宝塔区，勾画剖面线来得到具体数值，其剖面如图5. 可以看出，①RSEI波动幅度较大，在两个相邻区域会出现极大、极小值，这与物理学中的“扩散理论”不相符，因此该种现象不合理；②RO-RSEI模型也会存在两个相邻区域出现极大、极小值情况，但相比于RSEI模型，该现象明显有所改善，而M-RSEI模型的监测结果相比于其他两个模型，波动较为稳定，未出现相邻区域波动幅度较大现象. 表明移动窗口法和熵值法相结合对RSEI模型进行改进，可以提升生态环境质量高低值区域监测的准确性 .

为了进一步对比 RSEI、RO-RSEI和 M-RSEI模型监测结果在空间上的差异，以2015年为例，对各模型的等级面积、占比以及县（区）均值进行统计，结果如表6、表7和图6所示. 结果表明：①3个模型测评的生态环境质量空间分布相似，均表现为流域西北部和中部地区为“较差”等级，南部和东部下游地区为良好和优良等级 . 其中，RO-RSEI模型“很差”和“优良”等级占比相较于 RSEI 模型均有减少，表明移动窗口法的引入很好地改善了 模型对极值区监测结果的精度；②M-RSEI模型相比于RO-RSEI模型，在均值最小的靖边县和均值最大的宝塔区，数值上更接近于EQI的均值，表明熵值法相较于主成分分析法，具有更高的综合评价精度；③在延安市建设的新城区，M-RSEI模型的反演结果与原始影像的纹理结构拟合最好，说明M-RSEI模型在像元尺度上具有更好的空间表达精度，RO-RSEI模型次之，RSEI模型的监测结果明显偏低.

由此，基于 M-RSEI模型，反演了延河流域生态环境质量，其时空分布如图 7 所 示 . 结果表明：①2000\~2020年，延河流域生态环境质量整体得到了较好改善，“良好”和“优良”等级的面积占比不断增加，且生态环境质量重心逐步向流域西北部迁移，主要得益于流域生态修复和环境治理等措施的持续推进和实施. ②2000\~2010年，流域西北部生态环境质量下降，根据延安市生态管理局公告和许晓露［21］ 、董贞凯等［23］ 学者的研究，主要原因是该区域海拔高、地形起伏大、降雨频繁，土壤多为土质松散、软绵的黄绵土，存在严重的水土流失和土壤侵蚀问题. 之后，随着流域综合治理的实施，局地水土流失和土壤侵蚀问题有所改善；③2010\~2020年，生态环境质量显著提升 . 2015 年，流域中部地区出现生态环境质量断崖式下降，这是由于延安市政府为解决城镇化带来的建设用地紧张问题，于2012年实施了“削山造城”

![](images/f9e515925bdf94f12f18e880a6a71bf6df55301116b0d102bea42b69d59a7c62.jpg)  
图 5 2010 年 RSEI、RO-RSEI 和 M-RSEI 生态环境质量剖面  
Fig. 5 Ecological environment quality profile of RSEI， RO-RSEI， and M-RSEI in 2010

![](images/2b028a03b6c43e08152d8b92bd8e86064d1a1a782dc9af3a65551ab0e44228a3.jpg)  
图6　延河流域和流域内典型区域不同模型计算结果对比  
Fig. 6 Comparison of calculation results of different models in Yanhe River Basin and typical areas within the basin

表 6 RSEI、RO-RSEI和 M-RSEI 模型计算结果统计  
Table 6 Statistics of average calculation results of RSEI， RO-RSEI， and M-RSEI models   

<table><tr><td rowspan="2">等级</td><td colspan="2">RSEI</td><td colspan="2">RO-RSEI</td><td colspan="2">M-RSEI</td></tr><tr><td>面积 /km²</td><td>占比/%</td><td>面积 /km²</td><td>占比/%</td><td>面积 /km²</td><td>占比/%</td></tr><tr><td>很差</td><td>845.69</td><td>11.05</td><td>521.57</td><td>6.81</td><td>336.59</td><td>4.40</td></tr><tr><td>较差</td><td>1864.43</td><td>24.36</td><td>1842.45</td><td>24.07</td><td>1 775.30</td><td>23.19</td></tr><tr><td>中等</td><td>2 215.88</td><td>28.95</td><td>2 471.90</td><td>32.29</td><td>2 726.38</td><td>35.62</td></tr><tr><td>良好</td><td>1 677.43</td><td>21.91</td><td>1 869.17</td><td>24.42</td><td>2 033.61</td><td>26.57</td></tr><tr><td>优良</td><td>1 051.30</td><td>13.73</td><td>949.63</td><td>12.41</td><td>782.86</td><td>10.23</td></tr><tr><td>总计</td><td>7 654.73</td><td>100.00</td><td>7 654.73</td><td>100.00</td><td>7 654.73</td><td>100.00</td></tr></table>

“治沟造地”等工程 随着配套治理措施跟进，生态建设和经济建设协调发展，2020年该区域生态环境质量恢复明显 .

表7 2015年延河流域各县（区）模型均值统计Table 7 Statistics of model mean values of counties （districts）in the Yanhe River Basin in 2015  

<table><tr><td>地区</td><td>M-RSEI</td><td>RO-RSEI</td><td>RSEI</td><td>EQI</td></tr><tr><td>靖边县</td><td>0.483 2</td><td>0.5038</td><td>0.473 2</td><td>0.493 3</td></tr><tr><td>志丹县</td><td>0.482 5</td><td>0.4931</td><td>0.483 4</td><td>0.543 6</td></tr><tr><td>安塞县</td><td>0.569 5</td><td>0.5363</td><td>0.495 2</td><td>0.5563</td></tr><tr><td>宝塔区</td><td>0.572 5</td><td>0.553 7</td><td>0.5387</td><td>0.6041</td></tr><tr><td>延长县</td><td>0.559 9</td><td>0.542 6</td><td>0.5256</td><td>0.5832</td></tr></table>

# 3　讨论

# 3.1　测评模型的改进

在研究时间段内，RSEI第一主成分的贡献率介于 71.84%\~88.49% 之间，而 RO-RSEI的第一主成分贡献率介于41.53%\~93.68%之间，极值相差较大，该结果与前人的研究结果一致［17，37］ . 这是因为 RO-RSEI模型会“因地制宜”地根据中心像元附近下垫面的真实情况进行计算，少部分生态环境偏差区域只会对其周边环境造成影响，不会拉低偏远区域的生态环境值. Li等［35］ 在评估平余县的生态指数时，认为RSEI计算结果的随机性源自特征向量方向的差异，并指出当NDVI和WET分量的特征向量值为负时，应对PC1进行反转，否则无法实现批量使用，这与本研究的结果一致. 本研究在RO-RSEI模型的基础上，用熵值法代替主成分分析法所构建的 M-RSEI 模型，可以根据各指标对生态环境的作用情况设置归一化公式，使得各个指标所计算的权重均为正值，进而实现批量处理和生产.

![](images/ca54b4eb07d25908bf7989c6a88341bc3134e30254f53e7a9bf4c1adecc30bb4.jpg)  
图 7　基于 M-RSEI 模型的延河流域生态环境质量时空分布  
Fig. 7 Spatio-temporal distribution of ecological environment quality in Yanhe River Basin based on M -RSEI model

2021 年，生态环境部印发《区域生态质量评价办法（试行）》，首次提出生态质量指数（ ），并于年将其正式纳入国家对地方污染防治攻坚战成效考核，正式取代生态环境状况指数（EI），用来反映国家、省、市、县四级行政单元的区域生态质量状况. 从EI升级到 EQI，是对十多年来生态状况评价工作的系统升级 . 而本文所用的验证数据，是中国科学院所发布的EQI数据，具有一定的科学性与参考性. 由于验证数据的分辨率较小，因此空间分布验证均以县（区）为单位，经中国科学院所发布的 EQI 数据，与 RSEI、RO-RSEI、M-RSEI 模型的比较表明，M-RSEI 模型所计算的延河流域的整体均值，与以县（区）为单位的局部均值比较，均比其他2个模型更接近于EQI，因此- 更适合评估延河流域的生态环境质量

# 3.2　测评模型时空精度分析

时间尺度上，3个模型结果均值均呈现为整体上升的趋势，这一结果符合陕西省所发布的环境状况公告，近年来延河流域通过一系列生态恢复工程，特别是退耕还林、还草、梯田建设等措施，水土流失情况有所缓解，促进了生态区植被恢复与生态系统修复，从而提升了生态环境质量. 且3个模型相同年份的计算结果接近，表明模型具有较好的适用性.

在空间尺度上，个模型多年平均计算结果空间分布相似，这再次表明模型构建的可靠性 . M-RSEI模型的计算结果，在空间分布上更接近中国科学院生态所所发布的EQI值，尤其是在极值区域，具有较高的评价精度 . 这表明，移动窗口法改善了空间影响问题［18］ ，且熵值法相较于主成分分析法，具有更高的评价精度，这与程琳琳等［26］ 、王芳等［17］ 学者的研究结果一致. 由此说明M-RSEI模型对于定量描述流域生态环境质量的空间分布以及变化趋势具有较好的应 用 .

# 3.3　不足与展望

本研究基于 Landsat 遥感数据构建评价指标，虽然空间分辨率较高，但其时间间隔较长，难以反映生态环境在短期内的动态变化. 遥感数据的瞬时性问题使模型结果更偏向于某一时点的空间特征，而对生态过程的长期演化捕捉有限 . 此外，在移动窗口法中，窗口的大小根据前人研究结果设定［31，32］ ，存在一定的普适性，但在不同的生态系统中，其适用性可能会受到限制. 并且在3种模型的精度对比中，均以县域尺度的EQI数据为基准，因EQI数据分辨率低且缺乏像元级的空间分布信息，3种模型在空间特征细节上的差异无法完全验证. 未来研究可探索更高分辨率的基准数据及多尺度对比框架，以克服分辨率差异带来的验证不足. 此外，结合生态学过程模型与动态观测数据，将进一步提升模型对不同区域生态系统的适应性和评估精度.

# 4　结论

（）基于 模型，引入移动窗口法构建 -RSEI模型，可以有效地解决区域性差异问题，但无法实现批量化生产.

（2）基 于 RO-RSEI 模 型，运用熵值法构建 M-模型，可以较好地提高测评精度，与中科院所发布的EQI均值最为接近，特别是高值区和低值区的拟合效果良好 因此， - 模型在流域或区域空间尺度上对生态环境质量的监测具有更好的评价精度

（3）2000\~2020年延河流域的生态环境质量整体逐渐改善，但综合等级以“中等”为主，且空间分布上东南部优于西北部，修复重心逐渐向西北方向迁移.

# 参考文献：

［ 1］ 宋美杰，罗艳云，段利民 . 基于改进遥感生态指数模型的锡林郭勒草原生态环境评价［J］. 干旱区研究，2019，36（6）：1521-1527.Song M J， Luo Y Y， Duan L M. Evaluation of ecological environment in theXilin Gol Steppe based on modified remote sensing ecological index model［J］.Arid Zone Research，2019，36（6）：1521-1527.  
［ 2 ］ 辛会超，王贺封，张安兵，等. 2000—2020年漳河上游生态环境质量动态监测及驱动因素分析［］水土保持通报， ，43（）： -Xin H C， Wang H F， Zhang A B，et al. Dynamic monitoring of ecologicalenvironment quality and analysis on its driving factors in upper reaches ofZhanghe River Basin during 2000-2020［J］. Bulletin of Soil and WaterConservation，2023，43（1）：92-103.  
［ 3 ］ Quigley T M， Haynes R W， Hann W J. Estimating ecological integrity in theinterior Columbia River Basin［J］. Forest Ecology and Management，2001，153（1-3）：161-178.  
［ 4 ］ 汤丽妮，张礼清，王卓 . 人工神经网络在生态环境质量评价中的应用［］四川环境， ，22（）： -Tang L N， Zhang L Q， Wang Z. Application of artificial neural network to theassessment of eco-environment quality［J］. Sichuan Environment，2003，22（3）：69-72.  
［ 5 ］ Miao C L， Sun L Y， Yang L. The studies of ecological environmental qualityassessment in Anhui Province based on ecological footprint［J］. EcologicalIndicators，2016，60：879-883.  
［ 6 ］ Gupta K， Kumar P， Pathan S K，et al. Urban neighborhood green index – ameasure of green spaces in urban areas［J］. Landscape and Urban Planning，2012，105（3）：325-335.  
［ 7 ］ Wang Q F， Zeng J Y， Qi J Y，et al. A multi-scale daily SPEI dataset fordrought characterization at observation stations over from 1961China's mainlandto 2018［J］. Earth System Science Data，2021，13（2）：331-341.  
［ 8 ］ 梁建设，白永平，杨雪荻，等 . 基于多源数据的城市扩张中热环境演变及响应［J］. 环境科学，2022，43（6）：3365-3374.Liang J S， Bai Y P， Yang X D，et al. Thermal environment evolution andresponse mechanism of urban sprawl based on multi-source data ［J］.Environmental Science，2022，43（6）：3365-3374.  
［9］ Marull J， Pino J， Mallarach M J，et al. A land suitability index for strategicenvironmental assessment in metropolitan areas［J］. Landscape and UrbanPlanning，2007，81（3）：200-212.  
［10］ HJ 192-2015，生态环境状况评价技术规范［S］.HJ 192-2015， Technical criterion for ecosystem status evaluation［S］.  
［11］ 中华人民共和国生态环境部 关于印发《区域生态质量评价办法（试行 ）》的 通 知［EB/OL］. https：//www. mee. gov. cn/xxgk2018/xxgk/xxgk03/202111/t20211124_961564.html，2021-11-18.  
［12］ 徐涵秋 . 区域生态环境变化的遥感评价指数［J］. 中国环境科学，2013，33（5）：889-897.Xu H Q. A remote sensing index for assessment of regional ecological changes［J］. China Environmental Science，2013，33（5）：889-897.  
［13］ 李光哲，王浩，曹银璇，等 长株潭城市群生态环境质量时空演变及影响因素分析［J］. 自然资源遥感，2023，35（4）：244-254.Li G Z， Wang H， Cao Y X，et al. Spatio-temporal evolution and influencingfactors of ecological environment quality in the Changsha-Zhuzhou-Xiangtanurban agglomeration［J］. Remote Sensing for Natural Resources，2023，35（4）：244-254.  
［14］ 张云霞，汪仕美，李焱，等 . 2000—2020 年青藏高原生态质量时空变化［J］. 生态学杂志，2023，42（6）：1464-1473.Zhang Y X， Wang S M， Li Y，et al. Spatiotemporal patterns of ecologicalquality across the Qinghai-Tibet Plateau during 2000-2020［J］. ChineseJournal of Ecology，2023，42（6）：1464-1473.  
［15］ 朱冬雨，陈涛，牛瑞卿，等 . 利用移动窗口遥感生态指数分析矿区生态环境［J］. 武汉大学学报（信息科学版），2021，46（3）：341-347.Zhu D Y， Chen T， Niu R Q，et al. Analyzing the ecological environment ofmining area by using moving window remote sensing ecological index［J］.Geomatics and Information Science of Wuhan University，2021，46（3）：341-347.  
［16］ 张亚球 . 结合区域尺度优化的遥感生态质量评价方法研究［D］. 长春：长春工程学院，2021.Zhang Y Q. Research on remote sensing ecological quality evaluation methodcombined with regional scale optimization ［D］. Changchun： ChangchunInstitute of Technology，2021.  
［17］ 王芳，李文慧，林妍敏，等 . 1990～2020 年黄河流域典型生态区生态环境质量时空格局及驱动力分析［J］. 环境科学 ，2023，44（5）：2518-2527.Wang F， Li W H， Lin Y M，et al. Spatiotemporal pattern and driving forceanalysis of ecological environmental quality in typical ecological areas of theYellow River Basin from 1990 to 2020［J］. Environmental Science，2023，44（5）：2518-2527.  
［18］ Jiang J， Zhang Y Q， Li J Y，et al. Research on remote sensing ecologicalenvironmental assessment method optimized by regional scale ［J］.Environmental Science and Pollution Research，2021，28（48）：68174-68187.  
［19］ Zhu D Y， Chen T， Zhen N，et al. Monitoring the effects of open-pit mining onthe eco-environment using a moving window-based remote sensing ecologicalindex［J］. Environmental Science and Pollution Research，2020，27（13）：15716-15728.  
［20］ Bao G， Qin Z H， Bao Y H，et al. NDVI-based long-term vegetation dynamicsand its response to climatic change in the Mongolian plateau［J］. RemoteSensing，2014，6（9）：8337-8358.  
［21］ 许晓露 . 延河流域不同尺度生态地质环境质量评价与分析［D］. 成都：成都理工大学，2021.Xu X L. Evaluation and analysis of eco-geological environment quality atdifferent scales in Yanhe River Basin［D］. Chengdu： Chengdu University ofTechnology，2021.  
［22］ 房平，马云，申杰，等 . 延河流域水生态环境存在问题及对策［J］. 人民黄河， ，44（）： - ，Fang P， Ma Y， Shen J，et al. Problems and strategies of water ecologicalenvironment in Yanhe River Basin［J］. Yellow River，2022，44（1）：80-82，88.  
［23］ 董贞凯，穆兴民，赵广举，等 . 延河流域侵蚀产沙对有效降雨量及植被恢复的响应［J］. 泥沙研究，2020，45（5）：27-33.Dong Z K， Mu X M， Zhao G J，et al. Response of sediment yield to effectiverainfall and vegetation rehabilitation in the Yanhe River basin［J］. Journal ofSediment Research，2020，45（5）：27-33.  
［24］ 余慧婕，张方敏，马赫，等. 基于遥感生态指数的淮河流域生态环境质量时空演化及其驱动因素分析［J］. 环境科学，2024，45（7）：4112-4121.Yu H J， Zhang F M， Ma H，et al. Spatio-temporal evolution and drivingfactors of ecological environment quality in the Huaihe River Basin based onRSEI［J］. Environmental Science，2024，45（7）：4112-4121.  
［25］ 吴可人，高祺，王让会，等 . 基于 RSEI模型的石家庄生态环境质量评价［J］. 地球物理学进展，2021，36（3）：968-976.Wu K R， Gao Q， Wang R H，et al. Evaluation of ecological environmentquality in Shijiazhuang based on RSEI model［J］. Progress in Geophysics，2021，36（3）：968-976.  
［26］ 程琳琳，王振威，田素锋，等. 基于改进的遥感生态指数的北京市门头沟区生态环境质量评价［J］. 生态学杂志，2021，40（4）：1177-1185.Cheng L L， Wang Z W， Tian S F，et al. Evaluation of eco-environmentalquality in Mentougou district of Beijing based on improved remote sensingecological index［J］. Chinese Journal of Ecology，2021，40（4）：1177-1185.  
［27］ Xu H Q， Wang Y F， Guan H D，et al. Detecting ecological changes with aremote sensing based ecological index （RSEI） produced time series andchange vector analysis［J］. Remote Sensing，2019，11（20）， doi：10.3390/rs11202345.  
［28］ 杜高奇，李自强，赵勇，等. 基于RSEI的黄河流域生态环境质量监测与驱动因素分析［J］. 水利水电技术（中英文），2022，53（12）：81-93.Du G Q， Li Z Q， Zhao Y，et al. RSEI-based analysis on eco-environmentquality monitoring and driving factors of Yellow River Basin［J］. WaterResources and Hydropower Engineering，2022，53（12）：81-93.  
［29］ 傅楷翔，贾国栋，余新晓，等 基于改进遥感生态指数的青藏公路那（曲）安（多）段生态环境评估及驱动机制分析［］环境科学， ，45（3）：1586-1597.Fu K X， Jia G D， Yu X X，et al. Ecological environment assessment anddriving mechanism analysis of Nagqu and Amdo sections of Qinghai-Xizanghighway based on improved remote sensing ecological index［J］. EnvironmentalScience，2024，45（3）：1586-1597.  
［30］ 任媛. 基于RSEI指数的石羊河流域生态环境质量评价研究［D］. 兰州：西北师范大学，Ren Y. Study on ecological environment quality evaluation of Shiyang RiverBasin based on RSEl index［D］. Lanzhou： Northwest Normal University，2019.  
［31］ 邬建国 . 景观生态学：格局、过程、尺度与等级［M］. 北京：高等教育出版社，2001.Wu J G. Landscape ecology： pattern， process， scale and hierarchy［M］.Beijing： Higher Education Press，2001.  
［32］ 成文连，刘玉虹，关彩虹，等. 生态影响评价范围探讨［J］. 环境科学与管理，2010，35（12）：185-189.Cheng W L， Liu Y H， Guan C H，et al. The discussion about the scope ofecological impact assessment［J］. Environmental Science and Management，2010，35（12）：185-189.  
［ ］ 武锋强 基于 、 的生态环境评价与生态熵研究——以攀枝花地区为例［ ］成都：成都理工大学，Wu F Q. Study on evaluation of ecological and ecological entropy based on RSand GIS——taking the Panzhihua area as an example［D］. Chengdu： ChengduUniversity of Technology，2016.  
［34］ 王丽霞，郝晶，刘招，等. 基于MRSEDI与CA Markov的延河流域生态环境质量评价及预测［J］. 人民黄河，2023，45（1）：123-127，139.Wang L X， Hao J， Liu Z，et al. Evaluation and prediction of ecologicalenvironment quality in Yanhe River Basin based on MRSEDI and CA-Markov［J］. Yellow River，2023，45（1）：123-127，139.  
［35］ Li N， Wang J Y， Qin F. The improvement of ecological environment indexmodel RSEI［J］. Arabian Journal of Geosciences，2020，13（11）， doi：10.- - -  
［36］ 农兰萍，王金亮 . 基于 RSEI模型的昆明市生态环境质量动态监测［J］. 生态学杂志，2020，39（6）：2042-2050.Nong L P， Wang J L. Dynamic monitoring of ecological environment quality inKunming based on RSEI model［J］. Chinese Journal of Ecology，2020，39（6）：2042-2050.  
［37］ 刘英，党超亚，岳辉，等 改进型遥感生态指数与 的对比分析［］遥感学报， ，26（）： -Liu Y， Dang C Y， Yue H，et al. Comparison between modified remote sensingecological index and RSEI［J］. National Remote Sensing Bulletin，2022，26（）： -