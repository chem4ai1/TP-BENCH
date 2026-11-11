# CLM5在中国西南地区植被生长模拟的适用性分析

王黎欢1， 2，吕雅琼1 ，王梓奕

（1. 中国科学院、水利部成都山地灾害与环境研究所，四川 成都 610299；2. 中国科学院大学，北京 100049；3. 成都信息工程大学 大气科学学院/高原大气与环境四川省重点实验室，四川 成都 610225）

摘要：在全球变暖的背景下，西南地区整体上气温升高降水减少，作为中国重要的碳汇地区，西南地区的植被动态监测与模拟对深入了解其碳循环机制和促进经济可持续发展具有重要意义。本研究利用陆面过程模式（Community Land Model version5， CLM5），模拟和分析西南地区 2000 -2016 年叶面积指数LAI（Leaf Area Index， LAI）和总初级生产力 GPP（Gross Primary Productivity， GPP）的时空变化特征，并与多套遥感数据进行对比，评估CLM5在西南地区对LAI和GPP模拟的适用性。研究结果表明， CLM5能较好地模拟西南地区LAI和GPP的季节变化规律，但模拟存在对LAI生长季的高估，以及对GPP全年低估，对温带落叶阔叶灌木的LAI、高寒C3草甸的LAI、 GPP和C3草甸的GPP模拟效果较好。CLM5能够较好地刻画西南地区LAI和GPP空间分布格局，表现为由东南向西北递减，但整体上CLM5对西南地区LAI模拟偏高，特别是对贵州喀斯特地貌地区LAI的模拟偏高。与模型对LAI模拟高估相反， CLM5对西南地区GPP的模拟整体偏低，特别是云南地区。此外， CLM5对西南地区LAI和GPP的变化趋势模拟效果较差，特别是在云南大部分地区，遥感数据主要呈现上升趋势，而CLM5模拟呈现下降趋势。整体上， CLM5能模拟出西南地区LAI和GPP的季节变化规律和空间分布，但对云南和贵州部分地区的变化趋势模拟较差，仍需要针对四川盆地农田、云南森林、和贵州喀斯特地区植被发展更深入的参数化方案来提升模拟效果。

关键词： CLM5；叶面积指数；植被总初级生产力；西南地区文章编号： 1000-0534（2024）06-1586-14 中图分类号： Q948 文献标识码： ADOI：10. 7522/j. issn. 1000-0534. 2024. 00044

# 1 引言

在全球变暖不断加剧的背景下，中国西南地区自 2000 年以来干旱事件频发（Yu et al， 2014；杨春艳等， 2021）。过去的研究表明，西南地区气温升高降水减少，干旱指数 PDSI（Palmer Drought Sever‐ity Index）呈下降趋势，干旱化增强，易发生局部和区域性长时段的气象干旱（甄英等， 2019；杨春艳等， 2021）。对西南地区未来气候的模拟也表明未来温度持续增加，总降水减少，但极端天气频率增加，短时强降水呈现增加的趋势（Li et al， 2012；杨明鑫等， 2022）。植被作为陆地生态系统的关键组成部分，在调节碳、水和能量循环并影响全球气候变化方面发挥着至关重要的作用（Foley et al， 2000；Cao and Woodward， 1998），植被动态变化可以作为植被健康和生态系统稳定性的指标（Wang et al，2020）。叶面积指数 LAI（Leaf Area Index， LAI）作为表征陆地生态系统植被冠层结构特征、生物物理变化的关键参数（刘远和周买春， 2017； Sellers，1997），总初级生产力（Gross Primary Productivity，GPP）作为陆地生态系统碳循环的关键参数（Beer etal， 2010），可以量化植被研究，表征植被动态变化。

国内外学者广泛利用模型模拟来进行大尺度植被动态变化的研究，以进行在气候变化下植被的叶面积指数、植被覆盖度、生产力等植被生长变化的模拟，同时模拟过程中的物质能量交换。自20世纪 90 年代以来，动态全球植被模型（DynamicGlobal Vegetation Model， DGVM）成为植被模型研究的热点（王旭峰等， 2009）。目前国际上广泛应用的主要有 CLM-DGVM （The Community Land Mod‐el's Dynamic Global Vegetation Model）模型（Levis etal， 2004）、 LPJ（Lund-Potsdam-Jena Dynamic GlobalVegetation Model）模 型（Dickinson et al， 1986）、SEIB（Spatially Explicit Individual-Based DynamicGlobal Vegetation Model）模 型（ Sato et al， 2007）、IBIS（Integrated Biosphere Simulator Model）模 型（Foley et al， 1996）等，主要用于全球尺度上植被动态变化研究（车明亮等， 2014）。对全球植被分布和碳通量的模拟研究已成为生产力生态学的研究热点， Shao and Zeng（2011）利用 CLM-DGVM 研究了年际气候变率对全球植被平均分布的影响，发现气候年际变率导致全球植被总覆盖度下降，其中乔木和灌木减少而草地增加。Sun et al（2013）通过 LPJ的模拟结果表明，全球过去100年的植被碳储量整体上呈增加趋势。Sun （2009）基于LPJ模型对中国区域潜在植被分布和碳通量进行了模拟，结果表明中国区域的陆地生态系统是碳汇。在全球展开对模型的适应性评估也是模型发展的重要工作， Xueet al （ 2017）评估了 IBIS 模型对全球碳通量和地上生物量模拟效果，结果表明IBIS能以可接受的精度再现 GPP，在泛热带森林都对地上生物量 AGB（Aboveground Biomass）存在较大的偏差主要是由于特定植物功能类型的全球尺度参数固定引起。Ninomiya et al（2023）在全球站点模拟验证了耦合的SEIB 对 非 结 构 性 碳 水 化 合 物 NSC（non-structuralcarbohydrate）的模拟性能。Liang and Xie（2008）用CLM-DGVM中新的冠层截留方案在中国合理模拟了冠层截留的降水。Yuan et al（2014）证明 IBIS 可用于中国自然生态系统植被净初级生产力 NPP（Net Primary Productivity）的大规模模拟。目前对我国西南地区尤其是植被动态的模拟仍然较少。

西南喀斯特植物生长环境复杂，容易受到气候和人为干扰， Cai et al（2022）利用LPJ预测了中国西南自然恢复的潜在植被，以及基岩地质水文收支的影响 ，结 果 表 明 ，西 南 地 区 生 态 修 复 项 目 在2004 -2015 年的干旱时期也显著增加了 NDVI（Normalized Difference Vegetation Index）和 LAI。非碳酸盐区的厚土可以储存更多的水来支撑大部分森林并提高抗旱能力，而碳酸盐区风化基岩的持水能力有限，限制了大树的生长，降低了抗旱性。Xiong et al（2022）利用 SEIB 模拟西双版纳 GPP 在多梯度干旱情景下的动态过程，结果表明，旱季干旱事件对热带森林 GPP 的影响显著大于雨季干旱事件，雨季有效降水和土壤水分储量是研究区热带森林旱季抵御极端干旱事件的重要支撑。

美国国家大气研究中心（National Center for At‐mospheric Research， NCAR）发展的通用陆面模式CLM5（Community Land Model version 5），考虑了地表特征差异、不同土壤类型水力学热力学差异、不同植被类型下生态学差异等（Ke et al， 2012），CLM5在历史版本的基础上综合生物圈-大气圈传输方案陆面模型和中国科学院大气物理研究所陆面过程模型等模型的优点进行了优化（Lawrence etal， 2019）。NCAR 在 LPJ-DGVM 和 IBIS 模型的基础上，发展了一个全球动态植被模型（DGVM），后将DGVM耦合进 CLM，与CLM中的CN模块（Car‐bon-Nitrogen Cycle Module）耦合发展出 CLM 生物地球化学模块（Community Land Model with Biogeo‐chemistry， CLM-BGC）（Lu et al， 2020），是 目 前CLM陆面模式中能够模拟植被动态生长的模块。目前一些学者已运行CLM在中国部分地区进行了模拟研究，鲍艳等（2023）运用CLM4. 5对青藏高原植被进行了模拟，结果表明模型高估了南部和东部的LAI，地表水循环对高原植被变化起主要作用；Deng et al（2022）在青藏高原地区验证了 CLM5 的模拟效果，模拟GPP与遥感GPP由西北向东南递增的气候学特征相似，利用 CLM5-DGVM 模拟了植被变化对径流的影响，相较静态植被DGVM在三江源模拟的LAI增加，径流减少。

