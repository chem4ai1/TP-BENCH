# 西南地区水陆耦合的生态安全格局识别与生态韧性评估优化

程佳龙1，张军以1,2※

(1．重庆师范大学地理与旅游学院，重庆401331；2．三峡库区地表过程与生态修复重庆市重点实验室，重庆401331)

摘要：科学识别生态安全格局与生态韧性是区域生态安全建设的重要基础。为明晰西南地区生态安全格局与生态韧性，维护区域生态安全，该研究以西南地区为例，利用InVEST、耦合度模型等方法，基于水陆生态系统耦合量化生态系统服务，构建生态安全格局并评估其生态韧性，提出优化策略。结果表明：1）西南地区水陆耦合生态系统服务空间异质性显著，整体呈“西高东低”的空间特征。极高耦合区分布在川西、黔中、滇中等地，低耦合或未耦合区主要集中在大中型城市周边区。2）区域生态安全格局呈“两核心两带”的空间特征。“两核心”是以川西南、滇西北为中心的连片生态源地核心和以滇南为中心的分散生态源地次核心。“两带”是以渝南、黔北为核心和以川西边缘为核心的两条生态廊道。3）区域高韧性生态源地17块，呈现以川西南、滇西北源地为核心的空间特征；高韧性生态廊道34条，呈现川西南边缘及滇西南为核心的分布特征；生态夹点韧性呈现以滇中西、川西南边缘为核心的空间特征，高低韧性分布集中。高韧性生态夹点占比20.23%。4）构建了“三轴四区五核”的生态韧性优化格局，综合自然人文影响因素，提出了山地丘陵水土保持、小流域水土流失综合治理等生态修复措施。该研究考虑了水陆生态系统耦合的影响，细化了生态服务供给及生态安全格局分析，为实施生态修复提供了科学依据。

关键词：生态系统服务；生态安全格局；生态韧性；水陆耦合；西南地区 doi: 10.11975/j.issn.1002-6819.202412236

中图分类号：Q149 文献标志码：A 文章编号：1002-6819(2025)-08-0272-10程佳龙，张军以.西南地区水陆耦合的生态安全格局识别与生态韧性评估优化[J].农业工程学报，2025，41(8)：272-281i: 10.11975/j.issn.1002-6819.202412236 http://www.tcsae.0rg

CHENGJialong,ZHANGJunyi.Identifyingecologicalsecuritypatterandoptimizing ecologicalresilienceasessmentforwaterlandcouplingin Southwest China[J].Transactionsof the Chinese Societyof Agricultural Engineering (Transactionsof the CSAE),2025,41(8): 272-281.(in Chinese with English abstract)doi:10.11975/j.issn.1002-6819.202412236 http://www. tcsae.org

# 0引言

生态环境保护是关乎人类福祉的关键议题。生态环境问题导致的生态系统服务损耗一旦超过系统阈值，将会触发系统不可逆转的退化，危及区域生态安全[1]。西南地区是长江、珠江的重要水源涵养区及生态屏障，气候温暖湿润，生态资源丰富多样，是国家生态重点建设区[2]。在工业化和城镇化进程中，区域城镇规模持续增大，建设用地不断扩张，侵占了大量生态空间。同时，西南地区山地丘陵占比高，地形崎岖破碎，坡耕地比例大，乡村经济发展相对落后，不合理的农业生产对生态环境造成了严重影响，如陡坡耕种等造成的面源污染、土地石漠化等，严重威胁了区域水环境和生态系统的稳定3]。受自然环境禀赋限制和人类活动的扰动，西南地区面临着生态系统退化、生物多样性减少、水土流失等一系列生态问题，严重影响区域生态系统服务的供给能力[4]。因此，优化区域生态安全格局，增强生态服务供给能力，成为支撑区域社会经济高质量发展的重要途径。

