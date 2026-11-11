引用格式:戴肖杰，范晓梅，闵彤． 基于时空融合技术的高精度遥感蒸散计算［J］． 科学技术与工程，2023，23( 25) : 10688-10700.［］    ， ， ( ) :

# 基于时空融合技术的高精度遥感蒸散计算

戴肖杰，范晓梅 ，闵彤( 南京信息工程大学地理科学学院，南京 )

摘 要 在利用遥感数据进行蒸散计算时，常因云雨污染和单一传感器限制，导致影像数据缺失严重，特别是在一些景观破碎化程度高的地区，较难获取高时空分辨率的蒸散序列 以黄河三角洲为研究区，基于增强型时空自适应融合模型构建高时空分辨率的遥感数据集，结合地表能量平衡系统模型采用先估算后融合和先融合后估算两种方式估算了区域  年高时空分辨率的蒸散时间序列，探讨了融合算法和蒸散模型相结合的可行性和估算精度。 结果表明: 增强型时空自适应反射率融合模型(        ， ) 算法性能较好，融合反射率与实际反射率的相关系数均在   以上; 地表能量平衡系统(    ， ) 模型估算的显热通量与通量站数据的均方根误差(    ， ) 仅为    ，融合模型估算的水面蒸发与蒸发皿折算数据的相关系数达到了  ;黄河三角洲蒸散量随季节变化较大，其中夏季蒸散量约占全年的  ，不同地物类型的年蒸散量差异明显，为; 蒸散的空间分布格局受海陆分布和土地利用的影响显著，沿海的滩涂和水体蒸散量最高，自然植被明显高于人工地物; 算法与 模型的耦合方式对蒸散结果，先融合后估算方案的蒸散精度更高( R ;) ，有效提高了蒸散的时空分辨率，更适用于黄河三角洲地区。

关键词 时空融合技术; ;  模型; 蒸散; 黄河三角洲中图法分类号 ; 文献标志码

# High-precision Remote Sensing Evapotranspiration Estimation Based on Spatiotemporal Fusion Technology

DAI Xiao-jie,FAN Xiao-mei\*，MIN Tong(    ，      ， ， )

