# 嘉陵江流域生态系统服务动态变化及权衡协同分析

王天雯 1,2，罗明良\*1,2，白雷超 1,21. 西华师范大学地理科学学院，四川 南充 637009；2. 西华师范大学嘉陵江流域研究所，四川 南充 637009摘要：嘉陵江流域作为长江上游重要生态屏障，其生态系统服务的有效管理对保障生态安全与推动可持续发展具有重要意义。基于 InVEST 模型，评估了 2000－2020 年间土壤保持、生境质量、碳储量和产水服务等 4 项生态系统服务的时空变化特征；结合地理探测器分析了自然因子和人类活动对其的驱动作用；以地形梯度进行分区，通过皮尔逊相关性和空间自相关方法，揭示了全域和分区情形下不同服务间的权衡与协同关系。结果表明，1）20年间，嘉陵江流域的生态系统服务呈现“整体上升、局部平稳”特征。土壤保持和产水服务显著增长，土壤保持高值区集中于地势陡峭、植被良好的东南和西北地区；而产水服务呈“南高北低”格局，高值区位于降水充沛的南部；生境质量略有下降，碳储量相对稳定，空间分布与土壤保持服务类似。2）生态系统服务在自然因子和人类活动的共同驱动下发生变化，受土地利用、植被覆盖、坡度、降水和高程等因素及其交互作用的显著影响。3）流域生态系统服务的权衡与协同关系在时间、空间及地形梯度分区上差异显著，不同梯度内部服务关系各具特征，其中低梯度区作用较弱，中梯度区协同性增强，高梯度区以权衡为主。该研究揭示了嘉陵江流域生态系统服务的时空动态特征及其权衡协同关系，为流域优化生态功能布局、提升生态服务水平提供了科学支持。

关键词：生态系统服务；嘉陵江流域；InVEST 模型；权衡协同；地理探测器

DOI: 10.16258/j.cnki.1674-5906.2025.06.006

中图分类号：X171.1；X196；P283.1 文献标志码：A 文章编号：1674-5906（2025）06-0888-14引用格式：王天雯, 罗明良, 白雷超, 2025. 嘉陵江流域生态系统服务动态变化及权衡协同分析[J]. 生态环境学报, 34(6):888-901.

WANG Tianwen, LUO Mingliang, BAI Leichao, 2025. Dynamic Changes and Trade-off-Synergy Analysis of Ecosystem Services in the Jialing River Basin [J]. Ecology and Environmental Sciences, 34(6): 888-901.

生态系统服务是指自然生态系统通过其结构、功能和过程，直接或间接满足人类生存与福祉需求的多种服务和产品（傅伯杰，2010；郭宗亮等，2022）。生态系统服务涵盖了供给、调节、支持和文化等功能（Costanza et al.，1998；Boyd et al.，2007；Carpenter et al.，2009）。然而，自 21 世纪初千年生态系统评估（MA）以来，已有超过 60%的关键生态系统服务呈现出不同程度的下降趋势（Hassan etal.，2005）。联合国 2023 年对可持续发展目标（SDGs）的评估进一步指出，超过 30%的目标已停滞甚至出现倒退（傅伯杰等，2024），表明人类活动导致的资源过度开发和环境恶化正加剧供需矛盾，并引发生态系统服务的持续退化。

与此同时，由于生态系统服务种类繁多且空间分布不均，不同服务之间呈现出复杂的交互机制和动态关系，主要表现为此消彼长的权衡关系和相互增益的协同关系（李双成等，2013）。全球生态系统服务的优化面临前所未有的挑战。作为连接自然环境与社会发展的桥梁（赵文武等，2018），厘清生态系统服务的动态变化、驱动机制及其相互作用关系，对农业资源管理（Cumming et al.，2014）、生物多样性保护（文志等，2020）、城镇协调发展（韩磊等，2024）以及全球气候变化应对（韩会庆等，2018）等领域的科学决策与可持续发展具有重要意义。

自 20 世纪末，Costanza et al.（1998）从经济学角度评估生态系统服务的价值以来，生态系统服务的理论与方法研究逐渐扩展到多个学科领域，如生态学（Bagstad et al.，2013）、地理学（陈心盟等，2021）等。随着研究的深入，未来的研究将更多地关注社会学等角度对生态系统服务的影响（Peng et al.，2023）。关于生态系统服务研究的理论方法，戴尔阜等（2016）、傅伯杰等（2016）和李婷等（2018）重点总结了统计学、空间分析、情景模拟分析、生态系统服务流动性等方法，并借助InVEST 等模型，深入开展生态系统服务的评估及其权衡与协同分析。

基于上述理论与方法，前人已开展了相关的研究。在分析方法上，孙彦等（2024）利用贝叶斯网络模型分析了贵州省生态系统服务的权衡关系增强的潜在区域，但该模型在长时间序列变化的表达上存在一定局限性。潘竟虎等（2017）则通过空间热点制图法识别了嘉峪关酒泉地区的生态系统服务热点区，但未进一步分析生态系统服务与空间分布之间的相关关系。目前，关于长江流域的生态系统服务研究主要集中于中下游地区，而上游嘉陵江流域的研究仍较少，且现有的时空变化分析大多侧重于单一生态服务的变化。例如，胡孟珂等（2022）研究了 2001－2020 年嘉陵江流域植被覆盖度的时空变化，发现该地区植被覆盖度总体呈上升趋势，尤其在低海拔和东南部地区改善明显，而高海拔和城市周边区域则出现退化。赵宾华等（2023）分析了嘉陵江流域潜在蒸发量的年际与季节性变化，揭示了气温与湿度之间的交互影响。然而，关于多种生态服务的综合分析，尤其是长时序的整体变化研究仍显不足。

习近平总书记高度重视长江生态环境保护，强调“要将修复长江生态环境置于压倒性位置”（石秀秀，2021）。嘉陵江流域作为长江上游的重要生态屏障和“中华水塔”的关键区域，肩负着重要的生态功能。该流域的生态系统丰富多样，涵盖森林、草原、湿地、农业及城镇等多各种类型，面临着经济发展与环境保护的双重挑战（朱月华，2023）。目前，嘉陵江流域面临的主要生态问题包括水资源利用低效、湿地退化、水土流失，以及上游采矿和产业发展带来的次生环境风险（郭丹等，2022），这些问题加剧了经济与生态保护的矛盾。因此，亟需开展该流域生态系统服务系统性研究，以揭示嘉陵江流域生态环境保护的关键问题及其解决路径。本文首先采用 InVEST 模型，分析嘉陵江流域在2000、2010 和 2020 年间土壤保持、生境质量、碳储量和产水服务的时空动态变化。同时，基于地理探测器方法定量分析各项服务的主要影响因素的驱动机制，并通过皮尔逊相关性分析和空间自相关方法，从全局和地形梯度分区下评估不同生态系统服务之间的相互作用关系。研究结果可为嘉陵江流域实现生态保护与流域协调发展的双赢提供理论依据和实践参考。

# 1 研究区概况与数据来源

# 1.1 研究区概况

