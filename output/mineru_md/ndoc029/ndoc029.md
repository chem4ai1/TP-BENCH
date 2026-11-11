# 湿地生态系统服务与景观生态风险时空演变及关联性以杭嘉湖平原为例

王丽娜1 ，杨国福2 ，李嘉欣1 ，张梦娴1 ，徐 斌1\*( 1. 浙江农林大学风景园林与建筑学院，浙江 杭州 311300; 2. 浙大城市学院艺术与考古学院，浙江 杭州 310015)

摘 要: 理解生态系统服务和生态风险的时空演变特征及相互关系，是制定针对性生态系统管理策略以维持区域生态安全和可持续发展的基础 湿地为人类提供了多类重要的生态系统服务，同时其生态敏感度较高，容易受到城市化和人类活动的干扰。 以杭嘉湖平原为研究对象，基于 2000、 2010、 2020 年 3 期土地利用及社会经济学统计数据，采用 InVEST 生态系统服务模型 景观生态风险指数 双变量空间自相关分析方法和空间回归模型等方法，评估并探究生态系统服务功能与景观生态风险的时空演变趋势及关联性 结果表明: ( 1) 从2000～2020 年，杭嘉湖平原湿地生态系统服务以东南部的高值区为核心向外依次扩散，逐渐降低，随着时间的推移逐渐由聚集性向分散性转变 ( 2) 2000、 2010 和 2020 年，景观生态风险指数分别为 0. 028 6、 0. 027 7和 0. 026 6，研究区整体从中等风险等级转入较低风险等级，研究区生态风险状况有所改善，高和较高风险区主要呈片状分布在研究区西部及北部 ( 3) 景观生态风险与生态系统服务存在一定的空间集聚特征，景观生态风险与综合生态系统服务之间的关系表现出显著负向相关，即景观生态风险与综合生态系统服务存在互馈效应，负向影响与关联随时间推移逐渐减弱。 研究结果能为制定降低区域生态风险、 增强生态系统服务能力维持湿地生态系统持续健康稳定的政策提供理论依据。

关键词: 湿地; 生态系统服务; 生态风险; 时空关联性; 空间回归模型; 杭嘉湖平原中图分类号: TU984. 115 文献标识码: A 文章编号: 1004-8227( 2024) 09-2043-16DOI: 10. 11870 /cjlyzyyhj202409017

湿地是地球上陆地与水相互作用形成的独特而又重要的生态系统，在调节气候、 供水、 生物多样性、 维护人类健康方面具有重要的功能和价值［1，2］。 然而，近 30 a 以来，在人类活动干扰和湿地自身脆弱性的共同因素影响下，湿地景观结构不断变化和退化，所带来的生态环境问题已逐渐成为制约城市持续健康发展的重要因素［3，4］。因此，越来越多的研究者聚焦湿地退化［5］、 湿地景观格局及其动态特征、 驱动因素的识别［6］、 生态风险与服务价值评估［7］等方面，对湿地的保护和发展展开研究。

生态系统服务与景观生态风险是衡量区域生态安全的核心内容，分别作为正向和负向指标的方式指示了生态系统的健康状态与受威胁的程度［8］。 生态系统服务是指生态系统的结构、 功能与过程能维持人类生产发展和生态过程所提供的自然条件和效用［9］，例如固碳、 水文调节、 作物生产和生物多样性保护等［10］。 千年生态系统评估中将其分为供给、 调节、 文化和支持服务共四类。 生态系统服务的空间量化已经逐渐成为环境保护［6］、 重点生态区识别［11］、 生态补偿机制［12］等决策制定的重要依据。 生态风险评估是一种能够有效测量人为压力、 环境污染或自然灾害等外部干扰对区域生态系统的负面影响的工具［13］。 基于经典生态风险评价，湿地生态风险评价最初较多关注化学污染物等微观因素等对小地理区域内的湿地生态系统与人类健康的风险受体潜在的不利影响，例如罗松英等人对湛江湾红树林湿地沉积物中的重金属问题进行了全面的风险分析［14］，Qu 等［15］基于风险商数法，结合概率风险评估模型对太湖湿地农药残留生态风险进行评估。 而随着气候变化和人类活动的范围的扩大，湿地生态风源范围逐渐从单一的工业污染因子向自然灾害、 人为压力等多风险源转变，发展而来的区域生态风险更多的开始聚焦空间异质性的展现，例如 Xu 等［16］从风险源和生态受体入手构建区域综合生态风险评估模型并应用在黄河三角洲湿地的风险评估中。 同时，作为生态风险的一个重要分支的景观生态风险能有效综合多种因素并衔接景观要素镶嵌 景观格局演化和生态过程，在湿地生态系统安全评估和未来效益的预测当中已得到广泛的应用［17，18］

现阶段，关于两者的研究已由独立转向融合，开展区域生态系统服务和景观生态风险的时空演变及相互作用的研究已逐渐成为新的热点和研究方向并且出现了不同的研究范式［19，20］。 一方面是在景观生态风险模型的基础上，通过分析景观类型变化，改进景观格局分析方法，将生态系统服务功能纳入风险评价体系，以提升风险评估的全面性和科学性［21，22］。 另一方面研究多聚焦同时段下服务与风险的动态过程及两者关联机制，探讨两者之间的空间分布情况与相互影响程度［23，24］。 国内多位学者已采用生态系统服务价值核算、 景观生态风险指数核算、 双变量空间自相关模型等方法分别探讨了流域 城市 生态脆弱区等区域的生态系统服务价值和生态风险的时空动态特征及其关联性，印证了其方法的可行性［25～ 27］。 也有学者进一步探讨了两者之间的权衡关系，或将生态系统供需关系纳入风险评估评价框架中，将研究区划分为不同的服务－风险类型，提出分区适应性管理策略［28，29］。 总体而言，前人的研究在理论和方法上都取得了长足的进步，当前的研究多专注于讨论服务与风险之间是否存在一定相关性，较少聚焦整体或单一生态系统服务对景观生态风险的影响程度。 然而，以湿地作为研究对象，分析其重要生态系统服务功能和景观生态风险评价的时空关系及相关性的研究较少，本文将对该部分研究内容进行补充和丰富。

本研究以杭嘉湖平原湿地为案例对象，采用生态系统服务与权衡综合评价 ( Integrated Valua-tion of Ecosystem Services and Trade－offs，InVEST)模型［30］评估四个重要生态系统服务功能，通过景观格局指数的方法评估区域生态风险并分析其时空变化特征。 在此基础上利用双变量空间自相关、 空间回归模型分析景观风险和生态系统服务的关联性以及空间影响关系，试图回答以下科学问题: ( 1) 2000～2020 年的杭嘉湖平原湿地典型生态系统服务功能与景观生态风险有怎样的时空演变特征趋势 ( 2) 基于两者间空间关联特征，有怎样的潜在优化路径，以降低研究区内湿地生态风险，保证景观功能的可持续供给，并为构建生态安全格局的区域管理提供科学参考。

# 1 研究区域与方法

# 1. 1 研究区域

杭嘉湖平原位于浙江省东北部，( 119°68'E～121°16'E，30°05'N ～ 31°01'N) ，属长江三角洲平原的一部分，是浙江省最大的堆积平原，总面积约 8. 43× 103 km2 ，连接上海 、 江苏和浙江三地 。研究区的行政范围包括了嘉兴市全境，湖州市南浔区 吴兴区 德清县，杭州市余杭区 临平区、 上城区、 拱墅区全境，钱塘区、 西湖区的部分区域( 图 1) 地处亚热带季风气候，冬季温和，夏季漫长而炎热潮湿，年平均气温 17. 5℃，年降水量约 1 100～1 500 mm。 杭嘉湖平原地面平均海拔 3～7m，地势低平，水网稠密。

杭嘉湖平原毗邻太湖与钱塘江水系，密集的河网和低海拔孕育了丰富的湿地类型［31］。 随着长江三角洲地区经济迅速发展和激烈的城市扩张，湿地景观格局面临强烈的扰动和变化，湿地面积减少 破碎化程度提高，并伴随着水土流失 作物生产能力降低、 栖息地质量下降等环境问题，威胁着区域整体生态安全。

