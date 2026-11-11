# 皖江流域生境质量评价及多情景优化研究

吴雨桐，於冉\* ，余祺琪，王成，张紫涵安徽农业大学经济与管理学院，安徽 合肥 230036

摘要：皖江流域是长江中下游地区重要的生态屏障区，探究该区域生境质量变化特征对区域生态可持续发展具有重要意义。以皖江流域为例，利用 1990－2020 年土地利用数据，结合 InVEST 模型和地理探测器探讨区域生境质量时空分布特征及驱动因素，并采用PLUS 模型预测模拟区域2030年 4 种不同情境下的土地利用及生境质量变化。结果表明，1）耕地和林地是研究区主要土地利用类型，两者面积约占总面积的 77%。1990－2020 年期间，研究区主要土地利用变化是由耕地向建设用地转入，转入面积为2.69×103 km2。2）1990－2020年期间，研究区生境质量平均指数由0.550下降至0.535，区域整体生境质量水平下降，生境低水平面积扩张趋势明显。3）1990－2020年生境质量时空分异是自然和社会因子的共同作用，主要影响因子是土地利用类型，其次是高程。各因子之间的交互作用对生境质量变化的解释力比单个因子更强。4）2030年多情景模拟结果显示，与2020年相比，惯性发展、城镇发展生境平均指数下降0.003、0.006，耕地保护情景生境与 2020 年持平。生态保护情景生境平均指数上升 0.004，该情景实现了生态保护与经济发展的动态平衡。研究结果可为地区规划景观格局与生态可持续发展提供有效的决策支持。

关键词：InVEST 模型；PLUS 模型；地理探测器；生境质量；皖江流域

DOI: 10.16258/j.cnki.1674-5906.2025.06.013

中图分类号：X14；X821 文献标志码：A 文章编号：1674-5906（2025）06-0961-13引用格式：吴雨桐, 於冉, 余祺琪, 王成, 张紫涵, 2025. 皖江流域生境质量评价及多情景优化研究[J]. 生态环境学报, 34(6):961-973.

WU Yutong, YU Ran, YU Qiqi, WANG Cheng, ZHANG Zihan, 2025. Evaluation and multi-scenario optimization of habitat quality in the basin of Yangtze River in Anhui Province [J]. Ecology and Environmental Sciences, 34(6): 961-973.

在快速城市化与工业化的背景下，城市作为人口高度密集的空间载体，面临着气候变化与人类活动带来的双重挑战（Chen et al.，2021）。这一趋势不仅会导致土地利用结构的显著变化，还进一步加剧了整体生境的退化或景观的破碎（邓越等，2018），对人类和动物的生存环境构成了威胁。生境质量是衡量区域生物多样性和生态系统稳定性的重要指标，其变化直接影响生态系统健康与服务功能，进而阻碍生态的可持续发展（谢余初等，2018）。随着对生境质量研究的深入，研究学者们发现，除土地利用的直接影响外，生境质量同时也受自然条件和经济条件的共同作用（杨永等，2024）。因此，评价生境质量并探讨其影响机制是应对生态问题、保护生态环境的关键手段。

目前国内外学者对生境质量的研究主要分为两类，分别是实地考察评估（谢怡凡等，2020）和模型预测评价（侯孟阳等，2019）。在众多用于评估生境质量的模型中，InVEST 模型因其操作灵活、通用性强等优点而被广泛应用于生境质量的评价中（Kunwar et al.，2020）。该模型在生态功能区或流域、省域、市域等多个不同空间尺度的生境质量研究中取得了良好效果（王燕等，2020；梁晓瑶等，2020；高周冰等，2022；勾蒙蒙等，2023）。然而，现有研究多聚焦于土地利用格局与生境质量关系的探讨，为了更全面地掌握生境质量在长时间尺度上的变化规律，并精确反映整个区域长期的生境状况，对未来不同情境下的生境质量进行模拟和预测显得尤为重要（朱增云等，2020）。

土地利用结构的变化可以通过多种模型进行模拟与预测。其中，元胞自动机地学模型（CA 模型）与马尔科夫模型（Markov 模型）的结合使用有效提高了预测模拟的准确性（杨国清等，2007；Huang et al.，2020；张舟等，2024），但仍存在驱动因素不明确和模拟精度有待提升的问题（谢一茹等，2020）。随着学者们对土地利用模拟模型的深入研究，Liang et al.（2021）提出了基于随机森林算法的 PLUS 模型，通过引入多类型随机斑点种子生成机制和用地扩张分析策略版块，显著提升了预测结果的精确度。基于此，一些学者对 PLUS 模型方法进行了适应性改进，并应用于不同情景下的土地利用时空变化特征预测。例如，张廷等（2024）利用 PLUS 和 InVEST 模型预测了哈尔滨市在 3 种不同情景下的土地利用格局，并据此进行了生境质量分析；马瑞等（2023）通过耦合 PLUS 和 GMOP 模型，对昌吉回族自治州在 2 种设定情景下的各地类空间分布格局进行了模拟预测，进而实现了该地区土地利用格局的结构优化。

基于此，本研究综合利用 1990－2020 年皖江流域土地利用数据，选择 InVEST、PLUS、地理探测器等模型，聚焦于研究区过去与未来生境时空变化及优化策略，试图解决以下科学问题：1）该区域在 1990－2020 年期间土地利用与生境质量时空演变特征如何？2）该区域2030 年在 4种不同情境下土地利用与生境质量时空演变特征如何？3）该区域生境质量变化影响机制如何？以上科学问题的解决有利于为地区规划未来景观格局与生态可持续发展提供有效决策支持。

# 1 研究区概况与数据来源

# 1.1 研究区概况

皖江流域（图1）位于安徽省中南部（29°33′N－33°13′N，115°21′E－119°38′E），毗邻长三角，属于北亚热带湿润季风气候，总面积约为7.6×104 km2 。这一地域涵盖了安庆、池州、铜陵、芜湖、马鞍山、宣城、滁州和合肥8座城市以及六安市的金安区和舒城县。该地区地势南北高、中间低，地貌主要以平原为主，东南方向以皖南山区为主，而东西方向则以皖西丘陵和大别山脉为主。自 2010 年起，皖江流域被正式确立为中国首个国家级产业转移承接示范区，随着产业转移的持续深入，该地区经济实力实现了快速增长（曹玉红等，2019）。然而，伴随着经济的快速发展，林地破坏、围湖造田等一系列人为活动对该地区的生态环境质量造成了负面影响。2010 年国务院批复《皖江城市带承接产业转移示范区规划》强调资源与环境保护的首要地位并加强对该地区的生态保护和环境治理（张立伟等，2018）。因此，针对皖江流域生态环境保护的相关研究显得尤为重要。

# 1.2 数据来源及预处理

选取皖江流域 1990、2000、2010 和 2020 年空间分辨率为 30 m 的土地利用数据，重分类按照GB/T 21010—2017《土地利用现状分类》标准（中华人民共和国国家质量监督检验检疫总局和中国国家标准化管理委员会，2017），将土地利用数据分为 6 个一级类，17 个二级类，数据坐标系统一转为 Krasovsky_1940_Albers 投影坐标系。选取 9 个驱动因子确定其对研究区生境质量变化的作用（表1），地形数据则采用了来源于地理空间数据云（http://www.gscloud.cn/）30M DEM 产品，并使用ArcGIS 10.4软件提取了坡度、坡向信息。归一化植被指数（NDVI）在国家生态科学数据中心（http://www.nesdc.org.cn/）下载。土地利用数据、年均温度、年降雨量、人口密度、GDP 数据均来源于中 国 科 学 院 资 源 环 境 科 学 与 数 据 中 心（https://www.resdc.cn/）。在地理探测器数据处理过程中，通过 ArcGIS 10.4 生成 1 km×1 km 渔网点阵，采样点为 25 403 个。

![](images/68ec2f69701f98642439b958efdd20a608889a33f7f141996238cbbdca636d66.jpg)  
图 1 研究区区位图  
Figure 1 The location map of the study area

表 1 自然与经济因子指标  
Table 1 Natural and economic factors   

<table><tr><td>因子</td><td>指标名称</td><td>单位</td><td>标注</td></tr><tr><td>自然环境因子</td><td>高程</td><td>m</td><td>X</td></tr><tr><td rowspan="10"></td><td>坡度</td><td>0</td><td>X</td></tr><tr><td>坡向</td><td>1</td><td>X3</td></tr><tr><td>NDVI</td><td>1</td><td>X4</td></tr><tr><td>年均温度</td><td>℃</td><td>X5</td></tr><tr><td>年降雨量</td><td>mm</td><td>X6</td></tr><tr><td>社会经济因子 土地利用类型</td><td>1</td><td>X7</td></tr><tr><td>每平方千米人口密度</td><td>人</td><td>X8</td></tr><tr><td>每平方千米GDP</td><td>万元</td><td>X9</td></tr></table>