如图 1 所示，嘉陵江流域（103°45′E－109°00′E，29°20′N－34°25′N），总面积约 1.6×105 km2 ，流经陕西省、甘肃省、四川省、重庆市，约占整个长江流域面积的 9%。作为长江流域面积最大、流量第二的子流域，嘉陵江在长江水系中占据重要位置，尤其是其上游是三峡水库的主要水源之一，对三峡水库的水量和生态影响显著（谭晶华等，2024）。流域内主要水系包括嘉陵江干流、渠江和涪江，三者在重庆合川附近汇聚，形成扇形向心水系。整个流域的地势特征表现为东北和西部较高，向东南逐渐降低，整体趋于平缓，拥有丰富的地貌类型。上游主要为山地地形，中游为盆地和丘陵，下游则流经四川盆地东部的平行峡谷区，形成峡谷河流（胡孟珂等，2022）。流域大部分地区属于亚热带湿润季风气候，气候温和，四季分明，年均降水量超过1000mm。然而，降水在年内的分配受季风影响较大，加之人类活动频繁，导致流域内水土流失严重，滑坡和泥石流等地质灾害频发，成为长江水系支流中含沙量最高的河流之一（董鑫等，2024）。中下游地区冬季温暖多雾，上游则常遭霜雪风暴，春夏季节则易出现春旱和初夏干旱。

# 1.2 数据来源

本文选取 2000、2010、2020 年等 3 个年份数据，对各年份数据进行基础处理，统一像元大小为30 m，投影为 WGS_1984_UTM_ZONE_48N。数据来源如下：

1）降雨数据来自 NOAA（https://gis.ncdc.noaa.gov），空间分辨率为 1 km，利用年降水栅格数据以及气象站站点的数据进行克里金插值确立。2）气温数据来自国家地球系统科学数据中心（http:/www.geodata.cn/），空间分辨率为 1 km。3）土壤数据来自世界土壤数据库（HWSD）中国土壤数据集，数据来自国家冰川冻土沙漠科学数据中心（http://www.ncdc.ac.cn），包含土壤类型、土壤质地、含沙量、土壤含水量等数据。4）DEM 数据使用 ASTER 数据来源于地理空间数据云（https://www.gscloud.cn/）。5）NDVI 数据来源于中国科学院生态科学数据中心（http://www.nesdc.org.cn/）。6）土地利用数据来源于中国科学院资源环境科学与数据中心（https://www.resdc.cn/），涵盖 2000、2010、2020 年共 3 期，空间分辨率为 30 m。7）人口密度、GDP 等人文经济数据来自 2000－2020 年四川省、陕西省、重庆市、甘肃省等各省市统计年鉴。

# 2 研究方法

# 2.1 生态系统服务评估

基于嘉陵江流域实际情况选取土壤保持、产水服务、生境质量和碳储量 4 类服务，所有服务均采

![](images/9d426c92210d013ae818dc117295500316adaf4b8e0f6e0280e5f3548bd912eb.jpg)  
图 1 研究区概况图  
Figure 1 Location of the studied area

用 InVEST 模型来估算。

# 2.1.1 土壤保持

采用 InVEST 模型中的泥沙输移比模块（Sediment Delivery Ratio，SDR）来评估该地区的土壤保持情况。基于修正的通用土壤流失方程（TheRevised Universal Soil loss Equation，RUSLE），通过估算嘉陵江流域潜在侵蚀量和实际侵蚀量的差值来评估土壤保持量（刘月等，2019；廖洪圣等，2024）。具体公式如下：

![](images/3c35b05cbebdbfd36efcce40eb6f8d18a7877e270eb983eeecdc479863d0edfc.jpg)

![](images/c087933c1914be555c1a365e626fb28ec5b9f345ec6b2b5c47f3532062c03a8c.jpg)

![](images/6d5fe2c7894405987c6391ae9a216e76b53a0a758225116dfb186841cb1b4db3.jpg)

P——水土保持因子，参考前人的研究（王万忠等，1996）对 P 进行赋值。

# 2.1.2 产水服务

产水服务直接影响流域的水量平衡和水分循环（高雅玉等，2024）。本研究采用 InVEST 模型中的产水量模块（Water Yield Service，WS）来评估该地区的年均产水量。该模块基于 Budyko 的水热耦合曲线（Chen et al.，2020），具体相关参数的使用参考相关论文（戴尔阜等，2020）。基本计算过程如下：

![](images/f1e4c40c423466c2d6ccfde647d66e74e479a5595b314ab558f822c369bd2ac6.jpg)

式中：

Sc— 土壤保持量（t·hm−2 ）；Sp— 潜在年土壤侵蚀量（t·hm−2 ）；Sf— 土壤实际侵蚀量（t·hm−2 ）；R— 降雨侵蚀力因子，使用适应嘉陵江流域的降雨侵蚀力模型（张竞哲等，2023）得到；K——土壤可蚀性因子，采用 EPIC 模型计算；L 和 S——坡度和坡长因子；C——植被覆盖因子；

式中：

Wx— 每个 x 栅格的年产水量（mm）；Ax— 每个 x 栅格的年际蒸散量（mm）；Rx— 栅格 x 的年降水量（mm）

# 2.1.3 生境质量

采用 InVEST 模型中的生境质量模块（HabitatQuality，HQ）进行该地区生境质量的评估，模型中运行所需的参数参考相关地区已有的研究（张小瑜等，2024）进行赋值，计算公式如下：

![](images/486086a72cc39e3b4b05c054b8537c7ab1aee64dc71aeaec17794bac997d5203.jpg)

式中：

Hij — 土地利用类型 j中 x 栅格的生境质量；  
Hj — 土地利用类型 j 的生境适宜度；  
Dxj — 土地利用类型j中x栅格的生境退化度；  
k— 半饱和常数；  
z— 模型默认参数。

# 2.1.4 碳储量服务

InVEST 模型的碳储量模块（Carbon Storage，CS）包含地上生物量、地下生物量、土壤碳和死亡有机碳等 4个碳库的大小（王启名等，2023）。参考前人得到的碳密度情况（虎帅等，2018）计算不同土地利用类型的对应平均碳密度的总和，其计算公式如下：

![](images/fbd5bc116fabf6957c0091f86f333db39ccbdaa221d0b41f5eba96c0612bff91.jpg)

![](images/6ea0f7b1436f2d6b130b2f7707f62f25fd56d57b6ac9ed0c5bcccc161e82130b.jpg)

式中：

Ct— 总碳储量（t·hm−2 ）；  
Ca— 地上生物碳储量（t·hm−2 ）；  
Cb— 地下生物碳储量（t·hm−2 ）；  
Cs— 土壤碳储量（t·hm−2 ）；  
Cd— 死亡有机碳储量（t·hm−2 ）；  
i— 土地利用类型；  
Si — 土地利用类型 i 的面积。

# 2.2 地理探测器

地理探测器是一种用于量化地理现象空间差异性并揭示其驱动因素的统计分析方法（王劲峰等，2017）。本文使用地理探测器中的单因子探测和交互作用探测模块，借助 R 语言中的“GD”包，分析驱动因素对生态系统服务的时空变化的影响机制。根据研究区的自然地理特征、生态系统服务的关键影响因素及数据可行性，并参考相关前人研究（张维琛等，2024），选取如表 1 的驱动因子，并对其选择依据进行说明。为定量衡量各驱动因子对生态系统服务的影响，本文采用 q 值作为衡量指标，其物理意义在于量化驱动因子对地理现象空间异质性的解释力，取值范围为[0, 1]，取值越大，表明该因子对空间异质性的解释力越强，影响越显著；反之，则影响较小。在交互作用探测采用 q 值来衡量两个因子互动对空间异质性的共同解释力。

具体计算公式如下：

![](images/4e52e0ff6b50282b5c604fa820f102589d8d704a97c35f7a1d7bc0ef05b0beae.jpg)

式中：

h=1, 2, …；

L——变量 Y或因子 X 的分层；  
N——第 h 层和全区的单元数；  
σ2和σ2——h 层和全区的方差。

# 2.3 权衡协同分析

# 2.3.1 Pearson 相关性分析