［Abstract］        ， causeofthelimitationofasinglesensorandcloudandrainpolution，especiallyiareas withhighdegreeoflandscapefragmentation, itisdificult toobtainhighspatialandtemporalresolutionevapotranspirationsequence.TakingteYelowRiverDeltaasaneample, basedontheenhancedspatialandtemporaladaptivereflectancefusionodel，emotesnsingdatasetswithhightemporaladspatial resolutionwasconstructed.Thesurfaceenergybalancesystemmodelwasused toestimate theregional evapotranspiration timeseries withhigh temporal-spatialresolutionin2O2Obytwodiferentways.Thefeasibilityandestimationacuracyofcombiningfusionalgo rithmandevapotranspirationmodelwerediscussed.Theresultsshowthattheenhancedspatialandtemporaladaptiverflectancefusion modelESTARFM）algorithmhasgoodperformance，andthecorelationcoeffcientsetweenthefusioreflectanceandtheactualre flectancearebothaboveO.85.Therootmeansquarederor(RMSE）ofsensibleheatfluxestimatedbytheSEBS modelanduxstation dataisonly57.8W/m，ndthecorelationcoeficientbetweenwaterevaporationestimatedbythefusiondataandpanevaporation converteddataisO.93.Theevapotranspirationof theYellowRiver Deltavariesgreatlywithseasons，withsummer evapotranspiration accounting forabout40%ofthewholeyear.Theannual evapotranspirationof diferentsurfacefeaturesvariedsignificantly，ranging from548.2mm/ato1289.9mm/a.Thespatialdistributionpaternof evapotranspirationwassignficantlyafectedbylandandsea distributionandlandusendthehighestevapotranspirationasfoundincoastaltidalflatandwaterbodies，andnaturalvegetationwas obviouslyhigherthanartificialfeatures.ThecouplingmodeofESTARFMalgorithmand SEBSmodelhasacertaininfluenceonthe evapotranspirationresults.Theevapotranspirationaccuracyof thefusion beforeestimationschemeishigher（R=O.88，RMSE= 0.36mm/d），whichefectivelyimprovesthespatiotemporalresolutionofevapotranspirationandismoresuitablefortheYellowRiver Delta region.

spatiotemporal fusion technology；ESTARFM；SEBS model； evapotranspiration；Yellow River Delta

蒸散作为水循环和气候系统的中心过程，它不断驱动着气候系统，在地表能量平衡和水量平衡中具有举足轻重的地位［ ］。 蒸散代表着生态系统功能、气候、碳反馈及水循环之间的联系，它在水量预测、干旱分析、气候变化以及环境监测等方面发挥着不可替代的作用［］。 因此，精确量化蒸散的时空动态对于理解气候变化和优化水资源管理具有相当重要的意义。

近几十年，遥感技术的进步为区域蒸散的反演提供了新的可能，利用遥感反演蒸散已成为估算区域和全球蒸散最常用的手段［］。 目前，基于能量平衡原理的地表能量平衡系统(algorithm for land，SEBAL) ［］、 SEBS ( surface energy) ［］等蒸散模型应用较为广泛。模型除物理机理明确、计算简单外，该模型还提出了参数化方案，能够准确地计算热量粗糙长度，比其他蒸散模型采用固定值更为精确，在中国北方和欧亚地区均有良好表现。 等［］基于影像分别利用 模型和 模型对亚洲东北部地区的生态系统进行了蒸散的计算，并利用通量数据对结果进行了验证，结果表明 模型具有更高的准确性。 王晓勇等［］基于 模型对不同时期的海流兔河流域的蒸散进行量化，并结合长序列地下水监测数据和土地利用数据对不同土地类型转移量的地下水位及影响因素进行了分析。由此可见，前期的蒸散反演多采用 或等单一遥感数据，而单一传感器往往存在一些无法避免的数据缺陷［］。 比如， 数据虽然空间分辨率较高(  ) ，但重访周期较长(  ) 且易受云雨天气干扰，常出现影像缺失问题，无法进行长时间动态监测。 数据重访周期较短( ) ，但空间分辨率较粗(     ) ，无法适用于范围较小且地表复杂条件下的蒸散研究。 如何融合多源遥感数据发挥各自时空分辨率的优势，对于小区域的高精度蒸散反演具有重要的理论意义和应用价值 。

时空融合技术通过建立高空间与高时间分辨率数据之间的变化关系，对高空间分辨率数据的空间细节特征与高时间分辨率数据的时间变化信息进行有机结合，是获取高时空分辨率遥感影像的有效方法［ ］。 目前，已有众多国内外学者对时空融合算法展开了研究。 等［ ］提出一种时空自适应反射率融合模型（spatial and temporal adaptive reflec-， ) ，该方法在地表均质性较高时性能表现良好，但在地表异质度较高的情况下，其预测精度会降低，且此方法难以预测地表的突变现象［ ］。 为了提高 模型在复杂地表下的预测精度， 等［ ］提出了增强型时空自适应反 射 率 融 合 模 型 (adaptive reflectance fusion model，ESTARFM）,该算法考虑了像元反射率的时间变化特征，能够有效捕捉地物剧烈变化特征，提高了复杂下垫面情况下地表特征参数的融合精度［ ］。 目前，时空融合算法已被广泛应用于植被物候、干旱和水体监测等诸多领域［ ］，在蒸散反演中也有良好表现。 白亮亮等［ ］基于 系列数据和 模型估算了河套灌区的蒸散量，并结合 日蒸散数据，利用算法实现蒸散数据的空间降尺度，构建了河套地区高时空分辨率蒸散数据集。 尉毓姣等［ ］基于 模型获取了南京地区 空间尺度的蒸散数据，在此基础上，采用 模型将蒸散结果与 数据进行时空融合，并对模型的融合精度进行了评价。 利用 算法对 蒸散产品进行降尺度，是获取高精度蒸散的有效手段，但由于 数据对建设用地、水域等非植被像元赋予无意义数值，导致部分像元缺失，无法融合得到完整的蒸散数据。 对于水体、滩涂分布较广的滨海地区而言，如何构建区域内高时空分辨率的遥感数据集获取较为完整的蒸散序列是当前研究中亟须解决的问题。

因此，现以地表高度破碎化的黄河三角洲为研究区，利用 算法融合 和数据，构建研究区具有高时空分辨率的遥感数据集，并采用 模型计算了区域的日蒸散量。 通过比较融合反射率与实际反射率之间的差异，评估算法的性能，并利用彭曼公式估算的参考蒸散量、通量站观测数据及蒸发皿实测数据，对融合模型估算的蒸散结果进行了验证，探讨融合算法和蒸散模型结合的可行性和精度，以期为黄河三角洲水资源保护和生态系统良性发展提供科学依据，并为地表类型复杂且高度破碎化区域的蒸散研究提供新的思路。

# 1 材料与方法

# 1. 1 研究区概况

黄河三角洲位于山东省东营市境内的黄河入海口地区( ， ) ，是由黄河尾闾不断改道和泥沙淤积所形成的扇形地块［ ］，如图 所示。 研究区地属温带季风型大陆性气候，四季变化明显，年平均气温      ; 年均降水量   ， 分布在夏季，平均蒸散量为    。 区内地势整体呈西南高、东北低，平均高程在  以下，地下潜水普遍埋深较浅( 平均埋深为 ) ，且矿化度较高( 含盐量平均值为 14. 3 g / L) ［ ］。 自 20 世纪 70 年代以来，受农田开垦、油田开发等人为因素影响，黄河三角洲天然湿地大幅减少，区内景观破碎化程度不断加重［ ］。 目前，黄河三角洲面临着淡水资源匮乏、土壤盐渍化严重、生态系统失衡等问题［ ］。 因此，准确地计算区域蒸散量分析其时空变化过程可为正确估算土壤水分、预测农田旱情的发生和生态变化提供重要信息，对指导农业灌溉与排水、提高水资源的利用率等有着重要的意义。

![](images/efb5f6c61062cd59d18058b3e0d70cc314921660a2f19dfb864352a2c2f0303f.jpg)  
图 研究区概况  
Fig.1Overview of the study area

# 1. 2 数据来源

# 遥感影像数据

( ) 数据来源于美国地质调查局网站 ( :     ) ， 传 感 器 包 括 了传感器所有的波段，并对波段进行了重新调整，能够更好地避免大气吸收特征， 的第波段空间分辨率为 ，第   波段为热红外波段，空间分辨率为  ，回访周期均为  。 研究主要使用了 的第 波段来计算归一化植被指数 、地表反照率等参数，并基于 的热红外波段采用单窗算法［ ］来反演地表温度。 经筛选， 年 月— 年 月共有 期质量较好( 云 量 小 于  ) 的  影 像 见 表 。 采 用软件进行影像的辐射校正、大气校正和图像裁切等预处理工作，地表参数的计算通过波段运算工具完成。

( )  产品提供了  个波段的地表反射率，空间分辨率为 ，回访周期为 。数据是 地表温度产品，空间分辨率为 ，时间分辨率为 。 、数据均来源于美国航天局网站( :urs.earthdata.nasa.gov/）。由于MOD09A1、MOD11A2为正弦曲线投影，利用 软件将两种 产品重投影至与 数据一致的 坐标系，并将其空间分辨率统一采样为 ，对和 数据进行空间配准及波段匹配处理，以便后续进行数据融合。 和   的波段对应关系如表 所示。

表1 遥感数据类型及获取日期  
Table 1 Remote sensing data types and acquisition date   
表 2 MOD09A1 和 Landsat8 OLI 波段对应关系  

<table><tr><td>数据类型</td><td>行列号</td><td>日期</td></tr><tr><td>Landsat8 OLI</td><td>121/34</td><td>2019-1-07，2020-01-0，2020-02- 11，2020-03-14，2020-04-15，2020- 05-01，2020-05-17，2020-06-02， 2020-07-04，2020-07-20，2020-09- 06，2020-0-24，2020-1-09,2020- 1211,2021-01-28</td></tr><tr><td>MOD09A1/ MOD11A2</td><td>h27/v05</td><td>2020 年全年46 期及2019-1-06和 2021-01-27</td></tr></table>

Table 2 Band correspondence between MOD09A1 and Landsat8 OLI   

<table><tr><td rowspan="2">波段</td><td colspan="2">Landsat8 OLI</td><td colspan="2">MODIS</td></tr><tr><td></td><td></td><td>波段编号 波段范围/nm 波段编号 波段范围/nm</td><td></td></tr><tr><td>蓝波(blue)</td><td>Band 2</td><td>450~510</td><td>Band 3</td><td>459~479</td></tr><tr><td>绿波(green)</td><td>Band 3</td><td>530~590</td><td>Band 4</td><td>545~565</td></tr><tr><td>红波(red)</td><td>Band 4</td><td>630~690</td><td>Band 1</td><td>620~670</td></tr><tr><td>近红外（near infra- red, NIR)</td><td>Band 5</td><td>850~880</td><td>Band 2</td><td>841~876</td></tr><tr><td>短波红外1（short- wave SWIR1)</td><td></td><td>infrared 1，Band6 1570~1650 Band6 1628~1652</td><td></td><td></td></tr><tr><td>短波红外2（short- wave infrared 2，Band7 2110~2 290 Band7 2105~2155</td><td></td><td></td><td></td><td></td></tr></table>