# 2 研究方法

# 2.1 InVEST 模型及生境质量评价过程

生境质量计算公式如下（马良等，2015）：

![](images/e07e5ba310f64068ca0357e6fee12c640e0a7973047f1e48e49e22c616fbdd0d.jpg)

式中：

Lab— 土地利用类型b中栅格a的生境质量指数，其值域为 0－1；

Hb— 土地利用类型 b的生境适宜度；

——归一化常量，一般设定为 2.5。

生境退化度（Tab）计算公式如下（包玉斌等，2015）：

![](images/70fd01bce150f343c1c32d7c720520af3d314ab88d376fc26c264cbb79deee67.jpg)

式中：

x— 胁迫因子 n 所有栅格数量；  
Xn— 胁迫因子 n 实际占据的栅格数目；  
Gx— 归一化胁迫因子n的权重值，范围0－1；  
nx— 栅格x的胁迫因子n的具体值，范围0－1；  
jnax— 栅格a 的可达性程度；  
ωa— 栅格a 的可接近水平，范围 0－1；

Mbn——土地利用类型b对胁迫因子n的敏感性，其值域为0－1，指数越接近1，表示敏感性越高。

依据皖江流域的实际情况，选取人类活动性较高的城镇用地、农村居民地、工矿与交通用地、水田及旱地作为研究区生态环境威胁源。通过综合参考 InVEST 用户手册推荐值、结合相关专家的指导意见以及前人对流域、安徽湿地保护区生境质量的研究成果（Shang et al.，2021；Huang et al.，2020），对各个威胁因子的最大影响距离、权重、生境类型对各威胁因子的敏感度参数进行设置（表 2、3）。相关研究也表明该具体参数设置对于本研究区具有可实践性（Cao et al.，2023）。

# 表 2 威胁因子权重和最大影响距离

Table 2 The weight and the maximum influence distance of the threat source   

<table><tr><td>威胁因子</td><td>最大影响距离</td><td>权重</td><td>衰减函数</td></tr><tr><td>城镇用地</td><td>10</td><td>0.9</td><td>指数衰减</td></tr><tr><td>农村居民地</td><td>6</td><td>0.6</td><td>指数衰减</td></tr><tr><td>工矿与交通用地</td><td>5</td><td>0.5</td><td>指数衰减</td></tr><tr><td>水田</td><td>1</td><td>0.3</td><td>线性衰减</td></tr><tr><td>旱地</td><td>1</td><td>0.3</td><td>线性衰减</td></tr></table>

表 3 生境类型对威胁因子敏感度  
Table 3 Sensitivity of habitat types to threat factors   

<table><tr><td>土地利用类型 一级</td><td></td><td>生境适</td><td>用地 民用地通用地</td><td>城镇 农村居 工矿与交</td><td></td><td>水田旱地</td><td></td></tr><tr><td>地类</td><td>二级地类 水田</td><td>宜度 0.3</td><td>0.5</td><td>0.6</td><td>0.5</td><td>0</td><td>1</td></tr><tr><td>耕地</td><td>旱地</td><td>0.3</td><td>0.5</td><td>0.6</td><td>0.5</td><td>1</td><td>0</td></tr><tr><td rowspan="4">林地</td><td>有林地</td><td>1</td><td>0.7</td><td>0.7</td><td>0.7</td><td>0.8</td><td>0.7</td></tr><tr><td>灌木林</td><td>0.9</td><td>0.6</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.6</td></tr><tr><td>疏木林</td><td>0.7</td><td>0.8</td><td>0.7</td><td>0.6</td><td>0.7</td><td>0.7</td></tr><tr><td>其他林地</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.6</td><td>0.4</td><td>0.5</td></tr><tr><td rowspan="4">草地</td><td>高覆盖度草地</td><td>0.8</td><td>0.6</td><td>0.7</td><td>0.4</td><td>0.6</td><td>0.7</td></tr><tr><td>中覆盖度草地</td><td>0.6</td><td>0.6</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>低覆盖度草地</td><td>0.5</td><td>0.6</td><td>0.5</td><td>0.5</td><td>0.4</td><td>0.5</td></tr><tr><td>河渠</td><td>0.9</td><td>0.5</td><td>0.4</td><td>0.4</td><td>0.4</td><td>0.4</td></tr><tr><td rowspan="4">水域</td><td>湖泊</td><td></td><td></td><td></td><td></td><td>0.6</td><td>0.7</td></tr><tr><td></td><td>1</td><td>0.7</td><td>0.6</td><td>0.5</td><td></td><td></td></tr><tr><td>水库坑塘</td><td>0.9</td><td>0.6</td><td>0.6</td><td>0.4</td><td>0.5</td><td>0.6</td></tr><tr><td>滩地 城镇用地</td><td>0.8</td><td>0.7</td><td>0.8</td><td>0.6</td><td>0.6</td><td>0.4</td></tr><tr><td rowspan="3">建设 用地</td><td>农村居民用地</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>工矿与交通用地 裸地</td><td>0 0.1</td><td>0 0.2</td><td>0 0.1</td><td>0 0.1</td><td>0 0</td><td>0 0</td></tr></table>

# 2.2 基于 PLUS 模型的土地利用模拟

# 2.2.1 LEAS

选取 8 类驱动因子作为用地扩张的驱动因子，利用 LEAS模块（张廷等，2024）获取 17 种地类扩张概率和各个驱动因素对各土地利用地类变化的贡献度。

# 2.2.2 领域权重

邻域权重（张舟等，2024）是反映各类土地利用类型在空间驱动因素作用下扩张能力的参数，本研究参考王保盛等（2019）的赋值方法计算得出 17个地类的邻域权重值。具体公式如下：

![](images/7676652094f07cf3e0dfa6151caff639ea95c1346c472887763762a7c03a5e39.jpg)

Xi — 某用地类型 i 的邻域权重；

ΔTi — 研究时段内该用地类型变化值；

ΔTmin 和 ΔTmax— 该时段内各用地类型变化的最小值和最大值。

# 2.2.3 土地利用模拟情景设置

本研究通过调整 Markov 链转移矩阵概率得到4 不同情境下的土地利用转移概率（Li et al.，2022），其公式如下（杨国清等，2007）：

![](images/577f2f0c4c6354ae26ec16a7a9162e64ca73fb123343291087e0fe48fefed65f.jpg)

式中：

P— 面积；

Pij — 第i类土地转换为第 j 类土地的面积；  
m— 土地利用的类型数；

i，j— 研究期初与研究期末的土地利用类型。

PLUS 模型在皖江流域适用性较强（He et al.，2023；唐文睿等，2024），鉴于此，为探究多情景下皖江流域土地利用变化状况，根据《安徽省国土空间规划（2021－2035 年）》中提到的“改善生态环境质量、加强城镇规划治理”的重点任务，参考前人经验研究以及研究区特点，设置惯性发展、城镇发展、耕地保护以及生态保护 4 种情景预测 2030年皖江流域土地利用时空变化格局。

惯性发展情景（IDS）下，保持原有转移概率不变，不加入其他限制条件。城镇发展情景（UDS）下，限制建设用地向其他地类的转化，增加其他地类向建设用地转化的概率（Hu et al.，2020）。耕地保护情景（PPS）下，水域作为限制区，并限制耕地向建设用地转化以确保耕地面积（唐文睿等，2024）。生态保护情景（EPS）下，水域作为限制区，并限制林地、草地向建设用地的转化，提高耕地向林地、草地转移概率（黄木易等，2025）。各情景成本设置如表 4 所示。

# 2.2.4 准确性验证分析

模拟预测结果准确性可用 kappa 系数表示，当Kappa 系数≥0.75 时，证明实验模拟结果准确度越高（孙毅中等，2020）。其表达式如下：

![](images/435a1140b19d34ba2a79879f8ed6e9ff87f6654a4e8eb1b7562d3cad06a02d07.jpg)

其中：

A— 模拟网格总数；

C— 模拟网格随机总数；为预测模拟准确性，将基于2010年土地利用数据模拟得出的2020年预测结果与 2020 年的实际土地利用数据进行对比，

研究结果显示，Kappa 系数为 0.941，验证了模拟预测结果的可靠性。

# 2.3 地理探测器

地理探测器（王劲峰等，2017）能够深入分析地理空间特征并揭示造成这种现象背后的驱动力。具体公式如下：

![](images/f59447eb831af6350667840ae12028441a40bcef11526ce2938a86198034572c.jpg)

式中：

q— 影响因子对生境质量的影响程度，范围为 0－1；

L——X 的分层，即分类或分区；

Nh 和 N——层 h 和研究区的单元数；

2 σh和 σ2——层 h 和研究区生境质量空间分异的方差。自然因素和社会因素作为自变量 X，交互作用探测可以分析出不同驱动因子之间的共同作用是否对生境质量存在增强或减弱影响。双因子交互作用结果类型如表 5所示。