# 1. 2 数据来源与预处理

土地利用数据来源于中国科学院资源与环境数据云 平 台 ( http: / /www. resdc. cn) 空 间 分 辨 率为 30m。 从长期来看，在湿地的破坏与恢复过程中，湿地与其他土地利用类型始终存在着相互转换。 根据 《拉姆萨尔公约》 《湿地分类》和 《土地利用现状分类》，对杭嘉湖平原的湿地类型进行了 2级划分和空间识别，本研究将杭嘉湖平原湿地类型分为自然湿地( 河流湿地 湖泊湿地 滩涂滩地) 与人工湿地( 水库坑塘、 稻田湿地) 共两大类六小类，其他用地包括耕地、 森林、 草地、 建设用地和未利用地［6］。 年降水量以及蒸散发数据来源于国家地球系统科学数据中心( http: //www. geodata. cn /) 植被归一化指数( NDVI) 数据来 源 于 国 家 生 态 科 学 数 据 中 心 ( http: / /www. nesdc. org. cn /) 粮食年产量和水资源数据来源于 《浙江省水资源公报》 《浙江省统计年鉴》以网格作为基础评价单元，通过 Fragstats 软件计算出研究区湿地平均斑块面积约为 2. 23km2 ，参考相关文献［32］采用平均斑块面积的 2～5 倍将研究区划分为 3 km×3 km 的单元网格，最终获得1 014个评价单元。

![](images/c53fb2959fae12ca64fa451d31923a113e770f217dfa5dfc63f425075b80a55c.jpg)  
图 1 研究区概况及土地利用情况( 数据为 2020 年)  
Fig. 1 Overview of study area and land use ( the data is 2020)

![](images/9c1b72150fe9b12df703cb309c7a9e7d531f8fa1e6c0871afa36a26eb0128959.jpg)  
图 2 2000 ～ 2020 年研究区湿地类型分布  
Fig. 2 Distribution of wetland types in study area，2000－2020

# 1. 3 方法

# 1. 3. 1 湿地生态系统服务评估

根据研究区中面临的环境资源问题与特定景观所提供的代表性功能，选择固碳( Carbon Stor-age) 、 产 水 量 ( Water Yield) 、 生 境 质 量 ( HabitatQuality) 作物生产( Crop Production) 4 个典型的生态系统服务功能表征研究区的湿地生态系统服务能力。 相比于价值量法，使用生态系统服务功能评估 InVEST 模型可对多种单项生态系统服务功能进行空间直观的量化与动态变化的显性表达［33］。 同时，因其允许输入用户研究地区的相关数据，因而可适用于全球范围内景观或区域尺度的生态系统服务功能评估，具有较强的可推广性，已在国内外各类尺度的生态系统服务功能评估中得到较广泛的应用。 根据InVEST 用户指南使用相应的模块对固碳、 产水、 生境质量服务进行评估，并使用归一化植被指数( NDVI) 数据，评价作物生产功能，本研究各景观功能的具体过程如表1 所示。

表 1 典型生态系统服务功能的方法与过程  
Tab. 1 Methods and processes for typical ecosystem service functions   

<table><tr><td>景观功能</td><td>模型或原理</td><td>评价方法</td><td>方法描述 Ci为地类i的总密度，Ciabove为地类i的地上</td></tr><tr><td>固碳</td><td>通过土地利用类型及相 应的碳密度评估碳储量</td><td>Ci= Ciabore +Cibeom +Cisoil +Cidead M n CxS Ctotal = 台</td><td>碳密度，Cibeloe为地类i的地下碳密度，Cidead 为地类i的死亡有机质碳密度，Cisou为地类i 的土壤有机质碳密度，C为地类i的碳总密 度，Ctotal为总碳储量，S表示地类i的总面 积，n表示地类总个数，碳密度参数依据文 献34得到</td></tr><tr><td>产水量</td><td>基于年降水量、年潜在 蒸散量以及植被类型、 土壤深度和植物有效含 水量来评估产水量</td><td>AETxj) xP Y= P AETx PETx (PETx) 1/ω P + 1+ Px Px AWCx×Z PETx=Kcx×EToxωx= ×1.25 二 Px dxy</td><td>Yxj为栅格x的年产水量；AETxj为栅格x的 年实际蒸散量(mm)；P.为栅格x的年降水 量（mm)；PETx为参考作物蒸散；ETox为由 Penman-Monteith公式计算的潜在蒸发量； ωx代表气候和土壤特性的非物理参数；Kcx 表示作物蒸散系数；Z为季节常数；AWCx指 植物可利用水量 （1）i代表地类y中威胁因子r对地类x的 影响程度；dxy代表地类x与地类y间的线性</td></tr><tr><td>生境质量</td><td>生境质量是指生态环境 能够提供适合自然生态 条件的能力，高低能反 映区域生境的破碎程度 以及对生境退化的抗干 扰能力</td><td>（1）线性衰减 linear decayirxy = 1- (drmax) （2）指数衰减 exponential decay 2.99) irxy =exp D Q=H(1 D +K²</td><td>距离；dmax则为威胁因子r空间上的最大胁 迫距离。各类因子通过结合杭嘉湖地区数 据可获得性及经济发展水平后确定。 (2）Qx为土地利用类型下栅格x的生境质量 指数，H为j类土地利用生境适宜性，两者取 值范围均为0~1，其中1为最适宜。K为半饱 和常数，一般取生境退化程度最大值dx的1/ 2。Z值为规范化常数，通常设置为2.5</td></tr><tr><td>作物生产</td><td>栅格植被状况指数(VCI) 的占比，将作物分配到 各栅格3。基于耕地的 NDVI数据计算VCI表征 作物生产能力</td><td>利用研究区域内各耕地 VCIi GP=GP,X MvcI NDVI -NDVImin VCI = ×100% NDVImax -NDVImin)</td><td>GPi为第i个耕地网格的粮食产量，GP,为整个 研究区域的粮食总产量；n为研究区耕地总格 数；NDVI为第i个耕地网格的年NDVI值。 NDVImax和NDVImin分别表示研究区耕地年 NDVI的最大值和最小值。GP数据来自杭嘉 湖地区逐年的统计年鉴，单位为t/hm2</td></tr></table>

# 1. 3. 2 湿地景观生态风险评估

区域生态风险指数高低与研究区内各土地类型的空间组合状况及其所占比例有密切关联。 在前人相关研究的基础上［11，36］，本研究选择通过综合景观干扰度指数和景观脆弱度指数来构建土地 利 用 生 态 风 险 指 数 ( Ecological Risk Index，ERI) 衡量生态系统的内部脆弱性与外部因素的干扰程度，以此评估研究区各评价单元的生态风险差异。

![](images/0d36f8ac7e3b27c267ec0aa32ab06edb98f00fc1ae331954d4fc74c87e0a8b8b.jpg)

式中: ERIk 为研究区第 k 个样本单元的景观风险值; n 为评价单元内景观类型的个数; Aki 为第 k 个评价单元中景观类型 i 的面积; Ak 为第 k 个评价单元总面积; Ri 为第 i 类景观损失指数; Qi 、E 分别为的景观脆弱度指数和景观干扰度指数。景观干扰度指数由景观破碎度指数( C ) 景观分离度指数( Ni ) 和景观分维度指数( Fi ) 组成。参考前人研究［36］，各景观指数的权重 a、 b、 c 分别赋值为 0. 5、 0. 3 和 0. 2，公式及其生态学意义见表 2。 不同景观类型对环境的敏感性和对生态风险的适应能力存在差异。 参考相关文献［37，38］和本研究区域实际情况，湿地与非湿地景观类型的景观脆弱性被划分为7 个等级，分别为未利用地－滩涂－滩地、 河流湿地－湖泊湿地、 水库坑塘、 旱地－稻田湿地、 草地、 林地、 建设用地，为消除量纲进行归一化 处 理，各 类 景 观 脆 弱 度 值 为 0. 162、 0. 116、0. 085、 0. 058、 0. 040、 0. 026、 0. 018 。

表 2 景观生态风险的计算公式  
Tab. 2 Formula for calculating landscape ecological risk   

<table><tr><td>景观指数</td><td>计算公式</td><td>参数解释</td><td>生态意义</td></tr><tr><td>景观破碎度指数（Ci）</td><td>C= ni/Ai</td><td>ni为景观类型i的斑块数，Ai为景观i 的总面积</td><td>表示景观破碎化程度，其值越高，表 明景观单元内部稳定性越低，对应的 生态风险越大</td></tr><tr><td>景观分离度指数（Ni）</td><td>1 ni Ni= A 2 × A A</td><td>A为景观总面积</td><td>表示空间分布中各斑块的离散化程度， 其值越大，斑块分布越分散，破碎化 程度越高</td></tr><tr><td>景观分维度指数（Fi）</td><td>F=2ln(P;/4)/lnA;</td><td>Pi是i类景观类型的周长</td><td>表示景观受到风险源的干扰后其形态 变化的程度，其指数越大代表自身对 应的斑块形状越复杂</td></tr><tr><td>景观干扰度指数（E）</td><td>E= aC+bN+cF;</td><td>a、b、c分别为指标Ci、Ni、F的权 重，a+b+c=1</td><td>表示不同景观所代表的生态系统受到 干扰(主要是人类活动)的程度 衡量不同景观类型对外界干扰后的恢</td></tr><tr><td>景观脆弱度指数（Qi）</td><td>由专家打分归一化获得</td><td>根据研究区特征，将景观类型的脆弱 性等级划分为7个等级，并进行归一 化，得到各自的脆弱性指数</td><td>复能力与敏感性，其值越高表明景观 越脆弱</td></tr><tr><td>景观损失度指数（Ri）</td><td>R=E×Qi</td><td>通过景观干扰度指数E;和景观脆弱度 指数Q;综合反映</td><td>表示不同景观类型生态系统受外界干 扰时其自然属性损失的程度</td></tr></table>

# 1. 3. 3 综合生态系统服务

由于模型得到的不同服务之间测量单位不同，使得上述四种服务功能在获得生态系统总服务功能方面不具有直接可比性。 为了消除这种差异，本文构建综合生态系统服务指数评估区域总体生态系统服务水平，综合生态系统服务的指数计算公式如下:

![](images/ae1e93635e1f5e2066c4885bac88fa7798f162a561949b51dc024e6eb2357a08.jpg)

式中: ESIj 是指 4 种不同生态系统系统服务的加和; ESNij 是归一化后网格 j 的第 i 个生态系统服务。 为了统一产水量、 生境质量、 碳储量和作物生产的标准，使用以下公式对生态系统服务的价值进行标准化:

![](images/d12a0fef542bfacc1a25f5e834da6c8b480d9b5c500b53299bf2876582a52b6e.jpg)

式中: ESNij 表示各景观功能的标准化值; ESij为网格 j 的第 i 个生态系统服务原始值; ESi min 和ESi max 为各景观功能的最小值和最大值。 参照相关研究［39］，本文假设所有生态系统服务功能都同样重要，综合生态系统服务的取值范围是 0～4。

# 1. 3. 4 双变量空间自相关模型

通常使用空间自相关模型探索某一种或两种属性是否存在空间集聚性和异质性，分为全局空间自相关和局部空间自相关［26］。 为了探究研究区湿地生态系统服务和生态风险的空间相关特征，采用双变量空间分析模型，利用全局自相关系数Moran’ s I 指数反映整体空间关联和差异状况，计算公式如下:

![](images/13c5aed9d87230ec6a354063a02195a094420ff9860f6f84c209869e502c7db2.jpg)

式中: Isr为单位面积生态系统服务价值s 和生态风险指数 r 的双变量全局自相关系数; yi.s 和 yi.r为第 i 个评价单元单位面积生态系统服务价值和生态风险指数; σs 和 σr 为方差。

为了全面具体地反映研究区各部分之间的空间关联性，采用 LISA 进行局部空间自相关分析，以表述空间局部集聚和离散效应。

# 1. 3. 5 地理加权回归( GWR) 分析

双变量空间自相关反应个空间单元位置的要素观测值与相邻单元的观测值之间的关联程度，地理加权回归分析( GWR) 模型则是作为一种考虑变量空间异质性的以及变量之间具体影响程度空间回归模型。 GWR 模型将空间位置融入模型中，不仅能克服 OLS 模型忽视空间效应、 回归系数呈现区域整体平均值的不足，且能够充分展现自变量与因变量之间的作用关系在不同空间地理位置的分布特征［40］。 因此，本研究采用 GWR 模型，以综合生态系统服务为自变量，景观生态风险为因变量，分析湿地生态系统服务与生态风险之间的空间影响特征，提升景观生态风险与服务关系的空间异质性的表达，公式如下。

![](images/69db41bc0e5a3dbdee4e212803de3c37f8ec507d3962eb1cd946a27bd2e56477.jpg)

式中: yi 是空间位置 i 上的因变量; ( μi，γi)为点 i 的空间位置; K 是自变量的个数; xik 为解释变量 xik 在 第 i 个 样 本 点 的 值; β0( μi，γi) 和βk( μi，γi) 分别表示为空间位置 i 处的空间截距，以及第 K 个解释变量在空间位置 i 上的回归系 数 。

# 2 结果与分析

2. 1 湿地生态系统服务功能的时空动态

![](images/bc5e442d8e525a1d4ace7d564b0bbc324fa09fd764e5a1b7601eceb8e396a0f5.jpg)  
图 3 2000～2020 年研究区湿地典型生态系统服务的时空动态  
Fig. 3 Spatial and temporal dynamics of typical ecosystem service of wetlands in study area，2000－202

2000～2020 年 4 种典型生态系统服务功能的空间格局呈现明显的空间异质性( 图 3) ，各景观功能的平均值也随时间变化明显( 表 3) 。 农作物生产高值区集中分布在嘉兴市大部分区域，稻田湿地分布连片，作为重要商品粮基地的嘉兴地区的粮食生产能力较强，而西南部的杭州地区该服务功能比较薄弱。 时间尺度上看，粮食生产能力逐步减 弱，2010 ～ 2020 年 平 均 降 低 了 19. 73% 。研究时段内生境质量呈现中间低、 四周高的空间分布形式，低值区域呈西南至东北走向，主要分布于杭州市主城区中心区，嘉兴南湖区、 桐乡市等城市建设快速发展地区。 因其人类活动干扰，湿地呈现出碎片化、 解体化、 连通性降低的情况，导致湿地生态承载力变化和生境质量的持续下降。 产水量高值区主要分布于研究区西部，产水量在研究时段内呈现快速增长的趋势，2010 ～ 2020 时段达到了 46. 85%的高增长率 同时，研究区整体固碳能力都处于较高水平，低值区主要分布在各类水域面积较大的天然湿地中，整体的湿地固碳能力小幅下降。 功能受损最严重的是作物生产服务，提升最明显的产水服 务 。

表 3 2000～2020 年杭嘉湖平原湿地生态系统服务的变化  
Tab. 3 Methods and processes for typical ecosystem service functions   

<table><tr><td rowspan="2">生态系统服务指标</td><td colspan="3">年均值</td><td colspan="2">变化率</td></tr><tr><td>2000年</td><td>2010年</td><td>2020年</td><td>2000~2010年</td><td>2010~2020年</td></tr><tr><td>碳储量均值(t/ha)</td><td>13.4</td><td>13.2</td><td>13.0</td><td>-1.49%</td><td>-1.51%</td></tr><tr><td>产水量均值(mm)</td><td>436.9</td><td>510.6</td><td>749.8</td><td>16.87%</td><td>46.85%</td></tr><tr><td>生境质量均值</td><td>0.39</td><td>0.36</td><td>0.35</td><td>-7.69%</td><td>-2.78%</td></tr><tr><td>作物生产均值(t/ha)</td><td>11.07</td><td>10.49</td><td>8.42</td><td>-5.24%</td><td>-19.73%</td></tr></table>

本研究在样本单元的基础上，将 4 种服务进行标准化处理，利用 Arc Gis 叠加分析功能，将 4种服务功能综合叠加后分配到样本单元的中心点，利用普通克里格插值法绘制各单元中心值的综合生态系统服务功能图，利用自然断裂法将其划 分 为 低 ( ESI ≤ 1. 756 ) 较 低 ( 1. 756 ＜ ESI ≤2. 171) 中( 2. 171＜ESI ≤ 2. 325) 较高( 2. 325＜

ESI ≤ 2. 431) 、 高( 2. 431＜ESI ≤ 2. 769) 5 个等级，形成3 期综合生态系统服务空间格局分布( 图4)研究时段内，研究区生态系统服务面积占比以较高服务和高服务区为主，低服务和较低服务区分布面积较小，生态系统服务等级由高到低以高值区为核心依次向外扩散分布，整体的服务水平呈现西、 南部高、 北部低的空间分布形式。 高服务

![](images/f4d696d12decb0beb720007fec32309ec32cc20f3d4436ab0cb3e36d3ef26d09.jpg)  
图 4 2000 ～ 2020 年研究区湿地综合生态系统服务的空间格局与时空动态

Fig. 4 Spatial pattern and spatial－temporal dynamics of integrated ecosystem service of wetlands in study area，2000－202区呈团状集中分布在研究区南部的海宁县、 西部的余杭区等，2000～2010 年面积占比显著下降了26. 63%，2010 ～ 2020 年 上 升 6. 12% 较 高 服 务区呈环状分布在较高服务区的外沿，面积呈现上升趋势( 9. 00%) ; 中等服务、 较低服务区面积都呈现先上升后下降的趋势，2000～2010 年分别增长 15. 91% 5. 47%，2010 ～ 2020 年下降 9. 72%1. 36%，两者交织分布于较高服务区外沿，整体生态服务水平呈现先下降后上升的趋势。

# 2. 2 湿地景观生态风险的空间格局变化

利用普通克里金法对研究区 2000～2020 年的湿地景观生态风险进行空间插值，并利用自然间断点法划分为低风险( ERI≤0. 019 2) 较低风险( 0. 019 2＜ERI ≤ 0. 027 8) 中风险( 0. 027 8＜ERI≤ 0. 034 1 ) 较 高 风 险 ( 0. 034 1 ＜ ERI ≤ 0. 0438) 高风险( 0. 043 8＜ERI ≤ 0. 082 5) 2000 年 、2010 年和 2020 年研究区的平均 ERI 值分别为0. 028 6 0. 027 7 和 0. 026 6，随时间的推移呈小幅下降趋势，说明区域整体生态安全状况稳步改善，根据结果进而绘制出了 3 个研究时期的生态风险时空分异图( 图 5) 总体上以中、 次低风险区为主，占整个区域的 69%以上，其次是次高风险 低风险和高风险。 在两个研究时段内，次高风险、 高风险地区的变化较小。 低风险区和次低风险区呈上升趋势，2000～2020 年总增长率分别为 5. 00%和 2. 00%，中风险区呈逐年减少趋势，共减少了 6. 00% 。

研究区生态风险呈现明显的空间异质性，出现低值总体连片 高值局部集聚的分布特征高风险区域主要分布于湖州市南浔、 嘉兴市秀洲、 嘉善区及沿海的海盐县、 海宁市钱塘江入海口、 杭州市西湖区部分地区，较高风险及中风险区域呈团状连片分布于高风险区域外围，该区域主要以稻田湿地、 水库坑塘、 湖泊湿地与河流湿地为主。 较低风险区分部广而分散，几乎覆盖整个杭嘉湖地区的各个地市。 低风险地区主要分布于研究区西部，以及临近城市开发建成区的周围。

![](images/482baca43d0174dc3d511a12aa9893c6ebeb1f7c8812101a6b93d4a75b8f3cdb.jpg)  
图 5 2000～2020 年研究区湿地景观生态风险空间格局与时空动态

Fig. 5 Spatial pattern and spatial－temporal dynamics of ecological risk in wetland landscapes in study area，2000－

2.3 景观生态风险与生态系统服务的相关性分析

# 2. 3. 1 双变量全局空间自相关

采用双变量空间自相关模型，对杭嘉湖平原湿地生态系统服务能力和景观生态风险的空间关联特征进行分析，结果表明( 图 6) ，2000 ～ 2020 年 Mo-ran ’ I 指数依次为－0. 119，－0. 233，－0. 088，这说明研究区ESI 与ERI 存在着负向空间关联性。

# 2. 3. 2 双变量局部空间自相关

通过采用 LISA 聚类图进行局部空间自相关分析，对散点图中通过了显著性检验的区域单元运用聚类图进行地理表达，根据其空间关联模式将其划分为不显著区、 低服务－低风险区( L － L) 、低服务－高风险区( L－H) 、 高服务－低风险区( H－L) 和高服务－高风险区( H－H) ( 图 7) 。

![](images/4681cb1ca45641c86eadfad216ef1394416e198287f99027888fff8682e5e7e4.jpg)  
图 6 2000～2020 年研究区湿地单位面积生态风险与综合生态系统服务散点分析图

![](images/bd23cd9ba5d7d0a4280dbcbd5b4fd7f2929edf383b0eec197d6f734dd83fbe99.jpg)  
Fig. 6 Scatter analysis of ecological risk and integrated ecosystem service per unit area of wetlands in study area，2000－2020   
图 7 研究区湿地景观生态风险与综合生态系统服务 LISA 聚类图

Fig. 7 LISA clustering of ecological risks and integrated ecosystem services of wetland landscapes in study area

低服务－高风险区代表研究区单位面积生态系统服务能力低但生态风险等级高的区域。 其呈团状分布于研究区北部湖州的南浔、 吴兴区，以及嘉兴的秀洲、 嘉善县，该区域广泛交织分布着湖泊河流、 滩地等天然湿地及桑基鱼塘等人工湿地，生态敏感度高、 生态稳定性弱，作物生产供给服务以及固碳释氧的能力较低，同时面临被其他用地侵占的高风险。 高服务－高风险区多呈点状分布于低服务－高风险区外围，主要的湿地类型除了稻田湿地、 湖泊河流、 水库坑塘外还有部分滩涂滩地，随时间变化部分低服务－高风险区域转化为高服务－高风险区域。 高服务－低风险区主要分布在研究区西部一隅，以成片林地以及稻田湿地为主。 低服务－低风险区域主要出现在杭州的拱墅、 上城区，该区大部分为建设用地，湿地面积少且零散，服务与风险水平均保持较低状态。

2.4 生态系统服务对景观生态风险的关联特征演变为进一步探讨二者的空间作用关系，阐释其相关性在地理空间的分布情况，采用空间回归模型分析生态系统服务对于景观生态风险具体影响程度。 表 4 为 OLS 和 GWR 的拟合结果，通过对比，GWR 模 型 比 OLS 模 型 的 AICc 值 降 低298. 371 个单位，R2 和调整后 R2 指数提高，说明 GWR 模型的结果更优，能更好地解释综合服务能力对景观生态风险关系空间分布的影响。 图8 分别显示了 2000 、 2010 和 2020 年研究区湿地生态系统服务与景观生态风险的回归系数和空间分布，回归系数大小差异显著，说明影响研究区生态风险的服务水平存在空间异质性，且从 3 年的均值来看整体都呈负相关状态且逐渐降低。 空间的特征分析上，负相关显著的区域集中在研究区西部与东北部地区。 其中，德清、 吴兴、 嘉善、 余杭区等地，该区域单位服务功能变化对于生态风险的下降幅度驱动较强，服务弱化的同时更易加剧风险的恶化，风险对于服务能力的敏感性强烈。 少部分网格呈正相关，主要分布在研究区南部、 北部及东部沿海，表明该区域的服务与风险存在正相关关系，服务的提升同时可能会带来风险的提升。 此外，也呈现出明显的时间趋势。 2010 年正负相关显著区缩减，但至 2020 年，两者之间的有相关性的区域显著扩张。

# 表 4 OLS 模型与 GWR 模型拟合效果比较

Tab. 4 Comparison of fitting effectiveness between OLS   

<table><tr><td colspan="4">model and GWR model</td></tr><tr><td>模型</td><td>AICc</td><td>R²</td><td>调整后的R</td></tr><tr><td>OLS</td><td>513.243</td><td>0.414</td><td>0. 465</td></tr><tr><td>GWR</td><td>214.872</td><td>0.601</td><td>0.479</td></tr></table>

![](images/ae51f36f2dc5572fbcc006991c04c5ad1b373b937bc7b08e7d5a300f3c74adbe.jpg)  
图 8 2000 ～ 2020 年湿地景观生态风险与生态系统服务地理加权回归分析结果Fig. 8 Results of geographically weighted regression analysis of ecological risks and ecosystem servicesin wetland landscapes，2000－2020

从识别生态系统服务典型服务功能角度出发，分别探讨不同服务与风险之间的协同互馈或权衡机制有助于在决策实施层面中提供科学支持，以降低整体环境的生态风险 本文采用 SPSS软件分别分析了景观生态风险与四种典型生态系统服务功能之间的相关性( 表 5) 。 结果表明，景观生态风险与综合生态系统服务呈现负相关，这与空间上的结果相互印证。 同时，风险与固碳、产水功能呈显著负相关效应，生境质量与风险的相关性程度逐步降低，而风险与作物生产功能呈显著正相关，生产能力的提升可能导致风险的增加。 2000～2020 年研究区综合生态系统服务与景观生态风险均为负相关且相关性先增高后降低，同时也应关注关键服务能力与风险之间的联系

表 5 生态系统服务功能与景观生态风险指数的相关性  
Tab. 5 Correlation of ecosystem services and landscape ecological risk index   

<table><tr><td>年份</td><td>固碳(CS)</td><td>生境质量(HB)</td><td>产水量（WY)</td><td>作物生产(CP)</td><td>综合生态系统服务（ESI)</td></tr><tr><td>2000</td><td>-0.402 **</td><td>-0.073*</td><td>-0.195 **</td><td>0.078*</td><td>-0.292 **</td></tr><tr><td>2010</td><td>-0.394 **</td><td>-0.021</td><td>-0.222 **</td><td>0.143 **</td><td>-0.372 **</td></tr><tr><td>2020</td><td>-0.320**</td><td>-0.033</td><td>-0.267 **</td><td>0.138 **</td><td>-0.273 **</td></tr></table>