本文采用改进的 Pearson 相关分析法（陈心盟等，2021）分析该研究区的权衡协同情况，利用 R语言计算 2000、2010 和 2020 年等3 个时段各类生态服务之间的相关性系数并进行显著性检验（王奕淇等，2025），并绘制相关性热图。计算公式如下：

![](images/9ff9bf0e99e39ead27e7ace908ee0a1111560f485b2efd065c7039da375241f2.jpg)

式中：

R——相关系数；  
A 和 B——两类生态系统服务变量；  
A-和B-——A 和B 变量的平均值；  
i——年份；  
n— 样本量。当 R>0，表示两类生态服务之间协同关系；R<0，表示为权衡关系。

# 2.3.2 空间自相关分析法

利用 GeoDA和 ArcGIS 软件，以嘉陵江流域的县域为基本单元，使用双变量 Moran’s I 指数来衡量研究区各生态系统服务之间的空间依赖关系（庞彩艳等，2024）。

表 1 地理探测因子的选取  
Table 1 Selection of geographic detection factors   

<table><tr><td>编号</td><td>因素类别</td><td>影响因素</td><td>选取理由</td></tr><tr><td>X</td><td>地形地貌</td><td>高程</td><td>高程与坡度共同影响区域气候、水文过程及植被分布，调节地表径流与土壤侵蚀强度，决定</td></tr><tr><td>X</td><td></td><td>坡度</td><td>了生态系统服务的空间分布格局</td></tr><tr><td>X</td><td>植被</td><td>归一化植被指数(NDVI)</td><td>反映了植被覆盖率</td></tr><tr><td>X4</td><td>气候</td><td>年平均气温</td><td>气温和降水作为气候变化的关键指标，通过调节水热条件、影响植被生长环境及区域水文过</td></tr><tr><td>X5</td><td></td><td>年平均降水量</td><td>程，对生态系统服务的供给和空间分布产生重要影响</td></tr><tr><td>X6</td><td>人为因素</td><td>土地利用情况</td><td>土地利用类型直接决定生态系统服务的功能分布；GDP 和人口密度共同反映了经济发展水平</td></tr><tr><td>X7</td><td></td><td>国内生产总值（GDP)</td><td>和人类活动强度，城镇扩张、资源开发及高密度人类活动可能导致土地资源过度利用，显著</td></tr><tr><td>X8</td><td></td><td>人口密度</td><td>影响生态系统服务的供给与调节能力</td></tr></table>

![](images/a63e73e15071be5fe0b4eca0654d0fd0f3cdbe388c15f16b54135a485df705f3.jpg)

式中：

Mi ——局部莫兰指数；  
n— 空间单元总数；

Yi和 Yk——第 i 和第 k 空间单元的生态系统服务值；Y-为所有空间单元生态系统服务值的平均值；gik— 空间权重矩阵中的元素，表示空间单元i 与 k 的空间关联性。

# 2.3.3 地形位指数

地形位指数是一个综合高程与坡度信息的指标，用于反映区域地形的空间分异特征。本文基于地形位指数，参考前人研究成果（胡孟珂等，2022），采用自然间断法将研究区域划分为 5 个梯度等级，并进行不同等级区域内生态系统服务权衡协同情况的分析。具体公式如下：

![](images/31292b5b4bb4922bf7766eafa08fe5bd8cf732384279a8b6ccb15700b0c7b465.jpg)

式中：

T——地形位指数；

E 和E-— 某个栅格单元内的高程和平均高程；

F和F-——某一栅格单元内的坡度和平均坡度。高程和坡度越大，地形位指数越大；反之则越小；高程大坡度小和高程小坡度大的则位于地形位指数中间值。

# 3 研究结果和分析

# 3.1 嘉陵江流域生态系统服务时空动态变化特征分析

从 2000－2020 年嘉陵江流域 4 类生态系统服务的变化情况（图 2 和表 2），分析如下：

嘉陵江流域的土壤保持量从2486.3 t·hm−2增至3 125.6 t·hm−2 ，2000－2010 年期间增幅 18.4%，2010－2020 年增长 6.2%。空间上土壤保持服务量呈现“东南、西北高，南北低”的格局。高值区集中在南充西充县、广元昭化区和巴中南江县等地，这些地区地势陡峭、植被覆盖良好，治理措施得力，且人为对植被覆盖良好地区扰动较少，因此土壤保持量高。低值区则位于流域中下游的平原和城镇化区域，因地势平坦农田占比大且作物对土壤保持能力弱，所以在时间维度上变化较小，基本保持稳定。

产水服务在 2000－2020 年间显著提升。产水量从 2000 年的 2 596.8 m3 ·hm−2 增加到 2020 年的5736.5 m3 ·hm−2 ，南部高值区如渠县和邻水县的增幅超过 30%，而北部地区的增长则相对较小，约为10%。产水服务呈现“南高北低”的分布格局。南部地区如达州渠县、广安邻水县和巴中恩阳区等地，因降水充沛，地形和植被有利于水源涵养，产水服务量较高。而在北部的高海拔地区，如甘肃舟曲县、陇南大部分区县，由于降水量相对较少，且地势较高，产水服务量较低。

从 2000－2020 年，嘉陵江流域的生境质量整体上略有下降。高值区主要分布在流域的西北、东北部及中部山区，例如广元青川县和巴中通江县等地，生境质量长期保持在“较高”或“高”水平，指数达 0.65以上。相比之下，南部区域受成渝经济圈的人类活动影响较大，生境质量相对较低，指数多在 0.45－0.50 之间。碳储量和生境质量的整体分布趋势较为相似，2000－2020 年间碳储量变化不大，高值区域集中在流域西北部和的甘南藏族自治州和陇南市部分地区，低值区则主要位于流域南部的南充、遂宁和重庆片区，碳储量相对较低。

# 3.2 嘉陵江流域生态系统服务变化归因分析

本文在综合前人的研究成果的基础上，考虑到地形、气候、植被覆盖和人类活动等多种情况选取了如表 1 的所示的 8 种驱动因子，利用地理探测器对嘉陵江流域生态系统服务驱动力进行分析。

# 3.2.1 单因子探测

如图 3 显示，嘉陵江流域的生境质量在各年份中主要受到土地利用的显著影响，q 值从 2000 年的 0.79 和 2010 年的 0.83 上升至 2020 年接近 0.90。此外，年平均气温、GDP和植被覆盖度对生境质量也有较高的 q 值，说明气候条件和人类活动对其影响显著。随着时间推移，人类活动相关因子（如GDP、人口密度）的 q 值逐步上升，反映出生境质量受人类活动干扰的增加。土壤保持服务主要受地形因素和年降雨量的影响较大，地形因素中坡度的影响最为显著，q 值在 2000、2010 和 2020 年分别为 0.30、0.21 和 0.33。此外，年降雨量和植被覆盖也是土壤保持的重要影响因素，降水量的变化是影响土壤侵蚀程度的重要因素，而植被覆盖则能有效减少土壤侵蚀，从而提升土壤保持能力。产水量的主要影响因子是年降雨量和高程。年降雨量的 q 值则从 2000 年的 0.56 增加至 2020 年的 0.59，降雨量的变化直接影响水源补给，高程值的 q 值从 2000－2020 年 3 年的 q 值分别为 0.48，0.46，0.44，高程则决定了地表径流和水源涵养的空间分布。除此以外，人类活动对产水量的影响逐渐加大，GDP和土地利用的 q 值从 2000－2020 年均有不同程度的上升，反映出经济发展对水资源的依赖性增加。碳储量的空间分布主要受植被覆盖度、年降雨量和土地利用的影响。在各年份中，植被覆盖度的 q 值较高，分别为 0.28、0.32 和 0.34，表明植被分布和类