# 专 题 数 据

( ) 气象数据。 气象数据均下载于中国气象数据网( : ) ，选取研究区垦利站的日气温、气压、风速等气象要素，作为 模型的输入参数。 选取日照时数、日平均气温、相对湿度等要素用于彭曼公式的参考蒸散量估算。

( ) 通量站数据。 通量站验证数据来源于国家生态科学数据中心( :      ) ，山东禹城农田生态系统国家野外科学观测研究站的通量数据产品是利用 技术体系进行标准化的质量控制和数据处理后的通量日值数据。

( ) 土地利用类型数据。 在参考研究区已有土地利用类型图的基础上，根据黄河三角洲 年一期 遥感影像，按照自然资源部土地分类标准分类并制作了研究区的土地利用现状图，如图  所示，主要包括林地、水体、滩涂、农田、芦苇沼泽和 建 设 用 地  种土地利用类型。 课 题 组 又 在年 月通过野外调查，对土地利用图分类的准确性进行了验证。

![](images/83fae719850d5a40b51e38d9719c27fa5caf1aad29353f84aacbade2238fe6fe.jpg)  
图   年黄河三角洲土地利用分布  
Fig.2Land use distribution in the Yellow River Delta in 2020

# 2 研究方法

研究基于 算法和 模型获取了黄河三角洲较高时空分辨率的蒸散数据，并对蒸散的时空格局及典型地物的蒸散特征分析，技术流程如图 所示。 主要步骤如下: ①首先对 和遥感影像进行预处理; ②利用 算法生成高时空分辨率遥感数据集; ③ 年黄河三角洲地区 的计算和验证; ④结合土地利用数据分析黄河三角洲蒸散时空格局及典型土地利用的蒸散特征。

# 2. 1 时空融合算法

使用的时空融合算法是由  等［ ］提出的增强型时空融合模型( ) ，该模型不仅考虑到了像元反射率的空间可变性、中心像元与周围像元的光谱相似性、还考虑到了不同时相上反射率值的变化，并使用滑动窗口的方法来抑制低空间分辨率影像的边界效应，有效提高了融合精度。 该模型通过输入两个时相的 数据和 数据，以及一个预测时相的 数据，从而生成预测时相的 数据。 融合过程忽略了影像的几何校正和大气校正的误差，首先确定搜索窗口大小，根据空间、光谱相关性使用搜索窗口在两期 反射率数据中搜索与中心像元光谱特征相似的像元，然后结合两期  反射率数据赋予每个相似像元距离权重和转换系数，通过权重来分配相似像元对中心像元的贡献率，再根据以上两期及预测期的数据计算时间权重，最后加入 数据获取的时间关系系数，生成预测时期的 尺度反射率数据。 预测时期反射率的具体计算公式如下 。

![](images/1cfd00184502408ec7ee78eac2a657bcb8efd43c1ffc28513140ed9d7f6cee53.jpg)  
Fig.3Technical flowchart

![](images/48ba26ce8dfa63483e030459de31456173b23dedd581231b7e4ea9945f463526.jpg)

式中: R 为最终预测时期的高分辨率反射率; ω 为相似像元搜索窗口，主要由地物类型的异质性所决定，这里取  个  像元大小范围; tp为预测影像时期; B 为遥感影像的 B 波段; Rm 、 Rn 分别为 Tm 、Tn 时期融合影像的反射率; Rk 为 Tk 时期预测的高分辨率影像的反射率，k = m，n; RL 、 RM 分别为影像 、 影像反射率; ( xω /2 ，yω /2 ) 为中心像元位置; ( xi，yi) 为第 i 个相似像元位置; N 为相似像元的数量; Wi 为综合权重因子; Vi 为转换系数 。

Tm 和 Tn 时期的时间权重 Tk，根据 tk ( k = m，n) 时期与预测时期 tp 之间的反射率变化幅度由式( ) 计算而来 。

![](images/65a5c497729c14dde267bb5c13de42089d569c6b0d6f16b57a5eb1eb5e487071.jpg)

# 2. 2 蒸散量计算方法

所使用的蒸散量计算方法是地表能量平衡系统模型( ) ，它是目前应用比较广泛的单层能量平衡模型之一。 该模型具有坚实的理论基础，物理机理明确，而且考虑的气象要素较少，便于应用。模型的基本理论依据是地表能量平衡方程，在某一时刻的地表能量可表示为

![](images/e5579c66b0bb189dd7a9405e9ca614397cf8bc6d1435ff097b068254d01a87e5.jpg)

式( ) 中: Rn 为净辐射通量，  ; G 为土壤热通量，  ; H 为显热通量，  ; λ 为水的汽化潜热， ; E 为瞬时蒸散量， (  · ) ; λ E 为潜热通量，  。