西南地区植被类型丰富，生态系统对气候变化脆弱敏感，是我国生态环境工程的重点实施区，也是重要的碳汇区（Piao et al， 2009），植被动态监测与模拟对深入了解碳循环机制和促进经济可持续发展具有重要意义。模式评估是模式发展中不可或缺的重要一环，为模式的发展与改进提供了依据。本研究基于离线模式下的CLM5（BGC模块）

模拟和分析西南地区 2000 -2016 年 LAI 和 GPP 时空变化特征，并与多套遥感数据进行比较，评估CLM5在西南地区对LAI和GPP的模拟能力，进行CLM5 在中国西南地区植被生长模拟的适用性分析。

# 2 资料来源与方法介绍

# 2. 1　研究区概况

中国西南地区包括云南、贵州、四川3个省级行政区和重庆市，地处北回归线附近，气候以亚热带季风气候和热带雨林气候为主，降水量充沛，雨热同季，紧邻青藏高原，地跨三级阶梯，受亚热带季风气候和高山山地气候的影响，局地气候复杂多变，存在明显的空间差异。该区地质地貌复杂，地形以山地、高原、盆地及丘陵为主，也是我国喀斯特地貌的集中分布区。区内植被覆盖度较高，类型丰富，主要有灌丛、针叶林、阔叶林、草丛和沼泽等，各种植被类型的生态系统对气候变化脆弱敏感（Xu et al， 2020），受人类活动影响较大。该区西部多以高寒草地为主，植被季节和空间异质性明显，东部主要以亚热带植被为主，在过去30年中形成了中国最大的陆地碳汇（Piao et al， 2009），人类活动强度的分布也有反差，大部分集中在西南东部。西南地区在维护生物多样性和国家生态安全方面发挥着重要作用，同时也是我国生态环境工程的重点实施区［图1，数据来源于：中华人民共和国植被图（1∶1000000），中国科学院中国植被图编辑委员会（中国科学院中国植被图编辑委员会）， 2021，中国科学院植物科学数据中心， DOI： 10. 12282/plant‐data. 0155， CSTR： 34735. 11. PLANTDATA. 0155］。文中所涉及的地图是基于自然资源部标准地图服务系统下载的审图号为GS（2019）1822号中国地图中的云南省、贵州省、四川省、重庆市制作，底图无修改。

![](images/fa7fe6d6065b9ac7fbd2b52c9d831e46bb3e6d25684fc9534697b0b05929accc.jpg)  
图1　西南地区植被类型  
Fig. 1 Map of vegetation types in Southwest China

# 2. 2　数据来源

# 2. 2. 1　大气强迫数据CRUNCEPv7

CRUNCEP包括气温、降水、温度、风速等的长时间序列数据，是一套驱动陆面模式大气强迫场数据集，可用于研究植被生长、蒸散发和初级生产力、陆气碳交换等。CRUNCEPv7（Viovy， 2018）是目前数据集的最新版本。CRUNCEP是两套数据（CRU TS3. 2 0. 5°×0. 5°月数据涵盖 1901 -2002 年期间和 NCEP 再分析 2. 5°×2. 5° 6 h 数据涵盖 1948-2016年期间）的融合，空间分辨率为0. 5°×0. 5°，时间分辨率为6 h。

# 2. 2. 2　观测数据

观测数据来自于国家生态数据中心资源共享服务平台（http： //www. nesdc. org. cn），研究使用贡嘎山站 2015 -2016 年 5 -10 月 LAI、西双版纳站2004 年 5 月至 2006 年 6 月 LAI、西双版纳站 2010 -2016 年 LAI、西双版纳站 2003 -2010 年 GPP 观测数据对模型模拟结果进行验证，数据信息如表 1所示。

表1 站点信息表Table 1 Site information  

<table><tr><td>站点</td><td>简称</td><td>经纬度</td><td>植被类型</td><td>时间</td></tr><tr><td>贡嘎山站</td><td>GG_LAI</td><td>29°33&#x27;N,102°00&#x27;E</td><td>亚高山森林</td><td>2015-2016年</td></tr><tr><td>西双版纳站</td><td>XSBN_LAI1</td><td>21°56&#x27;N,101°15&#x27;E</td><td>热带森林</td><td>2004-2006年</td></tr><tr><td>西双版纳站</td><td>XSBN_LAI2</td><td>21°56&#x27;N,101°15&#x27;E</td><td>热带森林</td><td>2010-2016年</td></tr><tr><td>西双版纳站</td><td>XSBN_GPP</td><td>21°56&#x27;N,101°15&#x27;E</td><td>热带森林</td><td>2003-2010年</td></tr></table>

# 2. 2. 3 LAI 遥感数据

GLASS-LAI，全球陆面卫星（GLASS）LAI产品是由北京师范大学生成并发布的 GLASS 产品套件的一部分。该时间序列 LAI乘积是由 AVHRR反射率 数 据 利 用 广 义 回 归 神 经 网 络 生 成 的（http： //www. geodata. cn）。

GLOBMAP-LAI产品提供了 0. 08°的空间分辨率，时间跨度从 1982 -2019 年。从 2000 -2019 年，该产品由中分辨率成像光谱仪（MODIS）表面反射率数据生成，时间分辨率为8天。1981 -1999年，该产品是根据 AVHRR 数据与 MODIS LAI 之间的像素级关系从AVHRR观测值生成的，时间分辨率为每半个月一次。使用聚类指数将有效LAI转换为总 LAI（Liu et al， 2012）。

GIMMS-LAI，第三代全球库存建模和制图研究（GIMMS）LAI产品由波士顿大学制作。它是由AVHRR、 GIMMS、 NDVI3G 利 用 人 工 神 经 网 络（ANN）模型生成的（Zhu et al， 2013）。

# 2. 2. 4 GPP 遥感数据

GLASS-GPP，是全球陆表特征参量产品年均植被总初级生产力产品，是由北京师范大学生成并发布的GLASS产品套件的一部分，具有长时间序列、高分辨率、高精度的特征（http： //www. geodata. cn）。

GLOBMAP-GPP（A global 0. 05° dataset forgross primary production of sunlit and shaded vegeta‐tion canopies），该产品基于GLOBMAP叶面积指数（GLOBMAP-LAI）、 CRUJRA 2. 2 气象数据以及欧洲航天局气候变化倡议土地覆盖（ESA-CCI）数据驱动，使用修正的双叶光利用效率（TL-LUE）模型构建（Bi et al， 2022）（https： //doi. org/10. 5061/dryad.dfn2z352k）。

GIMMS-GPP（Global Monthly GPP from an Im‐proved Light Use Efficiency Model）， 是 基 于GIMMS-3g FPAR和MERRA-2气象信息数据，通过LUE模型构建，并根据FLUXNET数据进行增强（Madani and Parazoo， 2020）。（https： //doi. org/10.3334/ORNLDAAC/1789）。

所用遥感数据详细信息如表2所示。

# 表2 遥感数据信息表

Table 2 Remote sensing data information   