注: ＊＊ 表示 P ＜ 0. 01，\* 表示 P ＜ 0. 05

# 3 讨论

研究湿地风险与服务之间的关系，可有效关联生态系统与人类福祉，对于维持整个区域的发展和湿地生态系统健康水平的提升具有重要作用［41］。

# 3. 1 杭嘉湖平原生态系统服务的时空格局及变化特征

从杭嘉湖平原四类典型服务的时空趋势上来看，与 前 人 研 究 结 果 有 相 互 印 证、 互 为 补充［23，42］，也有存在差异的情况，整体的服务时空趋势也不尽相同。 这可能是采用重要生态系统服务功能表征整体生态系统服务的评估方法受所选指标因素影响较大，且测定服务的评价方法、 数据来源、 研究区湿地特点有别，导致最终结果在时空变化上存在差异［23］。 在研究时段内，我们观测到不同生态系统服务功能呈现出区域不平衡性( 图 4) ，这可能由于生境质量服务低值呈明显的西南－东北走向，带状分布于快速城市化区域周边，但产水量与作物生产水平则呈现不同的西高东低的态势( 图 3) 同时，服务变化与全球变暖等气候因子也密不可分，长江流域径流量与降水量变化直接影响了产水量的提升［43］，单项服务之间的变化速率存在明显差异( 表 3) ，整体服务的水平受到供给、 调节、 支持服务的交织影响，这解释了服务无法一直维持较为稳定状态的现象