模型采用地表能量平衡指数法来确定蒸发比，根据地表能量平衡方程，当地表处于极度干燥状态下，其潜热通量为零，此时显热通量为最大值，Hdry 可表示为

![](images/325a37bd25a4f113c34c52e503308f2949810f58b8e9310ba867020ffc821034.jpg)

在地表极湿润环境下，土壤水分供应充足，此时显热通量为最小值，Hwet 可表示为

![](images/e5e754b8d33ec0e02fde93eff327b4835dbeed87c24f907c76acc91cdc99ec10.jpg)

极湿润条件下的潜热通量 λEwet 可以根据方法［ ］求得。

相对蒸散比可以由实际显热与干、湿限显热的关系得到，即

![](images/53b8f45c4f0535580e2cbffe0d859f0bcce0d131455d879b2c802e709aa3651f.jpg)

最终蒸发比定义为实际蒸散与可用能量之比，计算公式为

![](images/588f9dec9224c3d135efc437d0836f52f821d6fb47d06fd4ca4ce34e7eca9663.jpg)

从而得到瞬时蒸散量为

![](images/ee1053e850c1605318bdb6a2fb4d48a947f022fe19f872bcd44c6b0bb5e595b0.jpg)

式( ) 中: ρw 为水密度，  。

# 2. 3 时间尺度扩展

# 日尺度蒸散扩展

通过 模型获取的是卫星过境时刻的瞬时蒸散量，但在实际研究中长时间尺度的蒸散量才更有意义。 假设能量通量在一天中会发生变化，但各组分之间的比例即蒸发比在一天中保持不变，因此日平均蒸发比就等于过境时刻的瞬时蒸发比。 日蒸散量计算公式为

![](images/d5356d01a5c2f1b53dc0aa68efc9eaf0aec134d1efc0b0de097535dcd4132627.jpg)

式( ) 中: d 为日蒸散量， ; Λ 为日均蒸发比;Rnd 为日净辐射; Gd 为日土壤热通量; λ 为水的汽化热量， 。

# 月尺度蒸散扩展

月尺度蒸散的扩展借鉴了日尺度蒸散扩展的思想， 等［ ］认为，某一天的实际蒸散 与日参考作物蒸散 r 之间的比值是不变的。 通过计算某一天晴空遥感影像的 与 r 之间的比值 d，并以该比值作为某段时间内的特征值来计算这一段时间内的实际蒸散。 其计算公式为

![](images/17af455255dfb2614d5d64ca415baf247ea908ae539952a749672a4c133f8297.jpg)

日参考蒸散量由世界粮农组织推荐的Penman-Monteith ［ ］公式计算得，即

![](images/41b270398eea586d2abf8ac90661f91534b5c8e7d2831a0737f43af10db6ba8e.jpg)

式( ) 中: r 为参考蒸散量， ; Rn 为净辐射通量，  ; G 为土壤热通量，  ; Ta 为大气温度， ; U2 为 高处的风速， ; es 为平饱和水汽压， ; ea 为实际水气压， ; Δ 为饱和水汽压与温度的曲线斜率，  ; γ 为干湿常数， 。

通过 算法获得了时间分辨率为的 数据，因此式( ) 中的 8dr为  累积的参考蒸散量，而  的实际蒸散量的总和为

8d  d 8dr

# 2. 4 精度评价方法

# 融合算法精度评价

为验证融合算法的性能，选取 年 月日、 月 日和 月 日的影像作为实验，随机选取研究区内的  个像元对融合反射率与实际反射率进行对比，得到各日期不同波段的拟合曲线，并使用相关系数 R、均方根误差 、平均相对误差 对融合影像的质量进行评价。

![](images/7a1263453d45e4091a87a73fccafc63545442356affd5bb42d9922c203ef8b9a.jpg)

![](images/27bc5f01b78b909269292adb204dfd3066151a94d940e29a37cbbda62b1bb331.jpg)

式中: n 为样本大小; Pi、 Oi 分别为模拟值和实际值; P  、  O 分别为 Pi 、 Oi 的平均值 。

# 蒸散结果精度评价

研究区日蒸散结果的总体精度采用彭曼公式估算的日参考蒸散量进行验证，对比融合蒸散与参考蒸散量的变化过程，并对二者进行线性拟合，采用 R、 评价了融合蒸散结果的可靠性。

研究区地表覆盖类型复杂且破碎化程度较高，对区域内每种覆盖类型的蒸散结果进行验证较为困难，由于研究区内农田和水体分布范围较广，二 者 的 面 积 占 比 分 别 达 到 了 和，所以研究重点对区域内农田和水体的蒸散计算结果进行验证。 研究区内缺少通量站数据，而禹城农田观测站与研究区基本处在同一纬度，同位于鲁西北平原和黄河下游引黄灌区，距离研究区仅 ，水热条件和地表环境与研究区基本一致，因此采用禹城站观测的显热通量与研究区农田生态系统的瞬时显热通量进行线性拟合，并利用 R、 验证农田蒸散的计算精度。水体蒸散的验证采用垦利气象站的蒸发皿数据进行，对比水体的估算值与蒸发皿折算数据的散点分布并利用 R、 评价水体蒸散结果的准确性 。

# 3 结果与分析

# 3. 1 影像融合结果及精度验证

将 个不同日期的 影像和融合影像在标准假彩色合成下的图像( 图 ) 进行对比( 像元 像元) ，由图 可见，融合影像空间细节良好、地物纹理清晰，能够明显区分不同地物间的反射率差异，与原始 影像的整体差异较小。植被、裸地等混合像元较少的单一地表，融合反射率变化较小，预测精度较高。 居民区、建设用地等地物交汇区域，融合影像受 波段和混合像元的影响，部分建筑物有些泛红。 同时， 算法假设像元反射率随时间变化稳定且随时间的变化是线性的，而在复杂地表下像元反射率的变化并非线性，这也可能导致融合影像的反射率变化。

