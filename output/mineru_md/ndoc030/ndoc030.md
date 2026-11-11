# 基于大气CO2浓度升高对植被最大光能利用率的模拟及CASA模型的改进

郑泽豪1，张乐涛¹，王清源²，魏仪媛¹，何梦真¹，卫颖颖1（1.河南大学地理与环境学院，环境与规划国家级实验教学示范中心，河南 开封 475004；2.西北农林科技大学水土保持研究所，陕西 杨凌 712100)

摘要：[目的]为了在大气CO浓度不断升高的背景下准确估算植被净初级生产力（NPP)。[方法」在Carnegie-Ames-Stanford Approach(CASA)模型中引人CO浓度因子,来模拟不同植被类型的最大光能利用率，并在此基础上对改进后模型的NPP估计潜力进行探索。[结果］2000—2020年，年平均大气CO2浓度在中国陆地范围均表现为显著升高趋势,平均增幅为 2.14μmol/(mol·a);纳入CO胁迫因子后,植被类型按最大光能利用率从大到小为农田>常绿阔叶林>混交林>针叶林>灌丛>湿地>草地(1.85,1.69,1.30,0.87,0.52,0.40,0.40 g/MJ);CASA_CO模型对 NPP的估算精度相比于原CASA模型得到提高,CASA_COz模型在植被水平和综合水平的 NPP模拟值与实测值之间的R分别提升-0.1%～3.7%和0.5%,RMSE分别降低0.3%～9.2%和0.7%,年NPP估算结果的RMSE降低1.9%;CASA_CO模型改善CASA模型对整体 NPP的低估,由 10.62%降至9.81%,CASA_CO模型对春季、秋季和冬季的整体 NPP分别低估5.11%,2.72%,2.51%，夏季高估0.53%。[结论]在模型中考虑CO浓度变化对植被的影响，可以提高 NPP 估算的精度。

关键词：CO2；NPP；最大光能利用率；通量塔；植被类型中图分类号：X173 文献标识码：A 文章编号：1009-2242-(2024)05-0305-10

# Simulation of Vegetation Maximum Light Use Efficiency and Improvement of the CASA Model Based on Elevated Atmospheric CO2 Concentrations

ZHENG Zehao1 ， ZHANG Letaol ，WANG Qingyuan² ,

WEI Yiyuan’，HE Mengzhen’，WEI Yingying1 (1. National Demonstration Center for Environmental and Planning，College of Geography and Environmental Science，Henan University，Kaifeng,Henan 475O04，China；2. Institute of Soil and Water Conseruation，Northwest A&F University，Yangling，Shaanxi 7121oo，China)

Abstract: [Objective] In order to accurately estimate net primary productivity (NPP） of vegetation under the context of rising atmospheric CO2 concentrations.[Methods] A CO2 concentration factor was introduced into the Carnegie-Ames-Stanford Approach （CASA） model to simulate the maximum light use eficiency of diferent vegetation types. Based on this，the potential of the improved model for NPP estimation was explored.[Results] From 200o to 202O，the annual average atmospheric COz concentration in China's terrestrial areas showed a significant increasing trend，with an average increase of approximately 2.14 μmol/ (mon·a). After incorporating the CO2 stress factor，the vegetation types were ranked by maximum light use efficiency in the following order cropland>evergreen broadleaf forest>mixed forest>needleleaf forest> shrub>wetland>grassland (1.85，1.69，1.30，0.87，0.52，0.40，0.40 g/MJ). The estimation accuracy of NPP by the CASA_CO² model was improved compared to the original CASA model. The R² between the simulated and measured NPP values at the vegetation level and the comprehensive level increased by 一0.1% to 3.7% and 0.5%，respectively，and RMSE decreased by 0.3% to 9.2% and 0.7%，respectively. The RMSE of annual NPP estimation results decreased by1.9%.The CASA_CO2 model improved the underestimation of overall NPP by the CASA model，reducing it from 10.62% to 9.81%.The CASA_COz model underestimated the overall NPP for spring，autumn，and winter by 5.11%，2.72%，and 2.51%，respectively，while overestimating it for summer by 0.53%.[Conclusion] Considering the impact of CO2 concentration changes on vegetation in the model can improve the accuracy of NPP estimation.

Keywords:carbon dioxide； NPP； maximum light use eficiency； fluxes observation sites； vegetation types

Received:2024-05-14 Revised:2024-06-10 Accepted:2024-06-25 Online(www.cnki.net):2024-09-12

工业革命以来，大气CO浓度急剧上升，全球气候系统经历显著的变化[1]。这些变化不仅引起全球气温的升高和气候模式的改变，还直接影响生态系统的结构和功能。CO作为温室气体，其浓度升高增强温室效应，加剧气候变暖，进而影响生态系统的动态过程和碳循环机制。有研究[2表明，当今大气中的CO2浓度未达到植物进行光合作用的最适宜浓度，作为光合作用的重要底物，大气CO浓度升高可提升胞间CO浓度，加快植被的光合作用速率，从而提高植被的生产力[3]。深入研究CO2浓度升高对陆地生态系统功能的影响，尤其是对植被生产力的影响，对于理解碳循环和全球碳收支具有重要意义。

植物通过光合作用所固定的光合产物扣除其自身的呼吸消耗后剩余的部分被定义为 NPP[4],它体现植被将无机碳固定、转化为有机碳的效率，是研究碳循环的重要指标，在全球碳收支和气候系统中具有重要作用[5]。准确量化区域或全球尺度的NPP对进一步理解陆地生态系统与环境变化的相互作用至关重要。在估算NPP的各类模型中，基于遥感数据的光能利用率模型具有精度高、模型结构简单、输入数据易于获取等优点[6]，在区域及全球尺度的NPP 估算中得到广泛的应用。此类模型的 NPP 估算过程基于光能利用率理论[]：植被生长取决于入射太阳辐射中用于光合作用并被植物吸收的部分(APAR)和由最大光能利用率（LUEmax）估算的实际光能利用率(LUE)。LUEmax是光能利用率模型的重要构成部分，其值的确定直接影响光能利用率模型对NPP 的估算结果[8],早期的模型假设LUEmax在全球范围内是一个常数，但随着研究的深入,学者们[9-11]发现，这对区域NPP的估算造成很大的误差，并认为植被类型不同，其LUEmax亦不同。LUEmax受各种环境因素胁迫而下调得到LUE，这些胁迫因子主要有温度、水分、CO2浓度及营养元素供应等[3,12]。然而，并非所有模型对相同的胁迫因子都下调LUE,最简单的模型仅以温度为基础，大部分模型还包括水分条件。尽管CO浓度及养分可用性等环境胁迫因子对LUE有重要的影响[3,13],但它们在光能利用率模型中往往被忽略，导致模型对 NPP的估算精度难以得到进一步的提升。

基于大气CO2浓度升高对植被NPP带来的重要影响，本研究将CO胁迫因子引入CASA模型，利用涡度相关通量观测数据，结合遥感数据和气象数据模拟出不同植被类型的LUEmax，并比较原CASA模型和修改后模型的NPP估算精度。以期更加准确地估算陆地植被NPP,为评估全球碳循环和生态系统响应提供科学依据。

# 1材料与方法

# 1.1研究区概况

本文以中国14个通量观测站点观测的植被类型为研究对象，探索不同植被类型的LUEmax，并对模型进行校准和验证。研究站点共覆盖7种植被类型，其中4个为草地，1个为湿地，1个为灌丛，2个为针叶林,2个为混交林,2个为农田，2个为常绿阔叶林(图1）。

# 1.2数据来源与处理

1.2.1通量数据和气象数据本研究使用的通量数据如生态系统净CO交换（NEE)、生态系统呼吸(RE)等,气象数据如温度、空气相对湿度、风速、大气压、太阳辐射、净辐射、降水量等，来自国家生态数据中心资源共享服务平台（http://www.nesdc.org.cn/)提供的各碳水通量观测数据集。本研究共收集14个通量观测站点的数据（共85个站点年，978个有效样本)（表1)，并引用欧盟哥白尼全球土地服务中心提供的方法[14]对通量数据进行处理得到NPP,步骤为：NEP=-NEE,GPP=NEP+RE,NPP=O.5×GPP。式中：NEP为净生态系统生产力；GPP为总初级生产力;0.5为碳利用效率，依据经验确定。

![](images/dc6bbb376daabcbedc2f90c829195911d95f46718bc13348566139a4b2fa4c4c.jpg)  
注：基于自然资源部标准地图服务网站审图号为GS(2023)2763号的标准地图制作，底图边界无修改。  
图1通量观测站点分布与土地覆盖分类  
Fig.1Distribution of fluxes observation sites and land cover classification

1.2.2大气CO浓度数据大气CO2浓度数据来自国家生态数据中心资源共享服务平台（http://www.nesdc.org.cn/），空间分辨率为1°,时间分辨率为月，其中，2003—2009 年的大气CO浓度基于二氧化碳信息分析中心化石燃料CO2历史排放数据和按纬度分解的CO2浓度的纵向特征构建，2010—2020 年的大气CO浓度利用GOSAT和OCO-2卫星反演数据，基于地理统计学方法插值获得。

1.2.3NDVI数据NDVI遥感数据来自美国国家航空航天局的 MODl3Q1 数据集(https://ladsweb.modaps.eosdis.nasa.gov/）,空间分辨率为 250 m,时间分辨率为16天。本研究利用Python 对该数据进行最大值合成，得到月NDVI影像数据。通量塔的贡献区一般为塔高的10倍[15]，其中超过70%足迹的贡献区分布于通量塔200 m以内[16]，结合通量塔塔高与影像数据的空间分辨率，本研究将距离通量观测站点坐标最近的4个像元的 NDVI平均值作为通量观测站点观测范围的月NDVI数据。

1.2.4土地覆盖数据本研究使用国际地圈-生物圈计划(IGBP)的MODIS土地覆盖分类方案，MODISIGBP土地覆盖数据来源于MCD12Q1土地覆盖科学数据产品，空间分辨率为1km，将MODISIGBP的17种土地覆被类型重新划分为9类[17-18]（图1)：常绿阔叶林、落叶阔叶林、针叶林、混交林、农田、草地、灌丛、湿地和其他类型(非植被区域，如水体、永久

雪地、城市和未利用地)。

# 表1通量观测站点

Table 1Fluxes observation sites   

<table><tr><td>站点</td><td>坐标</td><td>植被类型</td><td>观测年份</td></tr><tr><td>长白山</td><td>128.0958E,42.4025N</td><td>混交林</td><td>2003—2010</td></tr><tr><td>鼎湖山</td><td>112.5342E,23.1736N</td><td>混交林</td><td>2003—2010</td></tr><tr><td>海北灌丛</td><td>101.3333E,37.6667N</td><td>灌丛</td><td>2003—2010</td></tr><tr><td>千烟洲</td><td>115.0667E,26.7333N</td><td>针叶林</td><td>2003—2010</td></tr><tr><td>禹城</td><td>116.5700°E,36.8289N</td><td>农田</td><td>2003—2010</td></tr><tr><td>海北湿地</td><td>101.3167E,37.6167N</td><td>湿地</td><td>2004—2009</td></tr><tr><td>内蒙古</td><td>116.4040°E，43.3255N</td><td>草地</td><td>2004—2010</td></tr><tr><td>哀牢山</td><td>101.2333E,24.5381N 常绿阔叶林</td><td></td><td>2009-2013</td></tr><tr><td>西双版纳</td><td>101.2667E,21.9000N 常绿阔叶林</td><td></td><td>2010—2014</td></tr><tr><td>海北草地1</td><td>101.3167E,37.6167N</td><td>草地</td><td>2011—2013,2016—2018, 2020</td></tr><tr><td>元江</td><td>102.1667E,23.3000N</td><td>草地</td><td>2013—2015</td></tr><tr><td>呼中</td><td>121.0178E,51.7811N</td><td>针叶林</td><td>2014—2018</td></tr><tr><td>若尔盖</td><td>102.5500E,32.8000N</td><td>草地</td><td>2016—2018,</td></tr><tr><td>长岭</td><td>123,4703E,44.5967N</td><td>农田</td><td>2020 2018-2020</td></tr></table>

# 1.3研究方法

1.3.1Manner-Kendall 检验和 Theil-Sen 斜率估计

本研究采用Manner-Kendall（M-K）非参数检验[19]逐像元计算大气CO浓度随时间的变化趋势。由于M-K非参数检验只能提供变量趋势的正负和统计显著性，不能明确变量趋势的大小，本研究又引入Theil-Sen斜率估计法对大气COz浓度的变化程度进行量化。

1.3.2CASA 模型 CASA模型[20]是一个典型的光能利用率模型，在全球和区域尺度下NPP估算的研究中都得到广泛地应用，计算公式为：

![](images/881052699ae4d4020eb7c14dabd20d728dfa6f60ad68b192e03fffe30ffff868.jpg)

式中：APRA为植被吸收的光合有效辐射[MJ/（m²·mon)];LUE为植被的实际光能利用率(g/MJ）。

CASA模型利用基于实际气温与植被最适气温关系的温度胁迫因子和基于实际蒸散量与潜在蒸散量关系的水分胁迫因子来下调LUEmax得到LUE，计算公式为：

![](images/5885f76c78e470b4be61e38e72acf8b7f9e72d2ac586ba82dac976d0e6a2ecf6.jpg)

式中：T和W分别为温度胁迫系数和水分胁迫系数;LUEmax为最大光能利用率(g/MJ）。

![](images/65bd1767ed45a6116f3d81073c881f2d8cbd398c3f477c6d49f095fa20da878b.jpg)

式中：T为低温和高温时植物内在的生化作用对光合的限制;T为环境温度偏离植物最适生长温度时对光合的限制。

水分胁迫是植被的水分条件对植被生理特征造成的影响，它与环境中有效水分的质量分数有关，

CASA模型中水分胁迫因子W为0.5～1.0,其计算公式为：

![](images/f5d2174cf717b09c655fdc89abe699cf8b00ad0680bf01664a75a786f24dcc6d.jpg)

式中：E为区域实际蒸散量;E,为区域潜在蒸散量，当E>Ep时,说明水分充沛,W取1。

1.3.3考虑CO浓度的 NPP估算CASA模型在模拟LUEmax时没有考虑CO浓度对植被生产力的影响，本文参考改进的 EC_LUE 模型[13],引入CO胁迫因子来下调LUE,对CASA模型进行改进得到CASA_CO2模型为：

NPP=APARXT XW XCO2 XLUEmax (5)式中：COz为CO浓度对LUE 的胁迫作用，其计算公式与参数说明为

![](images/0d491568875dce81802165592eb4519b2e05afe775bfc3f5fef697d4337e9340.jpg)

![](images/04166e6c33b90619c7b2f01e4c8f336d2625e8c12a766fa5fad1a88de6dbdb73.jpg)

式中:φ 为无暗呼吸时的CO补偿点(μmol/mol);Ci为叶片内部 CO浓度（μmol/mol);Ca为大气CO浓度(μmol/mol);X 为叶片内部与大气CO浓度的比值。

![](images/a8fa3a6bb5f8df926291b81ef453fd0174137ad1c79f9028886983e1ea4c1246.jpg)

![](images/d555c34c4ac825ce2f4789df77c03cbb7c39bc27c9b3a5cc2a128ed79ac679ce.jpg)

式中：VPD为饱和水汽压差(Pa);为X对VPD的敏感性;K 为 Rubisco 酶的 Michaelis-Menten 系数；η\*为水在25℃时的相对黏度。

![](images/d40897ab8825f01df4683edc011631b050f3fe3df6d3bc93021020aa061a95d6.jpg)

式中：P为O的分压，近似为21278.25Pa;K和K。为 CO和O的Michaelis-Menten 常数;R为摩尔气体常数,设为8.314J/（mol·K)。

![](images/7155e4885854415a47b64d0ac86b4e064cbfc9eb61f4d089114a625c0b05ccae.jpg)

![](images/fb54ef1d2756e39988bc49c9590b22b7271ec41f9c1066198742a994034e6636.jpg)

式中：Ta为空气温度(K)。

1.3.4最大光能利用率的模拟按时间顺序，选取各通量观测站点前2/3年份的样本用以确定不同植被类型的LUEmax,剩余样本用于模型精度的评价。首先，计算出各通量观测站点每月的NPP、APAR、T、W和CO2,并代入公式(5)移项,可得其对应的LUEmax，后根据误差最小原则分别模拟各通量观测站点的LUEmax。

每个通量观测站点或植被类型NPP实测值与模拟值之间误差(E)的计算公式为：

![](images/dcf3987ec68d4caae07d288c0f460509bc644900ee466807bdf9f917bd7611e0.jpg)

式中：x 为待定的LUEmax;i为某通量观测站点的样本数；j为某通量观测站点的最大样本数；n为APAR×T×W ×CO2。可将公式(13)展开,得到公式(14)：

![](images/16a31e17d7621b1bb8c14ef94e61bf5495d1c8f84ab57e24e22c7f4df3df8a75.jpg)

当E(x)最小时求的LUEmax的值为：

![](images/4281a2d9c22a6e6936009935caa7fd1b0ed290ad44054faa45a42a90fc6c51f7.jpg)

1.3.5模型检验分别将CASA模型和CASA_CO模型的NPP估计值与通量观测站点的NPP实测值比较，并通过计算决定系数(R)和均方根误差(RMSE)来评估模型的NPP估计性能，R²越大、RMSE越小，表明模型性能越好。

# 2结果与分析

# 2.1大气CO浓度时空变化分析

2.1.1大气CO浓度的空间分布与季节变化2000—2020年间中国4个季度的平均大气CO浓度表现出明显的空间分布与季节变化特征(图2)。从空间分布来看，4个季度大气CO2浓度的高值区都集中分布在东部，且表现为辐射状分布，向四周逐渐降低；低值区具有季节性变化，在春季和夏季主要分布在北部地区，在秋季和冬季主要分布在西南地区。

从季节变化来看，2000—2020 年的平均大气COz浓度在春夏秋冬分别为394.11～404.26，384.57～398.37,392.60～400.58,396.62～403.78 μm0l/mol,在春季达到最高，夏季降至最低，秋季大气CO浓度高于冬季，尤其在西部地区这种差距最为明显。

2.1.2大气CO浓度的年际变化Mann-Kendall趋势检验表明,2000—2020 年平均大气CO2浓度在全国表现出显著升高的趋势(Zmin=11.50>2.58,p<0.01)，Theil-Sen 斜率(0i)为1.82～2.28 μmol/（mol·a),平均值为2.14μmol/(mol·a)（图3)。大气COz浓度升高速度在空间上表现出东部地区快于西部地区，北部地区快于南部地区的特征。

# 2.2最大光能利用率模拟结果

2.2.1各通量观测站点的最大光能利用率各个通量观测站点植被类型的LUEmax模拟结果见表2。在未引入CO胁迫因子时,LUEmax模拟值为0.18～1.18 g/MJ，引入CO胁迫因子后，LUEmax模拟值为0.28～1.72g/MJ,在所有站点中，内蒙古(草地)的LUEmax最低，禹城(农田)的LUEmax最高。除混交林外，由改进前后2种模型模拟的同一种植被类型在不同站点的LUEmax值都较为接近,说明同种植被类型的LUEmax不随空间或时间的变化而变化。

![](images/527ddcc6ab549d56f1bb026f5d1039141f91b5d18432c3dbafc43c2808ec5c2e.jpg)  
注：基于自然资源部标准地图服务网站审图号为GS(2023)2763号的标准地图制作，底图边界无修改。

Fig.2Spatial distribution and annual changes of annual average atmospheric COconcentration from 2ooo to 2020

![](images/f31dfd73d85f94c59e52a6f823a955dfb1d68ff7812e9f6b85e5126cf42449b7.jpg)  
图22000一2020年平均大气CO浓度空间分布与季节变化  
注：基于自然资源部标准地图服务网站审图号为GS(2023)2763号的标准地图制作，底图边界无修改。  
图32000一2020年年平均大气CO2浓度年际变化斜率分布格局  
Fig.3The spatial pattern of interannual variation slope of average atmospheric CO concentration during 2ooo to 2020

2.2.2各植被类型的最大光能利用率本研究在模拟植被类型的LUEmax时，为了站点权重的一致，对同种植被类型的站点选取相同数量的样本，模拟结果见表3。在未引入CO胁迫因子时，LUEmax模拟值为0.27～1.22g/MJ,引入CO胁迫因子后，LUEmax模拟值为0.40～1.85g/MJ。不同植被类型的LUEmax存在差异,从大到小依次为农田>常绿阔叶林>混交林>针叶林>灌丛>湿地>草地，该排序在2个模型模拟下相同，表明不同植被类型受到的CO2胁迫相近。农田的LUEmax最高，可能与农田的高生产力和管理实践有关;森林植被类型的LUE.ax高于其他植被类型，相同环境条件下，森林植被类型更有助于碳汇。

表2各通量观测站点LUEmax模拟值  
Table 2Simulated values of LUEmax at various fluxes observation sites   
表3各植被类型LUEmax模拟值  

<table><tr><td rowspan="2">站点</td><td rowspan="2">植被类型</td><td rowspan="2">样本数</td><td colspan="2">LUEmax/(g·MJ-1)</td></tr><tr><td>CASA</td><td>CASA_CO2</td></tr><tr><td>海北草地</td><td>草地</td><td>60</td><td>0.28</td><td>0.42</td></tr><tr><td>若尔盖</td><td>草地</td><td>24</td><td>0.32</td><td>0.45</td></tr><tr><td>内蒙古</td><td>草地</td><td>48</td><td>0.18</td><td>0.28</td></tr><tr><td>元江</td><td>草地</td><td>24</td><td>0.27</td><td>0.38</td></tr><tr><td>海北湿地</td><td>湿地</td><td>36</td><td>0.28</td><td>0.40</td></tr><tr><td>海北灌丛</td><td>灌丛</td><td>60</td><td>0.40</td><td>0.52</td></tr><tr><td>千烟洲</td><td>针叶林</td><td>60</td><td>0.73</td><td>0.89</td></tr><tr><td>呼中</td><td>针叶林</td><td>36</td><td>0.73</td><td>0.88</td></tr><tr><td>鼎湖山</td><td>混交林</td><td>60</td><td>0.74</td><td>1.08</td></tr><tr><td>长白山</td><td>混交林</td><td>60</td><td>1.03</td><td>1.50</td></tr><tr><td>禹城</td><td>农田</td><td>60</td><td>1.14</td><td>1.72</td></tr><tr><td>长岭</td><td>农田</td><td>24</td><td>1.12</td><td>1.64</td></tr><tr><td>哀牢山</td><td>常绿阔叶林</td><td>36</td><td>1.16</td><td>1.67</td></tr><tr><td>西双版纳</td><td>常绿阔叶林</td><td>36</td><td>1.18</td><td>1.69</td></tr></table>

Table 3Simulated values of LUEmxfor various vegetation types   

<table><tr><td rowspan="2">植被类型</td><td rowspan="2">样本数</td><td colspan="2">LUEmax模拟值/(g·MJ-1)</td></tr><tr><td>CASA</td><td>CASA_CO2</td></tr><tr><td>草地</td><td>96</td><td>0.27</td><td>0.40</td></tr><tr><td>湿地</td><td>36</td><td>0.28</td><td>0.40</td></tr><tr><td>灌丛</td><td>60</td><td>0.40</td><td>0.52</td></tr><tr><td>针叶林</td><td>72</td><td>0.72</td><td>0.87</td></tr><tr><td>混交林</td><td>120</td><td>0.90</td><td>1.30</td></tr><tr><td>常绿阔叶林</td><td>72</td><td>1.17</td><td>1.69</td></tr><tr><td>农田</td><td>48</td><td>1.22</td><td>1.85</td></tr></table>

# 2.3模型性能比较

分别模拟原CASA模型与CASA_CO模型对每个站点的 NPP估算值和 NPP实测值的关系（图4)发现，不同站点的NPP估计值与NPP实测值表现出不同的相关性。2个模型估算结果的R均表现为长岭>海北灌丛>长白山>若尔盖>海北草地>海北湿地>呼中>元江>内蒙古>西双版纳>千烟洲>鼎湖山>禹城>哀牢山，其值分别为0.458～0.948和0.454～0.947，除哀牢山站，其他站点都大于0.55，且主要集中在0.70以上（10个)，且p值都小于0.01，表明模型模拟效果理想;RMSE分别为3.40～44.71,3.41～44.01g/（m²·mon)，同种植被类型的通量观测站点的RMSE接近，不同植被类型的RMSE 的差异较大。CO浓度胁迫的引入提高9个站点的R²，并使若尔盖、内蒙古、元江、海北灌丛、西双版纳、千烟洲、呼中、鼎湖山、长白山、海北湿地和禹城等11个站点的RMSE分别降低0.40,0.15,0.40,0.09,1.41,0.11,1.78,0.07,0.05,1.43,0.56g/（m²·m0n)。整体来看，CASA_CO模型对不同通量观测站点NPP估计的表现优于原CASA模型。