表 5 双因子交互作用结果类型  
Table 5 Types of two-factor interaction result   

<table><tr><td>判断依据</td><td>交互作用类型</td></tr><tr><td>q(Xi ∩X2)&lt;Min[q(Xi),q(X2)]</td><td>非线性减弱</td></tr><tr><td>Min[q(Xi),q(X2)]&lt;q(X1∩X2)&lt;Max[q(Xi)+q(X2)]</td><td>单因子非线性减弱</td></tr><tr><td>q(Xi ∩X2)&gt;Max [q(Xi),q(X2)]</td><td>双因子增强</td></tr><tr><td>q(Xi ∩ X2)=q(X1)+q(X2)</td><td>自变量独立</td></tr><tr><td>q(Xi ∩ X2)&gt;q(Xi)+q(X2)</td><td>非线性增强</td></tr></table>

# 3 结果分析

# 3.1 土地利用变化与生境质量评价

3.1.1 1990－2020 年土地利用演变结果

研究区 1990－2020 年土地利用分布如图 2 所示。在此期间，研究区的主要土地利用类型为耕地和林地，分别集中分布在研究区的中北部和南部区域，两者面积约占研究区面积的 77%。城镇用地呈现出显著地向外扩张趋势，扩张的主要区域集中在长江沿岸地带以及巢湖西北部。相比之下，农村居民点以及工矿与交通用地的分布则相对分散，其扩张区域主要位于研究区地势相对较低的平坦地带。

表 4 各情景土地利用转移矩阵  
Table 4 Multi-scenario land use transition matrix   

<table><tr><td rowspan="2">地类</td><td colspan="6">惯性发展情景</td><td colspan="6">城镇发展情景</td><td colspan="6">耕地保护情景</td><td colspan="6">生态保护情景</td></tr><tr><td>a</td><td>b</td><td>C</td><td>d</td><td>e</td><td>f</td><td>a</td><td>b</td><td>C</td><td>d</td><td>e</td><td>f</td><td>a</td><td>b</td><td>C</td><td>d</td><td>e</td><td>f</td><td>a</td><td>b</td><td>C</td><td>d</td><td>e</td><td>f</td></tr><tr><td>a</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0 0</td><td>0</td><td></td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>b</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>C</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>d</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>e</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>f</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

a：水田、旱地；b：有林地、灌木林、疏木林、其他林地；c：高覆盖度草地、中覆盖度草地、低覆盖度草地；d：河渠、湖泊、水库坑塘、滩地；e：城镇用地、农村居民用地、工矿与交通用地；f：裸地；其中 0 表示不允许转化；1 表示允许转化；矩阵内行表示转出；列表示转入

![](images/c92c4163e43f52beaf8685487f0243bb1a5480d10e611aa5d8a7d9fae980daf0.jpg)  
图 2 1990－2020 年土地利用分布示意图Figure 2 Land use distribution and changesfrom 1990 to 2020

研究区 1990－2020 年各用地面积的变化情况及具体变化率如表 6 和表 7 所示。总体而言，耕地、林地和草地的面积呈现出下降趋势，其中耕地的变化率最为明显，达到−6.71%，林地和草地的变化率分别为−1.19%和−1.51%。相反，水域、建设用地和未利用地的面积则整体呈现上升趋势，变化率分别为 2.18%、74.10%、215.76%，建设用地和未利用地增长速率较为明显。研究区土地利用类型的转换主要表现为耕地和林地向建设用地、草地以及水域的转换，具体来说，1990－2020 年期间，研究区内水域、建设用地和其他用地转入面积大于转出面积，耕地、林地、草地转出面积大于转入面积。其中，转出面积最多的地类是耕地，共转出 3.57×103 km2 ，尤其向建设用地面积转入了 2.69×103 km2 。林地共转出 949.2 km2 ，尤其向耕地转入了 537.9 km2 ，向草地和建设用地分别转入 242.2 km2 和 154.9 km2 。

# 3.1.2 1990－2020 年生境质量演变结果

将研究区生境质量结果按照自然断点法进行等级划分，分别为低、较低、中等、较高、高5个等级（霍艾迪等，2024），取值区间分别为0－0.098、0.098－0.498、0.498－0.80、0.80－0.898、0.898－1。由图

# 表 7 1990－2020 年土地利用转移矩阵

Table 7 Statistics of land area from 1990 to 2020 km2   

<table><tr><td rowspan="2">1990年 土地 利用类型</td><td colspan="6">2020 年土地利用类型</td><td rowspan="2">转出 面积</td></tr><tr><td>耕地</td><td>林地</td><td>草地</td><td>水域</td><td>建设用未利用 地</td><td>地</td></tr><tr><td>耕地</td><td>3.60×104</td><td>519.2</td><td>81.2</td><td>273.7</td><td>2.69×10</td><td>7.3</td><td>3.57×103</td></tr><tr><td>林地</td><td>537.9</td><td>1.94×104</td><td>242.2</td><td>11.8</td><td>154.9</td><td>2.3</td><td>949.2</td></tr><tr><td>草地</td><td>170.5</td><td>172.9</td><td>5.10×10³</td><td>13.5</td><td>62.7</td><td>0.3</td><td>419.9</td></tr><tr><td>水域</td><td>134.8</td><td>12.8</td><td>11.0</td><td>5.16x10</td><td>29.0</td><td>0.1</td><td>187.7</td></tr><tr><td>建设用地</td><td>238.4</td><td>8.1</td><td>3.1</td><td>6.4</td><td>3.36×103</td><td>0.3</td><td>256.3</td></tr><tr><td>未利用地</td><td>0.1</td><td>0.2</td><td>0.1</td><td>0.0</td><td>0.0</td><td>4.3</td><td>0.4</td></tr><tr><td>转入面积</td><td>1.08×103</td><td>713.2</td><td>337.7</td><td>305.4</td><td>2.94×103</td><td>10.3</td><td></td></tr></table>

3所示，研究区的生境质量整体呈下降趋势，通过对比图 2 的土地利用分布可看出，生境质量高和较高的区域主要分布在皖西和皖南山区、中部的巢湖以及升金湖等湖泊湿地。这些区域生态系统结构稳定，人类活动相对较少，因此生境质量得以保持较高水平。相比之下，研究区中北部以及东南部沿江周边生境质量较低，这些地区的土地利用类型相对单一，主要以水田和旱地为主。而长江沿岸以及巢湖西北部的城镇集中区，是生境质量最低的区域。这些区域受城镇化加速和人类活动频繁影响，生境质量显著下降且低生境水平面积扩张趋势明显。

![](images/64994081b87a87d55e02d5cc054c4033f94523fb95258c65cd2f45d81f378fc3.jpg)  
图 3 1990－2020 年生境质量分布示意图Figure 3 Habitat quality change from 1990 to 2020

表 6 1990－2020 年土地利用类型面积及比例  
Table 6 Area and proportion of land use types from 1990 to 2020   

<table><tr><td rowspan="2">地类</td><td colspan="2">1990年</td><td colspan="2">2000年</td><td colspan="2">2010年</td><td colspan="2">2020年</td><td>面积变化量</td><td>面积变化率</td></tr><tr><td>面积/km²</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td></tr><tr><td>耕地</td><td>3.95×104</td><td>53.18</td><td>3.90×104</td><td>52.45</td><td>3.78×104</td><td>50.89</td><td>3.70×104</td><td>49.83</td><td>-2.49×103</td><td>-6.71</td></tr><tr><td>林地</td><td>2.03×104</td><td>27.32</td><td>2.02×104</td><td>27.18</td><td>2.01×104</td><td>27.07</td><td>2.01×104</td><td>27.00</td><td>-239.4</td><td>-1.19</td></tr><tr><td>草地</td><td>5.52×103</td><td>7.43</td><td>5.49×103</td><td>7.39</td><td>5.45×103</td><td>7.34</td><td>5.44×103</td><td>7.32</td><td>-82.1</td><td>-1.51</td></tr><tr><td>水域</td><td>5.35×103</td><td>7.20</td><td>5.38×103</td><td>7.23</td><td>5.46x103</td><td>7.35</td><td>5.47×103</td><td>7.35</td><td>116.6</td><td>2.18</td></tr><tr><td>建设用地</td><td>3.62×103</td><td>4.87</td><td>4.27×103</td><td>5.74</td><td>5.46×10</td><td>7.34</td><td>6.30×103</td><td>8.48</td><td>2.68×103</td><td>74.10</td></tr><tr><td>未利用地</td><td>4.6</td><td>0.01</td><td>4.8</td><td>0.01</td><td>5.1</td><td>0.01</td><td>14.6</td><td>0.02</td><td>10.0</td><td>215.76</td></tr></table>