![](images/ae4a3ceb69b5976ffda5c1cf9c286a786d1873779b04ee682e16fc2107993bcd.jpg)  
（a）土壤保持

![](images/be1461762e78c7a60e5117d039bfe5f78efc7340e8f53384cf24fc17f3cd4f72.jpg)  
（b）产水服务

![](images/173140ca0fa810d5c2256992b90687776aa6978c97ac0a7ec164b8952f7695d2.jpg)  
（c）生境质量

![](images/a9a6001e50e1cadec2b2e09ff64c4d667ca12e8ddf5fede7ec19da2de3755ce7.jpg)  
图 2 2000－2020 年嘉陵江流域生态系统服务时空分布格局

Figure 2 The spatial and temporal distribution pattern of ecosystem services in the Jialing River Basin from 2000 to 2020型对碳储量至关重要。随着时间推移，土地利用的影响逐渐增强，反映出土地利用变化对区域碳储量的潜在影响。

# 3.2.2 交互因子探测

如图 4 可知，嘉陵江流域的生态系统服务交互因子分析结果表明，不同服务对自然因子和社会经

# 表 2 2000－2020 年嘉陵江流域生态系统服务量

Table 2 The ecosystem service values in the Jialing River Basin from 2000 to 2020   

<table><tr><td>年份</td><td>土壤保持量/ (t:hm-2)</td><td>产水量/ (m³hm-2)</td><td>生境质量 指数</td><td>碳储存量(以C计)/ (Mg·hm-2)</td></tr><tr><td>2000</td><td>2 486.3</td><td>2 596.8</td><td>0.56</td><td>272</td></tr><tr><td>2010</td><td>2 944.5</td><td>3 879.6</td><td>0.54</td><td>278</td></tr><tr><td>2020</td><td>3125.6</td><td>5736.5</td><td>0.52</td><td>281</td></tr></table>

济因子的响应差异显著。土壤保持服务受坡度与植被覆盖度的交互作用影响，q 值达到 0.45，说明在坡度较大的区域，植被覆盖能够显著减少土壤侵蚀，增强土壤保持能力。同时，坡度与降水量的交互作用 q 值为 0.39，反映了降水在不同坡度下对土壤流失的不同影响。产水服务主要受高程与降水量的交互作用 q 值为0.42，显示出在较高海拔和降水丰富的地区，产水服务具有较强的稳定性和持久性。此外，坡度与植被覆盖度的交互作用影响，q值为 0.35，表明在地形较为陡峭且植被覆盖良好的区域，水源涵养能力较强。碳储量则主要由植被覆盖度和降水量的交互作用决定，q 值为 0.52，说明植被在碳吸收和储存中的关键作用，尤其在降水充足的情况下能够进一步提升碳储量。此外，植被覆盖度与坡度的交互作用 q值为 0.49，显示坡度和植被的结合对碳储量分布也有重要影响，特别是在坡度较大且植被丰富的地区，碳储量相对较高。生境质量则显著受到土地利用与植被覆盖度的交互作用影响，q 值为 0.74，这表明土地利用方式和植被覆盖度对生境质量的空间分布具有重要影响，特别是在土地利用方式优化、植被良好的区域，生境质量相对较高。此外，高程与土地利用的交互作用 q 值为 0.68，也表明自然因子在一定程度上影响生境的空间分布，尤其在高海拔、植被较好的区域，生境质量相对更高。

# 3.3 嘉陵江流域生态系统服务权衡协同变化分析

# 3.3.1 嘉陵江流域全域权衡协同关联特征

经过 R 平台运行后得到 2000－2020 年嘉陵江流域 4 类生态系统服务之间存在不同的相关关系（如图 5），其均通过 0.01 显著性检验。从 2000－2020 年，产水服务与碳储量始终表现出负相关关系，这表明在嘉陵江流域，产水服务的增加往往伴随着碳储量的减少，两者之间存在较为稳定的权衡关系。碳储量与生境质量均呈现出显著的正相关，这说明碳储量的增加有助于生境质量的提升，两者之间存在较为稳固的协同关系。土壤保持与生境质量均表现为正相关，且相关性逐步增强，显示出两者之间的协同效应逐渐显现。这表明随着时间的推移，土壤保持对生境质量的贡献逐渐增加，二者的协同关系不断加强。土壤保持与碳储量之间的相关性相对较低，但在 2000年和 2010 年之间呈现正相关，而在 2020 年时略有减弱。

![](images/32da551bc624223cb4e734270dc09a7a8cca5eb36444b52ee352cf92fba1f4fe.jpg)  
图 3 2000－2020 年嘉陵江流域生态系统服务单因子探测统计结果  
Figure 3 Single-factor detection statistics for ecosystem services in the Jialing River Basin from 2000 to 2020

![](images/29278ca4c3e44d0081634e0b64d7d24f63d083eb02857189f48bd4a86905642d.jpg)  
图 4 2000－2020 年嘉陵江流域生态系统服务交互因子探测结果

![](images/48caa09bb5e913e10dbf76487dcc7d45d1f42a869cefb71d8ed18e8f5693719b.jpg)  
Figure 4 Interaction Factor Detection Results for Ecosystem Services in the Jialing River Basin from 2000 to 2020   
图 5 2000－2020 年嘉陵江流域全域生态系统服务相关系数  
Figure 5 Correlation coefficients of ecosystem services in the Jialing River Basin from 2000 to 2020

# 3.3.2 权衡协同空间特征

以嘉陵江流域县区为单元，使用双变量Moran’s I指数空间自相关法，将各类生态系统服务的权衡协同关系特征的集聚与分散，按照高高集聚、低低集聚关系为协同关系，高低集聚与低高集聚为权衡关系，又按照不同程度划分为不同级别：

不显著、低权衡、较低权衡、中等权衡、较高权衡、高权衡；低协同、较低协同、中等协同、较高协同、高协同。如图 6 所示的嘉陵江流域整体空间分异特征，总体上看协同权衡的高值和低值主要集中在流域的西北部和东南部，呈现西北至东南的倾斜。产水量与碳储量和生境质量与产水量的强权衡关系主要集中在阿坝藏族羌族自治州若尔盖县、九寨沟以及甘南藏族自治州舟曲县，低权衡主要分布在南部绵阳、遂宁重庆境内的诸多县区。而产水量与土壤保持的高权衡与低权衡的分布格局与前者正好相反，高权衡主要集中在东南部如广安岳池县、重庆城口县等诸多区县。土壤保持与碳储量、土壤保持与生境质量和碳储量与生境质量的强协同关系均集中在北部和东部的区县，如北部甘肃境内的陇南宕昌县和礼县等，达州的宣汉县、万源市等地。

![](images/db0d495be8c72280fa862bee7780955de7e50940a4283fe8b5a5291e2fb78463.jpg)  
图 6 嘉陵江流域生态系统服务权衡协同程度空间分布  
Figure 6 Spatial distribution of trade-offs and synergies in ecosystem services in the Jialing River Basin

# 3.3.3 嘉陵江流域地形梯度分区下权衡协同关联特征