<table><tr><td>数据名称</td><td>空间分辨率</td><td>时间分辨率</td><td>来源</td></tr><tr><td>GLASS-LAI</td><td>0. 05°</td><td>8天</td><td>http://www. geodata.cn</td></tr><tr><td>GLOBEMAP-LAI</td><td>0.08°</td><td>8天/半月</td><td>www. globalmapping. org</td></tr><tr><td>GIMMS-LAI</td><td>1/12°</td><td>半月</td><td>http://pan.baidu.com/s/lmhK2zTA</td></tr><tr><td>GLASS-GPP</td><td>0. 05°</td><td>8天</td><td>http: //www. geodata. cn</td></tr><tr><td>GLOBMAP-GPP</td><td>0. 05°</td><td>月</td><td>https://doi.org/10.5061/dryad.dfn2z352k</td></tr><tr><td>GIMMS-GPP</td><td>1/12°</td><td>月</td><td>https://doi.org/10.3334/ORNLDAAC/1789</td></tr></table>

# 2. 3　实验设计

CLM5是CLM的最新版本，对土壤和植物水文进行了显著的改进，包括对Richards方程的自适应时间步长进行求解，以及对冠层截留和基于土壤干表层的蒸发阻力参数化方案的完善（Lawrence etal， 2019），可以提供连续的地表水热模拟。本文用于模拟LAI、 GPP的BGC模块是CLM5中的生物地球化学模块（记为CLM5-BGC）。该模块考虑了不同的生态系统特征和生理生态参数的差异，能模拟不同植被类型的碳、氮、水循环、能量流动，以及模拟植被生长过程，输出包括叶面积指数（TotalProjected Leaf Area Index， TLAI）、总 初 级 生 产 力（Gross Primary Productivity， GPP）在内的多种过程变量。

本研究选取CLM-BGC进行离线模拟试验，使用2000 -2016 年 CRUNCEPv7 大气强迫数据为驱动，研究区域为西南地区，空间分辨率为0. 1°×0. 1°，模拟结果为月输出。为获取模式平衡态，要对模型进行初始化（spinup），即通过模拟不断趋向平衡状态，使模型和大气强迫充分适应，降低因初始场引起模拟结果的误差。本研究使用CRUNCEPv7为强迫场，模型默认初始文件为初始场，模式初始化680年，经检验模型达到平衡状态。使用得到的模式状态作为新的初始场，模拟 2000 - 2016 年的LAI、 GPP， LAI模拟结果记作CLM-LAI， GPP模拟结果记作CLM-GPP。

# 3 结果与分析

# 3. 1　站点验证

利用西南地区内贡嘎山站、西双版纳站的观测LAI 和西双版纳站通量站点的 GPP 观测数据对CLM-LAI和CLIM-GPP进行验证（图2）。图2（a）给出了贡嘎山站 2015、 2016 年 5 -10 月的 LAI 变化，模型未能模拟出观测LAI的单峰变化规律。图2（b）给出了西双版纳站2004 -2006年LAI，模型模拟与之相较，能够模拟季节的升降变化，但变化幅度波动较大。图2（c）给出了2010 -2016年西双版纳站点 LAI，图 2（d）给出了 2003 -2010年 GPP模式模拟结果与站点观测数据季节变化特征相似，表现为单峰变化，但在非生长季存在明显的低估。总体上， CLM能模拟出西双版纳站LAI和GPP的季节变 化 特 征 ，但 对 个 别 站 点 的 整 体 模 拟 效 果 较差（表3）。

![](images/d1af1507f020ebd67b2237bcd27a93431d2715935e8670bed45d57b18c86f6dd.jpg)  
图2　站点上LAI和GPP的月变化  
（a）贡嘎站 2015 -2016年 LAI，（b）西双版纳站 2004 -2006年 LAI，（c）西双版纳站 2010 -2016年 LAI，（d）西双版纳站 2003 -2010年 GPPFig. 2 Monthly changes of LAI and GPP at the site.（a） LAI of Gongga Station in 2015-2016，（b） LAI of Xishuangbanna Stationin 2004-2006，（c） LAI of Xishuangbanna Station in 2010-2016，（d） GPP of Xishuangbanna Station in 2003-2010

# 3. 2　区域验证

模式模拟结果与站点遥感LAI季节变化特征相似，表现为单峰变化，模式存在生长季的高估［图3（a）］。模式对西南地区LAI年平均变化模拟较差，存在明显的高估，并且波动较大［图 3（b）］。此外，模型中对西南地区的气候变化做出了响应，模型模拟结果中2002年、 2009年出现了转折，这对应了苏秀程等（2014）研究结论——2002 年前后西南地区由湿润化转为干旱化，进入相对干旱期；且2009年后降水具有明显的突变，降水总体呈下降趋势（甄英等， 2019；杨春艳等， 2021）。

模式里，与对西南地区LAI的高估不同，模式对西南地区的GPP存在低估。模式模拟结果与站点遥感GPP季节变化特征相似，表现为单峰变化；模型模拟的年平均变化也对2002年、 2010年前后的气候变化做出了响应［图4（b）］。表4给出了模拟值与遥感数据的均方根误差对比。CLM对西南地区整体的模拟效果较好。其中， CLM-LAI月平均变化得最接近GLOBMAP-LAI的月平均变化，均方根误差 RMSE 为 1. 2988 m2·m-2 ； CLM-LAI 年平均变化最接近GLOBMAP-LAI，均方根误差RMSE为

表3 CLM模拟值与观测值的相关系数（CORR）和均方根误差（RMSE）  
Table 3 Correlation coefficient and root mean square error between CLM analog value and observed value   

<table><tr><td></td><td>CORR(p&lt;0.01)</td><td>RMSE</td></tr><tr><td>GG-LAI</td><td>0.3812</td><td>0. 4464</td></tr><tr><td>XSBN-LAI1</td><td>0.3282</td><td>2. 0544</td></tr><tr><td>XSBN-LAI2</td><td>0. 3778</td><td>1. 8231</td></tr><tr><td>XSBN-GPP</td><td>0. 6625</td><td>88. 8921</td></tr></table>

GG-LAI 表 示 贡 嘎 站 LAI； XSBN-LAI1 表 示 西 双 版 纳 站2004 -2006 年 LAI； SXBN-LAI2 表 示 西 双 版 纳 站 2010 -2016 年LAI； XSBN-GPP 表示西双版纳站 GPPP。 LAI 之间的均方根误差单位为 m2 ·m-2； GPP 之间的均方根误差单位为 gC·m-2·mon−1 .（GG-LAI means LAI of Gongga Station； XSBN-LAI1 means LAI of Xish‐uangbanna Station from 2004 to 2006； XSBN-LAI2 means LAI of Xi‐shuangbanna Station from 2010 to 2016； XSBN-GPP means GPP ofXishuangbanna Station. The RMSE unit of LAI is m2 ·m-2； The RMSEunit of GPP is gC·m-2·mon−1 ）

1. 0817 m2·m-2 ； 2000 -2016 年 逐 月 变 化 最 接 近GLASS-LAI 均 方 根误 差 RMSE 为 1. 3362 m2·m-2 。CLM-GPP模拟效果最接近GIMMS-GPP，月平均变化均方根误差RMSE为35. 7125 gC·m·2 mon-1 ；年平均变化均方根误差 RMSE 为 28. 2515 gC·m·2 mon-1 ；逐月变化 RMSE 为 38. 5991 gC·m2·mon-1 。

不同植被类型年内的物候变化对模拟植被生长至关重要，通过对遥感数据和模拟数据的主要植被功能类型的年内变化对比发现，遥感数据的LAI和GPP在年内表现为单峰变化，峰值在生长季的7 -8月。模型对温带常绿针叶林、温带常绿阔叶林的LAI在年内模拟效果较差，无法模拟出年内的季节变化；高估了温带落叶阔叶灌木、高寒C3草甸在3 -11月的LAI，低估了温带落叶阔叶灌木、高寒C3草甸、非高寒C3草甸在1月、 2月、 12月（非生长季）的LAI。模型能基本模拟GPP的季节变化特征， GPP在春季随植被生长而快速上升，在6 -7月达到最大值，到秋冬逐渐变小；相比遥感数据，模型低估了温带常绿针叶林的GPP，且模型模拟的温带常绿阔叶林的GPP出现了双峰变化，峰值在2月和7月；此外模型低估了高寒C3草甸全年的GPP；并且高估非高寒C3草甸生长季GPP，低估了非生长季的GPP。