从图4中可以看出，在1990－2020年期间，研究区生境退化度较高区域扩散明显，这表明土地利用变化对研究区生态系统结构扰动较大。其中，退化度值较小的区域主要分布在南部、北部林地山区、中部耕地，这些区域土地利用类型较稳定，缺少人类干扰。退化度中等的区域主要分布在研究区西北部，并且逐渐向沿江地区蔓延，这些区域处于建设用地外围，开发可能性强，具有一定人类活动性。而退化度严重的区域则主要分布在城镇建成区的外围。这些区域由于地势平坦，易于开发和利用，如建设、农业扩张等频繁的人为活动，因此土地利用变化显著，导致生境质量严重下降，生境退化度升高。

# 3.1.3 生境质量驱动力分析

地理探测器的单因子探测结果和因子交互作用探测结果如表 8、图5所示，9 个驱动因子的 p值均小于 0.005，通过显著性检验（王劲峰等，2017）。1990－2020 年期间，坡度、NDVI 因子影响力增加。各单影响因子解释力 q 值平均值由大到小排序为：土地利用>高程>坡度>人口密度>降雨量>NDVI>气温>GDP>坡向。土地利用因子和高程因子是影响研究区生境质量的主要因素，其次是坡度、人口密度、降雨量。因子之间的交互作用对生境质量变化解释力的增强效果明显，例如，1990－2020年期间，GDP单个因子对生境质量平均解释力较低，叠加坡度因子后，其解释力平均值增至 0.423；人口密度因子叠加坡度因子后，其解释力平均值增至 0.449。综上所述，尽管自然环境因素对研究区生境质量的影响巨大，但在一定程度上，但社会经济因素同样在生境质量的变化中发挥着不可忽视的推动作用。

# 3.2 基于土地利用模拟的生境质量预测分析

# 3.2.1 土地利用变化驱动因子贡献度分析

采用 PLUS 模型中的 LEAS 模块得出 8 个驱动因子对 17 种地类扩张的贡献度（图 6）。从结果来看，高程是影响泥滩、低覆盖度草地、其他林地分布的主要因子，在这些用地的扩张中占据了重要地位；坡度主要是影响灌木林、疏林地分布的主要因子；坡向是影响有林地分布的主要因子；NDVI 是影响水库坑塘、中覆盖度草地分布的主要因子；气温是影响高覆盖度草地、旱地、其他林地分布的主要因子；降雨量是影响旱地、湖泊、城镇用地、工矿与交通用地分布的主要因子；人口密度主要是影响裸地、城镇用地分布的主要因子，GDP 主要是影响中覆盖度草地、城镇用地分布的主要因子，突出了社会经济因子对城市扩张的作用。

# 3.2.2 2030 年土地利用多情景模拟结果

从2030年4种情景和2020年土地利用分布图中选取 3 个区域，分别是 A区（巢湖西北部城镇集中区）、B区（长江下游沿江地区）和 C 区（长江上游沿江地区）。这3部分区域土地利用格局分异各具特点，其中，A 区地势平坦，土地利用变化显著；B 区靠近长江沿岸且城镇较为集中。C 区城镇相对集中且周边具有一定的生态空间。由图7可见，惯性发展情景与城镇发展情景相似，城镇扩张情境中，建设用地扩张趋势较 2020 年和2030 年其他情景最为明显。耕地保护情景下，建设用地面积明显小于 2020 年和 2030 年其他情景，尤其是在 A区域和 B 区域，即中心城市或沿江城镇集中区。生态保护情景与惯性发展情景相比，建设用地面积减少。而生态用地（如林地、草地、水域）方面，各情景之间的差异均较小。

![](images/c853226b790cbbd5e818c8e16ae2bd9815503acc17fc17a1770dce0a0afdd5ad.jpg)  
图 4 1990－2020 年生境质量退化度分析  
Figure 4 Degradation degree of habitat quality from 1990 to 2020

表 8 生境质量空间分异驱动因子探测结果  
Table 8 Detection results of spatial differentiation driving factors of habitat quality   

<table><tr><td rowspan="2">驱动因子</td><td colspan="2">1990年</td><td colspan="2">2000年</td><td colspan="2">2010年</td><td colspan="2">2020年</td><td colspan="2">1990-2020年</td></tr><tr><td>q值</td><td>排序</td><td>q值</td><td>排序</td><td>q值</td><td>排序</td><td>q值</td><td>排序</td><td>平均q值</td><td>排序</td></tr><tr><td>高程（X）</td><td>0.378</td><td>3</td><td>0.374</td><td>2</td><td>0.373</td><td>2</td><td>0.377</td><td>2</td><td>0.376</td><td>2</td></tr><tr><td>坡度（X）</td><td>0.385</td><td>2</td><td>0.368</td><td>3</td><td>0.367</td><td>3</td><td>0.374</td><td>3</td><td>0.374</td><td>3</td></tr><tr><td>坡向（X）</td><td>0.004</td><td>9</td><td>0.004</td><td>9</td><td>0.004</td><td>9</td><td>0.004</td><td>9</td><td>0.004</td><td>9</td></tr><tr><td>NDVI（X4)</td><td>0.210</td><td>5</td><td>0.160</td><td>6</td><td>0.141</td><td>6</td><td>0.154</td><td>6</td><td>0.166</td><td>6</td></tr><tr><td>气温（X5）</td><td>0.129</td><td>8</td><td>0.135</td><td>7</td><td>0.135</td><td>7</td><td>0.148</td><td>7</td><td>0.137</td><td>7</td></tr><tr><td>降雨量（X6)</td><td>0.215</td><td>6</td><td>0.219</td><td>5</td><td>0.220</td><td>5</td><td>0.200</td><td>5</td><td>0.214</td><td>5</td></tr><tr><td>土地利用（X7)</td><td>0.925</td><td>1</td><td>0.882</td><td>1</td><td>0.882</td><td>1</td><td>0.896</td><td>1</td><td>0.896</td><td>1</td></tr><tr><td>人口密度（Xg）</td><td>0.242</td><td>4</td><td>0.240</td><td>4</td><td>0.225</td><td>4</td><td>0.233</td><td>4</td><td>0.235</td><td>4</td></tr><tr><td>GDP（X9）</td><td>0.150</td><td>7</td><td>0.119</td><td>8</td><td>0.130</td><td>8</td><td>0.146</td><td>8</td><td>0.136</td><td>8</td></tr></table>

![](images/2b3b5fd2812a2f75bca32b94e4aee19d674cded37b2ac76929c305244eafc26d.jpg)  
图 5 生境质量分异特征影响因子的交互作用探测结果 Figure 5 Interaction detection results of factors affecting habitat quality differentiation characteristics

![](images/92a5a7c872a7eeb506d48e15c0b673b481bc8cc5f98fd1024a9fb52ed1f45846.jpg)  
图 6 土地类型扩张驱动因子贡献度  
Figure 6 Contribution degree of driving factors of land expansion

从 4 种情景模拟结果分析（表 9），惯性发展情境下，研究区土地利用变化基本延续过去 30 年的变化趋势，其中，建设用地增加了 799.1 km2 。城镇发展情境下，与 2020年相比，建设用地扩张尤为显著，增幅达到 1.28×103 km2 ，较惯性发展情景增加了 484.5 km2 。同时，耕地、林地、草地和未利用地的减少幅度也进一步扩大，分别减少了 1161.5、102.7、40.1 和 6.2 km2 。耕地保护情境下，与 2020年相比林地面积减少 51.1 km2 ，耕地面积增加 70.3km2 。与惯性发展情景相比，建设用地面积大幅减少798.7 km2 。生态保护情景下，与 2020 年相比耕地面积减少了 766.2 km2 ，建设用地扩张受到控制，其增加面积减少到 292.9 km2 ，林地与水域面积均呈现增长态势。特别是林地，增幅高达 476.2 km2 。与惯性发展相比，林地增加了 535.5 km2 ，建设用地减少了 506.2 km2 ，生态建设一定程度抑制了城市发展。

![](images/067391e1120f976d565c870df604b50b690f6c058b6b9ed700fe7d37dca946bc.jpg)  
图 7 2030 年 4 种情境下土地利用模拟结果  
Figure 7 Simulation results of land use under four scenarios in 2030

表 9 不同情境下各用地类型面积变化  
Table 9 Changes of land use types under different scenarios   