# 3. 2 杭嘉湖平原景观生态风险的时空格局及变 化特征

从杭嘉湖平原湿地景观生态风险的时间动态来看，在研究时段内呈下降趋势，这一时间尺度特征与 Li 等［44］在辽河河口湿地的研究保持一致。总体而言，高风险与次高风险区域变化幅度不大，主要是中风险转化为低风险与次低风险，从而使得区域的风险水平下降。 从空间动态上看，主要体现在靠近城市建成区周围的稻田湿地中低风险斑块的增加，以及滨海滩涂等中高风险湿地趋向减少甚至消失( 图 5) 。 结合 Li 等［44］和 Yang等［45］的研究，这一现象的原因主要是城市扩张和土地开发强度变化一定程度上促进部分临近建设区的湿地景观向低脆弱性的人工景观转变，在适度的人类干扰的情况下使得空间异质性增强、 景观敏感性降低，湿地呈现出风险转低的情况［46］，且该区域多以单一的稻田湿地景观为主，抗干扰能力强。 高风险与次高风险出现的区域中湿地地类分布复杂零散且多为天然湿地，各湿地的破碎度与分离度较高，在脆弱度同样高的情况下，造成了高风险的出现。 同时，积极的生态政策也是风险水平发生变化的主要因素之一 中国在步入21 世纪后逐步开始加大对于湿地的保护及合理利用，浙江省地方层面计划并实施了退耕还湿的政策，颁布实行了 《浙江省湿地保护条例》等相关法律法规与条例［6，47］。 随着对于湿地保护认知的提升，减缓了湿地锐减的趋势，同时回应了研究区整体生态风险水平逐步下降的原因，证明过去湿地保护政策起到了一定的效用，但这仍旧不足以彻底扭转湿地的流失。 随着时间的推移，更需建立更加健全且精准化、 全面化湿地综合管理保护体系 。