以 2020 年嘉陵江流域为例分析，各地形梯度区的各类生态系统服务相关性与以全域分析的关系差异显著（如图 7）。且在不同地形梯度区内，生态系统服务之间的关系及其强度因梯度类型和空间位置的不同而呈现差异性。2000－2020 年的全域各个服务之间的权衡协同关系是相对均衡的，而在 1 级地形梯度区，各生态服务之间的相互作用总体较弱，其中产水服务与碳储量的协同关系最为显著，相关系数为 0.331，而碳储量与生境质量的权衡关系最强，相关系数为−0.292。2 级地形梯度区，以弱协同为主，其中产水服务与生境质量为 0.252，弱协同较为突出，碳储量与生境质量之间为−0.510，表现出显著的权衡关系。3 级和 4 级地形梯度区协同特征较强，产水服务与土壤保持在 3 级和4级均表现出显著协同，相关系数分别为 0.492 与0.531；5 级地形梯度区则以权衡关系为主，产水服务与生境质量为−0.331，碳储量与生境质量为−0.271，均表现为显著权衡。

# 4 讨论

本研究结合郭丹等（2022）对嘉陵江流域主要生态环境问题的剖析，以平衡生态环境保护与经济发展为目标，分析了土壤保持、碳储量、产水量和生境质量等4类关键生态系统服务的时空变化以及驱动因素，并从全域以及以地形梯度分区下权衡协同关系以及空间分布。

# 4.1 生态系统服务时空动态变化与驱动因素

研究表明，嘉陵江流域在过去 20 年间土壤保持服务和产水量均有不同程度的提升。土壤保持服务空间分布变化与产水量分布变化趋势一致，其高值区域均由流域东南向西北逐渐转移。结合驱动因素分析，这一趋势可能是受降雨变化的影响，这与张竞哲等（2023）对于嘉陵江流域的降雨侵蚀力分布变化基本一致。而生境质量和碳储量的变化主要集中在南部城市群集中的区域。碳储量呈增长趋势，而生境质量则有所下降。两者虽均受到植被覆盖和土地利用的显著影响，但是影响机制存在差异。通过探测驱动因子发现，碳储量的变化主要受到植被覆盖驱动，植被覆盖度高的地方碳储量更佳；而生境质量方面，土地利用的影响高于植被覆盖度，这与张小瑜等（2024）的研究具有相似性，但是不同于刘如龙等（2024）认为黄河流域生境质量受地形影响最高的结论，这一差异可能源于嘉陵江流域受人类活动干扰强度不同，使得土地利用变化对生境质量的影响更加显著。

![](images/bc7e9f19dda29b2c645be424b18d654941590b6c65cbd41b4c6568c7cad449a3.jpg)  
图 7 嘉陵江流域各地形梯度分区生态系统服务权衡协同相关系数 Figure 7 Trade-offs and synergies correlation coefficients of ecosystem services in different topographic gradient zones of the Jialing River Basin

# 4.2 生态系统服务权衡协同关系

嘉陵江流域的高协同和高权衡区通常集中分布，而在其他流域的研究中（杨强强等，2021；张继平等，2025）呈现出更为交错复杂的多热点分布格局，这种差异可能与研究的空间尺度及影响因素的空间分布差异密切相关（庞彩艳等，2024）。所以本文进一步通过全域与地形梯度分区进行对比，揭示了不同尺度的下生态系统服务的权衡协同关系。在全域分析中，产水量与碳储量在过去 20 年基本上维持权衡关系，而在地形梯度分区中除了 2 级分区外，均显示协同关系；碳储量和生境质量、产水和土壤保持与全域表现相反，而其他服务的关系中除了个别区域，基本与全域关系一致。在不同分区中，同样的生态系统服务关系因所处地形梯度分区的不同而表现出显著差异。碳储量和产水服务在2 级分区内表现为权衡，其他均表现为协同；生境质量和产水服务在 5 级分区表现为权衡，其余则为协同。表明，不同地形梯度分区的人类活动强度、土地利用类型和资源禀赋存在显著差异，从而对生态系统服务关系的空间分布产生重要影响（袁乐等，2024）。

# 4.3 区域生态系统服务优化建议

嘉陵江流域的生态系统服务优化需综合考虑其时空异质性及全域与分区视角下的权衡与协同关系，因地制宜地采取科学管理措施。基于本文研究结果和四川、重庆、陕西、甘肃四省市《国土空间规划（2021－2035 年）》的相关内容，提出如下优化建议：

地形梯度1级区域以川东北经济区和重庆主城都市区为主，包括南充、遂宁、广安和重庆等成渝城市群。该区域是人口和城镇化程度较高的核心区，人类活动频繁。建议统筹城镇、农业和生态功能，协调碳储量和水资源利用，合理规划人口和城镇规模。具体而言，应通过基于自然的解决方案（NbS）协同推进生态、生产、生活的高效融合，以提升区域产水服务和碳储量，优化城镇发展与生态系统服务的平衡。

2 级分区的中游丘陵地带主要分布着四川盆地的粮油主产区，应加强耕地的休耕修复，发展高标准农田，提升土壤保持能力。降低农业空间的利用强度，避免不合理的耕作方式，提升区域内部的生境质量。

3 级分区和 4 级分区覆盖川东平行岭谷和秦巴山地生态功能区， 包括唐家河大熊猫国家公园等重要的国家级生态保护区。建议依托现有良好的生境条件，强化该区域的生态保护制度，进一步提升生境质量与碳储量的协同关系。在优化植被覆盖和合理土地利用的基础上，加强产水服务与土壤保持的协同管理，推动生态系统服务的可持续供给。

5 级分区则主要以若尔盖等多个国家生态公园为代表的生态保护区，应严格控制开发活动，重点加强资源保护与管理。通过综合碳汇管理和水土资源保护，减少产水服务对生境质量的负面影响，促进区域碳储量与水土保持的协同效应，提升生态系统服务供给能力。通过区域功能分区与精细化管理的结合，可有效实现生态系统服务的协同提升，为嘉陵江流域的高质量发展奠定坚实基础。

# 4.4 不足和展望

在探究生态系统服务变化时，应用 InVEST 模型的参数选择和驱动因素的设定可能存在一定的主观性，尤其是在获取驱动因素时，依赖各省市统计年鉴数据也可能引入不确定性。此外，本文仅从全域和地形梯度分区上分析了生态系统服务的协同与权衡关系，未来研究可以进一步深入探讨不同空间尺度下权衡协同关系的响应特征，并分析不同权衡协同关系背后的驱动机制。未来研究应从模型优化、多尺度分析和驱动机制探索等方面进一步深化，以便更全面、准确地揭示生态系统服务的权衡协同机制。

# 5 结论

本文基于嘉陵江流域 2000、2010 和 2020 年三期数据，利用 InVEST 模型分析了生态系统服务时空动态变化，并通过地理探测器识别了影响这些变化的驱动因子。从全域与分区视角，结合相关性分析、双变量空间自相关法，探讨了生态系统服务的权衡协同关系及空间分异特征。主要研究结论如下：

1）嘉陵江流域的生态系统服务整体呈现“整体上升、局部平稳”的特征。土壤保持和产水服务增长较显著，但空间分布不同。土壤保持高值区集中在地势陡峭、植被良好的东南和西北地区，而产水服务呈“南高北低”格局，高值区位于降水充沛的南部。生境质量略有下降，受人类活动影响较大；碳储量相对稳定，空间分布与生境质量类似，高值区集中在植被覆盖度高的西北和东南区域，而低值区则在成渝经济圈的城镇集中的区域。

2）嘉陵江流域生态系统服务在自然因子和人类活动的多重驱动下发生变化。单因子分析显示，生境质量主要受土地利用和植被覆盖度影响，土壤保持依赖坡度和降水，产水量主要受到降水和高程影响，碳储量则与植被和降水相关。交互因子分析揭示，土壤保持在坡度与植被协同下增强，产水服务在坡度与降水交互中稳定性提升，碳储量与生境质量分别受植被与降水、土地利用的协同作用显著影响。