<table><tr><td rowspan="3">地类</td><td rowspan="2">2020年</td><td colspan="6">2030年</td><td colspan="6">2020-2030年变化</td></tr><tr><td colspan="2">IDS</td><td colspan="2">UDS</td><td colspan="2">PPS</td><td colspan="2">EPS</td><td colspan="2">IDS UDS</td><td>PPS</td><td>EPS</td></tr><tr><td>面积/km²</td><td>面积/km²</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td><td></td><td>面积/km²</td><td></td><td></td></tr><tr><td>耕地</td><td>3.7×104</td><td>3.63×104</td><td>48.82</td><td>3.59×104</td><td>48.27</td><td>3.71×104</td><td>49.93</td><td>3.63x104</td><td>49.56</td><td>-757.6</td><td>-1161.5</td><td>70.3</td><td>-766.2</td></tr><tr><td>林地</td><td>2.01×104</td><td>2×104</td><td>26.92</td><td>2×104</td><td>26.87</td><td>2×104</td><td>26.94</td><td>2.06×104</td><td>27.51</td><td>-59.3</td><td>-102.7</td><td>-51.1</td><td>476.2</td></tr><tr><td>草地</td><td>5.44×103</td><td>5.42×103</td><td>7.29</td><td>5.4×103</td><td>7.27</td><td>5.42×103</td><td>7.29</td><td>5.42×103</td><td>7.31</td><td>-23.3</td><td>-40.1</td><td>-21.7</td><td>-21.9</td></tr><tr><td>水域</td><td>5.47×10</td><td>5.51×103</td><td>7.41</td><td>5.49×103</td><td>7.38</td><td>5.47×103</td><td>7.36</td><td>5.48x103</td><td>7.38</td><td>39.0</td><td>20.6</td><td>2.4</td><td>16.7</td></tr><tr><td>建设用地</td><td>6.3×10</td><td>7.1×103</td><td>9.55</td><td>7.59×10</td><td>10.20</td><td>6.3x103</td><td>8.48</td><td>6.6x103</td><td>8.23</td><td>799.1</td><td>1.28×103</td><td>0.4</td><td>292.9</td></tr><tr><td>未利用地</td><td>14.6</td><td>10.3</td><td>0.01</td><td>8.4</td><td>0.01</td><td>7.9</td><td>0.01</td><td>10.5</td><td>0.02</td><td>-4.3</td><td>-6.2</td><td>-6.7</td><td>-4.1</td></tr></table>

IDS：惯性发展情景；UDS：城镇发展情景；PPS：耕地保护情景；EPS：生态保护情景

# 3.2.3 2030 年预测生境质量分析

惯性发展情境下，生境质量平均指数为 0.532，较 2020 年减少 0.003；城镇发展情景下，该指数进一步滑落至 0.529，降幅达 0.006；而耕地保护情境则相对稳定，生境质量平均指数为 0.535，与 2020年基本持平。相比之下，生态保护情境下的生境质量有所提升，平均指数为 0.539，较2020 年增加了0.004。从 4 种情境和 2020 年生境质量结果中选取3 个区域，从 3 种不同情境下 A 区域、B 区域、C区域的生境质量情况（图 8）来看，城镇发展情境对生境质量的负面影响最为突出，低质量生境区域显著增加。相反，在耕地保护和生态保护情境下，低质量生境区域则明显减少。4 种情景下的高质量和较高质量生境区域变化不明显。

从4种情景模拟结果分析（表10）可见，惯性发展情境下，生境质量呈现分化趋势。具体而言，较低和中等质量的生境面积分别减少了 763.7、5.72×103km2 ，而低质量、较高质量及高质量生境的面积则分别增加了 785.5、4.86×103 、819.8 km2 。城镇发展情境下，低质量与中等质量的生境面积减少更为显著，分别为 1.17×103 、5.7×103 km2 。低质量、较高质量和高质量生境的面积变化分别为增加 1.27×103 、4.84×103 、736.6 km2 。与惯性发展情景相比，城镇发展情景下的低质量和较低质量生境面积占比均有所上升。耕地保护情境中，牺牲生态建设保护耕地，高水平生境质量面积较 2020 年减少了 53.8 km2 。相比之下，在生态保护情境中，高质量生境面积较2020年增加了485.9km2 ，较低质量生境面积减少了768.2 km2 ，显示出生态保护措施对提升生境质量的积极作用。

![](images/10a15e58dc34020b4097ce1cf1db9d746d0f5b8a2837faa18291c206b537ba2a.jpg)  
图 8 2030 年 4 种情境下生境质量模拟结果  
Figure 8 Simulation results of habitat quality under four scenarios in 2030

表 10 不同情境下生境质量面积变化  
Table 10 Changes of habitat quality grade under different scenarios   

<table><tr><td rowspan="3">生境质量 等级</td><td rowspan="2">2020年</td><td colspan="8">2030年</td><td colspan="4">2020-2030年变化</td></tr><tr><td colspan="2">IDS</td><td colspan="2">UDS</td><td colspan="2">PPS</td><td colspan="2">EPS</td><td colspan="2">IDS</td><td colspan="2">PPSEPS</td></tr><tr><td>面积/km²</td><td>面积/km</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td><td>面积/km²</td><td>占比/%</td><td></td><td>面积/km²</td><td></td><td></td></tr><tr><td>低</td><td>6.32×103</td><td>7.1×103</td><td>9.55</td><td>7.59×103</td><td>10.20</td><td>6.3×103</td><td>8.48</td><td>6.6×103</td><td>8.87</td><td>785.5</td><td></td><td>1.27×10 -13.2 279.4</td><td></td></tr><tr><td>较低</td><td>3.71×104</td><td>3.63×104</td><td>48.83</td><td>3.59×104</td><td>48.29</td><td>3.71×104</td><td>49.95</td><td>3.63×104</td><td>48.83</td><td>-763.7</td><td></td><td>-1.17×10 64.9 -768.2</td><td></td></tr><tr><td>中等</td><td>6.49×103</td><td>766.5</td><td>1.03</td><td>790.3</td><td>1.06</td><td>6.46×10³</td><td>8.69</td><td>6.47×103</td><td>8.70</td><td></td><td></td><td>-5.72×10 -5.7×10² -26.3 -19.0</td><td></td></tr><tr><td>较高</td><td>1.25×10³</td><td>6.11×103</td><td>8.22</td><td>6.1×103</td><td>8.19</td><td>1.26×10³</td><td>1.69</td><td>1.25×10³</td><td>1.68</td><td>4.86×103</td><td>4.84×10</td><td></td><td>11.34.8</td></tr><tr><td>高</td><td>2.32×104</td><td>2.41×104</td><td>32.37</td><td>2.4×104</td><td>32.25</td><td>2.32×104</td><td>31.19</td><td>2.37×104</td><td>31.92</td><td>819.8</td><td></td><td>736.6-53.8 485.9</td><td></td></tr></table>

IDS：惯性发展情景；UDS：城镇发展情景；PPS：耕地保护情景；EPS：生态保护情景

# 4 讨论

# 4.1 皖江流域生境质量变化影响机制

为应对城市扩张与生态恶化之间的矛盾，“长江大保护”和“长江经济带”等一系列保护和发展政策相继实施（何寿奎，2019），这在一定程度上缓解了皖江流域生态系统结构失稳的趋势。然而，总体上研究区生境质量仍呈波动下降态势，主要原因是建设用地扩张，这也与现有的研究结果相吻合（张立伟等，2018；Cao et al.，2023）。地理探测器模型结果显示，土地利用类型对生境质量变化具有基础和关键性的作用，地形地貌的改变是主要原因，而人口密度是重要驱动力。

从土地利用类型对生境质量的影响来看，1990－2020 年期间，研究区建设用地面积占比从 4.87%增长至 8.48%，耕地和林地分别向建设用地转入了2.7×103 、154.9 km2 ，可见城市的快速扩张占用了大量农业与生态用地，导致生境质量指数下降，生境持续退化。人口密度代表着人类活动的广度及潜在的深度，在经济利益的驱动和社会发展的双重压力下，人类对城镇开发的需求逐渐提高，导致生态系统服务结构受到更多人类干扰，最终导致生境质量恶化。此外，地形地貌通过影响生物多样性及资源禀赋空间分布，间接作用于区域生境质量（许梦杰等，2024），尤其是在皖江流域地势相对平坦的区域，人口密度较高，导致区域生态环境逐渐人工化。因此，如何充分利用地形地貌蕴含的自然环境禀赋，促进生境质量提升，并缓解人类活动导致的潜在环境恶化趋势，已成为区域生态环境综合管理研究亟待解决的关键课题。

# 4.2 皖江流域生境质量优化策略

结果显示，耕地与生态保护措施能有效遏制建设用地过度扩张，进而稳定并提升生境质量。耕地保护措施遏制了建设用地对耕地的侵占，减缓了研究区域生境质量的退化。生态保护情境中，尽管耕地面积有所缩减，但关键生态区域（如林地）面积增加，致使生境质量相较于2020年有所改善，为皖江流域的可持续发展探索了新路径。因此，耕地与生态保护政策并行是抑制建设用地无序扩张、防止生境恶化的有效策略。未来皖江流域的区域规划应优先保护生态用地（如林地、水域等），严格控制建设用地扩张，避免占用耕地，以提升区域生境质量水平。林地分布与高程、气温高度相关，建设用地分布与高程、气温、人口密度高度相关，且与低生境区域具有空间一致性。因此在推进区域生境质量提升和生态功能维持的过程中，规划部门应基于“因地制宜”规划思想，依据地形地貌特点调整并管控自然空间与人类生活空间（Jiang et al.，2021）。具体来说：