![](images/ce68de5df4c0c3345258e4a1567ec6862fa9aa745ea8a8fb4963ccf339347528.jpg)  
图3　西南地区LAI区域验证  
（a）月平均变化，（b）年平均变化，（c）2000-2016年逐月变化  
Fig. 3 Southwest LAI Regional Verification.（a） monthly mean change，（b） yearly meanchange，（c） monthly changes of LAI in Southwest China from 2000 to 2016

表5给出了西南地区主要的几种植被类型（温带针叶林、温带常绿阔叶林、温带落叶阔叶灌木、高寒C3草地、非高寒C3草地）模拟值与遥感数据的相关系数和均方根误差（\*表示通过0. 01的显著性检验）。

模式模拟的温带针叶林的GPP、温带落叶阔叶灌木的LAI、高寒C3草甸和C3草甸的LAI、 GPP与遥感值具有很好的对应关系；量值上，对温带落叶阔叶灌木的 LAI（均方根偏差 RMSD<5 m2·m-2）、高寒

![](images/5d2d7feeeb70023346eb72fb208e08bd722c29814ca4b187b26111f7815d1dd0.jpg)  
图4　西南地区GPP区域验证  
（a）月平均变化，（b）年平均变化，（c）2000 -2016年逐月变化  
Fig. 4 Southwest GPP Regional Verification.（a） monthly mean change，（b） yearly mean change，（c） monthly changes of LAI in Southwest China from 2000 to 2016

表4 CLM模拟值与遥感值的均方根误差（RMSE）  
Table 4 Root mean square error between CLM simulations and observations （RMSE）   

<table><tr><td></td><td>GLASS-CLM</td><td>GLOBMAP-CLM</td><td>GIMMS-CLM</td></tr><tr><td>LAI-months</td><td>1.3100</td><td>1. 2988</td><td>1. 5827</td></tr><tr><td>LAI-years</td><td>1. 1206</td><td>1. 0817</td><td>1.3188</td></tr><tr><td>LAI</td><td>1. 3362</td><td>1. 3477</td><td>1. 6206</td></tr><tr><td>GPP-months</td><td>38. 5772</td><td>57. 2723</td><td>35. 7125</td></tr><tr><td>GPP-years</td><td>36. 7360</td><td>51. 0551</td><td>28. 2515</td></tr><tr><td>GPP</td><td>39. 1615</td><td>58.4316</td><td>38.5991</td></tr></table>

LAI之间的均方根误差单位为m2·m-2 ； GPP之间的均方根误差单 位 为 gC·m-2·mon−1 （The RMSE unit of LAI is m2·m-2 ； TheRMSE unit of GPP is gC·m-2·mon−1 ）

C3 草 甸 的 LAI（均 方 根 偏 差 RMSD<2 m2·m-2）、GPP（均方根偏差 RMSD<51 gC·m2·month-1）和 C3草甸的GPP（均方根偏差 RMSD<55 gC·m·2 month-1）模拟效果较好。其中，温带常绿针叶林的模拟LAI与遥感LAI显著负相关，模拟GPP与遥感GPP显著正相关；温带常绿阔叶林的模拟LAI与遥感LAI显著负相关，模拟GPP与遥感GPP不显著正相关；温带落叶阔叶灌木的模拟LAI与遥感LAI显著正相关，模拟GPP与遥感GPP不显著正相关；高寒C3草甸和非高寒C3草甸模拟LAI、 GPP与遥感GPP呈正相关。

# 3. 3　空间分布

从遥感数据来看，西南地区LAI、 GPP的空间分布，总体上呈现出从东南向西北减小的特征，云南南部地区最高，西南地区东部大于西部，四川盆地地区小于周围地区的分布特点， CLM基本模拟出该空间分布特征。CLM-LAI整体上偏高，特别是对东部LAI的模拟偏高，且没有模拟出四川盆地和周围地区的差异。CLM-GPP相较遥感数据整体偏低，特别是云南地区。

图 7 给出了遥感和模拟 LAI、 GPP 的变化趋势，不同的遥感数据产品对西南地区LAI、 GPP的变化趋势描述本身存在较大的差距。GLASS-LAI在云南南部和三省交界处呈现上升趋势，其他地区呈现下降趋势， GLOBMAP-LAI 和 GIMMS-LAI 在大部分地区呈现上升趋势，而模拟LAI在大部分地区呈现下降趋势。而 GLASS-GPP四川北部和三省交界处呈现上升趋势，其他地区呈现下降趋势，GLOBMAP-LAI和GIMMS-LAI在大部分地区呈现上升趋势，而模拟LAI在西南部地区呈现下降趋势，在东北部呈现上升趋势。CLM5能模拟出四川东北部地区 LAI 和 GPP 的上升趋势，但总体上CLM5对西南地区LAI和GPP的变化趋势模拟效果较差，特别是在云南地区，遥感数据主要呈现上升趋势，而CLM5模拟呈现下降趋势。

![](images/cc03e9b3fb43eab799790d81b2333b7f374d2c54590fc8a0971619c1edbeabb6.jpg)  
图5　西南地区不同植被类型LAI、 GPP年内循环  
Fig. 5 The annual cycles of LAI and GPP of dominant PFTs （Plant Functional Types） in southwest China

表5 不同植被类型CLM模拟值与遥感值的相关系数（CORR）和均方根误差（RMSE） Table 5 Correlation coefficient and root mean square error between CLM analog value and observed value of dominant PFTs in southwest China   

<table><tr><td rowspan="2"></td><td colspan="6">CORR(p&lt;0.01)</td><td colspan="4">RMSE</td></tr><tr><td>NEM Tr</td><td>BEMTr</td><td>BDM Sh</td><td>C3 AR</td><td>C3 NA</td><td>NEMTr</td><td>BEM Tr</td><td>BDM Sh</td><td>C3 AR</td><td>C3 NA</td></tr><tr><td>GLASS-LAI</td><td>-0.3417*</td><td>-0.9640*</td><td>0.7789*</td><td>0.8145*</td><td>0.8729*</td><td>2.7507</td><td>3.4402</td><td>3.9987</td><td>1. 6758</td><td>5.8075</td></tr><tr><td>GLOBMAP-LAI</td><td>-0.2807*</td><td>-0.9262*</td><td>0.7059*</td><td>0.8434*</td><td>0.7924*</td><td>2.9735</td><td>3.5025</td><td>4. 0947</td><td>1. 1460</td><td>5.8281</td></tr><tr><td>GIMMS-LAI</td><td>-0.4934*</td><td>-0.9279</td><td>0. 6322</td><td>0.8253*</td><td>0.8771*</td><td>3.1039</td><td>3.5402</td><td>4.3754</td><td>1. 5663</td><td>6.1491</td></tr><tr><td>GLASS-GPP</td><td>0.9404*</td><td>0.5844</td><td>0.9566</td><td>0.9926*</td><td>0.9755*</td><td>91.0288</td><td>44. 0428</td><td>61.4734</td><td>40.5645</td><td>54.4765</td></tr><tr><td>GLOBMAP-GPP</td><td>0.9448*</td><td>0.5147</td><td>0.9654</td><td>0.9708</td><td>0.9746</td><td>96.0797</td><td>57.9482</td><td>43.4601</td><td>50.1744</td><td>35.5633</td></tr><tr><td>GIMMS-GPP</td><td>0.9395*</td><td>0.4250</td><td>0.9570</td><td>0.9929*</td><td>0.9807</td><td>86.2731</td><td>58.2418</td><td>45.1248</td><td>13.1104</td><td>33.2783</td></tr></table>