![](images/ffc428dfd41bdc1490221f98e5a04b533efd0b30a894fc17896a50b89655c2e8.jpg)  
图4模型 NPP估算精度比较(站点)  
Fig.4Model NPP estimation accuracy comparison (site)

分别将CASA模型和CASA_CO模型对不同植被类型的NPP估值与实测NPP数据进行比较（图5)发现,对于研究中的7种植被类型，利用CASA_CO2模型估算的NPP与实测NPP之间的线性回归线都比利用CASA模型更贴合1：1线。

比较2个模型对各植被类型NPP模拟结果的R和RMSE发现，模型对不同植被类型的估计效果具有差异,R²分别为0.654～0.941,0.659～0.941,RMSE分别为9.74～50.84,9.66～50.36g/（m²·m0n)，且p值都小于0.01,表明模型的模拟结果均较为理想。其中草地、灌丛和湿地的估算精度较高[R²>0.850,RMSE<20.00g/（m²·mon)],农田的估算精度最低。各植被类型检验样本的CO2浓度变异系数为0.26%～3.01%，除湿地以外,CASA_CO模型的R²都大于原CASA 模型，提升0.1%～3.7%;CASA_CO模型的RMSE都小于原CASA模型，降低0.3%～9.2%,表明CO胁迫因子的引入还提高模型对不同植被类型NPP估计的精度。