# 3. 3 杭嘉湖景观生态风险与生态系统服务的内在联系与表征

景观生态风险以及生态系统服务均是景观格局与生态过程相互作用的综合结果。 城市化及工业化等带来的土地利用覆被及耕种强度变化导致了景观结构与功能破坏［48］，进而体现在生态过程中，降低了湿地生态系统的服务能力，同样通过损失与概率的累乘综合表征为景观生态风险的提升，这是两者存在关联的内在逻辑［20］。 长江流域是湿地侵占较为严重的区域，长期处在损失与恢复的过程中，人口激增带来的粮食压力使得更多的自然湿地转化为稻田湿地，沿海区域则因围海造田等工程使得滨海滩涂等自然湿地大量损失，之后部分的稻田湿地逐步转化为建设用地，这一过程几乎是不可逆转的［42］。 即使在政策指导下湿地有所恢复，但是恢复多为水库坑塘 稻田等人工湿地，自然湿地所能提供的生态系统服务是人工生态系统无法比拟的［49］，因此保护自然湿地应成为维持湿地生态系统稳定的重点。

空间自相关的结果表明服务与风险之间存在负向的空间依赖性( 图 6) ，这与部分前人研究一致［25，41］，但与贾艳艳等［27］在长江流域安徽段的研究结论 “存在一定的空间正相关性”不同。 究其原因，可能是相比于流域或城市群，两者的关系受到湿地这一极易受扰动的景观类型的影响，显示出不同的结论。 值得一提的是，在两者相关性研究中针对服务功能的测定上，本文所选取的叠加多种服务功能的方法与国内大部分学者采用的价值当量法不同，评估方法基于不同的原理，一定程度上也会带来结果的差异。

# 3. 4 基于风险与服务关系指导下的优化策略