3）嘉陵江流域生态系统服务的权衡协同关系在时间、空间以及不同地形梯度区呈现显著差异。2000－2020年间，全域范围内产水服务与碳储量呈稳定的权衡关系，碳储量与生境质量、土壤保持与生境质量则表现为稳固的协同关系，且协同效应逐渐增强。空间上，权衡与协同特征呈现西北至东南倾斜，高权衡区集中于西北部，强协同区分布于北部和东部。地形梯度分区分析显示，不同梯度区的生态服务关系显著差异，1 级区相互作用较弱，3 级和 4 级区协同增强，5 级区以权衡为主。

# 参考文献：

BAGSTAD K J, SEMMENS D J, WAAGE S, et al., 2013. A comparative assessment of decision-support tools for ecosystem services quantification and valuation [J]. Ecosystem Services, 5: 27-39.   
BOYD J, BANZHAF S, 2007. What are ecosystem services? The need for standardized environmental accounting units [J]. Ecological Economics, 63(2-3): 616-626.   
CARPENTER S R, MOONEY H A, AGARD J, et al., 2009. Science for managing ecosystem services: Beyond the millennium ecosystem assessment [J]. Proceedings of the National Academy of Sciences of the United States of America, 106(5): 1305-1312.   
CHEN X, SIVAPALAN M, 2020. Hydrological basis of the Budyko curve: Data-guided exploration of the mediating role of soil moisture [J]. Water Resources Research, 56(10): WR028221.   
COSTANZA R, DARGE R, GROOT R, et al., 1998. The value of the world’s ecosystem services and natural capital [J]. Ecological Economics, 25(1): 3-15.   
CUMMING G S, BUERKERT A, HOFFMANN E M, et al., 2014. Implications of agricultural transitions and urbanization for ecosystem services [J]. Nature, 515: 50-57.   
HASSAN R M, SCHOLES R, ASH N, 2005. Ecosystems and human wellbeing: Biodiversity synthesis [M]. Washington DC: Island Press.   
PENG J, XIA P, LIU Y X, et al., 2023. Ecosystem services research: From golden era to next crossing [J]. Transactions in Earth, Environment, and Sustainability, 1(1): 9-19.   
陈心盟, 王晓峰, 冯晓明, 等, 2021. 青藏高原生态系统服务权衡与协同 关系[J]. 地理研究, 40(1): 18-34. CHEN X M, WANG X F, FENG X M, et al., 2021. Ecosystem service trade-off and synergy on Qinghai-Tibet Plateau [J]. Geographical Research, 40(1): 18-34.   
戴尔阜, 王晓莉, 朱建佳, 等, 2016. 生态系统服务权衡: 方法、模型与 研究框架[J]. 地理研究, 35(6): 1005-1016. DAI E F, WANG X L, ZHU J J, et al., 2016. Methods, tools and research framework of ecosystem service trade-offs [J]. Geographical Research, 35(6): 1005-1016.   
戴尔阜, 王亚慧, 2020. 横断山区产水服务空间异质性及归因分析[J]. 地理学报, 75(3): 607-619. DAI E F, WANG Y H, 2020. Spatial heterogeneity and driving mechanisms of water yield service in the Hengduan Mountain region [J]. Acta Geographica Sinica, 75(3): 607-619.   
董鑫, 李艳忠, 董亭忆, 等, 2024. 基于 GEE的嘉陵江流域生态环境质量 演 变 及 驱 动 因 子 分 析 [J/OL]. 广 西 科 学 , 1-12 [2025-3-24]. https://doi.org/10.13656/j.cnki.gxkx.20240912.001. DONG X, LI Y Z, DONG T Y, et al., 2024. Analysis of Long-term Dynamic Evolution Characteristics and Driving Mechanism of Ecological Environment Quality in the Jialing River Basin Based on GEE [J/OL]. Guangxi Sciences, 1-12 [2025-3-24]. https://doi.org/ 10.13656/j.cnki.gxkx.20240912.001.   
傅伯杰, 2010. 我国生态系统研究的发展趋势与优先领域[J]. 地理研究, 29(3): 383-396. FU B J, 2010. Trends and priority areas in ecosystem research of China [J]. Geographical Research, 29(3): 383-396.   
傅伯杰, 于丹丹, 2016. 生态系统服务权衡与集成方法[J]. 资源科学, 38(1): 1-9. FU B J, YU D D, 2016. Trade-off analyses and synthetic integrated method of multiple ecosystem services [J]. Resources Science, 38(1): 1-9.   
傅伯杰, 张军泽, 2024. 全球及中国可持续发展目标进展与挑战[J]. 中 国科学院院刊, 39(5): 804-808. FU B J, ZHANG J Z, 2024. Progress and challenges of Sustainable Development Goals (SDGs) in the World and in China [J]. Bulletin of Chinese Academy of Sciences, 39(5): 804-808.   
高雅玉, 宋玉, 赵廷红, 等, 2024. 马莲河下游产水量时空演变特征[J]. 干旱区研究, 41(5): 776-787. GAO Y Y, SONG Y, ZHAO T H, et al., 2024. Spatiotemporal evolution of water yield in the lower Malian River Basin [J]. Arid Zone Research, 41(5): 776-787.   
郭丹, 蒋进元, 李莹杰, 等, 2022. 嘉陵江流域主要生态环境问题识别及 建议[J]. 环境保护, 50(17): 33-36. GUO D, JIANG J Y, LI Y J, et al., 2022. Main problems and countermeasures of ecological environment in Jialing River Basin [J]. Environmental Protection, 50(17): 33-36.   
郭宗亮, 刘亚楠, 张璐, 等, 2022. 生态系统服务研究进展与展望[J]. 环 境工程技术学报, 12(3): 928-936. GUO Z L, LIU Y N, ZHANG L, et al., 2022. Research progress and prospect of ecosystem services [J]. Journal of Environmental Engineering Technology, 12(3): 928-936.   
韩会庆, 张娇艳, 马庚, 等, 2018. 气候变化对生态系统服务影响的研究 进展[J]. 南京林业大学学报(自然科学版), 42(2): 184-190. HAN H Q, ZHANG J Y, MA G, et al., 2018. Advances on impact of climate change on ecosystem services [J]. Journal of Nanjing Forestry University (Natural Sciences Edition), 42(2): 184-190.   
韩磊, 高毅丰, 常钰卿, 等, 2024. 黄土高原城镇化与生态系统服务脱钩 关系[J]. 生态学报, 44(20): 9108-9121. HAN L, GAO Y F, CHANG Y Q, et al., 2024. Decoupling relationship between urbanization and ecosystem services on the Loess Plateau [J]. Acta Ecologica Sinica, 44(20): 9108-9121.   
胡孟珂, 于欢, 孔博, 等, 2022. 2001－2020 年嘉陵江流域植被覆盖度时 空变化特征[J]. 人民长江, 53(1): 82-89, 96. HU M K, YU H, KONG B, et al., 2022. Spatial-temporal variations of fractional vegetation coverage in Jialing River Basin from 2001 to 2020 [J]. Yangtze River, 53(1): 82-89, 96. 碳储量变化分析[J]. 水土保持研究, 25(3): 323-331. HU S, ZHANG X R, GUAN D J, 2018. Analysis on carbon storage change of construction land expansion in Chongqing based on InVEST Model [J]. Research of Soil and Water Conservation, 25(3): 323-331.   
李双成, 张才玉, 刘金龙, 等, 2013. 生态系统服务权衡与协同研究进展 及地理学研究议题[J]. 地理研究, 32(8): 1379-1390. LI S C, ZHANG C Y, LIU J L, et al., 2013. The tradeoffs and synergies of ecosystem services: Research progress, development trend, and themes of geography [J]. Geographical Research, 32(8): 1379-1390.   
李婷, 吕一河, 2018. 生态系统服务建模技术研究进展[J]. 生态学报, 38(15): 5287-5296. LI T, LÜ Y H, 2018. A review on the progress of modeling techniques in ecosystem services [J]. Acta Ecologica Sinica, 38(15): 5287-5296.   
廖洪圣, 卫伟, 石宇, 2024. 黄土丘陵区典型流域土壤侵蚀时空演变特征 及其驱动机制: 以祖厉河为例[J]. 生态环境学报, 33(6): 908-918. LIAO H S, WEI W, SHI Y, 2024. Characteristics of spatial and temporal evolution of soil erosion in typical watersheds in Loess Hilly Areas and its driving mechanisms: A case study of Zuli River [J]. Ecology and Environmental Sciences, 33(6): 908-918.   
刘如龙, 赵媛媛, 陈国清, 等, 2024. 内蒙古黄河流域 1990－2020 年生 境质量评估[J]. 干旱区研究, 41(4): 674-683. LIU R L, ZHAO Y Y, CHEN G Q, et al., 2024. Assessment of habitat quality in the Yellow River Basin in Inner Mongolia from 1990 to 2020 [J]. Arid Zone Research, 41(4): 674-683.   
刘月, 赵文武, 贾立志, 等, 2019. 土壤保持服务: 概念、评估与展望[J]. 生态学报, 39(2): 432-440. LIU Y, ZHAO W W, JIA L Z, et al., 2019. Soil conservation service: Concept, assessment, and outlook [J]. Acta Ecologica Sinica, 39(2): 432-440.   
潘竟虎, 李真, 2017. 干旱内陆河流域生态系统服务空间权衡与协同作 用分析[J]. 农业工程学报, 33(17): 280-289. PAN J H, LI Z, 2017. Analysis on trade-offs and synergies of ecosystems services in arid inland river basin [J]. Transactions of the Chinese Society of Agricultural Engineering, 33(17): 280-289.   
庞彩艳, 文琦, 丁金梅, 等, 2024. 黄河上游流域生态系统服务变化及权 衡与协同关系研究[J]. 生态学报, 44(12): 5003-5013. PANG C Y, WEN Q, DING J M, et al., 2024. Ecosystem services and their trade-offs and synergies in the upper reaches of the Yellow River basin [J]. Acta Ecologica Sinica, 44(12): 5003-5013.   
石秀秀, 2021. 习近平总书记关于长江经济带绿色发展重要论述研究 [D]. 武汉: 中国地质大学: 1-182. SHI X X, 2021. Research on the general Secretary Xi Jinping’s important discourse on green development of the Yangtze River economic belt [D]. Wuhan: China University of Geosciences: 1-182.   
孙彦, 蔺星娜, 李生, 等, 2024. 贵州省生态系统服务权衡时空动态与驱 动因子评估[J]. 环境科学学报, 44(9): 401-413. SUN Y, LIN X N, LI S, et al., 2024. Spatiotemporal dynamics and driving factor assessment of ecosystem service trade-offs in Guizhou Province [J]. Acta Scientiae Circumstantiae, 44(9): 401-413.   
谭晶华, 张运春, 张桥英, 等, 2024. 嘉陵江生态环境研究回顾与展望— 基于文献计量的可视化分析[J]. 西华师范大学学报(自然科学版), 45(1): 9-16. TAN J H, ZHANG Y C, ZHANG Q Y, et al., 2024. Review and prospect of ecological environment research on the Jialing River: visualized analysis based on bibliometric [J]. Journal of China West Normal University (Natural Sciences), 45(1): 9-16.   
王劲峰, 徐成东, 2017. 地理探测器: 原理与展望[J]. 地理学报, 72(1): 116-134. WANG J F, XU C D, 2017. Geodetector: Principle and prospective [J]. Acta Geographica Sinica, 72(1): 116-134.   
王启名, 杨昆, 李立晓, 等, 2023. 滇池流域水文生态系统服务权衡与协 同时空异质性及其归因分析[J]. 生态学报, 43(12): 4876-4891. and attribution analysis of hydrological ecosystem services trade-offs and synergies in Dianchi Lake Basin [J]. Acta Ecologica Sinica, 43(12): 4876-4891.   
王万忠, 焦菊英, 1996. 中国的土壤侵蚀因子定量评价研究[J]. 水土保 持通报 (5): 1-20. WANG W Z, JIAO J Y, 1996. Quantitative evaluation on factors influencing soil erosion in China [J]. Bulletin of Soil and Water Conservation (5): 1-20.   
王奕淇, 孙学莹, 2025. 黄河流域生态系统服务权衡协同关系及其时空 异质性[J]. 环境科学, 46(2): 972-989. WANG Y Q, SUN X Y, 2025. Trade-off and synergy of ecosystem services in the Yellow River Basin and their spatiotemporal heterogeneity [J]. Environmental Science, 46(2): 972-989.   
文志, 郑华, 欧阳志云, 等, 2020. 生物多样性与生态系统服务关系研究 进展[J]. 应用生态学报, 31(1): 340-348. WEN Z, ZHENG H, OUYANG Z Y, et al., 2020. Research progress on the relationship between biodiversity and ecosystem services [J]. Chinese Journal of Applied Ecology, 31(1): 340-348.   
杨强强, 徐光来, 李爱娟, 等, 2021. 青弋江流域生态系统服务评估与权 衡研究[J]. 生态学报, 41(23): 9315-9327. YANG Q Q, XU G L, LI A J, et al., 2021. Evaluation and trade-off of ecosystem services in the Qingyijiang River Basin [J]. Acta Ecologica Sinica, 41(23): 9315-9327.   
袁乐, 阿不都克依木·阿布力孜, 于苏云江·吗米提敏, 等, 2024. 基于生 态系统服务簇的生态功能区权衡与协同关系演变: 以吐哈地区为 例[J/OL]. 环境科学, 1-21 [2025-3-24]. https://doi.org/10.13227/j.hjkx. 202404272. YUAN L, ABULIZI A, MAMITIMIN Y, et al., 2024. Evolution of trade-offs and synergies in eco-functional zones based on ecosystem service bundles: A case study of the Turpan-Hami region [J/OL]. Environmental Science, 1-21 [2025-3-24]. https://doi.org/10.13227/ j.hjkx.202404272.   
张继平, 刘春兰, 王辉, 等, 2025. 基于生态系统服务及其权衡关系时空 演变特征的生态功能分区研究: 以潮白河流域为例[J]. 生态与农村 环境学报, 41(1): 61-71. ZHANG J P, LIU C L, WANG H, et al., 2025. Ecological function zoning based on the spatial-temporal change pattern of ecosystem services and their trade-offs: A Case study of the Chaobai River basin [J]. Journal of Ecology and Rural Environment, 41(1): 61-71.   
张竞哲, 莫淑红, 蒋凯鑫, 等, 2023. 基于模型适用性分析的嘉陵江流域 降雨侵蚀力时空演变特征[J/OL]. 西安理工大学学报, 1-9 [2025-3- 24]. https://link.cnki.net/urlid/61.1294.N.20231016.1914.004. ZHANG J Z, MO S H, JIANG K X, et al., 2023. Spatial and temporal evolutionary characteristics of rainfall erosivity in Jialing River Basin using applicability analysis of model [J/OL]. Journal of Xi’an University of Technology, 1-9 [2025-3-24]. https://link.cnki.net/urlid/61.1294.N. 20231016.1914.004.   
张维琛, 王惺琪, 王博杰, 2024. 塔布河流域生态系统服务时空格局及影 响因素分析[J]. 生态环境学报, 33(7): 1142-1152. ZHANG W C, WANG X Q, WANG B J, 2024. Spatiotemporal Pattern and Influencing Factors of the Ecosystem Services in the Tabu River Basin [J]. Ecology and Environmental Sciences, 33(7): 1142-1152.   
张小瑜, 周自翔, 唐志雄, 等, 2024. 无定河流域生境质量时空变化及预 测[J]. 中国沙漠, 44(3): 75-84. ZHANG X Y, ZHOU Z X, TANG Z X, et al., 2024. Spatio-temporal variation and prediction of habitat quality in Wuding River Basin [J]. Journal of Desert Research, 44(3): 75-84.   
赵宾华, 马方铭, 李占斌, 等, 2023. 嘉陵江流域潜在蒸散发时空演变特 征及其影响因素[J]. 水资源与水工程学报, 34(5): 43-51. ZHAO B H, MA F M, LI Z B, et al., 2023. Temporal and spatial evolution characteristics of potential evapotranspiration and its influencing factors in Jialing River Basin [J]. Journal of Water Resources & Water Engineering, 34(5): 43-51.   
赵文武, 刘月, 冯强, 等, 2018. 人地系统耦合框架下的生态系统服务 [J]. 地理科学进展, 37(1): 139-151. ZHAO W W, LIU Y, FENG Q, et al., 2018. Ecosystem services for coupled human and environment systems [J]. Progress in Geography, 37(1): 139-151.   
朱月华, 2023. 社会生态视角下嘉陵江流域生态系统服务时空变化及其 权衡/协同关系[D]. 兰州: 兰州大学: 1-80. ZHU Y H, 2023. Spatiotemporal changes of ecosystem services and their tradeoffs/synergies in the Jialingjiang Watershed, China from the perspective of social-ecological system [D]. Lanzhou: Lanzhou University: 1-80.