NEM Tr 表示温带针叶林， BEM Tr 表示温带常绿阔叶林， BDM Sh 表示温带落叶阔叶灌木， C3 AR 表示高寒C3草地， C3 NA表示非高寒 C3 草地。 LAI 之间的均方根误差单位为 m2·m-2 ； GPP 之间的均方根误差单位为 gC·m-2·mon−1 ， \*表示通过显著性检验 0. 01 （NEM Trstands for Needleleaf evergreen tree， temperate； BEM Tr stands for Broadleaf evergreen tree， temperate； BDM Sh stands for Broadleaf deciduousshrub， temperate； C3 AR stands for alpine C3 grassland， and C3 NA stands for C3 grassland. The RMSE unit of LAI is m2·m-2 ； The RMSE unit ofGPP is gC·m-2·month−1 ， \* indicates passing the significance test 0. 01）

# 4 结论与讨论

# 4. 1　结论

本研究基于陆面过程模式（CLM5）模拟西南地区2000 -2016年叶面积指数（LAI）和总初级生产力（GPP），与多套遥感数据进行比较分析其时空变化特征，得出以下结论：

（1） CLM5能较好地模拟西南地区LAI和GPP的季节变化规律，但模拟存在对LAI的生长季高估，以及对GPP全年低估的情况。模式对温带落叶阔叶灌木的LAI、高寒C3草甸的LAI、 GPP和C3草甸的GPP模拟效果较好。

（2） 模型能够较好地刻画西南地区LAI和GPP空间分布格局，表现为由东南向西北递减。整体上CLM5对西南地区LAI模拟偏高，特别是对东部喀斯特地貌地区LAI的模拟偏高。CLM5对西南地区GPP的模拟整体偏低，特别是云南地区。

（3） CLM5对西南地区LAI和GPP的变化趋势模拟效果较差，特别是在云南地区，遥感数据主要呈现上升趋势，而CLM5模拟呈现下降趋势。

总之， CLM5能模拟西南地区LAI和GPP的季节变化规律和空间分布，但对云南和贵州部分地区的变化趋势模拟较差，需要进一步提升。

![](images/7b31387c6e4486f4d4df0bab8a8c5d7e03a19d274c3a7abaef093af5e0b07aa9.jpg)  
图6　西南地区LAI、 GPP多年平均空间分布

![](images/5aa5fe1be64bc66ed8d829a960279f9992c7fa6771c6ed0a8d111836e8e6ccc1.jpg)  
Fig. 6 Multi-year average spatial distribution map of LAI and GPP in Southwest China   
图7　西南地区LAI、 GPP多年趋势变化空间分布空白部分表示没有通过显著性检验  
Fig. 7 Spatial distribution map of LAI and GPP trends in Southwest China over the years. The blank area indicates that it has not passed the significance test

# 4. 2　讨论

站点模拟与观测在量值上存在不同程度的偏差，在这可能是模型输入的驱动数据不够准确（李睿等， 2019）以及模型参数化方案对于样地的适应性不好造成的（Duan et al， 2006），此外观测样地与模型模拟在尺度差别也导致了偏差（Like et al，

2016）。刘佳凤（2023）基于贡嘎站的模拟结果表明CLM5对贡嘎山站2016年的年内变化模拟较差。更准确的模拟需要对参数化方案进行调整（付春伟等， 2022）。

不同的地表覆盖资料对模拟结果有较大影响，准确的地表资料是精准描述地表的关键，是模拟地表的能量交换和生物地球化学过程的重要基础（陈锋和谢正辉， 2009； Lawrence et al， 2018）。CLM 地表工具制作的地表资料对西南地区描述是否准确需要进一步对比分析。王媛媛等（2015）的研究表明，使用更精准的土地覆盖资料替换CLM中默认的土地覆盖资料能减小模拟误差。过去的研究认为西南地区土地覆盖类型转换是影响植被动态重要因素，同时人类活动对植被增长具有双重作用和空间差异性，生态工程的实施是植被“变绿”的重要原因（张雪梅等， 2017；洪辛茜等， 2021）。本模拟采用的是CLM的默认地表，也会造成模拟结果的偏差，后续应使用西南地区更加精确的地表覆盖数据提高模拟结果。

不同的遥感数据产品对西南地区LAI、 GPP的变化趋势描述不尽相同，说明作为评估标准的遥感数据本身也存在较大差异。这与 Jiang et al（2017）的研究结果一致，不同遥感产品之间存在明显的差异 ，这 可 能 是 NOAA（National Oceanic and Atmo‐spheric Administration）卫星轨道变化和 MODIS 传感器退化。侯吉宇等（2020）研究结果也表明不同遥感产品变化趋势在中国的空间分布格局存在明显差异。叶面积指数（LAI）数据是也是模拟GPP的重要参数，不准确的LAI会导致不够准确的GPP，Xie et al（2019）研究结果表明，不同的遥感 LAI 在不同植被类型的模拟适应性不同，且复杂地形的模拟差异较大，平坦地形模拟性能更好。西南地区地形复杂，更好地适应西南地区需要模型更进一步发展和优化。

模型在西南地区存在对LAI的高估和对GPP的低估，这与 Song et al（2021）和 Hu et al（2022）研究结果一致， CIMP6的地球系统模型对LAI的高估在全球范围内普遍存在，对GPP虽然也存在全球尺度的高估，但以CLM为陆面模型的模拟结果中，在青藏高原南部和东部的西南地区存在对GPP的低估。模型中对LAI高估和对GPP低估同时存在的原因可能是，虽然植被的LAI增大但植被的光合速率却下降造成的，这与 Ali et al（2016），李睿等（2019）研究结果一致。Li et al（2019）研究也表明，西南地区在干旱的作用下，不同的数据和模型都显示植被变绿和碳通量对干旱做出了响应，但它们在响应的程度上存在显著差异。

CLM5对西南地区LAI和GPP的变化趋势模拟效果较差，特别是在云南地区，遥感数据主要呈现上升趋势，而CLM5模拟呈现下降趋势，本文基于CLM5的植被动态模拟并没有模拟出人类活动的影响，可能是人类活动对植被的影响造成了模拟结果的差异（李美丽等， 2021；郑朝菊等， 2017）。过去的研究表明人类活动对植被动态具有较大的影响，未来模型的发展应考虑人类的影响（Lawrence andChase， 2010； Levis， 2010）。此外，火灾也是影响模型模拟效果的重要原因，西南地区干旱频发是我国林火高发地区之一（田晓瑞等， 2010），进一步的研究应当考虑火灾对植被动态的干扰（Thonicke etal， 2001； Hantson et al， 2016）。

# 参考文献：