在综合水平上比较2个模型的估算结果(图6)发现，2个模型都低估整体NPP，分别低估10.62%，9.81%。其中，春季分别低估5.31%,5.11%，夏季分别高估0.21%,0.53%，秋季分别低估2.93%,2.72%，冬季分别低估2.59%，2.51%，模型对夏季模拟结果最优，春季最差。相比原CASA模型,CASA_CO模型的R²增大0.0038,RMSE减小0.21g/（m²·mon),对整体 NPP的估算精度更高，表明CO胁迫的引入一定程度上改善模型对NPP 的低估。

将月NPP累加得到年 NPP,比较2个模型对年NPP 的估算精度(图7)发现,CASA_CO模型估算的年 NPP与年NPP实测值的回归直线比CASA模型的更接近1：1线，且CASA_CO2模型的RMSE比CASA模型小2.94g/（m²·a),表明CASA_CO模型对年NPP 的估算精度高于CASA模型。

# 3讨论

# 3.1LUEmax模拟的不确定性

有研究[17,21]表明，植被分类精度给LUEmax带来不确定性，本研究在对位于不同通量观测站点的相同植被类型的LUEmax进行模拟时发现，除混交林以外,草地、针叶林、农田和常绿阔叶林在不同通量观测站点的LUEmax模拟值都较为接近，混交林在鼎湖山站和长白山站的LUEmax模拟值分别为1.08，1.50g/MJ，出现这种差异的原因可能是植被分类精度不同。鼎湖山站和长白山站的植被类型分别可细分为常绿针、阔叶混交林和常绿、落叶阔叶混交林，鼎湖山站的LUEmax模拟值接近于针叶林站点的模拟值（千烟洲0.89g/MJ，呼中0.88 g/MJ)，长白山站的LUEmax模拟值接近于落叶阔叶林站点的模拟值（哀牢山1.67g/MJ,西双版纳1.69g/MJ)，这可能与混交林中各种林分的占比有关。