对比融合影像各波段反射率与实际反射率之间的散点分布( 图 ) ，由图 可知，融合反射率与实际反射率散点均匀分布于 线附近，各波段相关系数 R 均在 以上，平均相对误差 均小于，均方根误差 接近于 。 算法通过对移动窗口中的相似像素进行加权来提高中心像素反射率的预测性能，能够很好地反映空间变异性。 总体来讲， 算法在地表破碎、景观异质性较强的黄三角地区具有良好的适用性，融合精度能够满足后续研究需要。

![](images/f2cd4a83de193d8ec49e56a16b502b40b8f21d6c2551b72f5de4fcebd9e2a0fd.jpg)  
图 影像与融合影像对比  
Fig.4Comparison of Landsat images and fusion images

![](images/adcc2b4c100a449c9ddb6e61c0ae64764246dc6322af1994cdbf45db69c912d5.jpg)  
图 融合反射率与实际反射率散点图

# 3. 2 蒸散结果及精度验证

基于融合得到的高时空分辨率遥感数据，利用模型计算日 ，并将日 与彭曼公式估算的参考蒸散量及蒸发皿数据的变化过程进行对比( 图 ) ，由图 可见，模型计算的日蒸散量与蒸发皿数据、参考蒸散量的变化过程基本一致。 但受到降雨天气的影响，导致融合蒸散与蒸发皿数据之间存在部分的差异。

将 模型估算的瞬时显热通量与禹城站的显热通量数据进行对比，得到如图 所示的散点分布图。 可见，模型估算结果与通量站观测值的拟合效果较好，相关系数达到了 ，均方根误差仅为。 将 模型计算的水体日蒸散量与垦利站蒸发皿折算数据进行拟合( 图 ) ，模型计算的水面蒸发与蒸发皿折算的水面蒸发散点均分布于 线两侧，相较于 数据估算的水面蒸散结果，融合数据的水面蒸发与蒸发皿数据的相关系数 R 由  提 升 至 ，均 方 根 误 差 由0.44mm/d下降至0.35 mm/d。ESTARFM 算法和模型的结合不仅能够保证蒸散结果的计算精度，还能有效提高蒸散的时空分辨率。 综上所述，利 用  和  多时相遥感数据，基 于算法和  模型获得的高精度蒸散数据，避免了单一传感器和云雨污染的限制，能够满足地表破碎化地区的蒸散研究需求。

![](images/4c6eebc371af51b02f5b5cb8f23785d76d51fb5288b5dbf0c82cd8ac80d88902.jpg)  
图  模型计算的日蒸散量与日参考蒸散量及蒸发皿数据的对比  
Fig.6Comparison between daily evapotranspiration calculated by SEBS model with reference evapotranspiration and pan data

![](images/053f5c97c3b87610addc7c5c263a5c001553f4a9f3938fb5e233e59d394fbb3d.jpg)  
Fig.5Scatter plot of fusion reflectance with actual reflectance   
图  模型计算的瞬时显热通量与通量塔观测数据对比 Fig.7Comparison of instantaneous sensible heat flux calculated by SEBS model with flux tower observation data

# 3.3 蒸散时空格局

将研究区的月蒸散量叠加土地利用图，对区域蒸散的时空变化特征进行了研究( 图 ) 。 区域内蒸散随季 节 变 化 明 显，总蒸散量的变化规律为: 夏季 春季 秋季 冬季。 春季( — 月) 气温回升，农田和湿地植被开始进入生长季，区内平均蒸散量大约为 ，标准差为 ，低值主要集中在黄河故道两岸的裸地和孤东等植被稀疏地区，而高值分布在沿海滩涂和水体等区域，海陆差异明显;夏季( — 月) 降水增多，土壤水分充足，植物进入生长季中期，部分农田和湿地植被的蒸散量超过滩涂和水体。 区域平均蒸散量达到最大值( ) ，与其他季节相比，其空间变化幅度较大，标准差为，低值主要集中在西南部的荒地和居民区等植被覆盖率较低的内陆区域; 秋季( — 月) 区内平均蒸散量略低于春季，为  ，标准差为; 冬季(  月—次年  月) 由于气温较低，水循环缓慢，蒸散量较低，区内不同土地利用类型的平均蒸散量仅为 ，同时蒸散的空间变异性也较小，标准差仅为 。 由此可见，黄河三角洲各季节蒸散量空间分布特征较为相似，整体上由沿海滩涂向内陆逐渐减小，受到气温、降水和植被等因素影响，不同季节之间的蒸散量差异显著。

![](images/247c16d41903fb6158f1f48341eac60ba55cc8320950e837c7d731cd47cd1ce6.jpg)  
图 模型计算的水面蒸发与蒸发皿折算数据的相关性分析  
Fig.8Correlation analysis between water surface evaporation calculated by SEBS model and pan conversion data

黄河三角洲典型地表覆盖类型的蒸散量如图所示，可以看出，不同土地类型之间的蒸散量具有明显差异，总体表现为: 水体 滩涂 林地 芦苇沼泽 农田 建设用地。 水体的年蒸散量最大，达到了 ; 由于滩涂位于潮浸地带，下垫面含水量较高，其年蒸散量仅次于水体，达到了; 林地的植被覆盖度较高，需水量与储水量较大，年蒸散量达到了 ; 芦苇沼泽年蒸散量为   ，春季由于其植被覆盖度较低，蒸散量仅为 ，而夏季由于降水较多，植被生长旺盛，导致蒸散量显著增加(   ) ，秋季以后大部分芦苇枯萎或被收割因此蒸散下降至 ; 由于研究区农田多为旱地作物，植被覆盖度不及林地和湿地植被，年蒸散量仅为。 农田在春季和夏季由于灌溉和降水的补充，下垫面供水充足，蒸散量和林地差距不大，但秋季以后由于作物收割导致蒸散量下降明显; 建设用地由于其下垫面多为不透水面，导致四季的蒸散量都是最低，全年蒸散量为   。

# 4 讨论

# 4. 1 ESTARFM 算法的不确定性分析