根据服务－风险的关系类型集聚与空间回归结果( 图 7、 图 8) ，以及进一步对两者的影响机制进行了深入分析，杭嘉湖地区在未来的发展和规划中可以从以下几方面考虑湿地保护政策的制定，推进区域生态文明建设 ( 1) 随时间推移，部分低服务－高风险转向高服务－高风险区，说明该区服务水平不断提高，但潜在的风险水平不容小觑，且都处于服务对风险高度负影响的区域，意味着该区的服务提升能带来风险水平的下降。位于于此区的湖州南浔、 吴兴、 德清，嘉兴的嘉善、 秀洲区等地中自然湿地与人工湿地交织密切，应重视生态系统服务的功能，对三生空间进行集中化布置，降低人为活动对生态本底的侵扰。 加大诸如德清下渚湖重点湿地自然保护地及嘉兴运河湾湿地公园等生态存量的严格保护，提升湿地生物多样性、 恢复生态完整性、 减少破碎化，同时解决水环境污染问题带来的风险。 ( 2)位于西部的德清县、 余杭区中山区丘陵区域是高服务－低风险的分布区，该区自然资源禀赋较好，整体的生态系统服务较高，稻田湿地依山就势，应侧重保护原有各类景观，强化其对于生态安全格局的屏障作用。 ( 3) 低服务－低风险区主要分布在杭州市的主城区，该区受人为因素干扰强度大，无法提供较强的生态系统服务能力，而该区域长期处于服务与风险呈正影响的区域( 图 8) ，这意味着不能一味的提升服务能力。 参考前人的研究，近年来研究区降水量持续上升以及城市建设带来不透水面的增加，减少了下渗，两者结合使得非湿地区域的产水服务的快速提升［50］，这启示我们需大力推进退耕还湿与海绵城市建设，提升湿地的面积以及连通性，构建蓝绿基础设施网络，发挥湿地雨洪调蓄功能，促进雨水的下渗以及再利用，谨防城市内涝问题［31］。 同时延伸该地区湿地的休闲游憩、 科普教育等功能，发展湿地休闲农业，力求生态与经济的良性协同，提升潜在文化服务能力［51］。 ( 4) 杭嘉湖平原作为主要的粮食供应基地，稻田湿地是分布最为广泛且占地面积最大的湿地类型，这使得其供给服务能力在整个长三角区域都处于较高水平 但供给功能提升会带来风险增加( 表 5) ，因此如何实行稻田湿地的存量提升对于降低风险具有重要意义。 首先需集中保护研究区嘉兴市中部桐乡 海宁等区域的大面积的优质稻田湿地，制定合理的农业政策，采取农田作物多样性、 生物防治和保护性栽培等措施，提升人工湿地的使用效率，严格执行“非农化” “非粮化”政策，使整体粮食生产安全处于较为稳定的状态。 其次，对于人工湿地与自然湿地交织密切区域，则应实行科学的退耕退养，控制因盲目将稻田湿地转化为自然湿地时带来的生态风险［52］。 从价值－风险的综合角度，针对不同集聚区主体情况进行定位，有利于实现对划分区域的差异化管理。

# 3. 5 不足与展望

实际上，想要实现生态环境可持续健康发展仍是一个非常复杂且漫长的过程，结果显示服务对风险的负向影响与两者之间关联性随时间推移有所减弱，因此致力于实现风险与服务的协同互馈将是我们长期需要探索的课题。 受篇幅限制，本研究中并未深入探讨单项服务之间的权衡协同关系。 为此，下一步的研究重点可在了解服务之间的权衡与协同关系基础上将供需平衡调整纳入区域湿地的分层管理之中，或结合景观模拟预测模型，探讨未来不同情景下湿地服务与风险的分布情况，提高评价的有效性和全面性，从而有助于政策的有效实施以及湿地与社会和谐、 稳定地可持续发展。

# 4 结论

本文基于 2000 、 2010 和 2020 年的土地利用数据，定量评价了杭嘉湖地区湿地生态系统服务和景观生态风险的时空变异特征、 空间相关性以及两者关联，主要结果如下。

( 1) 研究时段内，整体的生态系统服务水平先下降后上升的趋势，生态系统服务以东南部的高值区为核心依次向外扩散，分布形式呈环状降低，随着时间的推移逐渐由聚集性向分散性转变 。

( 2) 研究时段内，景观生态风险指数分别为0. 028 6 0. 027 7 和 0. 026 6，总体呈现逐渐下降的趋势，在空间上呈现低值连片、 高值局部集聚的分布特征。 由中等风险等级转入较低风险等级。 高和较高风险区呈片状主要分布在研究区西部和北部，面积萎缩程度较小，低和较低生态风险区广泛分布在研究区的各个区域，随时间变化面积呈上升趋势，研究区整体生态风险状况小幅改善。

( 3) 根据空间自相关结果，景观生态风险与生态系统服务价值存在空间集聚特征，空间回归模型表明景观生态风险对生态系统服务具有负效应，总体生态系统服务的提升在一定程度上能带来风险水平的下降，且负向关联与影响逐渐减弱。

研究结果利用体现人类社会福祉的生态服务来最优化分析，提升风险管理的针对性，以期达到生态系统服务与景观生态风险之间的协同互馈，未来空间规划中需针对风险－服务的相关区域实行对应的生态措施，通过合理规划湿地保护红线，划定湿地禁止建设区与限制建设区，保护优质稻田，以确保可持续的服务供应，同时不断增强连通性，加大湿地教育科普与宣传，利于风险预警的同时促进湿地与人类社会和谐共生。

# 参考文献:

［1］ XUE Z，ZOU Y，ZHANG Z，et al． Reconstruction and future prediction of the distribution of wetlands in China ［J］． Earth ’ s