不同学者对同一植被类型LUEmax值的模拟结果有所差异，一部分原因是他们使用的光能利用率模型结构的不同[22]；另一部分原因是气象、通量等数据的来源不同，如温度、饱和水汽压差、土壤含水量等可通过卫星遥感图像获得，也可通过地面气象观测获得，通量数据的观测站点和年份不同等，甚至导致学者们[8,17-18,23-24]确定的不同植被类型LUEmax的大小顺序有很大不同。同样使用原CASA模型去模拟不同植被类型的LUEmax,本研究的模拟结果高于朱文泉等[17]的研究结果，可能与原CASA模型没有考虑CO浓度的胁迫作用有关。本研究使用的数据年份在2003—2020年，此间CO浓度高于朱文泉等[17]模拟LUEmax时(1989—1993年)的浓度,CO胁迫作用相对减小，从而提高 NPP,若不考虑CO胁迫因子，模拟的LUEmax值将变大。而本研究中，采用同一时段的数据模拟LUEmax,CASA 模型的模拟结果小于CASA_CO模型，这是因为CASA模型在计算LUE时，没有考虑CO胁迫对LUEmax的下调作用，根据实测数据反演的LUEmax小于CASA_CO模型，二者模拟的LUEmax的比值可视为植被在模拟时段所受到的平均CO胁迫作用。