基于 算法进行遥感数据的时空融合，结果表明，融合反射率与实际反射率之间的相关性均达到了  以上( 表 ) 。 算法能够充分利用像元之间的相似性并减小系统产生的误差，不仅能提升遥感数据的时空分辨率，同时还有较高的光谱还原度［ ］。 由表  可知，融合影像与实际影像在 、 等波段的相关性接近 ，而在 、 波段的相关性仅为 左右，这可能是由于不同传感器在光谱设置和光谱响应函数上有所差异，使得不同传感器之间存在系统性误差［ ］。 MODIS 在 SWIR1 、 SWIR2 波段的空间分辨 率 仅 为  ，且  与  传 感 器 在、 波段的光谱范围差异大于其他波段。另外， 月 日的融合精度( R   ) 高于 月日和 月 日( R    和 R   ) ，其原因主要是输入影像与融合预测影像的时间间隔不同。 张晓川等［ ］发现在融合过程中，输入数据与融合数据的日期间隔越短、输入影像质量越好，预测精度越高。 相比于 月 日和 月 日的输入影像， 月日的输入影像质量较好且与融合预测影像的时间间隔更短，地表类型变化更小，对应的光谱反射率更为相似。

相较于反射率的融合，地表温度的融合误差相对较大，众多研究［ ］表明，低空间分辨率影像的像元边界、混合像元等问题会增加融合过程的不确定性。 由于 地表温度是利用热红外波段基于单窗算法反演得到，空间分辨率为 ，而数 据 的 空 间 分 辨 率 仅 为  ，的低分辨率像元和边界效应会降低地表温度的融合精度［ ］。 总体来讲，ESTARFM 算法在地表破碎的黄河三角洲地区具有良好的适用性，并且输入影像质量越高、距离预测日期越近，其融合精度越高。 因此在研究中，应尽可能选择距离预测日期较近且质量较高的影像进行融合。

![](images/80bb22a6502a93b032c5db22b1d92afb874bd397b0fc55a2eaa6e61e6cfb2b9a.jpg)  
图  研究区不同季节蒸散量空间分布

![](images/c8382c15c43fb29657be0d68457964bf17ccade2947149ce3eb2616439d9bb44.jpg)  
Fig.9Spatial distribution of evapotranspiration in diferent seasons in the study region   
图  研究区典型土地利用类型的蒸散量Fig.10Evapotranspiration of typical land use types inthe study region

# 4. 2 融合算法与蒸散模型结合的可行性分析

为探讨不同融合方案对最终蒸散结果的影响，设计方案一( 先融合波段后计算蒸散) 和方案二( 先计算蒸散后进行融合) 两种融合方案，并将融合结果与 蒸散结果进行比较，系统评价两种融合方案的蒸散精度。

图 展示了两种融合方案的蒸散结果与原始蒸散结果对比，可见，两种方案的蒸散结果与实际 蒸散在空间分布上都具有一定的相似性，但方案一的蒸散结果与 计算的蒸散更为接近，二者日蒸散差值( 图 ) 主要集中在

![](images/15dfce1340382a6e942ce6ceca462e660fa696acda60d9deecd090f929184a57.jpg)  
图  融合蒸散影像与实际  蒸散影像对比 Fig.11 Comparison between fused evapotranspiration images and actual Landsat evapotranspiration image

# 表4 不同波段的反射率融合精度评价

Table 4 Accuracy evaluation of fusion reflectance in different bands   

<table><tr><td>日期</td><td>波段</td><td>Blue Green</td><td>Red</td><td>NIR</td><td>SWIR1 SWIR2 LST</td></tr><tr><td></td><td>R</td><td>0.93 0.94</td><td>0.95</td><td>0.95 0.96</td><td>0.95 0.87</td></tr><tr><td>4月15日RMSE0.03</td><td></td><td></td><td>0.025 0.022</td><td>0.019 0.019</td><td>0.019 1.481</td></tr><tr><td></td><td>MRE/% 21.7</td><td>15.3</td><td>11.4</td><td>7.3 6.5</td><td>8.1 0.4</td></tr><tr><td>5月17日RMSE0.017</td><td>R 0.91</td><td>0.87</td><td>0.92</td><td>0.93 0.85</td><td>0.86 0.91</td></tr><tr><td></td><td></td><td>0.013</td><td>0.018</td><td>0.026 0.026</td><td>0.030 0.816</td></tr><tr><td></td><td>MRE/% 14.7</td><td>9.7</td><td>6.7</td><td>5.6 9.4</td><td>16.0 0.2</td></tr><tr><td></td><td>R 0.92</td><td>0.92</td><td>0.95</td><td>0.89 0.91</td><td>0.93 0.84</td></tr><tr><td>6月2日RMSE0.03</td><td></td><td></td><td></td><td>0.025 0.022 0.019 0.019 0.019</td><td>1. 162</td></tr><tr><td></td><td>MRE/% 8.2</td><td>5.8</td><td>4.9</td><td>5.2 11.815.5</td><td>0.3</td></tr></table>

![](images/6906a9bb1150f1a913ef055838057eaa48cba702de727871e01f647cb723f475.jpg)  
图 融合蒸散与 蒸散的差值频率分布 Fig.12Frequency distribution of diference between fusion evapotranspiration and Landsat evapotranspiration

散的差值集中在 。 将融合蒸散与蒸散进行线性拟合，由图 可见，相较于方案二，方案一的拟合效果更好( R ) ，误差更小(    ) 。 该结果与 等［ ］ 研究的结果一致，他们比较了与拟议方案一和方案二相似的 种融合方案生成的 蒸散数据，发现方案一的误差(       ) 总是小于方案二和方案三(RMSE<3.7 mm/8 d: RMSE<3.3 mm/8 d)，并总结称降尺度后的蒸散与实际蒸散的一致性取决于地表参数反演的准确性，相较于先计算蒸散再进行融合降尺度，先融合出预测日期的反射率再计算蒸散更能提高蒸散的准确性。 方案二在先进行蒸散计算时，由于 影像的地表参数反演精度较低，且 地表温度影像常存在边界模糊和像元缺失等问题，导致 模型在估算中的不确定性增加，误差在后续的蒸散融合过程中会进一步增大［ ］。 而方案一先利用  算法模拟出预测时期的高分辨率影像，能够最大限度地减小系统偏差并抑制低分辨率像元的影响［ ］，提高了地表参数的反演精度，使得蒸散的计算误差较小 。