Ali A A， Fisher J B， Rogers A， et al， 2016. A global scale mechanis‐tic model of photosynthetic capacity （LUNA V1. 0）［J］. Geosci‐entific Model Development， 9（2）： 587-606. DOI： 10. 5194/gmd-9-587-2016.  
Beer C， Reichstein M， Tomelleri E， et al， 2010. Terrestrial Gross Car‐bon Dioxide Uptake： Global Distribution and Covariation withClimate［J］. American Association for the Advancement of Sci‐ence， 329（5993）： 834-8. DOI： 10. 1126/SCIENCE. 1184984.  
Bi W J， He W， Zhou Y Z， et al， 2022. A global 0. 05° dataset forgross primary production of sunlit and shaded vegetation canopiesfrom 1992 to 2020［J］. Scientific Data， 9（1）： 2052-4463. DOI：10. 1038/s41597-022-01309-2.  
Cai L B， Chen X， Huang R C， et al， 2022. Runoff change induced byvegetation recovery and climate change over carbonate and non-carbonate areas in the karst region of South-west China［J］. Jour‐nal of Hydrology， 604（127231）： 0022-1694. DOI： 10. 1016/j.jhydrol. 2021. 127231.  
Cao M， Woodward， et al， 1998. Dynamic responses of terrestrial eco‐system carbon cycling to global climate change［J］. Nature， 393（6682）： 249-249. DOI： 10. 1038/30460.  
Deng M S， Meng X H， Lu Y Q， et al， 2022. The response of vegeta‐tion to regional climate change on the Tibetan Plateau based on re‐mote sensing products and the dynamic global vegetation model［J］. Remote Sensing， 14（27）： 7540-7552. DOI： 10. 1029/2019JD030481.  
Dickinson R E， Henderson-Sellers A， Kennedy P J， et al， 1986. Bio‐sphere-atmosphere transfer scheme （BATS） for the NCAR Com‐munity Climate Model［J］. University Corporation for Atmospher‐ic Research， 213（26）： 2052-4463. DOI： 10. 5065/D6668B58.  
Duan Q， Schaake J， V. Andréassian， et al， 2006. Model ParameterEstimation Experiment （MOPEX）： an overview of science strate‐gy and major results from the second and third workshops［J］.Journal of Hydrology， 320（1-2）： 3-17. DOI： 10. 1016/j. jhy‐drol. 2005. 07. 031.  
Foley J A， Levis S， Costa M H， et al， 2000. Incorporating dynamicvegetation cover within global climate models［J］. Ecological Ap‐plications， 10（6）： 1620-1632. DOI： 10. 2307/2641227.  
Foley J A， Prentice I C， Ramankutty N， et al， 1996. An integratedbiosphere model of land surface processes， terrestrial carbon bal‐ance， and vegetation dynamics［J］. Global Biogeochemical Cy‐cles， 10（4）： 603-628. DOI： 10. 1029/96GB02692.  
Hantson S， Arneth A， Harrison S P， et al， 2016. The status and chal‐lenge of global fire modelling［J］. Biogeosciences Discussions，13（11）： 3359-3375. DOI： 10. 5194/bg-13-3359-2016.  
Hu Q W， Li T T， Deng X， et al， 2022. Intercomparison of global ter‐restrial carbon fluxes estimated by MODIS and Earth system mod‐els［J］. Science of the Total Environment， 810（18）： 152231.DOI： 10. 1016/j. scitotenv. 2021. 152231.  
Jiang C Y， Ryu Y， Fang H L， et al， 2017. Inconsistencies of interan‐nual variability and trends in long-term satellite leaf area indexproducts［J］. Global Change Biology， 23（10）： 4133-4146.DOI： 10. 1111/gcb. 13787.  
Ke Y， Leung L R， Huang M， et al， 2012. Development of high reso‐lution land surface parameters for the Community Land Model［J］. Geoscientific Model Development， 5（6）： 1341-1362. DOI：10. 5194/gmd-5-1341-2012.  
Lawrence D M， Fisher R A， Koven C D， et al， 2010. The communityland model version 5： description of new features， benchmark‐ing， and impact of forcing uncertainty［J］. Journal of Advances inModeling Earth Systems， 2019， 11 （12）. DOI： 10. 1029/2018MS001583.  
Lawrence P J， ChaseT N， 2010. Investigating the climate impacts ofglobal land cover change in the community climate system model［J］. International Journal of Climatology， 30（13）： 2066-2087.DOI： 10. 1002/joc. 2061.  
Lawrence P J， Lawrence D M， Hurtt G C， 2018. Attributing the car‐bon cycle impacts of CMIP5 historical and future land use andland cover change in the community earth system model（CESM1）［J］. Journal of Geophysical Research： Biogeoscienc‐es， 123（5）： 1732-1755DOI： 10. 1029/2017JG004348.  
Lawrence P J， Chase T N， 2010. Investigating the climate impacts ofglobal land cover change in the community climate system model［J］. International Journal of Climatology， 30（13）： 2066-2087.DOI： 10. 1002/joc. 2061  
Levis S， 2010. Modeling vegetation and land use in models of theearth system ［J］. Wiley Interdisciplinary Reviews ClimateChange， 1（6）： 840-856. DOI： 10. 1002/wcc. 83.  
Levis S， Bonan G B， Bonfils C， 2004. Soil feedback drives the mid-Holocene North African monsoon northward in fully coupled CC‐SM2 simulations with a dynamic vegetation model［J］. ClimateDynamics， 23（7/8）： 791-802. DOI： 10. 1007/s00382-004-0477-y.  
Li Z X， He Y Q， Wang P Y， et al， 2012. Changes of daily climate ex‐tremes in southwestern China during 1961-2008［J］. Global &Planetary Change， 80-81（0921-8181）： 255-272. DOI： 10.1016/j. gloplacha. 2011. 06. 008.  
Liang M L， Xie Z H， 2008. Improving the vegetation dynamic simula‐tion in a land surface model by using a statistical-dynamic cano‐py interception scheme［J］. Advances in Atmospheric Sciences，25（4）： 610–618. DOI： 10. 1007/s00376-008-0610-7.  
Like N， Jun X， Chesheng Z， et al， 2016. Runoff of arid and semi-aridregions simulated and projected by CLM-DTVGM and its multi-scale fluctuations as revealed by EEMD analysis［J］. Journal of Ar‐id Land， 8（4）： 506-520. DOI： 10. 1007/s40333-016-0126-4.  
Liu Y， Liu R， Chen J M， 2012. Retrospective retrieval of long-termconsistent global leaf area index （1981-2011） from combinedAVHRR and MODIS data［J］. Journal of Geophysical Re‐search： Biogeosciences， 117（G4）： 2169-8953. DOI： 10. 1029/2012jg002084.  
Lu X， Du Z， Huang Y， et al， 2020. Full implementation of matrix ap‐proach to biogeochemistry module of Community Land Modelversion 5 （CLM5）［J］. Journal of Advances in Modeling EarthSystems， 12（11）. DOI： 10. 1029/2020MS002105.  
Madani N， Parazoo N C， 2020. Global monthly GPP from an im‐proved light use efficiency model， 1982-2016［M］. ORNL Dis‐tributed Active Archive Center.  
Ninomiya H， Kato T， Vegh L， et al， 2023. Modeling of non-structur‐al carbohydrate dynamics by the spatially explicit individual-based dynamic global vegetation model SEIB-DGVM （SEIB-DGVM-NSC version 1. 0）［J］. Geoscientific Model Develop‐ment， 16（14）： 4155-4170. DOI： 10. 5194/gmd-16-4155-2023.  
Piao S L， Fang J Y， et al， 2009. The carbon balance of terrestrial eco‐systems in China［J］. Nature， 458（7241）： 1009-13. DOI： 10.1038/nature07944.  
Sato， H， Itoh， A， Kohyama， T， 2007. SEIB-DGVM： A new dynam‐ic global vegetation model using a spatially explicit individual-based approach［J］. Ecological Modelling， 200（3-4）： 279-307.DOI： 10. 1016/j. ecolmodel. 2006. 09. 006.  
Sellers P J， 1997. Modeling the exchanges of energy， water， and car‐bon between continents and the atmosphere［J］. Science， 275（5299）： 502-509. DOI： doi： 10. 1126/science. 275. 5299. 502.  
Shao P， Zeng X D， 2011. The impact of interannual climate variabilityon the mean global vegetation distribution［J］. Acta Ecologica Sini‐ca， 31（6）： 1494-1505. DOI： 10. 3724/SP. J. 1077. 2011. 00311.  
Song X， Wang D Y， Li F， et al， 2021. Evaluating the performance ofCMIP6 Earth system models in simulating global vegetation struc‐ture and distribution［J］. Advances in Climate Change Research，12（4）： 584-595. DOI： 10. 1016/j. accre. 2021. 06. 008.  
Sun G D， 2009. Simulation of potential vegetation distribution and es‐timation of carbon flux in China from 1981 to 1998 with LPJ dy‐namic global vegetation model［J］. Climatic and EnvironmentalResearch， 14（4）： 341-351. DOI： 10. 1016/S1003-6326（09）60084-4.

Sun X F， Yue T X， Fan Z M， et al， 2013. Spatiotemporal trends in