1）在地势较高的西南部大别山及南部皖南丘陵山区分布地带，该地区森林资源丰富，物种与生态紧密关联，因此针对该地区的生境质量优化策略应主要以维持与保护为主。例如，西南部大别山区向周边沿江平原的过渡地带，在城镇扩张情景和惯性发展情景中，这些区域存在城镇空间向丘陵缓冲区侵占趋势。因此，为防范生态系统结构受人类活动破坏，可因地制宜设置“农林业”低强度产业地带，适当发展经济林木产业和特色生态农产品，增强区域生态屏障安全，提高居民福祉和生态经济发展，并且在一定程度上避免了居民由于经济问题对周边林地的乱砍滥伐（于目良等，2024）。上述优化策略可为山区生态廊道的保护与生物多样性的维持提供重要的方案参考。

2）在地势较为平坦的江北平原丘陵地带，该地区主要以耕地与建设用地为主，开发潜力大。该地区中心城市持续扩张，中小城镇集中发展，易导致区域生态空间破碎化和生态系统服务功能退化。因此，应结合城镇发展定位和方向，控制中心城市无序扩张，尤其控制对生态源地（重要河流、湖泊、森林等）的侵占。在城镇发展规划中，合理布局湿地、森林公园等重要生态廊道，为区域生态系统服务流的传递提供通道，也为城市居民提供游憩场所。而集中连片城镇地带需平衡城镇与农业功能，改善城乡居民生产生活条件，推进农村环境综合整治，盘活现有建设用地规模（Zhao et al.，2022）。闲置土地可优先复耕，改善农业水利等基础设施，提升农业发展的韧性。上述措施可为促进城乡经济社会高质量发展及恢复低值区域生态系统（如农业生态系统）潜力提供方案参考。

3）沿江地区水资源丰富，湖泊湿地众多，城镇呈“带状”分布，与长江及其重要支流重叠。该区域高生境区域均呈散点分布，这与该地区城镇密布、湖泊沼泽与水系交织的复杂地貌等因素有关。相关研究表明，该区域是我国重要的生物多样性热点区和众多珍稀物种越冬地，支撑了该区域作为长江中下游地区关键生态廊道的重要地位（Cao et al.，2023）。为此，该区域应秉持“保护与开发并重”发展思路，重点保护升金湖、菜子湖等重要湖泊湿地及周边生态系统结构完整性，严禁一切高强度人为开发行为，保护珍稀濒危物种栖息地，维护区域生物多样性。同时，在长江干流及重要支流岸线建设防护林，设立河流生态缓冲区，防止城镇生态风险向水域扩散，为物种迁徙提供生态通道。沿江主要城镇地区则需依据城市发展定位，坚持生态优先，限制高污染高能耗产业，减轻人类活动对生态系统质量的负面影响。

# 4.3 不足与展望

InVEST 模型中生境质量模块能够有效反映生态系统服务功能以及生物多样性，地理探测器则能有效评估多种因素对生态环境变化的潜在影响，二者的结合应用提升了生境质量空间分析的精确性（霍艾迪等，2024）。然而，鉴于直接观测生境质量指标的困难，本文未对 InVEST 模型的评估结果进行校验与修正，但在构建模型参数时，参考了相关研究成果对各项参数进行了科学合理的设定。为提高未来研究结果的精确性，建议在细化生态系统分类的基础上加强参数校验（王秀明等，2020）。本文采用的 PLUS 模型能够预测未来不同情境下土地利用，但该模型存在一定局限性，特别是土地利用分布格局可能会受到政策调控的影响。然而，由于政策效果难以量化，本文在模拟未来土地利用空间格局时未考虑政策因素，这在一定程度上降低了模拟精度（Tang et al.，2020）。因此，未来研究中可进一步完善土地利用模拟情景设置，纳入政策、经济成本等现实因素作为情景约束条件。

# 5 结论

1）研究区土地利用结构分异特征明显，土地利用类型主要为耕地和林地，两者约占总面积 77%。在 1990－2020 年期间，建设用地面积显著扩增2.7×103 km2，其中耕地向建设用地转入 2.7×103km2 。建设用地扩张趋势明显，主要分布在长江沿岸地区以及巢湖西北部。

2）在1990－2020 年期间，生境质量平均指数分别为 0.550、0.544、0.539、0.535，整体呈递减趋势，且空间分布上自南向北逐渐降低。湖泊和有林地生境适宜度最高，建设用地生境适宜度最低。

3）研究区生境质量的变化受多重因素共同影响，其中，自然环境因子与社会经济因子间的相互作用相较于单一因子内部的相互作用更为突出。1990－2020年期间，土地利用是影响最为显著的因素，其解释力平均值高达 0.896，随后依次为高程（0.376）、坡度（0.374）及人口密度（0.235）。

4）土地利用模拟结果显示，2020－2030 年，4种预测情景下的生境质量排序为：生态保护情景最优，次之是耕地保护情景，再次为惯性发展情景，城镇发展情景则相对最差。生境质量平均指数依次为：0.539、0.535、0.532、0.529。建设用地扩张和林地减少是惯性发展和城镇发展情境下生境质量减少的主要原因。

# 参考文献：