Future，2018，6( 11) : 1508－1517．  
［2］ MAHDAVI S，SALEHI B，GRANGER J，et al． Remote sensingfor wetland classification: A comprehensive review ［J］． GI-Science ＆ Remote Sensing，2018，55( 5) : 623－658．  
［3］ NIU Z，ZHANG H，WANG X，et al． Mapping wetland changesin China between 1978 and 2008 ［J］． Chinese Science Bulle-tin，2012，57( 22) : 2813－2823．  
［4］ MA T，LI X，BAI J，et al． Tracking three decades of land useand land cover transformation trajectories in China ’ s large riverdeltas ［J］． Land Degradation ＆ Development，2019，30( 7) :799－810．  
［5］ 杨昊臻，杨小柳． 应用集萃法分析海河流域滨海湿地退化成因 ［J］． 水土保持研究，2021，28( 1) : 345－352，359．YANG H Z，YANG X L． Identifying the degradation causes ofthe coastal wetlands in Haihe River Basin based on meta－analy-sis ［J］． Research of Soil and Water Conservation，2021，28( 1) : 345－352，359．  
［6］ 朱 颖，王 杉，冯育青． 近 30 年太湖流域湿地生态系统服务价值对景观格局变化的响应: 基于“退田还湖”工程的实施 ［J］． 中国园林，2022，38( 1) : 88－93．ZHU Y，WANG S，FENG Y Q． Response of the value of wet-land ecosystem service in Taihu Basin to the change of land-scape pattern in the past 30 years: Based on the implementationof the project of restoring the lake from the land ［J］． ChineseLandscape Architecture，2022，38( 1) : 88－93．  
［7］ 杨 鑫，海新权，杨玉婷． 基于 Meta 分析的张掖黑河湿地生态系统服务价值评估［J］． 生态与农村环境学报，2023，39( 1) : 60－ 68YANG X，HAI X Q，YANG Y T． Meta－analysis－based assess-ment of ecosystem service value of Heihe wetland in Zhangye［J］． Journal of Ecology and Rural Environment，2023，39( 1) : 60 － 68．  
［8］ RAPPORT D J，COSTANZA R，MCMICHAEL A J． Assessingecosystem health ［J］． Trends in Ecology ＆ Evolution，1998，13( 10) : 397－402．．  
［9］ COSTANZA R，D ’ ARGE R，DE GROOT R，et al． The valueof the world ’ s ecosystem services and natural capital ［J］． Na-ture，1997，387: 253－260．  
［10］ BOLLIGER J，BTTIG M，GALLATI J，et al． Landscape mul-tifunctionality: A powerful concept to identify effects of environ-mental change ［J］． Regional Environmental Change，2011，11( 1) : 203 － 206． ．  
［11］ 乔 斌，曹晓云，孙玮婕，等． 基于生态系统服务价值和景观生态风险的生态分区识别与优化策略———以祁连山国家公园青海片区为例 ［J］． 生态学报，2023，43( 3) : 986－1004．QIAO B，CAO X Y，SUN W J，et al． Ecological zoning identi-fication and optimization strategies based on ecosystem servicevalue and landscape ecological risk: Taking Qinghai area of Qil-ian Mountain National Park as an example ［J］． Acta EcologicaSinica，2023，43( 3) : 986－1004．  
［12］ 王兆峰，杨钊颖，张海燕． 基于生态系统服务价值的洞庭湖生态经济区生态补偿标准与策略优化［J］． 湖南师范大学自然科学学报，2023，46( 5) : 63－71．WANG Z F，YANG Z Y，ZHANG H Y． Ecological compensa-tion standard and strategy optimization of Dongting Lake ecologi-cal economic zone based on ecosystem service value ［J］． Jour-nal of Natural Science of Hunan Normal University，2023，46( 5) : 63－71  
［13］ 李俊翰，高明秀． 滨州市生态系统服务价值与生态风险时空演变及其关联性 ［J］． 生态学报，2019，39( 21) : 7815－7828．LI J H，GAO M X． Spatiotemporal evolution and correlation a-nalysis of ecosystem service values and ecological risk inBinzhou ［J］． Acta Ecologica Sinica，2019，39 ( 21) : 7815 －7828．  
［14］ 罗松英，邢雯淋，梁绮霞，等． 湛江湾红树林湿地表层沉积物重金属形态特征、 生态风险评价及来源分析［J］． 生态环境学报，2019，28( 2) : 348－358．LUO S Y，XING W L，LIANG Q X，et al． Speciation，ecologi-cal risk assessment and source analysis of heavy metals in thesurface sediments of mangrove wetland in Zhanjiang Bay ［J］．Ecology and Environmental Sciences，2019，28 ( 2 ) : 348 －358．  
［15］ QU C S，CHEN W，BI J，et al． Ecological risk assessment ofpesticide residues in Taihu Lake wetland，China ［J］． Ecologi-cal Modelling，2011，222( 2) : 287－292．  
［16］ XU X，LIN H，FU Z． Probe into the method of regional ecologi-cal risk assessment－a case study of wetland in the Yellow RiverDelta in China ［J］． Journal of Environmental Management，2004，70( 3) : 253－262．  
［17］ 翟培秀，李飞雪，邱小倩，等． 长三角地区景观生态风险时空演变评估 ［J］． 水 土 保 持 研 究，2023，30 ( 4) : 245 －255．ZHAI P X，LI F X，QIU X Q，et al． Assessment on spatial－temporal evolution of landscape ecological risk in the YangtzeRiver Delta ［J］． Research of Soil and Water Conservation，2023，30( 4) : 245－255．  
［18］ XU W，WANG J，ZHANG M，et al． Construction of landscapeecological network based on landscape ecological risk assessmentin a large－scale opencast coal mine area ［J］． Journal of CleanerProduction，2021，286: 125523．  
［19］ 彭 建，党威雄，刘焱序，等． 景观生态风险评价研究进展与展望 ［J］． 地理学报，2015，70( 4) : 664－677．PENG J，DANG W X，LIU Y X，et al． Review on landscapeecological risk assessment ［J］． Acta Geographica Sinica，2015，70( 4) : 664－677．  
［20］ 曹祺文，张曦文，马洪坤，等． 景观生态风险研究进展及基于生态系统服务的评价框架: ESRISK ［J］． 地理学报，2018，73( 5) : 843－855．CAO Q W，ZHANG X W，MA H K，et al． Review of landscapeecological risk and an assessment framework based on ecologicalservices: ESRISK ［J］． Acta Geographica Sinica，2018，73( 5) : 843 － 855．  
［21］ 张师赫，李宝银，林玉英，等． 基于生态系统服务的景观生态风险评价及其驱动因素研究———以福建省为例 ［J］．水土保持研究，2022，29( 6) : 174－182．ZHANG S H，LI B Y，LIN Y Y，et al． Research on landscapeecological risk assessment and driving factors based on ecosys-tem services—A case study of Fujian Province ［J］． Research ofSoil and Water Conservation，2022，29( 6) : 174－182．  
［22］ 欧阳晓，朱 翔，贺清云． 基于生态系统服务和生态系统健康的生态风险评价———以长株潭城市群为例 ［J］． 生态学报，2020，40( 16) : 5478－5489．OUYANG X，ZHU X，HE Q Y． Incorporating ecosystem serv-ices with ecosystem health for ecological risk assessment: Casestudy in Changsha － Zhuzhou － Xiangtan urban agglomeration，China ［J］． Acta Ecologica Sinica，2020，40 ( 16 ) : 5478 －5489．  
［23］ LI W，WANG Y，XIE S，et al． Impacts of landscape multifunc-tionality change on landscape ecological risk in a megacity，Chi-na: A case study of Beijing ［J］． Ecological Indicators，2020，117: 106681．  
［24］ ZHANG D，JING P，SUN P，et al． The non－significant corre-lation between landscape ecological risk and ecosystem servicesin Xi ’ an Metropolitan Area，China ［J］． Ecological Indicators，2022，141: 109118．  
［25］ 靳甜甜，张云霞，朱月华，等． 黄土高原林区生态系统服务价值与景观生态风险时空变化及其关联性———以子午岭区为例 ［J］． 应用生态学报，2021，32( 5) : 1623－1632．JIN T T，ZHANG Y X，ZHU Y H，et al． Spatiotemporal varia-tions of ecosystem service values and landscape ecological riskand their correlation in forest area of Loess Plateau，China: Acase study of Ziwuling Region ［J］． Chinese Journal of AppliedEcology，2021，32( 5) : 1623－1632．  
［26］ 李 辉，周启刚，李 斌，等． 近 30 年三峡库区生态系统服务价值与生态风险时空变化及相关性研究 ［J］． 长江流域资源与环境，2021，30( 3) : 654－666．LI H，ZHOU Q G，LI B，et al． Spatiotemporal change and cor-relation analysis of ecosystem service values and ecological riskin Three Gorges Reservoir Area in the past 30 years ［J］． Re-sources and Environment in the Yangtze Basin，2021，30( 3) :654－666．  
［27］ 贾艳艳，唐晓岚，任宇杰． 长江流域安徽段生态系统服务价值与景观生态风险时空演变及其关联分析 ［J］． 南京林业大学学报( 自然科学版) ，2022，46( 3) : 31－40．JIA Y Y，TANG X L，REN Y J． Spatial－temporal evolution andcorrelation analyses of ecosystem service values and landscapeecological risks in Anhui section of the Yangtze River basin［J］． Journal of Nanjing Forestry University( Natural Sciences E-dition) ，2022，46( 3) : 31－40．  
［28］ 朱月华，侯宗东，徐彩仙，等． 基于生态系统服务供需关系的甘肃白龙江流域生态风险识别与管理 ［J］． 地理科学，2023，43( 3) : 423－433．ZHU Y H，HOU Z D，XU C X，et al． Ecological risk identifi-cation and management based on ecosystem service supply anddemand relationship in the Bailongjiang River Watershed ofGansu Province ［J］． Scientia Geographica Sinica，2023，43( 3) : 423 － 433．  
［29］ GONG J，CAO E，XIE Y，et al． Integrating ecosystem servicesand landscape ecological risk into adaptive management: In-sights from a western mountain－basin area，China ［J］． Journalof Environmental Management，2021，281: 111817．  
［30］ NELSON E，MENDOZA G，REGETZ J，et al． Modeling multi-ple ecosystem services， biodiversity conservation， commodityproduction，and tradeoffs at landscape scales ［J］． Frontiers inEcology and the Environment，2009，7( 1) : 4－11．  
［31］ 陈骏宇，王慧敏，刘 钢，等． “水－能－粮”视角下杭嘉湖区域生态系统服务供需测度及政策研究 ［J］． 长江流域资源与环境，2019，28( 3) : 542－553．CHEN J Y，WANG H M，LIU G，et al． Evaluation of ecosys-tem services and its adaptive policies in the hangjiahu region un-der water－energy－food nexus ［J］． Resources and Environmentin the Yangtze Basin，2019，28( 3) : 542－553  
［32］ O ’ NEILL R V，HUNSAKER C T，TIMMINS S P，et al． Scaleproblems in reporting landscape pattern at the regional scale［J］． Landscape Ecology，1996，11( 3) : 169－180．  
［33］ BAGSTAD K J，JOHNSON G W，VOIGT B，et al． Spatial dy-namics of ecosystem service flows: A comprehensive approach toquantifying actual services ［J］． Ecosystem Services，2013，4:117－125．  
［34］ 蔚 芳，詹小稳． 基于生境质量与碳储量的城市刚性开发边界划定 ［J］． 浙 江 大 学 学 报 ( 工 学 版) ，2019，53 ( 8) :1478－1487．WEI F，ZHAN X W． Delineation of rigid urban growth bounda-ry based on habitat quality and carbon storage ［J］． Journal ofZhejiang University ( Engineering Science ) ，2019，53 ( 8 ) :1478－1487．  
［35］ LIU W，ZHAN J，ZHAO F，et al． The tradeoffs between foodsupply and demand from the perspective of ecosystem serviceflows: A case study in the Pearl River Delta，China ［J］． Jour-nal of Environmental Management，2022，301: 113814．  
［36］ CHENG X，ZHANG Y，YANG G，et al． Landscape ecologicalrisk assessment and influencing factor analysis of basins in sub-urban areas of large cities – A case study of the FuchunjiangRiver Basin，China ［J］． Frontiers in Ecology and Evolution，2023，11: 1184273．  
［37］ 谢花林． 基于景观结构和空间统计学的区域生态风险分析［J］． 生态学报，2008，28( 10) : 5020－5026XIE H L． Regional eco － risk analysis of based on landscapestructure and spatial statistics ［J］． Acta Ecologica Sinica，2008，28( 10) : 5020－5026．  
［38］ HOU M，GE J，GAO J，et al． Ecological risk assessment andimpact factor analysis of alpine wetland ecosystem based onLUCC and boosted regression tree on the zoige plateau，China［J］． Remote Sensing，2020，12( 3) : 368．  
［39］ 任胤铭，刘小平，许晓聪，等． 基于 FLUS－InVEST 模型的京津冀多情景土地利用变化模拟及其对生态系统服务功能的影响 ［J］． 生态学报，2023，43( 11) : 4473－4487．REN Y M，LIU X P，XU X C，et al． Multi－scenario simulationof land use change and its impact on ecosystem services in Bei-jing－Tianjin－Hebei region based on the FLUS － InVEST Model［J］． Acta Ecologica Sinica，2023，43( 11) : 4473－4487．  
［40］ FOTHERINGHAM A S，BRUNSDON C，CHARLTON M． Geo-graphically weighted regression: the analysis of spatially varyingrelationships ［M］． Chichester，England: John Wiley ＆ Sons，2002．  
［41］ 孟晓璐，张艳芳． 景观格局变化下陕西汉江流域生态价值与风险的相关性研究［J］． 水土保持学报，2023，37( 3) :190－200．MENG X L，ZHANG Y F． Study on correlation between ecolog-ical value and risk of Hanjiang River Basin in Shaanxi Provinceunder landscape pattern change ［J］． Journal of Soil and WaterConservation，2023，37( 3) : 190－200．  
［42］ ZHANG X，WANG J，YUE C，et al． Impact of wetland changeon ecosystem services in different urbanization stages: A casestudy in the Hang－Jia－Hu Region，China ［J］． Ecological Indi-cators，2023，153: 110382．  
［43］ HU W，LI G，LI Z． Spatial and temporal evolution characteris-tics of the water conservation function and its driving factors inregional lake wetlands—Two types of homogeneous lakes as ex-amples ［J］． Ecological Indicators，2021，130: 108069．  
［44］ LI H，SU F，GUO C，et al． Landscape ecological risk assess-ment and driving mechanism of coastal estuarine tidal flats—Acase study of the liaohe estuary wetlands ［J］． Frontiers in Envi-ronmental Science，2022，10: 1070009．  
［45］ YANG D，ZHANG P，JIANG L，et al． Spatial change andscale dependence of built－up land expansion and landscape pat-tern evolution—Case study of affected area of the lower YellowRiver ［J］． Ecological Indicators，2022，141: 109123．  
［46］ OSMAN R W． Intermediate disturbance hypothesis ［M］/ /En-cyclopedia of Ecology． Amsterdam: Elsevier，2008: 1986 －1994．  
［47］ SUN T，LIN W，CHEN G，et al． Wetland ecosystem health as-sessment through integrating remote sensing and inventory datawith an assessment model for the Hangzhou Bay，China ［J］．Science of the Total Environment，2016，566－567: 627－640．  
［48］ YANG L，ZHANG S，YIN L，et al． Global occupation of wet-land by artificial impervious surface area expansion and its im-pact on ecosystem service value for 2001 – 2018 ［J］． Ecologi-cal Indicators，2022，142: 109307．  
［49］ MAO D，WANG Z，WU J，et al． China ’ s wetlands loss to ur-ban expansion ［J］． Land Degradation ＆ Development，2018，29( 8) : 2644－2657．  
［50］ 窦攀烽，左舒翟，任 引，等． 气候和土地利用/覆被变化对宁波地区生态系统产水服务的影响［J］． 环境科学学报，2019，39( 7) : 2398－2409．DOU P F，ZUO S D，REN Y，et al． The impacts of climate andland use /land cover changes on water yield service in Ningboregion ［J］． Acta Scientiae Circumstantiae，2019，39 ( 7 ) :2398－2409．  
［51］ 吴伟志，方 龙． 浙江省湿地资源现状及保护管理对策［J］． 浙江林业科技，2013，33( 3) : 81－84．WU W Z，FANG L． Resources and Conservation of Wetland inZhejiang ［J］． Journal of Zhejiang Forestry Science and Tech-nology，2013，33( 3) : 81－84．  
［52］ 陈楚文，鲍铭铭，王 庆，等． 与自然共生: 浙北平原湿地乡村的可持续发展路径探索 ［J］． 中国园林，2022，38( 6) : 23－28．CHEN C W，BAO M M，WANG Q，et al． Coexisting with na-ture: Exploring the path of sustainable development of wetlandvillages in the northern Zhejiang Plain ［J］． Chinese LandscapeArchitecture，2022，38( 6) : 23－28．