![](images/89b382f9df649f56b9aeaf34385a8ec551fbdd4dd37e169f8256f480692efdb5.jpg)  
图5模型 NPP估算值比较(植被)  
Fig.5Comparison of the NPP estimates by models (vegetation) http://stbcxb.alljournal.com.cn

注：散点的颜色表示季节，绿色为春季，黄色为夏季，橙色为秋季，蓝色为冬季。

![](images/f3eef64748586b2ab771d2e0a2263c8e71b260bb1d5e23e1cd345a3456d7473b.jpg)  
图6模型 NPP估算精度比较(综合水平)

300 (b）  
250  
200  
R²=0.7197RMSE=29.83g/（m²·mon）p=6.63e-10 1  
0 50 100 150 200 250 300NPP实测/（gm²·mon））

![](images/9762622b2729a9f5f4e255ffe568c6cf6582f5432f2fca973d9b491c073980ae.jpg)  
Fig.6Comparison of estimation accuracy of NPP by models (comprehensive level)   
图7模型年NPP估算精度比较  
Fig.7Comparison of estimation accuracy of annual NPP by models

CASA模型和CASA_CO模型在不同站点对NPP的解释率分别为0.458～0.948,0.454～0.947，变化范围大，且解释率高的站点分布在高纬度地区，解释率低的站点分布在低纬度地区，说明还存在其他与纬度相关的因素影响着植被的光能利用率，且在低纬度地区作用强烈，可能的因素有养分的可利用性和土壤酸碱度等。

# 3.2CASA_CO2模型在 NPP估算中的局限性

尽管LUE 模型被广泛应用于植被生产力的估算中，但这些模型仅能解释62%～70%的通量观测站点数据[12]。在以往的研究中，学者们通过在LUE模型中加入植被物候因子、提出新的指标如NIRRad[25]、区分直接PAR和漫射PAR[26]、区分日照叶片和遮荫叶片吸收PAR[27]等,试图提高光能利用率模型对植被生产力的估计精度。本研究在CASA模型中引入CO胁迫因子，无论是在通量观测站点、植被类型还是综合水平上，均提升模型对植被生产力估计的性能，对年NPP的解释达到86%。除此类环境因子,学者们[28]还表明，营养物质供给对植被生产力产生影响，如氮沉降增加植被的固碳作用。高浓度O3胁迫损耗植被生产力[29],林龄等植被自身条件也影响植被的生产力[30]。为了能够对植被生产力进行更加准确的估算，模型还需全面考虑以上这些因素。

在本研究中使用的CASA 模型和CASA_COz模型都对 NPP存在低估，类似的情况出现在其他一些模型中，如ZHANG等[23]研究发现,MOD17模型和EC-LUE模型低估夏季的GPP。这些模型都包含水分和温度胁迫因子，且都使用乘法对胁迫作用进行积分，可能是它们对生产力存在季节性低估的原因。与单因素胁迫相比,水分和温度胁迫的共同作用可进一步降低植物的光合效率[31]，但干旱胁迫的发生往往伴随着高温或低温胁迫，这种情况下对水分和温度胁迫相乘进行积分，使得二者的共同作用被高估。基于Liebig's定律的最小值法仅考虑胁迫作用最大的环境因子[32],该方法在解决光能利用率模型的生产力季节性低估这一问题中值得尝试，但其在光能利用率模型中的具体应用还有待进一步研究。

# 4结论

(1)中国陆地大气CO2浓度的高值区集中分布在东部，且呈辐射状向外降低，年平均大气CO2浓度表现出显著增长的长期变化趋势，平均 Theil-Sen 斜率为2.14 μmol/(mol·a)。

（2)CASA_CO模型模拟的不同植被类型的LUEmax为:农田(1.85g/MJ),常绿阔叶林(1.69g/MJ),混交林(1.30 g/MJ),针叶林(0.87 g/MJ),灌丛(0.52 g/MJ),湿地(O.40 g/MJ),草地(O.40g/MJ),在合理的管理措施下,农田和森林植被类型可作为主要的碳汇。