CHEN M J, BAI Z K, WANG Q R, et al., 2021. Habitat quality effect and driving mechanism of land use transitions: A case study of Henan water source area of the middle route of the south-to-north water transfer project [J]. Land, 10(8): 796.   
CAO Y, WANG C, SU Y, et al., 2023. Study on spatiotemporal evolution and driving forces of habitat quality in the basin along the Yangtze River in Anhui Province based on InVEST model [J]. Land, 12(5): 1092.   
HUANG Y, YANG B, WANG M, et al., 2020. Analysis of the future land cover change in Beijing using CA-Markov chain model [J]. Environmental Earth Sciences, 79(2): 60.   
HUANG M Y, YUE W Z, FENG S R, et al., 2020. Spatial-temporal evolution of habitat quality and analysis of landscape patterns in Dabie Mountain area of west Anhui province based on InVEST model [J]. Acta Ecologica Sinica, 40(9): 2895-2906.   
HU S, CHEN L Q, LI L, et al., 2020. Simulation of land use change and ecosystem service value dynamics under ecological constraints in Anhui Province, China [J]. International Journal of Environmental Research and Public Health, 17(12): 4228.   
HE N, GUO W X, WANG H X, et al., 2023. Temporal and spatial variations in landscape habitat quality under multiple land-use/land-cover scenarios based on the PLUS-InVEST model in the Yangtze River Basin, China [J]. Land, 12(7): 1338.   
JIANG L G, LIU Y, WU S, et al., 2021. Analyzing ecological environment change and associated driving factors in China based on NDVI time series data [J]. Ecological indicators, 129: 107933.   
KUNWAR R M, EVANS A, MAINALI J, et al., 2020. Change in forest and vegetation cover influencing distribution and uses of plants in the Kailash Sacred Landscape, Nepal [J]. Environment, Development and Sustainability, 22(2): 1397-1412.   
LI X, FU J Y, JIANG D, et al., 2022. Land use optimization in Ningbo City with a coupled GA and PLUS model [J]. Journal of Cleaner Production, 375: 134004.   
LIANG X, GUAN Q F, CLARKE K C, et al., 2021. Understanding the drivers of sustainable land expansion using a patch-generating land use simulation (PLUS) model: A case study in Wuhan, China [J]. Computers, Environment and Urban Systems, 85: 101569.   
SHANG J, CAI H S, LONG Y, et al., 2021. Temporal-spatial distribution and transition of habitat quality in Poyang Lake region based on InVEST model [J]. Resour. Environ. Yangtze Basin, 30(8): 1901-1915.   
TANG F, FU M C, WANG L, et al., 2020. Land-use change in Changli County, China: Predicting its spatio-temporal evolution in habitat quality [J]. Ecological Indicators, 117: 106719.   
ZHAO B X, LI S J, LIU Z S, 2022. Multi-scenario simulation and prediction of regional habitat quality based on a system dynamic and patchgenerating land-use simulation coupling model: A case study of Jilin Province [J]. Sustainability, 14(9): 5303. 境的影响——以陕西省黄河湿地自然保护区为例[J]. 干旱区研究, 32(3): 622-629. BAO Y B, LIU K, LI T, et al., 2015. Effects of land use change on habitat based on InVEST Model: Taking Yellow River Wetland nature reserve in Shaanxi Province as an example [J]. Arid Zone Research, 32(3): 622-629.   
曹玉红, 陈晨, 张大鹏, 等, 2019. 皖江城市带土地利用变化的生态风险 格局演化研究[J]. 生态学报, 39(13): 4773-4781. CAO Y H, CHEN C, ZHANG D P, et al., 2019. Evolution of ecological risk pattern of land use change in Wanjiang City Belt [J]. Acta Ecologica Sinica, 39(13): 4773-4781.   
邓越, 蒋卫国, 王文杰, 等, 2018. 城市扩张导致京津冀区域生境质量下 降[J]. 生态学报, 38(12): 4516-4525. DENG Y, JIANG W G, WANG W J, et al., 2018. Urban expansion led to the degradation of habitat quality in the Beijing-Tianjin-Hebei area [J]. Acta Ecologica Sinica, 38(12): 4516-4525.   
勾蒙蒙, 刘常富, 李乐, 等, 2023. 三峡库区典型流域生境质量时空演变 特征与情景模拟[J]. 生态学杂志, 42(1): 180-189. GOU M M, LIU C F, LI L, et al., 2023. Spatiotemporal variations and scenario simulation of habitat quality in a typical basin of the Three Gorges Reservoir Area [J]. Chinese Journal of Ecology, 42(1): 180-189.   
高周冰, 王晓瑞, 隋雪艳, 等, 2022. 基于 FLUS 和 InVEST 模型的南京 市生境质量多情景预测[J]. 农业资源与环境学报, 39(5): 1001-1013. GAO Z B, WANG X R, SUI X Y, et al., 2022. Multi-scenario prediction of habitat quality in Nanjing based on FLUS and InVEST models [J]. Journal of Agricultural Resources and Environment, 39(5): 1001-1013.   
侯孟阳, 姚顺波, 邓元杰, 等, 2019. 格网尺度下延安市生态服务价值时 空演变格局与分异特征——基于退耕还林工程的实施背景[J]. 自 然资源学报, 34(3): 539-552. HOU M Y, YAO S B, DENG Y J, et al., 2019. Spatial-temporal evolution pattern and differentiation of ecological service value in Yan’an city at the grid scale based on Sloping Land Conversion Program [J]. Journal of Natural Resources, 34(3): 539-552.   
黄木易, 汤玉茹, 郭芹, 等, 2025. 基于权衡/协同效应的安徽省生态功能 区识别及情景模拟研究[J]. 中国环境科学, 45(1): 450-464. HUANG M Y, TANG Y R, GUO Q, et al., 2025. Identification of ecological functional areas and multi-scenario simulation study in Anhui Province based on trade-off/synergy effect [J]. China Environmental Science, 45(1): 450-464.   
霍艾迪, 刘琪, 李心悦, 等, 2024. 秦岭北麓沣河流域矿区生境质量的时 空演变及驱动因素分析[J]. 农业工程学报, 40(8): 223-231. HUO A D, LIU Q, LI X R, et al., 2024. Spatial-temporal evolution and driving factors of habitat quality in Xiangyu mining area, Feng River basin, north foot of Qinling Mountains of China [J]. Transactions of the Chinese Society of Agricultural Engineering, 40(8): 223-231.   
何寿奎, 2019. 长江经济带环境治理与绿色发展协同机制及政策体系研 究[J]. 当代经济管理, 41(8): 57-63. HE S K, 2019. A study on the coordination mechanism and policy system of environmental governance and green development in the Yangtze River Economic Belt [J]. Contemporary Economic Management, 41(8): 57-63.   
梁晓瑶, 袁丽华, 宁立新, 等, 2020. 基于 InVEST 模型的黑龙江省生境 质量空间格局及其影响因素[J]. 北京师范大学学报(自然科学版), 56(6): 864-872. LIANG X Y, YUAN L H, NING L X, et al., 2020. Spatial pattern of habitat quality and driving factors in Heilongjiang Province [J]. Journal of Beijing Normal University (Natural Science), 56(6): 864-872.   
马瑞, 范燕敏, 武红旗, 等, 2023. 耦合 GMOP 与 PLUS 模型的干旱区土 地利用格局模拟[J]. 农业资源与环境学报, 40(1): 143-153. MA R, FAN Y M, WU H Q, et al., 2023. Simulation of land-use patterns in arid areas coupled with GMOP and PLUS models [J]. Journal of Agricultural Resources and Environment, 40(1): 143-153.   
马良, 金陶陶, 文一惠, 等, 2015. InVEST 模型研究进展[J]. 生态经济, 31(10): 126-131, 179. MA L, JIN T T, WEN Y H, et al., 2015. The Research Progress of InVEST Model [J]. Ecological Economy, 31(10): 126-131, 179.   
孙毅中, 杨静, 宋书颖, 等, 2020. 多层次矢量元胞自动机建模及土地利 用变化模拟[J]. 地理学报, 75(10): 2164-2179. SUN Y Z, YANG J, SONG S Y, et al., 2020. Modeling of multilevel vector cellular automata and its simulation of land use change [J]. Acta Geographica Sinica, 75(10): 2164-2179.   
唐文睿, 曹玉红, 2024. 基于 InVEST-PLUS 模型的皖江流域碳储量时空 演变及预测[J/OL]. 环境科学, 1-19 [2025-03-21]. https://doi.org/10. 13227/j.hjkx.202406063. TANG W R, CAO Y H, 2024. Spatial-temporal evolution and prediction of carbon reserves in Wanjiang River Basin with the InVEST-PLUS model [J/OL]. Environmental Science, 1-19 [2025-03-21]. https://doi. org/10.13227/j.hjkx.202406063.   
王秀明, 刘谞承, 龙颖贤, 等, 2020. 基于改进的 InVEST 模型的韶关市 生态系统服务功能时空变化特征及影响因素[J]. 水土保持研究, 27(5): 381-388. WANG X M, LIU X C, LONG Y X, et al., 2020. Spatial-temporal changes and influencing factors of ecosystem services in Shaoguan City based on improved InVEST [J]. Research of Soil and Water Conservation, 27(5): 381-388.   
王劲峰, 徐成东, 2017. 地理探测器: 原理与展望[J]. 地理学报, 72(1): 116-134. WANG J F, XU C D, 2017. Geodetector: Principle and prospective [J]. Acta Geographica Sinica, 72(1): 116-134.   
王燕, 高吉喜, 金宇, 等, 2020. 基于 2005－2015 年土地利用变化和 InVEST 模型的内蒙古巴林右旗农牧交错带生境质量研究[J]. 生态 与农村环境学报, 36(5): 654-662. WANG Y, GAO J X, JIN Y, et al., 2020. Habitat quality of farmingpastoral ecotone in Bairin Right Banner, inner mongolia based on land use change and InVEST model from 2005 to 2015 [J]. Journal of Ecology and Rural Environment, 36(5): 654-662.   
王保盛, 廖江福, 祝薇, 等, 2019. 基于历史情景的 FLUS 模型邻域权重 设置——以闽三角城市群 2030 年土地利用模拟为例[J]. 生态学报, 39(12): 4284-4298. WANG B S, LIAO J F, ZHU W, et al., 2019. The weight of neighborhood setting of the FLUS model based on a historical scenario: A case study of land use simulation of urban agglomeration of the Golden Triangle of Southern Fujian in 2030 [J]. Acta Ecologica Sinica, 39(12): 4284-4298.   
谢一茹, 高培超, 王翔宇, 等, 2020. 经济发展预期下的粮食产量与生态 效益权衡——黑龙江省土地利用优化配置[J]. 北京师范大学学报 (自然科学版), 56(6): 873-881. XIE Y R, GAO P C, WANG X Y, et al., 2020. Exploring the trade-offs between grain yield and ecological benefits in an economic development context: Land-use optimization of Heilongjiang Province [J]. Journal of Beijing Normal University (Natural Science), 56(6): 873-881.   
许梦杰, 陈凌秀, 谢慧黎, 等, 2024. 闽台海岸带生境质量时空演变及其 影响因素[J]. 海洋通报, 43(4): 546-556. XU M J, CHEN L X, XIE H L, et al., 2024. Temporal and spatial evolution of habitat quality in Fujian and Taiwan coastal zones based on land use change and its influencing factors [J]. Marine Science Bulletin, 43(4): 546-556.   
谢余初, 巩杰, 张素欣, 等, 2018. 基于遥感和 InVEST 模型的白龙江流 域景观生物多样性时空格局研究[J]. 地理科学, 38(6): 979-986. XIE Y C, GONG J, ZHANG S X, et al., 2018. Spatiotemporal change of landscape biodiversity based on InVEST model and remote sensing technology in the Bailong River Watershed [J]. Scientia Geographica Sinica, 38(6): 979-986.   
谢怡凡, 姚顺波, 邓元杰, 等, 2020. 延安市退耕还林(草)工程对生境质 量时空格局的影响[J]. 中国生态农业学报(中英文), 28(4): 575-586. XIE Y F, YAO S B, DENG Y J, et al., 2020. Impact of the ‘Grain for Green’ project on the spatial and temporal pattern of habitat quality in Yan’an City, China [J]. Chinese Journal of Eco-Agriculture, 28(4): 575-586.   
于目良, 刘悦俊, 张燕杰, 2024. 青藏高原未来土地利用变化与景观生态 风险多情景预测[J]. 长江流域资源与环境, 33(10): 2204-2218. YU M L, LIU Y J, ZHANG Y J, 2024. Multi-scenario prediction of future land use change and landscape ecological risk on the Qingzang Plateau [J]. Resources and Environment in the Yangtze Basin, 33(10): 2204-2218.   
杨永, 李瑞红, 刘航, 等, 2024. 东北农林交错区生境质量时空演变及归 因分析[J]. 生态学杂志, 43(5): 1399-1407. YANG Y, LI R H, LIU H, et al., 2024. Spatio-temporal evolution and driving forces of habitat quality in agroforestry ecotone of Northeast China [J]. Chinese Journal of Ecology, 43(5): 1399-1407.   
杨国清, 刘耀林, 吴志峰, 2007. 基于 CA-Markov 模型的土地利用格局 变化研究[J]. 武汉大学学报(信息科学版), 32(5): 414-418. YANG G Q, LIU Y L, WU Z F, 2007. Analysis and simulation of land-use temporal and spatial pattern based on CA-Markov model [J]. Geomatics and Information Science of Wuhan University, 32(5): 414-418.   
张廷, 胡玉柱, 胡海辉, 等, 2024. 基于 PLUS-InVEST 模型的哈尔滨市 土地利用及生境质量预测[J]. 环境科学, 45(8): 4709-4721. ZHANG T, HU Y Z, HU H H, et al., 2024. Prediction of land use and habitat quality in Harbin city based on the PLUS-InVEST model [J]. Environmental Science, 45(8): 4709-4721.   
张立伟, 张运, 黄晨, 2018. 皖江城市带近 20 a 生态环境变化遥感指数分 析[J]. 长江流域资源与环境, 27(5): 1061-1070. ZHANG L W, ZHANG Y, HUANG C, 2018. Remote sensing index analysis on ecological environment changes in the recent 20 years of City Belt in Wanjiang [J]. Journal of Nanjing Forestry University (Natural Sciences Edition), 27(5): 1061-1070.   
张舟, 刘晶晶, 张权, 等, 2024. 基于 PLUS-InVEST-Geodector 模型的苏 州市碳储量时空变化及驱动力分析[J/OL]. 环境科学, 1-17 [2025- 03-21]. https://doi.org/10.13227/j.hjkx.202405077. ZHANG Z, LIU J J, ZHANG Q, et al., 2024. Analysis of spatialtemporal variation and driving forces of carbon storage in Suzhou city based on the PLUS-InVEST-Geodector model [J/OL]. Environmental Science, 1-17 [2025-03-21]. https://doi.org/10.13227/j.hjkx.202405077.   
中华人民共和国国家质量监督检验检疫总局, 中国国家标准化管理委 员会, 2017. 土地利用现状分类: GB/T 21010—2017 [S]. 北京: 中国 标准出版社. General Administration of Quality Supervision, Inspection and Quarantine of the People’s Republic of China, Standardization Administration of the People’s Republic of China, 2017. Current land use classification: GB/T 21010—2017 [S]. Bejing: Standards Press of China.   
朱增云, 阿里木江·卡斯木, 2020. 基于地理探测器的伊犁谷地生境质量 时空演变及其影响因素[J]. 生态学杂志, 39(10): 3408-3420. ZHU Z Y, ALIMUJIANG K, 2020. Spatial-temporal evolution of habitat quality in Yili Valley based on geographical detector and its influencing factors [J]. Chinese Journal of Ecology, 39(10): 3408-3420.