生态系统服务评估是识别生态系统功能及其对人类福祉影响的重要途径[5]。目前，生态系统服务评估逐渐从以往的单一服务评估转向多维综合服务评估。研究主要涉及生态系统服务测度及其时空分布规律、土地利用变化对生态系统服务的影响[、城市生态系统结构[8]及生态系统服务供需关系演化机制[9]等。现有生态系统服务评估主要基于土地利用类型开展，忽视了水陆等不同类型生态系统空间镶嵌对生态系统服务供给的影响，评估难以全面反映区域生态系统“结构-功能”多样性对生态系统服务供给的影响。

生态安全格局通过生态网络（生态源地、生态廊道和生态节点等）构建及评价识别区域宏观生态系统结构与功能的稳定性[10]。其中，生态源地识别主要基于形态学空间格局[1I]、生态系统服务[12]、粒度反推法[13]等方法开展。生态阻力面构建通常选取高程、坡度、植被覆盖度等因素作为构成要素，以及生态安全指数[14]、土地阻力值[15]等。生态廊道识别多采用最小累积阻力模型[16]、图论方法[17]、电路理论[18]等方法。生态节点识别多用最小成本路径交点[19]、生态夹点及生态障碍点识别[20] 等方法。整体上，现有研究基本形成了“生态源地-生态阻力面-生态廊道-生态节点”的研究框架。区域生态安全格局本质上是区域生态服务的地域分工，是支撑区域生态安全的关键骨架[21]。生态安全格局并不能精准反映其区域生态的“结构-功能”和服务生产能力。生态韧性表征生态系统在扰动下的响应能力，是评估生态安全格局“结构-功能”的重要途径。生态韧性是指区域生态系统在应对干扰时表现出的生态抵抗性、适应性和恢复性的综合能力[22]。相关研究集中在城市生态韧性演化[23]、城镇化与生态韧性耦合[24]等方面。研究方法主要有指标体系法[25]、景观格局分析等[26]。现有生态韧性研究多聚焦于城市或森林等单一生态系统，缺乏在构建生态安全格局基础上的韧性评估。生态韧性关注生态系统的胁迫响应，生态安全格局关注生态系统的空间结构，并直接影响生态系统的功能，对区域生态系统韧性具有重要影响。

综上，将水陆生态系统的空间镶嵌纳入评估体系，有助于明晰区域水陆生态系统相互作用及其对生态服务的影响。将生态韧性纳入生态安全格局评价，是优化区域生态安全格局构建，提升区域生态安全水平的重要途径。研究以西南地区为例，基于水陆生态系统耦合，运用InVEST（integrated valuation of ecosystem services andtrade-offs）模型、耦合度模型、电路理论等评价生态系统服务，识别区域生态安全格局和生态韧性的空间特征，解析生态韧性主要影响因素，并提出差异化优化措施。

# 1材料与方法

# 1.1研究区概况

西南地区属亚热带季风气候和高原山地气候，湿润多雨，山地植被类型多样，年均降水量约为1100 mm,年均温约5～24℃，总面积约1.13×10km²。地形以山地为主，地貌复杂多样，地势西北高东南低。温暖多雨的气候、崎岖的地形和活跃的地质运动，形成了大量的构造湖、河成湖和火山湖，如滇中高原湖泊密集区、云贵高原湿地和川西北的连片沼泽湿地等，水生生态系统发达。西南地区生态地位极其重要，是长江、珠江上游生态安全和国家生态安全的重要组成部分。2023年，西南地区总人口2.1亿人，地区GDP总值169522亿元，平均城镇化率为55.64%，分别占全国总人口和GDP的14.67%、13.45%，区域内社会经济发展差异性明显。西藏属高寒地区，植被以草甸为主，生态系统敏感性高，农业规模小，人口总量小密度低，人类活动对区域生态干扰相对较小，故该研究未涉及。

# 1.2数据来源

研究数据包括气象数据、地表蒸发数据、土壤数据等12 种数据，利用ArcGIS10.8将影像数据投影校正，并重采样统一转换为500m×500m 的空间分辨率。其中，地表蒸散发数据（2015年、1000m）来源于国家生态系统观测研究网络科技资源服务系统(www.cnern.org.cn);数字高程模型（2020年、30m）、城镇位置数据（2020年）来源于地理空间数据云(http://www.gscloud.cn)；淡水食物产量数据（2020年）来自国民经济和社会发展统计公报和农业农村厅；道路数据（2020年）、水系数据（2020年）来源于 Open Street Map(http://openstreetmap.org)；气象数据（2020年、1000 m）来源于国家地球系统科学数据中心 (http://www.geodata.cn);土壤数据（2020年、100m）、土地利用数据（2020年、30m）来源于中国科学院资源环境科学与数据中心(http://www.resde.cn)；归一化植被指数（2020 年、30 m）来源于国家生态科学数据中心(http://www.nesdc.org.cn);夜间灯光数据（2020年、1000m）来源于HarvardDataverse (http://dataverse.harvard.edu)；行政区划数据（2020 年）来源于国家地理信息公共服务平台(htps://www.tianditu.gov.cn)。

# 1.3研究方法

# 1.3.1水陆耦合生态系统服务评价

# 1）水域和陆域生态系统服务评价

水域生态系统服务主要包括供给、调节、支持、文化等方面[27]。水资源供给是水域生态系统服务最重要的功能，是支撑区域发展的基础；水域储水的动态变化冗余是其在汛期发挥防洪和调节水资源时空分布不均的基础；水体的自净能力及温度调节是水域生态系统服务的重要组成；游憩潜力是水域生态系统供给人类文化需求的次生服务[28-30]。研究选取水源、食物供给、雨蓄调控、气候调节和水体净化、生物多样性维护、游憩潜力等水域生态系统服务，并基于前述各项服务的重要程度，采用层次分析法赋权构建水域生态系统服务评价指标体系(表1)，各因子分级加权求和，以评价水域生态系统服务，生境质量采用InVEST模型的生物多样性模块计算。

表1西南地区水域生态系统服务评价体系  
Table 1Evaluation system for water ecosystem services in   

<table><tr><td colspan="3">Southwest China</td></tr><tr><td>准则层I(权重) Criterion layer I (Weight)</td><td>准则层ⅡI (权重) Criterion layer II (Weight)</td><td>指标层(权重、属性) Indicator layer(Weight, attribute)</td></tr><tr><td rowspan="2">供给服务 Supply services (0.498)</td><td>水源供给 (0.339)</td><td>土地类型供水能力 (0.164、正向） 距主要水源地距离 /m(0.109、正向) 土壤下渗度/%</td></tr><tr><td>食物供给 (0.159)</td><td>(0.066、正向） 淡水食物供给能力 (0.159、正向)</td></tr><tr><td rowspan="3">调节服务 Regulating services (0.257)</td><td>雨蓄调控 (0.135)</td><td>水域面积/km² (0.094、正向） 不透水面面积/km² (0.040、负向）</td></tr><tr><td>气候调节 (0.089)</td><td>夏季气温调节能力 (0.089、正向)</td></tr><tr><td>水体净化 (0.034)</td><td>植被覆盖度 (0.015、正向） 距湿地及湖泊距离 /m(0.019、正向）</td></tr><tr><td>支持服务 Support services (0.149)</td><td>生物多样性维护 (0.149)</td><td>生境质量(0.119、正向) 距主要道路距离/m (0.030、负向）</td></tr><tr><td>文化休闲服务 Cultural and leisure services (0.096)</td><td>游憩潜力 (0.096)</td><td>距城市中心距离/m (0.038、正向) 水体自然度 (0.058、正向)</td></tr></table>

结合西南地区生境条件，研究选取水源涵养、土壤保持、固碳储碳3项服务评价陆域生态系统服务，通过

InVEST模型的产水、土壤保持和碳储量模块计算。各因子经分级等权叠加得到陆域生态系统服务评价结果[31-32]。

2）基于耦合度模型的水陆耦合生态系统服务评价

耦合度是描述两个或两个以上系统交互作用和相互影响的程度[33]。研究构建水陆耦合生态系统服务评价模型，测度水陆耦合生态系统服务，以有效反映水陆生态系统相互作用对区域生态系统服务的影响。公式如下：

![](images/474080539dc247a04c6768d304e5b72b133bd2c7c95a33669449426fa073c67b.jpg)

式中C代表水陆生态系统服务耦合度。Ui、U分别为陆域和水域生态系统服务重要性评价指数，重要性评价指数通过计算生态系统服务并模糊隶属度获得。

# 1.3.2生态安全格局识别

根据“生态源地-生态阻力面-生态廊道-生态节点”的逻辑链，识别西南地区生态安全格局[34-35]。步骤包括：

1）生态源地提取。根据西南地区水陆耦合生态系统服务评价结果，选取水、陆域高值生态系统服务斑块及高耦合斑块作为生态源地（不包括零碎斑块）。

2）生态阻力面构建。采用阻力系数和修正因子构建。地类不同直接决定土地的生态功能，不同地类对生态目标的影响采取阻力累计的方式进行量化。植被覆盖是不同地类生态系统的组成要素之一，其高低并不直接等同于地类生态功能，如土壤对地类生态功能具有重要影响。结合已有研究，构建生态阻力面指标（表2)，权重通过层次分析法确定。西南地区山地占比高，城镇化地区多集中在平原，采用地形位指数和夜间灯光指数作为地形和工业城镇空间聚集影响作用的修正因子。公式如下：

![](images/ee009c29195528aaceaa153a5cdae983e702e433747d9f539e953c42d87a9e8c.jpg)

![](images/c82b5446cef34f2d9a9ed407c71a462cdc97bb85e3350ce3dffe859367cccee3.jpg)

![](images/5e4f5a0e57e1dd0e9bf354972de79c5c713c0a704c5c4358a7109cab1954db22.jpg)

式中Tj为栅格j的地形位指数；E和E分别为栅格j和研究区的数字高程，m；Sj和Sg分别为栅格j和研究区的坡度，（°)；Aj为将Tj及夜间灯光指数Lj加权修正后的指标；α、β为权重系数；Mj为修正后阻力值；A为栅格j对应的土地利用类型t的平均综合修正指标；M为栅格j在空间中某个方向上的阻力值。

3）生态廊道识别及生态夹点模拟。通过ArcGIS10.8 的Linkage Mapper插件，计算潜在生态廊道空间布局，利用电路理论模拟区域生态夹点。

表2西南地区生态阻力面指标  
Table 2Ecological resistance index in Southwest China   

<table><tr><td colspan="2">生态阻力面指标（权重）</td><td colspan="6">阻力值Resistance value</td></tr><tr><td></td><td>Ecological resistance surface index (Weight)</td><td>1</td><td>10</td><td>20</td><td>40</td><td>80</td><td>100</td></tr><tr><td>评价因子</td><td>土地利用类型（0.839）</td><td>林地</td><td>水域</td><td>草地</td><td>耕地</td><td>未利用地</td><td>建设用地</td></tr><tr><td>Evaluation factors</td><td>植被覆盖度(N(0.161)</td><td>丨</td><td>≥70</td><td>50~&lt;70</td><td>30~&lt;50</td><td>&gt;10~&lt;30</td><td>≤10</td></tr><tr><td>修正因子</td><td>夜间灯光指数(L)（0.614)</td><td>一</td><td>≤12</td><td>&gt;12~22</td><td>&gt;22~35</td><td>&gt;35~&lt;49</td><td>≥49</td></tr><tr><td>Correction factor</td><td>地形位指数(T(0.386)</td><td>≤2</td><td>&gt;2~5</td><td>&gt;5~8</td><td>&gt;8~11</td><td>&gt;11~&lt;14</td><td>≥14</td></tr></table>

# 1.3.3生态韧性评估

基于生态安全格局的生态韧性能够反映宏观尺度生态系统的结构和功能，识别其关键区域和薄弱环节。研究将生态韧性分为生态源地韧性、生态廊道韧性及生态夹点韧性[3。生态源地的生态韧性主要受生态源地大小、源地破碎度、源地外部连接性及源地间连通性影响。源地复杂性能增加源地内生态流路径的多样性，连通性直接影响着生态流的传输，源地内部的核心景观占比和集聚程度对源地生态韧性影响最大。生态廊道是保障生态服务流传输的通道，高连通性最好。此外廊道长度、宽度等属性，廊道距离人类活动密集区等外部环境也是影响廊道生态功能的重要因素。生态夹点是生态廊道上狭窄的关键区域，其面积、质量对生态流控制意义重大，河流阻断和人类活动也是通过影响其面积、质量等间接影响生态夹点的功能。综上，参考已有研究[14]，构建西南地区生态韧性评价体系（表3）。

采用层次分析法赋权，利用Fragstats 4.2、ConeforSensinode2.6和ArcGIS10.8分别计算生态源地内部及复杂性指数；源地、廊道及夹点的连通性指数；源地外部性因素、廊道及夹点的内外部因素。公式如下：

![](images/79d42a09588dc982b54fe47de10781120942333c17d5178e9343781ac63177e8.jpg)

式中R为生态韧性指数，Wi、Ri为第i个指标的权重和结果。

表3西南地区生态韧性评价体系  
[able 3Evaluation system of ecological resilience in   

<table><tr><td colspan="3">Southwest China</td></tr><tr><td>目标层 Target layer</td><td>准则层（权重） Criterion layer(Weight)</td><td>指标层(权重、属性) Indicator layer(Weight,Attribute)</td></tr><tr><td rowspan="6">生态源地韧性 Resilience of ecological sources</td><td>源地内部性 (0.367)</td><td>核心景观比(0.182、正向) 聚集指数（0.182、正向）</td></tr><tr><td>源地复杂性</td><td>景观形态指数(0.127、正向)</td></tr><tr><td>(0.253)</td><td>连续性指数（0.127、正向)</td></tr><tr><td></td><td></td></tr><tr><td>源地连通性 (0.246)</td><td>可能连通性指数(0.123、正向)</td></tr><tr><td>源地外部性</td><td>整体连通性指数（0.123、正向) 生态源地到道路距离(0.068、负向)</td></tr><tr><td rowspan="6">生态廊道韧性 Resilience of ecological corridors</td><td>(0.137)</td><td>生态源地到城市距离(0.068、负向)</td></tr><tr><td>廊道连通性</td><td>可能连通性指数（0.286、正向）</td></tr><tr><td>(0.572)</td><td>整体连通性指数（0.286、正向）</td></tr><tr><td>廊道内部性</td><td>生态廊道长度(0.136、负向)</td></tr><tr><td>(0.227) 廊道外部性</td><td>生态廊道质量 (0.091、正向)</td></tr><tr><td>(0.202)</td><td>生态廊道到道路距离 (0.101、负向)</td></tr><tr><td rowspan="5">生态夹点韧性 Resilience of ecological</td><td>夹点内部性</td><td>生态廊道到城市距离(0.101、负向)</td></tr><tr><td></td><td>生态夹点质量（0.293、正向）</td></tr><tr><td>(0.532)</td><td>生态夹点面积(0.240、正向)</td></tr><tr><td>夹点外部性</td><td>生态夹点到道路距离(0.234、负向)</td></tr><tr><td>pinch points</td><td>(0.468)</td><td>生态夹点到河流距离(0.234、正向)</td></tr></table>

# 2结果与分析

# 2.1水陆耦合生态系统服务评价

2.1.1水、陆域生态系统服务评价

将水域生态系统的供给、调节、支持和文化休闲4项生态系统服务，陆域生态系统水源涵养、土壤保持、固碳储碳3项生态系统服务各自按权重叠加，根据生态系统服务评价结果值划分重要性等级，均利用自然断点法划分为5类，水域/陆域生态系统服务划分为：一般区[0,0.149]/[0,0.148]、次重要区(0.149,0.219]/(0.148,0.256]、中重要区(0.219,0.286]/(0.256,0.338]、高重要区(0.286,0.437]/(0.338,0.416]和极重要区 (0.437,0.881]/(0.416,0.836]，得到西南地区水、陆域生态系统服务空间分布格局（图1、图2）。

![](images/9c38659204a27a457da18bc0bb5e6f06bb2b758374f5d46ff78e27b665b36265.jpg)  
图1西南地区水域生态系统服务空间分布格局

![](images/47819b5735574c593f0b1b4163d99d01160c8b1e32a1378f6f656839c9d879f6.jpg)  
Fig.1Spatial distribution pattern of aquatic ecosystem services in Southwest China   
图2西南地区陆域生态系统服务空间分布格局  
Fig.2Spatial distribution pattern of land ecosystem services in Southwest China

水域生态系统服务分布受水域空间分布的严格控制。低值区（一般区、次重要区）主要分布在四川盆地、云南东部、贵州西南部等。高值区（高重要区、极重要区）主要分布在川中南河网密集区、滇西高原湖泊群、黔东湿地群等地，总面积约2.33×10km²，占比20.66%，地类主要为林地、草地及水域，林地占比最高。供给服务高值区分布与河流走向基本一致。调节服务高值区较少，与大型水体分布重叠，低值区分布零散。支持服务分布呈现“西高东低”的特征。文化休闲服务多分布于城市周边。

陆域生态系统服务空间上呈现“东高西低”的特征。高值区主要分布在云南中西部热带季雨林及云贵高原、四川盆地西南部边缘、重庆大部及贵州中东部的丘陵区，面积约6.87×10km²，占西南地区的60.96%，其中林地占比74.94%。低值区主要分布在川西北、滇中东等地，以水域及未利用地为主，占比分别为49.21%、48.01%。水源涵养服务东西分布差异较大。土壤保持服务分布较为零散，高值区分布呈现“H”型，低值区分布较为广泛。固碳服务高值区分布广泛，与林地、草地空间分布基本一致，低值区主要分布在河谷及城市地区。

# 2.1.2水陆耦合生态系统服务评估

利用自然断点法对西南地区水陆域生态系统服务耦合度进行分级，分为未耦合区[0,0.197]、低耦合区(0.197,0.816]、中耦合区(0.816,0.910]、高耦合区(0.910,0.962]、极高耦合区(0.962,1]，得到西南地区水陆生态系统服务耦合等级空间分布（图3)，其空间异质性显著，整体呈“西高东低”的空间特征。极高耦合区总面积7.13×10' km²，占比62.55%，地类主要为林地、草地，占比分别为48.79%、34.77%，多分布在川西、滇中、黔中等地。高耦合区分布分散且面积占比较小。中耦合区主要分布在川东、黔中西、滇东南等地。低耦合或未耦合区占比很小，主要集中在大中型城市周边地区。

# 2.2基于水陆耦合生态系统服务的生态安全格局分析

# 2.2.1生态源地选取与生态阻力面构建

选取西南地区水、陆生态系统服务高重要区、极重要区和水陆生态系统服务高耦合区、极高耦合区的重叠区域作为生态源地，并提取生态源点（源地几何中心点）（图4)。生态源地主要分布在四川盆地西部边缘、四川西南部及云南北部的高山林区、云贵高原南部等，在重庆东南部、贵州北部也有少量分布。生态源地功能完整性及辐射范围受斑块面积影响显著，故剔除面积小于400 km²的生态斑块，识别出生态源地68块，总面积约1.00×10km²，其中单块最大面积为23483.03km²，平均面积为1470.78 km²，占区域总面积的8.85%。地类主要为林地，占比93.14%。经计算修正后的生态阻力面呈现以城市聚落为高阻力的空间分布特征（图4)。修正后阻力面的高值区、低值区分布差异显著，高值区主要分布在城市及周边地区。

# 2.2.2生态安全格局分析

西南地区生态安全格局呈现“两核心两带”的空间分布特征（图5）。

![](images/f1efd89ec69ded738cdb2cfc919f611f986e866ab619efa1fbfb23752928767e.jpg)  
图3西南地区水陆生态系统服务耦合等级空间分布Fig.3Spatial distribution of water and land ecosystem servicecoupling levels in Southwest China

![](images/5cfcdbb459e371238aef9d1f28666bf90823dc404a5060cba6fda48451169613.jpg)  
图4基于水陆耦合生态系统服务的西南地区生态源地及生态阻力面 3.4Ecological sources and ecological resistance surfaces in Southwest China based on water-land coupled ecosystem serv

![](images/a8c9b2b5ce72d089f9b840db6fdc83f10ccde39ea5da4615c18b8bff46afaefd.jpg)  
图5西南地区生态安全格局、生态韧性空间分布及其优化  
5Spatial distribution characteristics and ecological security patern, ecological resilience in Southwest China

“两核心”是以川西南、滇西北为中心的连片生态源地核心和以滇南为中心的分散生态源地次核心。“两带”是以渝南、黔北为核心和以四川盆地西部边缘为核心的两条生态廊道建设带。连片生态源地的完整性和连续性较高，生态服务供给能力强；分散生态源地的生态廊道较多且较长。“两带”生态廊道数量相对较少，生态夹点较多，生态源地破碎度高。

识别出生态廊道167条，总长16579.29km，最长为 831.18km，平均长度99.28km；生态夹点262个，总面积72.04km²，最大为2.41km²，平均面积0.27km²。生态廊道空间分布呈现“西密东疏、西短东长”的特征。生态源地在川西南部及滇西北部高山区分布集中，生态廊道较短且密集。川西边缘、渝东南及黔北生态源地面积较小且分散，廊道较长而稀疏。生态夹点主要集中分布在川西南、滇中等地，主要为林地、耕地及草地。

# 2.2.3基于生态安全格局的生态韧性评估及优化格局

基于西南地区生态安全格局和生态韧性评价体系（表3）进行区域生态韧性评估，根据生态韧性评价结果值，利用自然断点法划为5级。生态源地/廊道/夹点生态韧性划分为：极低韧性[0,0.083]/[0,0.157]/[0,0.334]、较低韧性(0.083,0.205]/(0.157,0.235]/(0.334,0.457]、中等韧性(0.205,0.304]/(0.235,0.303]/(0.457,0.572]、较高韧性(0.304,0.468]/(0.303,0.481]/(0.572,0.706]、极高韧性(0.468,1]/(0.481,1]/(0.706,1]，获得西南地区生态韧性空间分布特征（图5）。

西南地区生态源地韧性整体表现为“西高东低”的空间分布特征。高韧性（较高韧性、极高韧性）生态源地17块，面积占比25%。低韧性(较低韧性、极低韧性)生态源地26块，占比38.24%。受生态源地面积、连通性和形态等影响，高韧性生态源地呈现以云南西北部、四川西南部源地为核心的空间特征，该区生态源地面积大，完整性好。低韧性生态源地集中分布在重庆东南部及贵州北部等地，在云南北部及南部、四川中部有少量低韧性源地呈零散分布，该区源地面积小、破碎程度高。高韧性生态廊道34条，占比20.36%；低韧性生态廊道71条，占比42.51%。高韧性生态廊道呈现以四川盆地西南部边缘、云南西南部为核心的分布特征，低韧性生态廊道主要分布在四川西部高山区、重庆中部、贵州西部及云南东部等地。生态夹点韧性空间分布受生态廊道影响，主要分布在云南中西部、四川盆地西南部边缘，高低韧性分布集中。高韧性、低韧性生态夹点分别占比20.23%、44.66%。

基于区域生态韧性评估和区域自然、社会经济发展特征，提出了西南地区“三轴四区五核”的生态韧性优化格局（图5）。“三轴”分别为中部的“东-西主轴”、西北部的“东北-西南主轴”以及西南部的“南-北次轴”。主轴分别连接西部核心生态源地与东北部生态源地、西部连片生态源地与东部生态源地。次轴连接西部连片生态源地与南部破碎生态源地。“四区”即西部（川西南、滇西北）和西南部（滇西南）生态保护区，东北部（川东、渝西）和东南部（滇东北、黔西）生态修复区。西部、西南部生态保护区地形以高原、山地为主，水资源丰富，天然植被完整性好，区域人类活动干扰较小，生态源地分布集中且完整。东南部生态修复区喀斯特地貌发育强烈，土地石漠化、工程性缺水干旱等问题突出，生态环境敏感且脆弱。东北部生态修复区地形相对平坦，工农业发达，人类活动集中且强烈，生态系统受人类活动影响显著，生境破碎。“五核”即两个主核心及三个次核心，主核心为轴带之间的关键节点，次核心为生态安全的关键连接区，是西南地区“四区三轴”的生态格局的重要支撑点。

# 3讨论

# 3.1基于水陆耦合的西南地区生态系统服务分析

西南地区水域生态系统服务受水域空间分布特征限制。西南地区喀斯特作用强烈，地表地下水交换迅速，难以形成大型湖泊湿地，区域水域多为中小型水体为主。水域生态系统受人类活动影响显著，工农业生产的消耗及其衍生的水土流失、面源污染、废物排放等直接影响了水环境质量。水域文化休闲服务与城镇化空间分布特征基本一致，其主要受消费需求驱动[37]。

西南地区陆域生态系统服务空间分布受地形及气候条件等自然因素限制[38]。除四川盆地拥有广大的耕地外，其他平坦区主要分布在各类河谷区，在此基础上形成主要的农业生产和城镇化地区，因此，陆域生态系统服务低值区的工农业生产和城镇化等人类活动已成为该区域生态服务的主导影响因素。已有研究表明湿润气候与低人类干扰是陆域服务高值的关键驱动[39]。陆域生态系统服务极重要区分布在云南西双版纳热带季雨林、川西高山区、渝东北秦巴山区和渝东南武陵山区，该区人类活动干扰较弱，也证明了人类活动对陆域生态系统服务的重要影响。此外，西南地区壤发育缓慢，土层浅薄，群落生物量为146.32～190.92t/hm²，远低于同纬度非喀斯特区[40]。云贵高原高山区植被覆盖度较高，在陆域生态服务中属于高值区，但富钙碱性土壤对植被的选择性，削弱了生态系统的服务功能[41]。因而，在进行生态系统服务能力评估时，不仅要考虑区域植被覆盖水平，还须综合考虑生态系统的生产力。

西南地区水域数量众多，单体小且分散，形成了独特的水陆镶嵌结构，其水域与陆域林地、草地等的空间邻接紧密，影响了生态系统服务空间分布。水陆耦合研究弥补了传统研究中“水域-陆域割裂评估”的不足。不同类型生态系统耦合在地形复杂区对生态系统服务的影响更为显著[42]，这也验证了上述观点。因此，西南地区生态系统保护要充分考虑生境基底质量、生态系统生产力、生态系统稳定性以及水域、草地、森林等生态系统间的相互作用等，关注生态系统“结构-功能”的协同性。

# 3.2基于生态安全格局的西南地区生态韧性及其影响因素分析

西南地区生态韧性与生态安全的空间异质性表现基本一致，主要受生态源地、廊道和夹点的质量和空间结构影响。生态源地的完整性对区域生态韧性起着决定性作用[43]。西南地区生态源地完整性受地形、植被覆盖等自然因素及人类活动影响显著。崎岖地形及其导致的耕地破碎化，一定程度上造成了生态源地的破碎化。西南地区植被破碎化受喀斯特作用、二元水文结构以及高强度农业活动、城镇化建设和土地利用变化等因素的限制[44，也间接证明了前述结论。生态高韧性区的生态源地受人类活动干扰少，生态系统结构稳定，形成了以自然地形阻隔为基础的高抗干扰能力，有利于物质循环和生物迁移，增强了区域生态系统的调节能力。此外，地形植被等塑造的多样化生境为生物迁移提供了缓冲，多样的局部小气候增强了生态系统的适应性[20]。以四川盆地为核心的地区相对平坦、工农业发展水平高，人类活动干扰强烈且集中，区域内生态源地分散，生态廊道稀疏，生态韧性较低。人类活动强度是西南地区生态安全格局极其重要的影响因素[45]。地形阻隔与人类活动共同塑造了西南地区“西高东低”的生态韧性空间格局。

# 3.3西南地区生态韧性优化格局与策略

“三轴”生态韧性提升应以自然林为基础，通过人工封育、植树造林等措施，选取乡土藤蔓、草本、灌木和乔木混植，形成“藤-草-灌-乔”多层植被结构，提高生态系统稳定性。“四区”中，西部、西南部生态保护区自然环境基底较好，生态系统调节能力较强，生态源地分布集中，应减少资源开发及农业生产等扰动，以封育保护为主，并设立生态保护缓冲区，实施“社区共管”等，开展常态化巡护监测，提高生态韧性。东南部生态修复区地形破碎，喀斯特作用强烈，地质灾害频发，应采用“林-草-田”“农-牧-林”“生态-经果林复合经营”等多种模式，同时搭配集雨窖、沉砂池等小型蓄水工程，因地制宜开展生态修复建设。东北部生态修复区地势平坦，人口产业集聚，应基于零散山丘林地，实施坡耕地退耕，加强农田防护林带、生态经济林带、城乡绿地保护和微型生态源地建设。应提高城市边缘区环城绿带、农田防护林、湿地公园等的连通性，形成生态源地网。“五核”生态修复应在改善生态夹点功能的基础上，通过造林、退耕还林还草、小流域水土流失综合治理、生态经济林种植等措施，提高夹点生态连通性和稳定性，并设置监测点，开展生态退化预警。此外，应加大生态修复资金投入，加强跨区域生态补偿机制建设，推进跨区域协同治理，加强生态研学、生态保护公众参与等，形成多维度多主体的全社会生态保护氛围。

# 3.4研究局限性

该研究的水陆生态系统服务耦合度只反映了生态系统服务量在空间上的相互关联程度，未能体现其相互作用对生态系统服务的具体影响。未来可探究水陆生态系统镶嵌对服务供给的影响机制。基于源地、廊道、节点等生态安全格局要素的生态韧性空间分布特征，导致生态韧性的评估结果一定程度上依赖于构建生态安全格局的科学性。人类活动通常直接作用于小规模的生态源地、廊道、夹点等生态要素，而生态安全格局未能完全反映小尺度生态修复建设等对生态源地、廊道等的影响作用，即宏观的生态韧性优化格局与微观的生态修复累积效应的规模阈值未能明确。未来应从格网尺度开展生态系统服务价值和服务重要性的权衡，优化生态源地提取，结合样地监测，以体现小尺度生态修复的累积效应。

# 4结论

该研究以西南地区为例，基于水陆生态系统耦合开展西南地区生态系统服务评价、生态安全格局识别和生态韧性评估，分析了基于生态安全格局的生态韧性空间分异的主要影响因素，提出生态安全优化措施。主要结论如下：

1）西南地区水域生态系统服务分布受水域空间分布的严格限制，陆域生态系统服务空间上呈现“东高西低”的分布特征。水陆耦合生态系统服务空间异质性显著，整体呈“西高东低”的空间特征。极高耦合区占比62.55%,分布在川西、滇中、黔中等地，高耦合区相对分布分散，低耦合或未耦合区主要集中在大中型城市周边地区。

2）识别出生态源地68块，生态廊道167条，生态夹点262个。西南地区生态安全格局呈现“两核心两带”的空间分布特征。“两核心”是以川西南、滇西北为中心的连片生态源地核心和以滇南为中心的分散生态源地次核心。“两带”是以渝南、黔北为核心和以四川盆地西部边缘为核心的两条生态廊道建设带。

3）西南地区高韧性生态源地共17块，呈现以云南西北部、四川西南部源地为核心的空间特征；高韧性生态廊道共34条，呈现以四川盆地西南边缘、滇西南为核心的分布特征；生态夹点韧性呈现以滇中西、四川盆地西南部边缘为核心的空间特征，高低韧性分布集中。高韧性生态夹点占比20.23%。

4）西南地区生态韧性受地形地貌及人类活动等多种因素影响。构建了“三轴四区五核”的生态韧性优化格局，基于自然及人文影响因素，提出了山地丘陵水土保持、小流域水土流失综合治理等生态修复措施。

# [参考文献]

[1]LI S,WU J,GONG J,et al. Human footprint in Tibet: Assessing the spatial layout and effectiveness of nature reserves[J].Science of the Total Environment,2018, 621:18-29. [2] 白晓永，张思蕊，冉晨，等.我国西南喀斯特生态修复的 十大问题与对策[J].中国科学院院刊，2023，38(12)：1903-   
1914. BAI Xiaoyong, ZHANG Sirui, RAN Chen, et al. Ten problems and solutions for restoration of karst ecosystem in Southwest China[J].Bulletin of Chinese Academy of Sciences,2023,   
38(12):1903-1914.(in Chinese with English abstract) [3] LI W, KANG J, WANG Y. Effects of habitat fragmentation on ecosystem services and their trade-offs in Southwest China:A multi-perspective analysis[J]. Ecological Indicators, 2024,167:   
112699. [4]王韵秋，胡业翠，高梦雯，等.多维视角下广西喀斯特石 漠化地区国土空间生态修复分区[J].农业工程学报，2023, 39(1): 223-231. WANG Yunqiu, HU Yecui, GAO Mengwen, et al. Land-space ecological restoration zoning of karst rocky desertification areas in Guangxi from multi-dimensional perspectives[J]. TransactionsoftheChineseSocietyofAgricultural Engineering (Transactions of the CSAE),2023,39(1): 223-231. (in Chinese with English abstract)   
[5]SANNIGRAHI S,CHAKRABORTI S,JOSHI P K,et al. Ecosystem service value assessment of a natural reserve region for strengthening protection and conservation[J]. Journal of Environmental Management,2019,244: 208-227.   
[6] 兰永真，孙特生，李韦韦.陇东黄土高原农田生态系统服 务及其权衡协同关系[J].农业工程学报，2023，39(12)： 236-244. LAN Yongzhen, SUN Tesheng,LI Weiwei. Trade-offs and synergies of farmland ecosystem services in Loess Plateau: A casestudy of Longdong Region， Northwest China[J]. Transactionsofthe ChineseSocietyofAgricultural Engineering(Transactions ofthe CSAE),2023,39(12): 236-244. (in Chinese with English abstract)   
[7] 陈欣蔚，李红波，张文博，等.里下河地区土地利用转型 对生态系统服务价值的影响—基于 Markov-FLUS 模型的 多情景模拟分析[J].资源科学，2025，47(1)：182-195. CHEN Xinwei, LI Hongbo, ZHANG Wenbo,et al. The impact ofland use transition on ecosystem service value in Lixiahe area: Multi-scenario simulation based on Markov-FLUS model[J]. Resources Science,2025,47(1): 182-195.(in Chinese with English abstract)   
[8] 王世清，冀正欣，卢龙辉，等.张家口市林地与水源涵养 功能时空变化及其耦合关系[J].农业工程学报，2023, 39(10): 131-140. WANG Shiqing, JI Zhengxin， LU Longhui， etal. Spatiotemporal changes and coupling relationship between forestland and water conservation function in Zhangjiakou City of China[J]. Transactionsof the Chinese Societyof Agricultural Engineering(Transactions of the CSAE),2023, 39(10):131-140.(in Chinese with English abstract)   
[9]YIN D, YU H, SHI Y,et al. Matching supply and demand for ecosystem services in the Yellow River Basin,China:A perspective of the water-energy-food nexus[J]. Journal of Cleaner Production,2023,384:135469.   
[10]彭建，赵会娟，刘焱序，等.区域生态安全格局构建研究 进展与展望[J].地理研究，2017，36(3)：407-419. PENG Jian，ZHAO Huijuan,LIU Yanxu,et al. Research progress and prospect on regional ecological security pattern construction[J]. Geographical Research,2017,36(3): 407-419. (in Chinese with English abstract)   
[11]潘卫涛，岳邦瑞，姚龙杰，等.耦合风险与服务的市域生 态安全格局构建——以陕西省咸阳市为例[J].应用生态学 报，2023，34(1):178-186. PAN Weitao，YUE Bangrui，YAO Longjie，et al.Urban ecological security pattern construction coupled with risk and service:A case study of Xianyang City， Shaanxi Province, China[J]. Chinese Journal of Applied Ecology,2023,34(1): 178- 186.(in Chinese with English abstract)   
[12]孙枫，章锦河，王培家，等.城市生态安全格局构建与评

价研究：以苏州市区为例[J].地理研究，2021，40(9): 2476-2493. SUN Feng, ZHANG Jinhe,WANG Peijia, et al. Construction and evaluation of urban ecological security pattern: A case study of Suzhou city[J]. Geographical Research, 2021, 40(9): 2476-2493.(in Chinese with English abstract)   
[13]杨文越，叶泓妤.基于生境质量的粤港澳大湾区生态网络 识别[J].生态学报，2023，43(24)：10430-10442. YANG Wenyue,YE Hongyu. Identification of ecological networks in the Guangdong-Hong Kong-Macao Greater Bay Area based on habitat quality assessment[J].Acta Ecologica Sinica,2023,43(24):10430-10442. (in Chinese with English abstract)   
[14] 孙梓渊，王赛鸽，陈彬.基于生态系统服务的生态安全格 局构建与生态韧性评估——以长株潭城市群为例[J].生态 学报，2024，44(11):4650-4661. SUN Ziyuan，WANG Saige，CHEN Bin.Construction of ecological security pattern and assessment of ecological resilience based on ecosystem services: A case study of Changsha-Zhuzhou-Xiangtan urban agglomeration[J]. Acta Ecologica Sinica,2024,44(11): 4650-4661. (in Chinese with English abstract)   
[15] 朱振肖，柴慧霞，张箫，等.武夷山主峰黄岗山片区生态 安全格局构建研究[J].环境工程技术学报，2022，12(5): 1437-1445. ZHU Zhenxiao, CHAI Huixia, ZHANG Xiao,et al. Research on the construction of ecological security pattrn in Huanggang Mountain area, the Main Peak of Wuyi Mountain[J]. Journal of Environmental Engineering Technology,2022,12(5):1437- 1445. (in Chinese with English abstract)   
[16] 罗莎莎，赖庆标，王旭东，等.基于生态保护红线的生态 安全格局构建与国土空间修复分区[J].农业工程学报， 2024，40(7): 288-297. LUO Shasha，LAI Qingbiao，WANG Xudong， et al. Construction of ecological security pattern and land-space restoration zoning based on ecological protection red lie[J]. Transactionsofthe ChineseSocietyofAgricultural Engineering (Transactions of the CSAE),2024,40(7): 288-297. (in Chinese with English abstract)   
[17]王子琳，李志刚，方世明.基于遗传算法和图论法的生态 安全格局构建与优化—一以武汉市为例[J].地理科学， 2022，42(10): 1685-1694. WANG Zilin, LI Zhigang, FANG Shiming. Construction and optimization of ecological security pattern based on genetic algorithm and graph theory: A case study of Wuhan City[J]. Geographical Science,2022,42(10):1685-1694. (in Chinese with English abstract)   
[18]王争磊，乔家君，刘海龙，等.黄河中游地区生态安全格 局时空演变及优化策略[J].农业工程学报，2024，40(19): 231-239. WANG Zhenglei, QIAO Jiajun, LIU Hailong,et al. Spatiotemporal evolution and optimization strategy of ecological security pattern in the Middle Reaches of the Yellow River of China[J]. Transactions of the Chinese Society of Agricultural Engineering(Transactions ofthe CSAE),2024,40(19): 231-239. (in Chinese with English abstract)   
[19]晁云舒，严雨桐，闫思嘉，等.基于MCR 和重力模型的县 域生态安全格局构建——以福建省永春县为例[J].水土保 持通报，2023，43(4):203-210. CHAO Yunshu, YAN Yutong, YAN Sijia, et al. County scale ecological security pattrn construction based on MCR model: A case study of Yongchun County,Fujian Province[J]. Bulletin of Soil and Water Conservation,2023,43(4):203-210.(in Chinese with English abstract)   
[20] MCRAE B H, DICKSON BG, KEITT TH, et al. Using circuit theory to model connectivity in ecology，evolution，and conservation[J]. Ecology,2008,89(10): 2712-2724.   
[21]冯惠懿，赵春江，唐文正，等.生态安全格局视角下村庄 用地减量地块识别与分区[J].农业工程学报，2022，38(17)： 254-263. FENG Huiyi, ZHAO Chunjiang,TANG Wenzheng,et al. Recognition and zoning of the reduced plot of village land fromthe perspective of ecological securitypaten[J]. Transactionsofthe ChineseSocietyofAgricultural Engineering(Transactions ofthe CSAE),2022,38(17): 254-263. (in Chinese with English abstract)   
[22]HOLLING C S. Resilience and stability of ecological systems[J].Annual Review of Ecological System,1973,4: 1-23.   
[23]王松茂，牛金兰.山东半岛城市群城市生态韧性的动态演 化及障碍因子分析[J].经济地理，2022，42(8)：51-61. WANG Songmao, NIU Jinlan. Dynamic evolution and obstacle factors of urban ecological resilience in Shandong Peninsula Urban Agglomeration[J]. Economic Geography,2022,42(8): 51-61.(in Chinese with English abstract)   
[24] 王少剑，崔子恬，林靖杰，等.珠三角地区城镇化与生态 韧性的耦合协调研究[J].地理学报，2021，76(4)：973-991. WANG Shaojian,CUI Zitian,LIN Jingjie, et al. Coupling relationship between urbanization and ecological resilience in the Pearl River Delta[J].Acta Geographica Sinica,2021,76(4): 973-991.(in Chinese with English abstract)   
[25]彭文斌，邝嫦娥，李文意，等.长江中游城市群城市更新 与生态韧性空间关联网络及影响研究[J].地理科学，2024, 44(11): 1936-1945. PENG Wenbin，KUANG Chang'e,LI Wenyi,et al. Spatial correlation network and impactsof urban renewal and ecological resilience in urban agglomerations in the middle reaches of the Yangtze River[J]. Geographical Science,2024, 44(11): 1936-1945.(in Chinese with English abstract)   
[26] 肖圣，多玲花，邹自力.基于“风险-连通性-潜力”的南昌 市生态韧性评估[J].应用生态学报，2023，34(3)：733-741. XIAO Sheng，DUO Linghua, ZOU Zili. Assessment of ecological resilience in Nanchang based on“risk-connectivitypotential”[J]. Chinese Journal of Applied Ecology,2023,34(3): 733-741.(in Chinese with English abstract)   
[27] LEEMANS R，DE GROOT R S. Millennium Ecosystem Assessment:Ecosystemsand HumanWell-being:A Framework for Assessment[M].Washington: Island Press.2003.   
[28]侯志康，许民，康世昌，等.中国西北地区降水相态分离 及其变化分析[J].农业工程学报，2023，39(8)：120-132. HOU Zhikang,XU Min,KANG Shichang,et al. Separation and variation of precipitation forms in Northwest China[J]. Transactionsofthe ChineseSocietyofAgricultural Engineering (Transactions of the CSAE),2023,39(8):120-132. (in Chinese with English abstract)   
[29]鲍玉海，贺秀斌，尹飞虎，等.西南地区农业水资源利用 及雨水资源高效调控技术路径研究[J].中国工程科学， 2024，26(6): 169-180. BAO Yuhai, HE Xiubin, YIN Feihu, et al. Current situation of agricultural water resource utilization and technology path for the efficient regulation rainwater resources in Southwestern China[J]. Strategic Study of CAE,2024,26(6):169-180. (in Chinese with English abstract)   
[30] 黄羽，幸悦，孙晓玉，等.河湖水生态系统服务价值核算 研究及应用展望[J].水生态学杂志，2023，44(1)：1-8. HUANG Yu, XING Yue, SUN Xiaoyu, et al.Research and prospect of river and lake water ecosystem service value evaluation[J]. Journal of Hydroecology,2023,44(1):1-8.(in Chinese with English abstract)   
[31] 徐彩仙，巩杰，燕玲玲，等.甘肃白龙江流域土壤保持服 务供需风险时空变化[J].生态学杂志，2021，40(5)：1397- 1408. XU Caixian, GONG Jie, YAN Lingling, et al. Spatiotemporal changes of supply and demand risk of soil conservation servicesin Bailongjiang watershed, Gansu Province[J]. Chinese Journal of Ecology，2021，40(5):1397-1408.(in Chinese with English abstract)   
[32] 唐志雄，宁荣荣，王德，等.黄河三角洲滨海湿地碳储量 及其对未来多情景的响应[J].生态学报，2024，44(8): 3280-3292. TANG Zhixiong, NING Rongrong,WANG De, et al. Carbon stocks in coastal wetlands of the Yellow River Delta and their response to future multi-scenarios[J].Acta Ecologica Sinica, 2024,44(8):3280-3292.(in Chinese with English abstract)   
[33] 陈晓丽，朱思阳，孔雪松，等.湖北省乡村人一地一业时 空耦合的状态与动态特征[J].中国农业资源与区划，2021, 42(10): 31-38. CHEN Xiaoli, ZHU Siyang, KONG Xuesong,et al. Dynamic and static characteristics of spatiotemporal coupling among rural population, land,and industry in Hubei Province[J] Chinese Journal of Agricultural Resources and Regional Planning,2021，42(10):31-38.(in Chinese with English abstract)   
[34] QIAO Q, ZHEN Z,LIU L,et al. The construction of ecological security pattern under rapid urbanization in the Loess Plateau: A case study of Taiyuan city[J]. Remote Sensing, 2023,15(6): 1523.   
[35] CUI X，DENG W，YANG J，et al. Construction and optimization of ecological security patterns based on social equity perspective: A case study in Wuhan， China[J]. Ecological Indicators,2022, 136: 108714.   
[36] YUAN Y,BAI Z, ZHANG J, et al. Increasing urban ecological resilience based on ecological security pattern: A case study in a resource-based city[J]. Ecological Engineering, 2022,175: 106486.   
[37] 孙琨，钟林生，张爱平，等.城市生态游憩空间休闲价值 对比分析——以常熟市为例[J].地理研究，2016，35(2): 256-270. SUN Kun，ZHONG Linsheng，ZHANG Aiping，et al. Comparative analysis on the leisure values of urban ecological recreation spaces:A case study of Changshu city[J]. Geographical Research,2016,35(2): 256-270.(in Chinese with English abstract)   
[38] 刘小波，王玉宽，刘勤，等.基于城市化梯度的中国西南 地区生态系统服务权衡与协同[J].生态学报，2023，43(22): 9416-9429. LIU Xiaobo,WANG Yukuan,LIU Qin,et al.Ecosystem service trade-offs and synergies in Southwest China based on urbanization gradient[J].Acta Ecologica Sinica, 2023,43(22): 9416-9429.(in Chinese with English abstract)   
[39] 李美丽，尹礼昌，张园，等.基于MODIS-EVI的西南地区 植被覆盖时空变化及驱动因素研究[J].生态学报，2021, 41(3): 1138-1147. LI Meili,YIN Lichang，ZHANG Yuan,et al．Tradeoffssynergies analysis of ecosystem services along urbanization gradient in Southwest China[J].Acta Ecologica Sinica,2021, 41(3):1138-1147.(in Chinese with English abstract)   
[40]杨汉奎，程仕泽.贵州茂兰喀斯特森林群落生物量研究[J]. 生态学报，1991，11(4)：307-312. YANG Hankui, CHENG Shize. Study on biomass of the Karst forest community in Maolan,Guizhou Province[J].Acta Ecologica Sinica,1991,11(4): 307-312. (in Chinese with English abstract)   
[41]罗美，周运超，唐凤华.不同植被下碳酸盐岩石发育形成 土壤属性研究[J].中国岩溶，2023，42(2)：277-289. LUO Mei, ZHOU Yunchao, TANG Fenghua. Soil properties of carbonaterocksunderdifferentvegetationtypes[J]. Carsologica Sinica, 2023,42(2): 277-289.(in Chinese with English abstract)   
[42] XIONG S,YANG F.Ecological resilience in water-land transition zones: A case study of the Dongting Lake region, China[J]. Ecological Indicators,2024,166:112284.   
[43]彭建，李慧蕾，刘焱序，等.雄安新区生态安全格局识别 与优化策略[J].地理学报，2018，73(4)：701-710. PENG Jian,LI Huilei, LIU Yanxu,et al. Identification and optimization of ecological security pattern in Xiong'an New Area[J].Acta Geographica Sinica,2018,73(4): 701-710.(in Chinese with English abstract)   
[44] CHEN Y,CHENG C,XIONG K,et al.Quantifying the biodiversity and ecosystem service outcomesof Karst ecological restoration: A meta-analysis of South China Karst[J]. Catena,2024,245: 108278.   
[45]贺祥.生态系统服务供给安全阈值视域下喀斯特地区生态 安全演变[J].地理科学，2021，41(11)：2021-2030. HE Xiang. Study on the evolution of ecological security in Karst area based on the threshold of ecosystem services[J]. Geographical Science,2021,41(11):2021-2030.(in Chinese with English abstract)

# Identifying ecological security pattern and optimizing ecological resilience assessment for water-land coupling in Southwest China

CHENG Jialong1，ZHANG Junyi1,2※

(1.SchoolofGeogaphyandTourism,ChongqingNormalUniversityChongqing41331,China;.Chongqing CityKeyLabotoryof Surface Processes and Ecological Restoration in the Three Gorges Reservoir Area, Chongqing 401331, China)

Abstract:Ecological security hasdominated regional ecological stabilityinrecent years.In order toclarifytheecological security paternandecologicalresilience in Southwest China and maintainregional ecological security，this study takes Southwest China as anexample,uses InVEST,coupling degreemodel and other methods to quantify ecosystem services based on water-land ecosystem coupling,buildanecological securitypaternand evaluateitsEcologicalresilienceandpropose optimization strategies.Theresults showthatremarkable spatial heterogeneity was observed inthe ecosystem services of the water-landcoupling in Southwest China.There was theoverallpatern of "higher in the west and lower intheeast".The extremelyhighcoupling levelwas distributed intheregions likewestern Sichuan,central Guizhou,andcentral Yunan.While the low or non-existent coupling areas were around the large and medium cities.The patern of ecological security also presented a "two cores and two belts" spatial configuration. Onecore was thecontigous areas of ecological sources in southwestern Sichuan and northwestern Yunnan.The secondarycore of ecological sources was scatered in southern Yunnan. The "twobelts"were the eological corridors thatcenteredaround southern Chongqing andnorthern Guizhou,andthe western edgeof the Sichuan Basin，respectively.Specificall，17high-resilienceecological sourceswere concentratedaround Southwestern Sichuan and northwestern Yunnan.34 high-resilience ecological corrdors were distributed mainlyalongthe Southwestern edge of the Sichuan Basin and in southwestern Yunnan.Theresilience of ecological pinch points was centered around central and western Yunnan and the southwestern edge ofthe Sichuan Basin.There was aconcentrated distribution of thehighand lowresilience levels,where thehighlyresilient ecological pinch pointsaccountedfor20.23%.Anecological resilience patternwasoptimizedasthe"threeaxes,fourregions,andfivecores"alongwiththespecificstrategies.Theargeted measures werealsoproposed forecologicalrestoration,suchas soil and water conservationinthe mountainous andhillyareas. Soil erosionwas also prevented toconsiderthe naturaland humanactivities in thesmall watersheds.The water-land coupled ecosystem services were assessed to determine the impact ofthe interaction among diferent regional water-land ecosystem types on the ecological service supplyand ecological securitypatterns.Assuch,theecologicalsecuritypatern was further optimizedat aregional scale.Thefindingcan also provide ascientific basis to precisely implement ecological restoration and regional ecological security.

Keywords: ecosystem services; ecological security pattern; ecological resilience; water-land coupling; Southwest China