# Spatial－temporal Evolution and Correlation of Wetland Ecosystem Services and Landscape Ecological Risks: A Case Study of Hangjiahu Plain

WANG Li-na1 ，YANG Guo-fu2 ，LI Jia-xin1 ，ZHANG Meng-xian1 ，XU Bin1 ( 1． School of Landscape Architecture，Zhejiang A＆F University ，Hangzhou 311300，China; 2． School of Art and Archaeology， Zhejiang University City College，Hangzhou 310015，China)

Abstract: Understanding the spatiotemporal characteristics and interrelationships among ecosystem services and ecological risks is crucial for crafting targeted ecosystem management strategies，ensuring regional ecological security and sustainable development． Wetlands provide various crucial ecosystem services to humanity，yet they exhibit high ecological sensitivity and are susceptible to disturbances from urbanization and human activities． This study focused on the Hangjiahu Plain，and utilized data from land use and socioeconomic statistics for 2000， 2010，and 2020． By employing the InVEST ecosystem service model，landscape ecological risk index，bivariate spatial autocorrelation analysis，and geographically weighted regression model，a quantitative assessment was conducted to explore the spatiotemporal trends and correlations between ecosystem service functions and landscape ecological risks． The results showed that: ( 1) From 2000 to 2020，the wetland ecosystem services in the study area decreased gradually from the high-value area in the southeast，and expanded outward sequentially． A transition from aggregative to dispersive with time was found． ( 2) The landscape ecological risk indices were 0. 0286，0. 0277，and 0. 0266，respectively． The overall ecological risk level in the study area shifted from a moderate risk level to a lower risk level． High and moderately high-risk areas were mainly distributed in patches in the western and northern parts of the study area． ( 3) Landscape ecological risks and ecosystem services exhibited spatial clustering characteristics． The relationship between landscape ecological risks and comprehensive ecosystem services showed a significant negative correlation，indicating a feedback effect． This negative impact and correlation gradually weakened over time． This study provided a theoretical basis for the development of policies aimed at reducing regional ecological risks and enhancing the capacity of ecosystem services to sustain the continuous health and stability of wetland ecosystems．

Key words: wetlands; ecosystem service; ecological risk; spatial-temporal correlation; spatial regression model; Hangjiahu Plain