# Evaluation and Multi-Scenario Optimization of Habitat Quality in the Basin of Yangtze River in Anhui Province

WU Yutong, YU Ran\* , YU Qiqi, WANG Cheng, ZHANG Zihan School of Economics and Management, Anhui Agricultural University, Hefei 230036, P. R. China

Abstract: Currently, due to the strain in human-land relationships, the accelerated advancement of economic globalization, and rapid population growth, various ecological challenges are gradually becoming a core focus for countries and international organizations. This is an important topic in research on the global ecosystem structure. With the rapid socio-economic development in China, the continuous expansion of construction land has become an inevitable trend, which not only exerts a profound impact on natural ecological changes and land cover structures but also poses a threat to the living environments of humans and animals. Habitat quality is the foundation and prerequisite of all ecosystem functions and services. Assessment of habitat quality and exploration of its impact mechanisms are key means of dealing with ecological problems and protecting the ecological environment. Additionally, research on the temporal and spatial changes in habitat quality and their influencing factors is vital for maintaining ecosystem balance and sustainability. The Basin of Yangtze River in Anhui Province serves as an essential ecological barrier in the middle and lower reaches of the Yangtze River, with important wetlands such as Shengjin Lake and Chaohu Lake. These wetlands are vital wintering and breeding grounds in China for dozens of nationally endangered wildlife species, including the Chinese alligator (Alligator sinensis) and hooded crane (Grus monacha), which also represent crucial nodes and wintering sites along the migration route of the East Asian-Australasian Flyway. Since 2010, the basin has been officially established as China’s first national-level demonstration zone for industrial transfer, resulting in rapid regional economic growth. However, significant ecological changes have occurred with the ongoing land-use development, attracting the attention of local governments and scholars. Therefore, ecological and environmental protection research is important. Therefore, this study comprehensively used land use data of the study area from 1990 to 2020 and selected the InVEST model, PLUS model, and geodetector to focus on spatiotemporal changes in past and future habitats in the study area and the optimization strategies. The following scientific issues should be addressed: 1) What are the spatiotemporal evolutionary characteristics of land use and habitat quality in this region from 1990 to 2020? 2) What are the spatiotemporal evolution characteristics of land use and habitat quality in the study area under the four 2030 scenarios? 3) What are the impact mechanisms of habitat quality change in the study area? The scientific issues that this study focuses on provide valuable insights and effective decision support for regional landscape planning and ecological sustainability initiatives. The results showed the following. 1) The dominant land use types in the study area were paddy and forest lands, which accounted for approximately 77% of the total area. Notably, from 1990 to 2020, the main land use types in the study area were converted from paddy land to construction land, with a total of 2 691.28 km2 . 2) During 1990–2020, the average habitat quality index decreased from 0.550 to 0.535 and the overall habitat quality decreased. 3) During 1990– 2020, both natural and social factors influenced the spatial distribution of the habitat quality. The main influencing factor was land use followed by elevation. The interaction of all factors had stronger explanatory power for the change in habitat quality than that of individual factors. 4) The results of the multi-scenario simulation in 2030 showed that compared with 2020, the average habitat index would decline by 0.003 under inertia development and by 0.006 under urban development scenarios. Conversely, the habitat index for the paddy-land protection scenario should be maintained at the 2020 level. Notably, the average habitat index for the ecological protection scenario exhibited an increase of 0.004, indicating successful attainment of a dynamic balance between ecological protection and economic development. Research indicates that paddy land protection and ecological protection measures have played a significant role in effectively curbing the excessive expansion of construction land within the study area, thereby stabilizing and enhancing habitat quality. In the context of ecological protection, although there has been a slight reduction in paddy land and a minor increase in construction land, key ecological areas such as forest land have seen growth. This improvement in habitat quality compared with 2020 opens up new approaches for sustainable development in the Yangtze River Basin in Anhui Province. Therefore, the simultaneous implementation of paddy land and ecological protection policies is an effective strategy to prevent further habitat degradation. Future regional planning should prioritize the protection of ecological land, such as forestland and water, and strictly control the expansion of construction land to avoid encroaching on paddy lands, thus comprehensively enhancing the regional habitat quality. Moreover, due to the distinct diversity of topographical features in the Basin of Yangtze River in Anhui Province, planning authorities should adhere to the principle of “adapting measures to local conditions” in order to reasonably adjust and manage natural and human living spaces based on topographic characteristics. For instance, in the southwestern Dabie Mountains and southern Anhui Hills, where high terrain and rich forest resources are prevalent, low-intensity “agroforestry” zones can be established to moderately develop economic timber industries and distinctive ecological agricultural products. This approach not only bolsters the security of the region’s ecological barrier, but also enhances local residents’ well-being and promotes eco-economic development, thereby mitigating deforestation of surrounding forests driven by economic challenges. In relatively flat Jiangbei Plain and hilly regions with abundant paddy land resources, it is essential to rationally control the disorderly expansion of central cities. By improving the living environment of urban and rural residents as a focal point, comprehensive rural environmental remediation should be pursued, with the appropriate consolidation of small, dispersed settlements and the optimal utilization of existing construction land resources. In water-rich areas along a river, it is crucial to adopt a development philosophy that balances “protection and development.” All high-intensity anthropogenic development activities must be strictly prohibited to safeguard habitats for rare and endangered species and to maintain regional biodiversity stability. Major urban areas along the river should be aligned with urban development positioning, uphold ecological priorities, and restrict highpollution and high-energy-consumption industries to mitigate adverse impacts of human activities on ecosystem quality.

Keywords: InVEST, PLUS; Geographical detector; Habitat quality; The basin of Yangtze River in Anhui Province