(3)CASA_CO模型通过引入CO胁迫因子的方式对CASA模型进行改进，无论是在通量站水平、植被类型水平还是综合水平上，相比于原模型，其模拟的NPP与实测NPP之间的R²更高,RMSE更低，对年NPP的估算精度也更高。CASA_CO模型有效降低 NPP估算的不确定性，为中国陆地植被和全球碳循环研究提供可靠的 NPP 估算。

# 参考文献：

[1] 王苗苗，王绍强，陈斌，等.2020—2050年CO施肥效应 促进全球陆地生态系统碳吸收[J].生态学报,2023,43 (6):2408-2418. WANG M M,WANG S Q,CHEN B,et al. CO2 fertilization promoting the carbon uptake of global terrestrial ecosystems in 2020—2050[J].Acta Ecologica Sinica, 2023,43(6):2408-2418.   
[2] WU J，GUAN K Y，HAYEK M，et al. Partitioning controls on Amazon forest photosynthesis between environmental and biotic factors at hourly to interannual timescales [J].Global Change Biology,2017,23(3):1240-1257.   
[3] DEKAUWE MG，KEENAN TF，MEDLYNBE, et al.Satellite based estimates underestimate the effect of CO² fertilization on net primary productivity[J]. Nature Climate Change,2016,6:892-893.   
[4] ZHENGY,SHEN RQ，WANG YW,et al. Improved estimate of global gross primary production for reproducing its long-term variation，1982—2017[J].Earth System Science Data,2020,12(4):2725-2746.   
[5] SUN C M, ZHONG X C,CHEN C,et al. Evaluating the grassland net primary productivity of Southern China from 20oo to 201l using a new climate productivity model[J].Journal of Integrative Agriculture,2016,15 (7):1638-1644.   
[6] RUNNING S W，THORNTON P E，NEMANI R, et al.Global terrestrial gross and net primary productivity from the earth observing system[M]//SALA O E,JACK-SON R B,MOONEY H A，et al. Methods in Ecosystem Science. New York: Springer,2000:44-57.   
[7] MONTEITH JL. Solar radiation and productivity in tropical ecosystems [J].Journal of Applied Ecology, 1972,9(3):747-766.   
[8] LV Y L，CHI H，SHI P C，et al.Phenology-based maximum light use efficiency for modeling gross primary production across typical terrestrial ecosystems[J].Remote Sensing,2023,15(16) :e4002.   
[9] TURNERDP，URBANSKIS，BREMERD，etal．A cross-biome comparison of daily light use efficiency for gross primary production LJ」.Global Change Biology, 2003,9(3):383-395.   
[10]RUIMY A，SAUGIER B,DEDIEUG.Methodology for the estimation of terrestrial net primary production from remotely sensed data [J].Journal of Geophysical Research:Atmospheres,1994,99(D3):5263-5283.   
[11] GOETZ S J，PRINCE S D. Remote sensing of net primary production in boreal forest stands[J].Agricultural and Forest Meteorology,1996,78(3/4):149-179.   
[12]高德新，王帅，李琰，等.植被光能利用率：模型及其不确 定性[J].生态学报,2021,41(14)：5507-5516. GAO D X,WANG S,LI Y, et al. Light use efficiency of vegetation:Model and uncertainty[J].Acta Ecologica Sinica,2021,41(14):5507-5516.   
[13]YUAN W，ZHENG Y，PIAO S，et al. Increased atmospheric vapor pressure deficit reduces global vegetation growth[J]. Science Advances,2019,5(8):e1396.   
[14]SWINNEN E，VAN H R，EERENS H，et al. Algorithm theoretical basis document:dry matter productivity (DMP) [EB/OL].[2023-6-16]. htps://land.copernicus.eu/en.   
[15]徐珂,邢艳秋,常晓晴.亚热带常绿针叶林光能利用率模 型优化与总初级生产力估算[J].森林工程,2021,37（5)： 28-36. XU K，XING Y Q，CHANG X Q. Model optimization and GPP estimation of light energy utilization in subtropical evergreen coniferous forest[J].Forest Engineering,2021,37(5):28-36.   
[16］王彦伟，罗维均，陈佳，等.2015—2019年贵州普定自然 恢复样地碳水通量观测数据集[J].中国科学数据,2023， 8(3):78-89. WANGYW,LUO WJ,CHENJ，etal.Adataset of carbon and water fluxes in the sample plots of natural regeneration at Puding Station of Guizhou Province(2015- 2019)[J].China Scientific Data,2023,8(3):78-89.   
[17」朱文泉,潘耀忠,何浩,等.中国典型植被最大光利用率 模拟[J].科学通报，2006,51(6):700-706. ZHU WQ,PAN Y Z,HE H,et al. Simulation of maximum light utilization efficiency of typical vegetation in China[J].Chinese Science Bulletin,2006,51(6):700-706.   
[18]YANG D, XU X L, XIAO F J,et al. Improving modeling of ecosystem gross primary productivity through re-optimizing temperature restrictions on photosynthesis[J].Science of the Total Environment,2021,788:el47805.   
[19］KENDALL M. Rank correlation methods[J].British Journal of Psychology,1990,25(1) :86-91.   
[20]POTTERC S，RANDERSONJT，FIELDCB，et al. Terrestrial ecosystem production：A process model 1 1 111 Biogeochemical Cycles,1993,7(4):811-841.   
[21]BAO S N，IBROM A，WOHLFAHRT G，et al.Narrow but robust advantages in two-big-leaf light use efficiency models over big-leaf light use eficiency models at ecosystem level[J].Agricultural and Forest Meteorology, 2022,326:e109185.   
[22]朱安然，孙睿，王梦佳.植被光能利用率遥感估算[J].遥 感学报,2021,25(6)：1227-1243. ZHUA R，SUN R，WANG MJ.Estimation of light use efficiency by using remote sensing data[J].National Remote Sensing Bulletin,2021,25(6):1227-1243.   
[23] ZHANG Y H,HU Z W,WANGJZ,et al. Temporal upscaling of MODIS instantaneous FAPAR improves forest gross primary productivity (GPP） simulation[J]. International Journal of Applied Earth Observation and Geoinformation,2023,121:el03360.   
[24]RUNNING S W，ZHAO M. MOD17 user’s guide.Daily GPP and annual NPP（MODl7A2/A3） products NASA earth observing system MODIS land algorithm[EB/OL]. [2015-10-07]. http://modis.gsfc.nasa.gov.   
[25]LIU L Y,LIU XJ,CHENJD,et al. Estimating maize GPP using near-infrared radiance of vegetation [J]. Science of Remote Sensing,202o,2:el00009.   
[26]CHEN S Y，SUI L C，LIUL Y，et al.Effect of the partitioning of diffuse and direct APAR on GPP estimation[J].Remote Sensing,2022,14(1) :e57.   
[27] HE M Z,JU W M,ZHOU YL，et al. Development of a two-leaf light use efficiency model for improving the calculation of terrestrial gross primary productivity[J]. Agricultural and Forest Meteorology,20l3,173:28-39.   
[28] ZHANG H L，BAI J，SUN R，et al. An improved light use efficiency model by considering canopy nitrogen concentrations and multiple environmental factors[J].Agricultural and Forest Meteorology,2023,332:el09359.   
[29]徐静馨，郑有飞，王圣，等.O3胁迫下冬小麦总初级生产 力的损耗模拟[J].环境科学,2019,40(10)：4725-4732. XUJX，ZHENG Y F，WANG S，et al. Simulated ozone damage on gross primary productivity(GPP） in a winter wheat field[J].Environmental Science,2Ol9，40 (10):4725-4732.   
[30]KINGDA，TURNERDP,RITTS WD.Parameterization of a diagnostic carbon cycle model for continental scale application[J].Remote Sensing of Environment, 2011,115(7):1653-1664.   
[31] XU Z Z，ZHOU G S. Effects of water stress and nocturnal temperature on carbon allocation in the perennial grass，Leymus chinensis [J]. Physiologia Plantarum, 2005，123(3):272-280.   
[32]PEI YY，DONGJW，ZHANG Y，et al.Evolution of light use efficiency models:Improvement,uncertainties, and implications[J].Agricultural and Forest Meteorology, 2022,317:e108905.

# （上接第284页）

[36]秦鹏程，刘敏，杜良敏，等.气候变化对长江上游径流影响预估[J].气候变化研究进展，2019,15(4)：405-415.QIN PC,LIU M,DUL M,et al.Climate change impactson runoff in the Upper Yangtze River Basin[J].ClimateChange Research,2019,15(4):405-415.  
[37]何旭,缪子梅，田佳西，等.基于CMIP6多模式的长江流域气温、降水与径流预估[J].南京林业大学学报（自然科学版），2024,48(2)：1-8.HE X，MIAO Z M，TIAN J X，et al. Temperature,precipitation and runoff prediction in the Yangtze RiverBasin based on CMIP 6 multi-model[J].Journal ofNanjing Forestry University（Natural Sciences Edition）,2024,48(2):1-8.

[38]王媛,苏布达,王艳君,等.“双碳”情景下抚河流域径流

变化特征[J].长江科学院院报，2023，40(2)：44-51. WANG Y，SU BD，WANG YJ，et al.Streamflow change in Fuhe River Basin under China’s dual-carbon scenario[J].Journal of Changjiang River Scientific Research Institute,2023,40(2):44-51.   
[39]DAMS J，NOSSENT J，SENBETA T B，et al.Multimodel approach to assess the impact of climate change on runoff[J].Journal of Hydrology,2015,529:1601-1616.   
[40］薛联青，白青月，刘远洪.人类活动影响下塔里木河流域 气象干旱向水文干旱传播的规律[J].水资源保护,2023， 39(1):57-62. XUEL Q，BAI QY，LIU Y H. Propagation law from meteorological drought to hydrological drought in the Tarim River Basin under the impact of human activities [J].Water Resources Protection,2023,39(1):57-62.