![](images/d4c3ae5832aa92dfb108dd27a58e189e2cb6c1c91e2c2c70ec5b353a34af7bc5.jpg)  
图  不同方案的融合蒸散与  蒸散相关性分析 Fig.13Correlation analysis between fusion evapotranspiration of different schemes and Landsat evapotranspiration

# 5 结论

将 时空融合算法与 模型相结合计算黄河三角洲地区的蒸散量，获得了研究区不同土地利用类型的高精度蒸散结果，并利用参考蒸散量、通量站和蒸发皿数据等对蒸散结果进行了验证，研究结果如下。

( ) 算法能够解决单一传感器限制和云雨污染的问题，不仅可以提高影像的时空分辨率，还有着较高的光谱还原度。 融合反射率与实际反射率的相关系数 R 均在 以上，均方根误差接近于 。 但融合效果对输入影像的质量要求较高，输入影像的质量越高、光谱差异越小，融合精度越高。

( ) 融合模型和蒸散模型的结合方式对蒸散的计算结果具有一定影响，先融合数据后计算蒸散的方法得到的蒸散结果精度更高，更适用于黄河三角洲地区的蒸散研究。 融合日蒸散量与参考蒸散量的变化趋势高度一致，二者相关系数 R 达到了。 模型计算的农田瞬时显热通量与通量站观测的显热通量的相关系数 R 达到了 ，均方根误差为  。 融合数据计算的水面蒸发与蒸发皿折算数据的相关系数 R 达到了 ，均方根误差 仅为   。 基于融合数据的蒸散结果在保证蒸散精度的同时，有效提高了蒸散的时空分辨率，能够满足地表破碎地区的蒸散研究需求。

( ) 黄河三角洲蒸散量随季节变化较大，夏季蒸散量较高，约占全年的 。 受土地利用和植被覆盖的影响，研究区蒸散量空间变异性较大，高值主要分布在沿海滩涂和内陆水体等区域，低值集中内陆居民区和西南部的裸地等植被覆盖率较低区域。 蒸散量在不同土地利用类型中具有明显的差异性，水体、滩涂等自然地物的蒸散量明显高于农田、建设用地等人工地物。

基于 算法和 模型能够有效提升蒸散数据的时空分辨率，但是融合算法对输入影像的质量要求较高，应尽可能选择时间间隔较短的输入影像以最小化地表突变所引起的反射率差异。研究区地表破碎化程度高，混合像元较多，这会对融合精度产生一定影响，后续应对时空融合算法进一步优化，提升融合精度并尝试多种传感器数据的融合，以构建长时间连续的高分辨率蒸散序列。

# 参 考 文 献