global vegetation carbon storage［J］. Resources Science， 35（4）：782-91. DOI： 1007-7588（2013）35： 4<782： QQZBTC>2. 0.TX； 2-X.  
Thonicke K， Venevsky S， Sitch S， et al， 2001. The role of fire distur‐bance for global vegetation dynamics： coupling fire into a Dy‐namic Global Vegetation Model［J］. Global Ecology and Biogeog‐raphy， 10（6）： 661-677. DOI： 10. 1046/j. 1466-822X. 2001. 00175. x.  
Viovy N， 2018. CRUNCEP version 7-atmospheric forcing data for thecommunity land model［M］. Research Data Archive at the Nation‐al Center for Atmospheric Research， Computational and Informa‐tion Systems Laboratory； Boulder， CO.  
Wang H， Yao F， Zhu H S， et al， 2020. Spatiotemporal variation ofvegetation coverage and its response to climate factors and humanactivities in arid and semi-arid areas： case study of the OtindagSandy Land in China［J］. Sustainability， 12（12）： 5214. DOI：10. 3390/su12125214.  
Xie X Y， Li A N， Jin H A， et al， 2019. Assessment of five satellite-derived LAI datasets for GPP estimations through ecosystem mod‐els［J］. Science of The Total Environment， 690（10）： 1120-1130.DOI： 10. 1016/j. scitotenv. 2019. 06. 516.  
Xiong Q， Sun Z Y， Cui W， et al， 2022. A study on sensitivities oftropical forest GPP responding to the characteristics of drought-case study in Xishuangbanna， China［J］. Water， 14（2）： 157.DOI： 10. 3390/w14020157.  
Xu K， Wang X P， Jiang C， et al， 2020. Assessing the vulnerability ofecosystems to climate change based on climate exposure， vegeta‐tion stability and productivity［J］. Forest Ecosystems， 7（3）： 12.DOI： 10. 1186/s40663-020-00239-y.  
Xue B L， Guo Q H， Hu T Y， et al， 2017. Evaluation of modeled glob‐al vegetation carbon dynamics： analysis based on global carbonflux and above-ground biomass data［J］. Ecological Modelling，355（38）： 84-96. DOI： 10. 1016/j. ecolmodel. 2017. 04. 012.  
Yu M， Li Q， Hayes M J， et al， 2014. Are droughts becoming more fre‐quent or severe in China based on the standardized precipitationevapotranspiration index： 1951-2010？［J］. International Journalof Climatology， 34（3）： 545-558. DOI： 10. 1002/joc. 3701.  
Yuan Q Z， Wu S H， Zhao D S， et al， 2014. Modeling net primary pro‐ductivity of the terrestrial ecosystem in China from 1961 to 2005［J］. Journal of Geographical Sciences， 24（1）： 3-17. DOI： 10.1007/s11442-014-1069-3.  
Zhu Z C， Bi J， Pan Y Z， et al， 2013. Global data sets of vegetationLeaf Area Index （LAI）3g and fraction of photosynthetically ac‐tive radiation （FPAR）3g derived from global inventory modelingand mapping studies （GIMMS） normalized difference vegetationindex （NDVI3g） for the Period 1981 to 2011［J］. Remote Sens‐ing， 5（2）： 927-948. DOI： 10. 3390/rs5020927.  
鲍艳，王玉琦，南素兰，等， 2023. 动态植被模型对青藏高原植被的模拟检验［J］. 高原气象， 42（2）： 333-343， DOI： 10. 7522/j.issn. 1000-0534. 2021. 00062. Bao Y， Wang Y Q， Nan S L， etal， 2023. Evaluation of vegetation characteristics over Qinghai-Xizang Plateau simulated by a vegetation dynamic model［J］. Pla‐1597teau Meteorology， 42（2）： 333-343. DOI： 10. 7522/j. issn.1000-0534. 2021. 00062.  
车明亮，陈报章，王瑛，等， 2014. 全球植被动力学模型研究综述［J］. 应用生态学报， 25（1）： 263-271. DOI： 10. 13287/j. 1001-9332. 2014. 01. 036. Che M L， Chen B Z， Wang Y， et al， 2014.Review of dynamic global vegetation models （DGVMs）［J］. Chi‐nese Journal of Applied Ecology， 25（1）： 263-271. DOI： 10.13287/j. 1001-9332. 2014. 01. 036.  
陈锋，谢正辉， 2009. 基于中国植被数据的陆面覆盖及其对陆面过程模拟的影响［J］. 大气科学， 33（4）： 681-697. DOI： 10. 3878/j. issn. 1006-9895. 2009. 04. 03. Chen F， Xue Z H， 2009. A landcover dataset based on chinese vegetation data and its impact onland surface simulations［J］. Chinese Journal of Atmospheric Sci‐ences， 33（4）： 681-697. DOI： 10. 3878/j. issn. 1006-9895.2009. 04. 03.  
付春伟，胡泽勇，卢珊，等， 2022. 基于CLM4. 5模式的季节冻土区土壤参数化方案的模拟研究［J］. 高原气象， 41（1）： 93-106.DOI： 10. 7522/j. issn. 1000-0534. 2021. 00050. Fu C W， Hu ZY， Lu S， et al， 2022. A simulation study on soil parameterizationscheme of seasonally frozen ground regions based on CLM4. 5［J］. Plateau Meteorology， 41（1）： 93-106. DOI： 10. 7522/j.issn. 1000-0534. 2021. 00050.  
洪辛茜，黄勇，孙涛， 2021. 我国西南喀斯特地区2001—2018年植被净初级生产力时空演变［J］. 生态学报， 41（24）： 9836-9846.DOI： 10. 5846/stxb202009122381. Hong X Q， Huang Y， SunT， 2021. Spatiotemporal evolution of vegetation net primary pro‐ductivity in the karst region of southwest China from 2001 to 2018［J］. Acta Ecologica Sinica， 2021， 41（24）： 9836-9846. DOI：10. 5846/stxb202009122381.  
侯吉宇，周艳莲，刘洋， 2020. 不同叶面积指数遥感数据模拟中国总初级生产力的时空差异［J］. 遥感技术与应用， 35（5）： 1015-1027. DOI： 10. 11873/j. issn. 1004-0323. 2020. 5. 1015. Hou JY， Zhou Y L， Liu Y， 2020. Spatial and temporal differences ofGPP simulated by different satellite-derived LAI in China［J］. Re‐mote Sensing Technology and Application， 35（5）： 1015-1027.DOI： 10. 11873/j. issn. 1004-0323. 2020. 5. 1015.  
李美丽，尹礼昌，张园，等， 2021. 基于MODIS-EVI的西南地区植被覆盖时空变化及驱动因素研究［J］. 生态学报， 41（3）： 1138-1147. . DOI： 10. 5846/stxb201907101451. Li M L， Yin L C，Zhang Y， et al， 2021. Spatio-temporal dynamics of fractionalvegetation coverage based on MODIS-EVI and its driving factorsin Southwest China［J］. 41（3）： 1138-1147. DOI： 10. 5846/stxb201907101451.  
李睿，张黎，景元书，等， 2019. 基于 FLUXNET 的 CLM 模型总初级生产力模拟评价与误差分析［J］. 生态学杂志， 38（9）： 2883-2895. DOI： 10. 13292/j. 1000-4890. 201909. 020. Li R， ZhangL， Jing Y S， et al， 2019. Evaluation and error analysis of grossprimary productivity using land surface model CLM overFLUXNET［J］. Chinese Journal of Ecology， 38（9）： 2883-2895.DOI： 10. 13292/j. 1000-4890. 201909. 020.  
刘佳凤， 2023. 青藏高原东缘森林通用陆面模式植被生长参数优化［D］. 成都：成都山地灾害与环境研究所， 1-115. Liu J F，2023. Optimization of vegetation growth parameters in the Com‐munity Land Model for the forest on the eastern edge of the Tibet‐an Plateau［D］. Chengdu： Institute of Mountain Hazards and En‐vironment， 1-115.  
刘远，周买春， 2017. 遥感反演植被叶面积指数的不确定性来源综述［J］. 江苏农业科学， 45（12）： 12-19. DOI： 10. 15889/j. issn.1002-1302. 2017. 12. 003. Liu Y， Zhou M C， 2017. Uncertainsources of remote sensing inversion of vegetation leaf area index：an overview［J］. Jiangsu Agricultural Sciences， 45（12）： 12-19.DOI： 10. 15889/j. issn. 1002-1302. 2017. 12. 003.  
苏秀程，王磊，李奇临，等， 2014. 近50a中国西南地区地表干湿状况研究［J］. 自然资源学报， 29（1）： 104-116. DOI： 10. 11849/zrzyxb. 2014. 01. 010. Su X C， Wang L， Li Q L， et al， 2014.Study of surface dry and wet conditions in southwest China in re‐cent 50 years［J］. Journal of Natural Resoueces， 29（1）： 104-116. DOI： 10. 11849/zrzyxb. 2014. 01. 010.  
田晓瑞，赵凤君，舒立福，等， 2010. 西南林区卫星监测热点及森林火险天气指数分析［J］. 林业科学研究， 23（4）： 523-529. TianX R， Zhao F J， Shu L F， et al， 2010. Hotspots from satellitemonitoring and forest fire weather index analysis for southwestChina［J］. Forest Research， 23（4）： 523-529.  
王旭峰，马明国，姚辉， 2009. 动态全球植被模型的研究进展［J］.遥 感 技 术 与 应 用 ， 24（2）： 246-251. DOI： 10. 11873/j. issn.1004-0323. 2009. 2. 246. Wang X F， Ma M G， Yao H， 2009.Advance in dynamic global vegetation models［J］. Remote Sens‐ing Technology and Application， 24（2）： 246-251. DOI： 10.11873/j. issn. 1004-0323. 2009. 2. 246.  
王媛媛，谢正辉，贾炳浩，等， 2015. 基于陆面过程模式CLM4的中国区域植被总初级生产力模拟与评估［J］. 气候与环境研究， 20（1）： 97-110. DOI： 10. 3878/j. issn. 1006-9585. 2014. 13208.Wang Y Y， Xie Z H， Jia B H， et al， 2015. Simulation and evalu‐ation of gross primary productivity in China by using land surfacemodel CLM4［J］. Climatic and Environmental Research， 20（1）：97-110. DOI： 10. 3878/j. issn. 1006-9585. 2014. 13208.  
杨春艳，严小冬，夏阳，等， 2021. 近56a西南区域降水分布及持续性干旱的研究［J］. 中低纬山地气象， 45（2）： 15-22. DOI： 10.3969/j. issn. 1003-6598. 2021. 02. 003. Yang C Y， Yan X D， XiaY， et al， 2021. Study on precipitation distribution and persistentdrought in southwest China in recent 56 years［J］. Mid-low Lati‐tude Mountain Meteorology， 45（2）： 15-22. DOI： 10. 3969/j.issn. 1003-6598. 2021. 02. 003.  
杨明鑫，肖天贵，李勇，等， 2022. CMIP6模式对我国西南地区夏季气候变化的模拟和预估［J］. 高原气象， 41（6）： 15. DOI： 10.7522/j. issn. 1000-0534. 2021. 00119. Yang M X， Xiao T G， LiY， et al， 2022. Evaluation and projection of climate change insouthwest China using CMIP6 model ［J］. Plateau Meteorology，41（6）： 15. DOI： 10. 7522/j. issn. 1000-0534. 2021. 00119.  
张雪梅，王克林，岳跃民，等， 2017. 生态工程背景下西南喀斯特植被变化主导因素及其空间非平稳性［J］. 生态学报， 37（12）：4008-4018. DOI： 10. 5846/stxb201611192354. Zhang X M，Wang K L， Yue Y M， et al， 2017. Factors impacting on vegeta‐tion dynamics and spatial non-stationary relationships in karst re‐gions of southwest China［J］. Acta Ecologica Sinica， 37（12）：4008-4018. DOI： 10. 5846/stxb201611192354.  
甄英，李永飞，何静， 2019. 川西北高原甘孜州地区降水变化特征及旱涝研究［J］. 水土保持研究， 26（6）： 191-197. Zhen Y， Li YF， He J， 2019. Research on Characteristics of Precipitationchange and drought and flood in ganzi region of northwest Sich‐uan Plateau［J］. Research of Soil and Water Conservation， 26（6）： 191-197.  
郑朝菊，曾源，赵玉金，等， 2017. 近15年中国西南地区植被覆盖度动态变化［J］. 国土资源遥感， 29（3）： 128-136. DOI： 10.6046/gtzyyg. 2017. 03. 19. Zheng C J， Zeng Y， Zhao Y J， et al，2017. Monitoring and dynamic analysis of fractional vegetationcover in southwestern China over the past 15 years based on MO‐DIS data［J］. Remote Sensing for Land & Resources， 29（3）：128-136. DOI： 10. 6046/gtzyyg. 2017. 03. 19.