# Dynamic Changes and Trade-off-Synergy Analysis of Ecosystem Services in the Jialing River Basin

WANG Tianwen1, 2, LUO Mingliang\*1, 2, BAI Leichao1, 2

1. College of Geographical Sciences, China West Normal University, Nanchong 637009, P. R. China; 2. Jialing River Basin Research Institute, Nanchong 637009, P. R. China

Abstract: Ecosystem services, which play a pivotal role in directly and indirectly satisfying human requirements, are provided by natural ecosystems through their structure, function, and processes. These services are extremely diverse and exhibit uneven spatial distributions. Intricate interaction mechanisms and dynamic relationships prevail among different services, which manifest mainly as trade-offs and synergies. Thus, analyzing the dynamic changes, driving mechanisms, and interactions of ecosystem services within a watershed holds great significance for ecological protection and coordinated regional development. The Jialing River Basin, serving as a pivotal ecological barrier in the upper reaches of the Yangtze River, is endowed with a rich and diverse ecosystem and assumes crucial functions, such as water conservation and ecological regulation. Nevertheless, irrational development and utilization within the basin have engendered a series of issues. These include inefficient utilization of water resources, wetland degradation, soil erosion, and secondary environmental risks stemming from upstream mining and industrial development. These problems present dual challenges in terms of both economic development and environmental protection. Currently, research on ecosystem services in river basins is predominantly centered on spatiotemporal dynamics and interactions. However, there is a lack of in-depth exploration of internal disparities and complex mechanisms within the basin. This is particularly evident in the comprehensive analyses of trade-offs and synergies at both basin-wide and regional scales. Although certain studies have explored individual ecosystem services within the Jialing River Basin, there remains a dearth of research on the comprehensive analysis of multiple ecosystem services and their intricate interactions. Therefore, this study was conducted as follows. Initially, the InVEST model was utilized to analyze and quantify the spatiotemporal dynamics of four key ecosystem services, namely, soil retention, habitat quality, carbon storage, and water yield, in the Jialing River Basin for the years 2000, 2010, and 2020. Second, by leveraging the GeoDetector method, single-factor and interactivefactor detections were utilized to quantitatively analyze the driving mechanisms of individual and interactive factors for each service. Subsequently, Pearson correlation analysis and spatial autocorrelation methods were employed to evaluate the trade-offs and synergies among different ecosystem services as well as the spatial distribution characteristics of these relationships. Finally, the basin was partitioned into regions based on the topographic position index. Subsequently, the interactions among different ecosystem services within each topographic gradient zone were analyzed. Key findings are as follows: 1) The ecosystem services within the Jialing River Basin, on the whole, exhibit a tendency of “overall growth with local stability”. Soil conservation and water yield services have experienced a remarkable increase; however, conspicuous disparities exist in their spatial distributions. High-value regions for soil retention are concentrated in the precipitous and densely vegetated southeastern and northwestern areas. Conversely, water yield services manifest a “southern-high, northern-low”. High-value regions are located in the southern part where precipitation is abundant. Habitat quality has experienced a slight decline, predominantly attributed to human activities, and carbon storage has remained relatively stable with a spatial distribution analogous to that of habitat quality. Specifically, high-value zones are located in the wellvegetated northwestern and southeastern regions, while low-value zones are found in highly urbanized areas, such as the Chengdu-Chongqing Economic Circle. 2) Additionally, changes in ecosystem services within the Jialing River Basin are jointly driven by natural factors and human activities. Single-factor analysis demonstrated that habitat quality was predominantly influenced by land use and vegetation cover. Soil conservation is closely associated with slope gradient and precipitation. Water yield is principally affected by precipitation and elevation. Carbon storage was strongly correlated with vegetation and precipitation. The analysis of interaction factors revealed that soil conservation was augmented under the synergistic action of slope gradient and vegetation. The water yield service demonstrated greater stability in the context of the interaction between the slope gradient and precipitation. Carbon storage and habitat quality were markedly affected by the synergistic effects of vegetation, precipitation, and land use. 3) The trade-offs and synergies of ecosystem services in the Jialing River Basin showed significant differences over time, across space, and among the different topographic gradient zones. From 2000 to 2020, across the entire region, there was a stable trade-off relationship between water yield service and carbon storage. There were stable synergistic relationships between carbon storage and habitat quality as well as between soil conservation and habitat quality, and the synergistic effects gradually increased. Spatially, the characteristics of trade-off and synergy showed a gradient change from northwest to southeast. Areas with a high degree of trade-off were concentrated in the northwest, whereas those with a strong synergistic effect were distributed in the north and east. The analysis of the classification based on the topographic position index showed that there are significant differences in the relationships between ecological services within different gradient zones. The interaction in zone 1 was relatively weak. The synergistic effect is enhanced in Zones 3 and 4, while in Zone 5, it mainly manifested as a trade-off relationship. Based on these findings, the optimization of ecosystem services in the Jialing River Basin requires a comprehensive consideration of its spatiotemporal heterogeneity, as well as the trade-off and synergistic relationships from the perspectives of both the entire region and its sub-regions. Scientific management measures should be implemented according to the local conditions. Future research should further enhance model optimization, conduct multiscale analyses, and explore driving mechanisms to more comprehensively and accurately uncover the trade-offs and synergies of ecosystem services, leading to a deeper understanding of their interactions. This study reveals the spatiotemporal dynamic characteristics of ecosystem services in the Jialing River Basin as well as their trade-off and synergistic relationships, providing a scientific basis for optimizing the ecological function layout and improving the level of ecological services in the basin. The findings provide a theoretical basis and practical reference for achieving mutually beneficial outcomes in both ecological protection and coordinated development in the Jialing River Basin.

Keywords: ecosystem services; Jialing River Basin; InVEST model; trade-offs and synergies; GeoDetector