［］ 牛建龙，王家强，程珍，等 — 年塔里木河干流流域潜在蒸散发动态变化及其定量气候驱动［］ 科学技术与工程， ， ( ) :Niu Jianlong，Wang Jiaqiang，Cheng Zhen，et al. The quantitativeclimate driving on potential evapotranspiration change from 1961 to2013 in the main stream of Tarim River [J]．Science Technology， ， ( ) :  
］ Zhao J,Chen X，Zhang J，et al．Higher temporal evapotranspira-tion estimation with improved SEBS model from geostationary mete-［ ］  ， ， (  ) :14981.  
］ Alhassan A，Jin M. Evapotranspiration in the tono reservoir catch-ment in upper east region of Ghana estimated by a novel TSEB ap-proach from ASTER imagery [J]．Remote Sensing，2020，12( ) :  
［4］ 杜鑫，苏涛． 基于线性双源遥感蒸散模型的作物估产———以河套灌区为例［］ 科学技术与工程， ， ( ) :Du Xin，Su Tao.Crop yield estimation based on linear dual-sourceremote sensing evapotranspiration model: a case study of Hetao iri-［ ］    ， ，( ) :  
[]Ning J,Gao Z,Xu F. Effects of land cover change on evapotranspi-ration in the Yellow River Delta analyzed with the SEBAL model［ ］     ， ， ( ) :  
［ ］  ， ， ，timation with HEC-HMS model using spatial evapotranspiration bythe SEBS model [J]．Water Resources Management，2021，35( ) :  
[]Liaqat U W，Choi M. Surface energy fluxes in the Northeast Asiaecosystem: SEBS and METRIC models using Landsat satelite ima-［ ］    ， ， :  
［］ 王晓勇，朱立峰，董佳秋，等 干旱 半干旱区下垫面变化对地下水位的影响［］ 西北地质， ， ( ) :Wang Xiaoyong，Zhu Lifeng，Dong Jiaqiu，et al.Influence of un-derlying surface change on hydrogeological conditions inarid and［ ］  ， ， (  ) :227-235.  
［9］ 李超，李雪梅，田亚林，等． 温度植被干旱指数时空融合模型对比［］ 遥感技术与应用， ， ( ) :Li Chao,Li Xuemei,Tian Yalin，et al.Time and space fusionmodel comparison of temperature vegetation drought index ]．Re-， ，  (  ) :832-844.  
［ ］ 陈啟英，安裕伦，奚世军 喀斯特高原区多源遥感数据时空融合模型适用性分析［］ 科学技术与工程， ， ( ) :6538-6546.Chen Qiying，An Yulun，Xi Shijun． Applicability analysis of spa-tio-temporal fusion model of multi-source remote sensing data inKarst plateau［J］． Science Technology and Engineering，2020，20( ) :  
［ ］  ， ， ，Landsat and MODIS surface reflectance:predicting daily Landsatsurface reflectance []．IEEE Transactions on Geoscience Remote， ， ( ) :  
［12］ 古春霞，李大成． 时空融合技术在区域地表覆盖时序分类中的应用［］ 测绘通报， ( ) :Gu Chunxia，Liu Dacheng.Application of spatio-temporal fusiontechnology in time series classification of regional land cover [].， ( ) :  
［13］ Zhu X，Chen J，Gao F，et al． An enhanced spatial and temporaladaptive reflectance fusion model for complex heterogeneous re-gions［J］． Remote Sensing of Environment，2010，114 ( 11 ) :2610-2623.  
［14］ 陈燕丽，何立，莫建飞，等． 融合 HJ-1 CCD 和 MODIS 数据生成高分辨率影像方法对比［］ 科学技术与工程， ，( ) :Chen Yanli,HeLi,Mo Jianfei,etal.Comparison of diffrent fu-sion methods for generating high spatial-temporal resolution datausing HJ- CCD and MODIS data [J]．Science Technology and， ， ( ) :  
［ ］ 张晓川，王杰 基于遥感时空融合的升金湖湿地生态水文结构分析［］ 遥感技术与应用， ， ( ) :Zhang Xiaochuan，Wang Jie.The analysis of eco-hydrologicalstructure of Shengjin Lake Wetland based on spatial and temporalfusion technology of remote sensing [J]．Remote Sensing， ， ( ) :  
［16］ Halim M A，Thomas S C． A proxy-year analysis shows reducedsoil temperatures with climate warming in boreal forest.Scien-， ， ( ) :  
［ ］ 程筱茜，洪友堂，陈劲松，等 基于  的内陆湖泊遥感动态变化监测［］ 自然资源遥感， ， ( ) :Cheng Xiaoqian，Hong Youtang，Chen Jinsong，et al．A study ofthe long-term remote sensing dynamic monitoring of inland based［ ］      ，， ( ) :  
［ ］ 白亮亮，蔡甲冰，刘钰，等 基于数据融合算法的灌区蒸散发空间降尺度研究［J］． 农业机械学报，2017，48( 4) : 215-223．Bai Liangliang,Cai Jiabing,Liu Yu,et al.Spatial downscaling ofevapotranspiration in large irrigation area based on data fusion algo-rithm .Transactions of the Chinese Society for Agricultural Ma-， ， ( ) :  
［ ］ 尉毓姣，朱琳，曹鑫宇，等 南京地区蒸散发降尺度研究—基于增强型时空自适应反射融合模型［］ 生态学报， ，( ) :Wei Yujiao，Zhu Lin，Cao Xinyu，et al．A downscaling study ofevapotranspiration in Nanjing based on the ESTARFM model ].， ， ( ) :  
［20］ Fan X，Min T，Dai X． The spatio-temporal dynamic patterns ofshallow groundwater level and salinity:the Yellow River Delta,［］ ， ， ( ) :  
［21］ Zhu Q，Li P，Li Z，et al． Spatiotemporal changes of coastline overthe Yellow River Delta in the previous 4O years with optical and［ ］  ， ， (  ) :rs13101940.  
［22］ 谢春华，张帅影，崔丽珍，等． 黄河三角洲地物遥感分类研究进展 与 趋 势 ［ ］ 科 学 技 术 与 工 程， ， (  ) :14571-4583.Xie Chunhua， Zhang Shuaiying，Cui Lizhen，et al. Progress andtrend of remote sensing classification of land cover in the YellowRiver Delta，China［J］． Science Technology and Engineering，， ( ) :  
［23］ Gao X，Du Z，Yang Q，et al． Energy partitioning and evapotrans-piration in a black locust plantation on the Yellow River Delta,［ ］    ， ( ) :  
［24］ 岳辉，刘英． 基于 Landsat 8 TIRS 的地表温度反演算法对比分析［］ 科学技术与工程， ， ( ) :Yue Hui,Liu Ying. Comparison and analysis of land surface tem-perature retrieval algorithms based on Landsat 8 TIRS .Science， ， ( ) :  
［25］ Kim O K，Choi J Y，Jang M W，et al． Watershed scale droughtassessment using soil moisture index [J]．Journal of the Korean， ， ( ) :  
［26］ Du J，Song K，Wang Z，et al． Evapotranspiration estimationbased on MODIS products and surface energy balance algorithms( )    ， ［ ］Chinese Geographical Science，2013,23:73-91.  
［27］ Talebmorad H，Ahmadnejad A，Eslamian S，et al． Evaluation ofuncertainty in evapotranspiration valuesby FAO56-Penman-Monteith and Hargreaves-Samani methods [J]. International Jour-nal of Hydrology Science Technology，2020，10(2）：135-147.  
［ ］ 管琪卉，丁明军，张华，等 算法在长江中下游平原地区的适用性研究［］ 地球信息科学学报， ， ( ) :1118-130.Guan Qihui,Ding Mingjun,Zhang Hua，etal.Analysis of appli-cability about ESTARFM in the middle-lower Yangtze Plain [J].Journal ofGeo-nformation Science，2021，23(6)：1118-1130.  
［ ］ 邬明权，牛铮，王长耀 多源遥感数据时空融合模型应用分析［］ 地球信息科学学报， ， ( ) :Wu Mingquan，Niu Zheng，Wang Changyao．Application andanalysis of spatio-temporal fusion model of multi-source remote［ ］    ， ，( ) :  
［ ］ 崔舜铫，姚佛军，连琛芹 多源遥感数据在植被覆盖区的水体信息提取［］ 科学技术与工程， ， ( ) :Cui Shunyao,Yao Fojun，Lian Chenqin．Water body informationextraction based on multisource remote sensing data in vegetation［ ］    ， ，( ) :  
[31]Ma Y,Liu S,Song L,et al.Estimation of daily evapotranspirationand irrigation water efficiency at a Landsat-like scale for an arid ir-rigation area using multi-source remote sensing data [J]．RemoteSensing of Environment，2018，216:715-734.  
［ ］  ， ， ，fusion method using surface heterogeneity information based on［］  ， ， ( ) :  
［ ］ Ke Y，Im J，Park S，et al. Spatiotemporal downscaling approa-ches for monitoring 8-day 3O m actual evapotranspiration [J].ISPRS Journal of Photogrammetry Remote Sensing，2017，126:79-93.  
［34］ Liu M，Liu X，Wu L，et al． A modified spatiotemporal fusion al-gorithm using phenological information for predicting reflectance ofpaddy rice in southern China [J]．Remote Sensing，2O18，10( ) :