# Vegetation Growth Simulation of the Community Land Model in the Southwest China

WANG Lihuan1， 2， LÜ Yaqiong1 ， WANG Ziyi3（1. Institute of Mountain Hazards and Environment， Chinese Academy of Sciences， Chengdu 610041， Sichuan， China；2. University of Chinese Academy of Sciences， Beijing 100049， China；3. College of Atmospheric Sciences， Chengdu University of Information Technology / Sichuan Key Laboratoryof Plateau Atmosphere and Environment， Chengdu 610225， Sichuan， China）

Abstract：Under the background of global warming， the temperature has increased frequently in the southwest， and the ecosystem in the southwest is vulnerable and sensitive to climate change in the past few decades. The southwest region is an important carbon sink area in China. Monitoring and simulation of vegetation variations is of great significance for an in-depth understanding of the carbon cycle mechanism and promoting sustainable eco‐ nomic development. Leaf Area Index （LAI） and Gross Primary Productivity （GPP）， as indicators of vegetation health and ecosystem stability， can be used to quantify vegetation studies and characterize dynamic changes of vegetation. Vegetation dynamic Model is one of the important means to study vegetation growth and change. Community Land Model （CLM） is one of the earliest land model with the function of vegetation dynamic simu‐ lation， the most developed and widely used land model in the world. Model evaluation is an indispensable part of model development， which provides a basis for model development and improvement. This study uses the Com‐ munity Land Model version5 （CLM5） to simulate and analyze the spatial and temporal variations of the leaf area index （LAI） and total primary productivity （GPP） in the southwest region across 2000 -2016， and compare it with multiple sets of remote sensing data to evaluate LAI and GPP simulations of CLM5 in the southwest. The re‐ sults showed that CLM5 could well simulate the seasonal variation of LAI and GPP in southwest China， but over‐ estimated LAI in growing season. The CLM5 can reasonably simulate LAI of temperate deciduous broadleaf shrubs， LAI， GPP of alpine C3 meadow and GPP of C3 meadow. CLM5 could capture the spatial distribution pattern of LAI and GPP in the southwest， which is decreasing from southeast to northwest， but CLM5 overesti‐ mates LAI in the whole southwest region， especially in the karst landform area of Guizhou. Contrary to the over‐ estimation of LAI simulation， CLM5's overall simulation of GPP in Southwest China is low， especially in Yun‐ nan province. In addition， CLM5 has a poor simulation of LAI and GPP trend in the southwest. Especially in most parts of Yunnan， remote sensing data mainly shows an upward trend， while CLM5 simulation shows a downward trend. In a word， CLM5 can simulate the seasonal change and spatial distribution of LAI and GPP in the southwest， but the simulation of the trend in some areas of Yunnan and Guizhou is poor， and more in-depth parametric schemes for the development of farmland in Sichuan Basin， Yunnan forests， and karst vegetation in Guizhou are needed to improve the simulation.

Key words：CLM5； leaf area index； gross primary productivity； southwest China