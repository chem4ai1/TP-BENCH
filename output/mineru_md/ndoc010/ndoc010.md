# 中国非光合植被覆盖度时空变化及其在气候梯度下对碳通量的影响

王春胜1,2,3，田庆久1,3\*，张文敏4 ，田家5\*，常莉莉6 ，张锐7 ，李前景1,3

1. 南京大学国际地球系统科学研究所，南京 210023  
2. 南京大学中国南海研究协同创新中心，南京 210093  
3. 南京大学江苏省地理信息科学与技术重点实验室，南京 210023  
4. 华东师范大学地理科学学院，上海 200241  
5. 北京航空航天大学仪器科学与光电工程学院，北京 100191  
6. 河海大学地球科学与工程学院，南京 211100  
7. 中国科学院西北生态环境资源研究院，兰州 730000  
\* 通讯作者，E-mail：tianqj@nju.edu.cn（田庆久），tianjia@buaa.edu.cn（田家）

2025-03-16收稿，2025-08-16修回，2025-09-19接受，2025-12-15网络版发表  
国家重点研发计划项目（2023YFF1303903）、青年人才托举工程项目（YESS20230043）、国家自然科学基金项目（42101321）和区域与城市生态安全全  
国重点实验室开放基金项目（SKLURE2023-2-6）资助

摘要 非光合植被（Non-Photosynthetic Vegetation，NPV）是陆地生态系统的重要组成部分，在植被与土壤碳交换等过程中发挥着关键作用。然而，现有的碳循环模型和遥感产品常将NPV误判为裸土，从而在碳通量模拟中引入结构性偏差。本研究基于Sentinel系列遥感影像和实地观测数据，构建了2016–2024年中国区域300 m分辨率的年尺度非光合植被覆盖度（f ）数据集。同时，提出了融合非光合植被、光合植被和裸土信息的生态系统碳交换通量（Ecosystem Car-bon Exchange Flux，ECEF）指数，为准确表征生态系统碳流动过程提供了新的方法。研究结果表明，2016–2024年间中国区域年均f 为0.3679，年均增长率为0.0014 a −1；在半干旱至半湿润气候区，f 达到了最高值（0.4235），年均增长率为0.0075 a −1。提升回归树（Boosted Regression Tree，BRT）分析显示，季度气温和降水是主导NPV空间分异的关键气候因子，分别解释了其变化的19.38%和15.22%。碳汇能力在不同气候区表现出显著差异，湿润区的碳汇能力明显高于干旱区，对应的ECEF值分别为0.95和−0.47。空间分析结果表明，ECEF与净生态系统交换量之间存在显著的负相关关系（Pearson r=−0.68，p<0.05，R 2 =0.46），表明ECEF可以作为气候梯度背景下碳通量估算的稳健代理指标。该研究强调了非光合植被在陆地碳循环中的核心作用，提出的ECEF为气候变化背景下的碳通量估算提供了重要的优化手段。本研究为全球，特别是观测数据稀缺区域的碳通量评估，提供了一条新的技术路径。

关键词 非光合植被，Sentinel卫星，碳通量，净生态系统交换，气候变化

# 1 引言

非光合植被（Non-Photosynthetic Vegetation，NPV）由枯枝、落叶、衰老茎秆及植物残体构成，与光合植被（Photosynthetic Vegetation，PV）共同构成植被生态系统的基本组成部分（Guerschman等，2009；Wang等，

2019）。光合植被通过光合作用实现碳的固定，非光合植被则主要参与有机碳的循环与再分配（Hu等，2011；Ver-relst等，2023）。非光合植被在调控大气、土壤和水圈之间的关键物质循环与能量流动中发挥着重要作用，但其在植被-土壤碳交换等生态功能上的作用常常被低估或忽视（Jackson和Prince，2016；Bai等，2024）。随着全球变暖和人类活动的不断加剧，植被层与土壤层之间的碳转移过程日益活跃，非光合植被已成为表征碳通量及揭示其动态变化的重要指标（Schile等，2013；Shen等，2021；Ma等，2024）。然而，现有的主流碳循环模型和土地覆盖产品常忽视或将非光合植被误判为裸土（Bare Soil，BS），从而导致碳通量估算存在显著偏差。因此，准确识别非光合植被对提高陆地碳循环评估的准确性和可靠性至关重要。

现有主流土地覆盖产品，如MODIS MCD12Q1、ESA CCI-LC、Copernicus全球土地覆盖和FROM-GLC等，普遍未能明确表征非光合植被，往往将其误分类为裸土、灌丛或农作物残茬等地类（Liu等，2021；Tsend-bazar等，2021；He等，2022；Yu等，2022）。这些产品依赖传统的分类体系（如IGBP和LCCS），但未将非光合植被作为独立成分进行优先考虑。由于非光合植被缺乏叶绿素且含水量较低，其光谱特性与裸土在可见光和近红外波段上高度相似，这使得遥感识别时容易混淆。此外，土壤性质的光谱差异进一步增加了分类的不确定性，使得准确区分非光合植被和裸土变得更加困难（Tian等，2023）。早期，区分非光合植被与裸土主要依赖高光谱成像技术，尤其是在1000–2500 nm的短波红外波段，通过纤维素吸收指数（Cellulose Absorption Index，CAI）、短波红外归一化残留指数（Shortwave InfraredNormalized Difference Residue Index，SINDRI）以及作物残留覆盖指数（Crop Residue Cover Index，CRCI）等光谱指数进行识别（Bai等，2021；Zhu等，2023）。然而，这些技术平台普遍存在时间分辨率低和数据获取受限的问题，限制了其在长期监测中的应用潜力（Liu等，2022）。近年来，基于非光合植被-裸土分离指数（NPV-Soil Separation Index，NSSI）以及更易获取的近红外卫星遥感数据（如Sentinel-2/3、WorldView-3、ZY-01、GF-5、EO-1 Hyperion等），显著提升了非光合植被覆盖度反演的可行性，尤其是在区域尺度和长期时间序列的监测中（Tian等，2021）。结合光谱指数三角特征空间的混合像元分解分析技术，能够有效提高光合植被、非光合植被和裸土三者面积比例（覆盖度）的区分精度，为跨生态系统尺度的非光合植被长期、大范围监测提供了技术支持。

非光合植被在全球陆地生态系统中不仅是土壤有机碳（Soil Organic Carbon，SOC）的关键来源，还作为物质循环和能量流动的重要载体，发挥着关键的生态功能（Verrelst等，2023）。非光合植被通过三种主要机制影响陆地碳通量。（1）影响有机质转移：非光合植被作为地表凋落物的主要成分，将有机质转移到土壤中，直接影响土壤表层的碳含量以及腐殖质的形成（Michopoulos等，2020；Õunapuu-Pikas等，2025）；（2）调节土壤呼吸：非光合植被通过释放二氧化碳等温室气体，从而影响大气中的碳浓度（Negash和Starr，2021）；（3）促进土壤碳汇：非光合植被输入土壤后，特别是易分解的部分，可能通过触发“启动效应”改变土壤微生物的活性和土壤化学成分，从而影响土壤碳库的稳定性（Wang和Huang，2020；Qiu等，2023）。这些机制在调节温室气体通量的同时，影响大气碳浓度并推动气候变化的进程。

然而，当前主流碳通量模型对非光合植被的显式表征能力仍有限。过程驱动模型（如Biome-BGC、LPJ、CLM和ORCHIDEE）通常未能有效整合能够反映非光合植被时空动态的遥感数据集（Pillai等，2019；Niu等，2021）。遥感驱动的模型（如MOD17、CASA、VPM和C-FIX）主要依赖绿色植被指数，仅估算光合活性部分的净初级生产力或总初级生产力，忽略了凋落物在碳循环中的重要作用（Wang等，2025）。尽管数据驱动方法（如FLUXCOM和DeepFlux）基于通量塔观测数据进行训练，但其使用的归一化植被指数（Normalized Difference Vege-tation Index，NDVI）等协变量或背景变异可能隐含了非光合植被的信号（Dou和Yang，2018）。这些方法尚未明确区分或解析非光合植被的功能作用，致使其在现有的大多数碳循环建模框架中依然被广泛忽视（Dennison等，2023）。为填补这一空白，亟需借助具备捕捉碳吸收与释放的动态平衡的光合植被、非光合植被和裸土体系，构建了一个既能反映碳汇潜力又揭示碳通量强度的综合性、稳健的指标。

本研究区横跨季风气候、温带大陆性气候和高山气候等多样气候区，植被类型丰富，为研究气候梯度下植被与气候相互作用提供了有利的条件（Cao等，2022；Ren等，2023）。基于这一生态异质性，本研究结合卫星遥感影像与实地观测数据，系统反演了2016–2024年间中国区域内非光合植被、光合植被及裸土的覆盖度（图1）。不同于传统模型仅聚焦光合植被，本研究首次将具有显著生态意义的非光合植被纳入碳通量评估体系，为全球碳通量观测稀缺或缺失区域的碳通量评估提供了有效的技术手段。研究主要聚焦以下三个方面：（1）揭示非光合植被覆盖度的时空动态及其驱动机制；（2）阐明非光合植被在陆地生态系统碳通量中的贡献与作用；（3）构建基于非光合植被、光合植被和裸土的稳健碳通量评估体系。本研究提出的遥感驱动框架，旨在提升生物量周转和碳交换过程的生态学真实性监测能力（Pugh等，2019；Wang等，2021），并可推广应用于全球气候过渡区，深化对气候梯度下生态系统碳通量响应机制的理解。

![](images/2f6538562c21f351b96c630e5b1b689dfe0f529dc9e7ccfe4cc2792d6bc3a003.jpg)  
审图号：GS京(2025)1623号  
图 1 非光合植被覆盖度反演及生态系统碳交换通量预测流程图

# 2 材料与方法

# 2.1 植被覆盖度反演的遥感产品

Sentinel-3卫星具备优化的光谱配置和广泛的时空覆盖能力，已成为开展大尺度非光合植被反演的理想遥感数据源。其约1400 km的宽幅扫描能力及高频次的重访周期，确保了观测数据的全面性与时效性，显著提升了时间序列的连续性和稳定性（Hu等，2019）。Sentinel-3配备了中心波长约820 nm、空间分辨率为300 m的近红外波段，增强了对植被结构的敏感性，便于计算如NSSI和NDVI。这些指数采用了对观测角度不敏感的光谱波段组合（如红光和近红外波段），有效缓解了由观测视角变化引起的地表反射率波动。基于NSSI和NDVI的像元线性解混过程受非线性效应影响极小，适合精确反演非光合植被、光合植被及裸土的地表覆盖度。Sentinel-3在温带森林、高山草甸及干旱草原等多样生态系统中均表现出稳定可靠的反演性能，展现了在不同生态环境下的稳健性与可迁移性。与此同时，Sentinel-2卫星具有高空间分辨率（10–20 m）的多光谱观测能力，覆盖了从可见光到短波红外的多个波段，有效满足全球陆地生态监测的多样化需求（Guerini等，2020）。Sentinel-2具备783和865 nm的波段，支持NSSI和NDVI指数的计算。其Level-2A产品经过Sen2Cor大气校正和双向反射分布函数（BidirectionalReflectance Distribution Function，BRDF）校正，显著减弱了影像中的角度效应（Li等，2018），使其在复杂地理区域的环境监测中表现优异，能够满足多样化生态系统的高精度观测需求（Fernandez-Beltran等，2019）。

中国的气候存在显著的区域异质性，导致不同生态系统中非光合植被的峰值时段存在明显的时序差异（Zhang等，2022）。为确保遥感影像在时间和光谱上的一致性，本研究遵循以下三项原则进行影像选取（网络版附表S1）。首先，影像采集时间应与区域物候相匹配，以确保选定的观测数据能够准确反映各气候区非光合植被覆盖的季节性峰值。具体来说，华北、东北和西北地区的影像采集时间定在9月底至10月初；西南地区则集中在9月至10月；华东和华中地区的最佳成像时间为11月，而华南地区则为12月。其次，仅保留云覆盖率低于10%的影像，云覆盖程度依据Sentinel-3 Level-1产品中的亮度像元进行判断。为进一步减少云的影响，本研究采用像素级云掩膜处理，并结合同期多时相观测数据进行合成，最大限度保留识别非光合植被所需的关键物候信号。最后，对于长期云覆盖或缺失观测数据的区域，特别是西南地区及高纬度多雪区域，本研究采用多时相合成技术，在区域物候峰值为中心的16–30天时间窗口内，从多幅卫星影像中筛选出最优的无云观测数据。对于残留的空缺区域，辅以Sentinel-2影像进行填补，以确保时空覆盖的完整性。补充数据采用Sentinel-2 Level-2产品，并通过重采样至300 m空间分辨率，以保证与Sentinel-3产品在空间尺度上的一致性。

Sentinel影像通过欧洲航天局（European SpaceAgency，ESA）官方渠道下载。在影像筛选过程中，依据元数据排除太阳天顶角大于60°或卫星观测角超过20°的Sentinel影像，以最大限度减少观测视角效应对数据质量的影响（Montenbruck等，2018）。此外，Sentinel-3影像需利用输入几何信息及地理查找表等已知几何参数进行初步校正和重投影，以确保影像的空间定位精确和几何一致性。随后，对Sentinel-3影像进行辐射定标、大气校正以及正射校正等预处理操作。上述处理均在ENVI5.6软件中完成。处理后的影像覆盖整个研究区域，并用于中国范围内NPV、PV及BS的反演分析。

# 2.2 实地观测数据

为验证非光合植被覆盖度的反演结果并支持生态系统碳交换通量建模，本研究整合了多源实地观测数据集，包括无人机影像、Google Earth影像和国家监测网络的长期生态观测数据（网络版附图S1a）（Liu等，2022）。自

2019年以来，在中国多个生态样区开展了无人机对地观测实验，涵盖华北（农田与落叶阔叶林）、西北（灌丛）、西南（高山草甸）、华东（亚热带常绿阔叶林）及华南（热带雨林、季雨林）等区域。实验区的选取充分考虑了气候、地形和土地覆盖差异，旨在代表中国干旱、半干旱、半湿润和湿润等主要气候区（Tian等，2023）。为了提高空间代表性，研究进一步整合了2020–2023年间的GoogleEarth历史影像，综合构建了亚米级覆盖度验证数据集（Liu等，2020）。所有可用的亚米级影像均选取于非光合植被的峰值期，涵盖了不同气候梯度和年份的高分辨率地表结构数据（表1）。经过地理配准、投影转换和重采样处理后，所有亚米级影像均被标准化至0.15 m的空间分辨率，所对应的像素视为纯像素。同时，采用10 m空间分辨率的Sentinel-2影像作为辅助验证数据。亚米级影像和Sentinel-2影像均基于监督式马氏距离分类方法划分为NPV、PV和BS三类。针对每个Sentinel-3像素，统计其对应区域内的分类像素数量并进行归一化，从而计算各类别的覆盖比例，并生成与产品空间分辨率相匹配的验证指标。

森林生物数据集包括通过样方调查获得的林分草本层、灌木层和乔木层的物种组成信息；草地生物数据集则包含草本层的物种组成及其鲜重和干重的测量数据（表1）。土壤数据来自森林和草地剖面，涵盖五个土层深度0–10、10–20、20–40、40–60和60–100 cm，重点测定土壤有机质含量（网络版附图S1b）。数据经清洗与整合后，与非光合植被覆盖度数据在时间和空间尺度上精确匹配，从而用于生态系统碳通量分析与建模。针对部分站点多年采样引起的时间自相关问题，本研究采用年度平均值进行处理。具体方法为：每年计算验证指标，并取其平均值，确保统计结果的独立性，避免多年份数据比较中的伪重复效应。

# 2.3 生物量遥感数据产品

为研究生态系统碳交换通量的空间格局，本研究整合了多项长期遥感数据集，重点关注生态系统中的三个主要动态碳库：生物量碳、凋落物碳（Litterfall Carbon，

表 1 亚米级影像及地面观测数据集参数  

<table><tr><td>数据集</td><td>数据源</td><td>时间跨度</td><td>原始分辨率</td><td>应用分辨率</td><td>应用目的</td></tr><tr><td>UAV影像</td><td>现场实验</td><td>2019-2023年</td><td>1-1.5 cm</td><td>0.15 m</td><td rowspan="2">反演结果验证</td></tr><tr><td>Google Earth影像</td><td>Google Earth地图</td><td>2020-2023年</td><td>~15 cm</td><td>0.15m</td></tr><tr><td>森林生物数据集</td><td>NSTI</td><td>2004-2021年</td><td>~0.25 m²</td><td>100 m²</td><td>森林结构</td></tr><tr><td>草地生物数据集</td><td>NSTI</td><td>1998-2021年</td><td>~0.25 m²</td><td>100 m²</td><td>草地结构</td></tr><tr><td>土壤养分数据集</td><td>NSTI</td><td>2004-2020年</td><td>~0.25m²</td><td>100m²</td><td>土壤有机碳</td></tr></table>

LC）和土壤有机碳（Soil Organic Carbon, SOC）。森林生态系统的凋落物碳数据来源于针对性构建的森林凋落物碳密度数据集。草地生态系统则采用了分别适用于华北温带草原和青藏高原高山草甸区域的两套地上生物量数据集。草地凋落物碳则通过实地测定的凋落物碳与地上生物量之间的经验关系进行估算（网络版附图S2）。土壤有机碳数据来自全球1 km空间分辨率的土壤有机碳库数据集。土壤呼吸（Soil Respiration，SoiR）数据来源于可获得的地面观测记录，涵盖全球主要气候区的数据。此外，本研究还纳入了全球5 km分辨率的月度净生态系统交换量（Net Ecosystem Exchange，NEE；网络版附图S3）数据，以支持更全面的碳平衡评估。在驱动因子分析时，所有数据的空间分辨率均统一至0.05°，碳变量以吨/公顷（t ha −1）为计量单位。通过上述数据集的融合，构建了综合的生物量碳通量评估框架，实现了对多样化生态系统碳储量与通量的多源协同分析。

# 2.4 其他补充数据

本研究主要采用的气象数据集为ERA5（网络版附图S4a–S4d），具体包括ERA5 DAILY提供的逐日气候重分析生产的2 m气温（Temperature，TEM）和降水量（Precipitation，PRE）数据集。土壤含水量（Soil Moisture，MS）数据来源于全球0.1°分辨率的地表土壤湿度数据集，提供月尺度的土壤含水量信息，单位为m 3 m −3（网络版附图S4e，S4f）。光合有效辐射吸收分数（Fraction of Photosynthetically Active Radiation，FPAR）产品具有500 m的空间分辨率，用于表征植被对光能的利用能力（网络版附图S4g，S4h）。太阳辐射（Solar Radiation，SR）数据来自全球地表太阳辐射数据集，空间分辨率为10 km，单位为W m −2（网络版附图S4i，S4j）。太阳激发叶绿素荧光（Solar-Induced Fluorescence，SIF）数据则采用神经网络生成的全球连续SIF产品，具备0.05°的空间分辨率（网络版附图S4k，S4l）。为分析非光合植被覆盖度变化的驱动因子，上述气候与辐射类数据均按年度（Annual，AN）与季度（Quarterly，QU）尺度进行划分，并与各区域非光合植被峰值发生时段相对应。此外，本研究还整合了海拔高度（Above Sea Level，ASL）与土壤黏粒含量（Soil ClayContent，SCC）等地形与土壤属性数据（网络版附图S4m，S4n）。地表反射特性采用500 m空间分辨率的MCD43A3短波波段黑天反照率数据集（Albedo；网络版附图S4o）进行约束。水分通量评估则基于中国区域1 km分辨率的月尺度潜在蒸散量（Potential Evapotranspiration，PET）数据集（网络版附图S4p）。上述所有数据均被系统整合入评估框架，保障多源信息的协调融合与综合分析能力（表2）。

# 2.5 基于遥感数据的覆盖度反演方法

本研究利用多光谱遥感数据，定量反演了陆地生态系统中的非光合植被覆盖度（f NPV），并同步提取了光合植被与裸土的覆盖度（f PV，f BS）。通过分析实验室实测的PV、NPV与BS光谱数据的导数光谱曲线，揭示了三类地表组分在820 nm波段的细微光谱响应差异（Tian等，2021）。各类遥感影像所用的光谱波段中心波长详见表3。为进一步开展NSSI构建的初步分析，本研究引入了ENVI最新扩展的光谱库，并结合ICRAF-ISRIC与ECOSTRESS等权威光谱数据库中的地物光谱数据，深入探讨了NPV与BS之间的光谱差异（Aitkenhead和Black，2018；Meerdink等，2019）。考虑到中国幅员辽阔、植被类型多样的特点，本研究进行了全国范围的地表光谱测量，系统评估了该指数在不同生态区域中的适用性与泛化能力。本研究的地面光谱数据采集覆盖了华北、西北及华东等典型区域（网络版附图S1a）。测量使用了ASD FieldSpec-4光谱辐射计，采集了350–2500 nm波段范围内的地表反射率数据，为后续植被指数的构建与验证提供了关键支持（Janse等，2018）。NSSI与NDVI的定义见公式（1）与（2）。基于NDVI-NSSI的指数三角空间法能够同步反演混合反射像元中不同组分的覆盖度（Guerschman等，2009）。在三角空间法中，假设每个像元由PV、NPV和BS三种地表组分按线性比例混合，这三种组分分别对应三角空间图的三个端元顶点。该模型的核心假设是三类组分的覆盖度之和为1，确保了像元组成的物理合理性与数学一致性。通过构建三角空间模型，可以有效分解各组分对像元反射的贡献。模型精度通过均方根误差（RootMean Square Error，RMSE）和决定系数（Coefficient ofDetermination，R 2 ）进行评估（详见网络版附表S2），参考数据包括亚米级影像及Sentinel-2数据集。根据既定方法，使用公式（3）–（5）分别估算PV、NPV和BS的覆盖度。

![](images/9b692e9c5cafe1c6365800c568856c777f84bd03d96a015b3129c88499df6882.jpg)

![](images/e5167ce576ddd6e92f0df85a93ca8c470e129b129770c1b9abe67e2379e6fb95.jpg)

其中，R right和R left分别代表中心波段820 nm两侧的波段。对于Sentinel-3，R right和R left可分别选用865和779 nm波段，而Sentinel-2则分别对应865和783 nm波段。R nir和R r分别表示近红外波段和红光波段的反射率，其中Sentinel-3的近红外波段为865 nm，Sentinel-2为842 nm，红光波段统一采用665 nm，以确保波长一致性。

![](images/641c5533968a335062ca3377b74b538e460f11b62088de3cedef3b2464f41170.jpg)

表 2 涉及非光合植被覆盖度反演和分析的遥感产品参数 a）  

<table><tr><td>数据集</td><td>数据源</td><td>时间跨度</td><td>原始分辨率</td><td>应用分辨率</td><td>应用目的</td></tr><tr><td>Sentinel-3</td><td>ESA</td><td>2016-2024年</td><td>300 m</td><td>300 m</td><td>非光合植被 覆盖度反演</td></tr><tr><td>Sentinel-2</td><td>ESA</td><td>2016-2024年</td><td>10-20 m</td><td>300 m</td><td>辅助数据; 反演结果验证</td></tr><tr><td>森林凋落物碳</td><td>TPDC</td><td>1982-2020年</td><td>0.05°</td><td>0.05°</td><td>森林碳估计</td></tr><tr><td>高山草甸 地上生物量</td><td>TPDC</td><td>2000-2020年</td><td>1 km</td><td>0.05°</td><td>草地碳估计</td></tr><tr><td>温带草原 地上生物量</td><td>NESDC</td><td>2000-2020年</td><td>30 m</td><td>0.05°</td><td></td></tr><tr><td>土壤有机碳</td><td>NESDC</td><td>1981-2019年</td><td>1 km</td><td>0.05°</td><td>土壤有机碳估计</td></tr><tr><td>土壤呼吸</td><td>NESDC</td><td>2000-2020年</td><td>1 km</td><td>0.05°</td><td>土壤呼吸分析</td></tr><tr><td>净生态系统 交换量</td><td>NESDC</td><td>2000-2020年</td><td>5 km</td><td>0.05°</td><td>ECEF结果验证</td></tr><tr><td>气温</td><td>GEE</td><td>1981-2023年</td><td>0.25°</td><td>0.05°</td><td rowspan="8">非光合植被时空变换变 化的决定因素分析</td></tr><tr><td>降水 光合有效辐射</td><td>GEE</td><td>1981-2023年</td><td>0.25°</td><td>0.05°</td></tr><tr><td>吸收分数</td><td>GEE</td><td>2000-2023年</td><td>500 m</td><td>0.05°</td></tr><tr><td>太阳激发 叶绿素荧光</td><td>TPDC</td><td>2000-2022年</td><td>0.05°</td><td>0.05°</td></tr><tr><td>太阳辐射</td><td>TPDC</td><td>1983-2018年</td><td>10 km</td><td>0.05°</td></tr><tr><td>土壤湿度</td><td>NESDC</td><td>2000-2020年</td><td>0.1°</td><td>0.05°</td></tr><tr><td>海拔</td><td>NESDC</td><td>1</td><td>0.05°</td><td>0.05°</td></tr><tr><td>土壤黏粒含量</td><td>NESDC</td><td>1</td><td>0.05°</td><td>0.05°</td></tr><tr><td>地表反射率 潜在蒸散量</td><td>NESDC NESDC</td><td>1981-2020年 1901-2023年</td><td>500 m 1 km</td><td>0.05° 0.05°</td><td></td></tr></table>

a） ESA，欧洲航天局（European Space Agency）；GEE，谷歌地球引擎（Google Earth Engine）；NSTI，国家科技基础设施（National Science &Technology Infrastructure）；TPDC，国家青藏高原数据中心（National Tibetan Plateau Data Center）；NESDC，国家地球系统科学数据中心（NationalEarth System Science Data Center）

表 3 Sentinel-2与Sentinel-3影像中用于构建NSSI及NDVI的光谱波段信息  

<table><tr><td>Satellite</td><td>Rright</td><td>Rleft</td><td>Rnir</td><td>R</td></tr><tr><td>Sentinel-3</td><td>Oa17</td><td>Oa16</td><td>Oa17</td><td>Oa8</td></tr><tr><td>Sentinel-2</td><td>B8A</td><td>B7</td><td>B8</td><td>B4</td></tr></table>

f = 1i i = PV, NPV, BS

其中，三个覆盖度参数f 、f 和f 需要通过求解获得。NDVI 、NDVI 、NDVI 分别表示三种端元的NDVI值，NDVI M表示混合像元的NDVI值；同理，NSSI PV、NSSI NPV、NSSI BS表示三种端元的NSSI值，NSSI M表示混合像元的NSSI值。所有端元的覆盖度范围限定在0–1之间。

# 2.6 陆地生态系统碳通量模型

本研究提出的ECEF指数结合了遥感反演的植被组分数据与碳循环理论框架，旨在定量描述陆地生态系统碳通量的时空变化特征。该指数综合考虑了光合植被、非光合植被和裸土三种功能组分在碳固定、凋落物转化及土壤呼吸过程中的关键作用，基于遥感可观测变量，构建了一个以生态过程为驱动的碳通量表征指标（Saba等，2021）。在自然生态系统中，碳主要储存在三个碳库中：生物量碳、LC及SOC。这三大碳库通过植物生命周期和土壤呼吸等生态过程紧密相连，共同构成陆地碳循环的核心机制。活体生物碳通过植物光合作用逐步积累，随着植物衰老或死亡，转化为非光合植被的凋落物碳，并在微生物分解作用下，进一步转化为土壤有机碳或释放为二氧化碳，从而驱动陆地生态系统中碳的输入与输出（Isson等，2020）。尽管凋落物碳库的总体规模较小，但其碳周转速率极高，在短周期碳循环中扮演着至关重要的角色。通过微生物的快速分解作用，凋落物将碳迅速释放至土壤和大气中，有效驱动土壤呼吸过程（Zhang等，2021）。

非光合植被在碳循环中扮演着至关重要的角色。它不仅标志着生物量从碳固定转向碳释放的临界阶段，还连接了生物量碳库和土壤碳库，起到了调控碳汇与碳源之间的桥梁作用。在本研究构建的生态系统碳交换通量指数中，明确将非光合植被的作用纳入碳循环模型。光合植被代表了碳固定的核心，体现了生态系统的碳汇潜力和光合作用效率，而非光合植被则代表衰老或死亡的植物组织，是凋落物碳积累的起点。该模型准确地刻画了非光合植被在碳循环中的双重作用：一方面，非光合植被的快速分解促进了有机质向二氧化碳的转化，显著增强了碳的流动性和短期释放速率；另一方面，非光合植被进入土壤后，可激发“激发效应”，显著活跃微生物活动，促进腐殖质合成，从而增强土壤碳库的稳定性和长期储存能力（Lees等, 2018）。ECEF不仅整合了光合植被、非光合植被和裸土的覆盖度（f PV、f NPV、f BS）考虑了其年际变化趋势（Δf PV、Δf NPV、Δf BS），从而实现了对碳库结构与时间演变的双重刻画，能够量化碳相关地表组分的结构组成和动态过程。

![](images/a058c9788a01b693a46b29e29f6af80af1e2aff832e1e81a705f664d6899fc04.jpg)

其中，f PV、f NPV、f BS分别表示光合植被、非光合植被和裸土的覆盖度，Δf PV、Δf NPV、Δf BS表示上述三类组分覆盖度的年际增长率。公式中的第一项描述了陆地生态系统碳通量的空间结构特征，即不同功能组分在地表的分布格局，反映生态系统当前的碳储量状态与碳库构成；第二项则刻画了碳库的动态演变过程，表征各组分在年际尺度上的变化趋势，捕捉碳输入与输出过程的方向与强度。这两部分因子的数值均归一化至（−1，1）之间，因此ECEF的整体取值范围为（−2，2），覆盖了从强碳汇状态（正值）到强碳源状态（负值）的生态系统碳交换动态。

为评估ECEF的生态适用性，本研究将其时空变化趋势与NEE进行了对比分析，考察了二者在空间和时间上的变化模式。为提高验证结果的代表性和稳健性，NEE数据按生态系统类型和气候区分组，以减少年度观测值之间的时间自相关性影响（Fu等，2019）。研究的关键进展包括如下三个方面。（1）功能组分整合：首次将光合植被、非光合植被和裸土的时间变化趋势纳入碳通量指数，实现了碳通量对环境变化的动态响应。（2）双因子结构：提出了同时考虑生态系统结构特征与演变轨迹的双因子结构，使得碳通量估算能反映当前状态与发展方向。（3）跨气候与多源验证：通过跨气候梯度和多源碳监测数据的验证，增强了ECEF模型的空间适应性和广泛性。这些创新显著提升了ECEF模型在气候变化背景下进行大尺度生态系统碳通量评估的潜力。需要指出的是，本研究的目标并非精确预测逐年碳通量，而是通过统计建模提取生态系统变化的整体模式和关键过程，从而加强对生态系统响应规律的理解。

# 2.7 提升回归树算法

提升回归树（Boosted Regression Tree，BRT）算法通过迭代构建多个回归树模型，以逐步优化整体预测性能（Shabani等，2020）。每一轮新树拟合上一轮模型的残差，通过对先前预测误差较大的样本赋予更高权重，持续减小模型预测值与观测值之间的偏差（Vidal-Macua等，2020）。在本研究中，基于BRT方法评估了影响f NPV空间变异的环境变量的重要性，并进一步开展部分依赖分析。通过剔除其他变量干扰，以揭示各驱动因子对f 变化的独立响应模式。为兼顾短期气候波动的平滑处理与空间梯度信息的保留，所有驱动因子与响应变量均采用较宽时间窗口（如3年滑动均值）进行均值化处理。该分析框架为深入理解不同气候区中非光合植被动态的主导控制机制提供了稳健且具可解释性的定量依据，揭示多重环境因子对非光合植被覆盖度时空变异的综合影响。

# 2.8 多元回归分析

本研究采用线性回归方法识别中国范围内f NPV、f PV与f 的变化趋势（详见第3.2节），并通过Mann-Kendall检验评估趋势的统计显著性（Gadedjisso-Tossou等，2021；Dhole等，2023）。在此基础上，结合不同植被类型的野外观测数据，构建了一个凋落物碳与f 之间的经验模型，量化非光合植被在碳输入过程中的作用。接着，采用多元线性回归分析，探讨三类地表功能组分（f NPV、f PV与f ）与各类碳库变量之间的相关性（详见第3.4节）。由于研究所用的遥感数据涵盖了2016–2024年的多个年份，且同一地点存在重复观测，这可能引入时间序列中的非独立性问题。为了减轻时间自相关对统计结果的影响，研究采取了以下策略：（1）大部分统计分析基于年度均值或年变化率，而非逐年原始值，以减少时间序列的相关性；（2）趋势分析侧重于变化方向与空间相关性，而非单一数据点的显著性检验；（3）通过在较大空间单元（如生态区或气候区）尺度上汇总数据，有效抑制局部噪声与年际波动，增强模式识别的稳健性。该方法体系在保持时序信号的同时，有效控制了时间非独立性问题，为后续碳通量动态模拟与驱动机制分析提供了可靠的统计基础。

# 3 实验结果

# 3.1 非光合植被覆盖度估算与精度评估

本研究基于Sentinel-3影像和Sentinel-2数据，采用NDVI-NSSI三角空间法估算了中国区域最大年度f NPV，生成的产品空间分辨率为300 m。与此同时，还提取了光合植被和裸土的覆盖度数据。模型精度通过与野外亚米级影像和独立Sentinel-2影像的对比评估，使用RMSE和R 2 指标（见网络版附表S1）。采样点的空间分布见网络版附图S1。使用不同空间分辨率的验证数据集有助于全面评估f 的反演准确性。结果表明，基于亚米级影像的RMSE为0.042，而Sentinel-2影像的RMSE为0.035，可能受到空间尺度效应的影响。尽管如此，亚米级影像和Sentinel-2影像的R 2 别为0.741和0.784，显示三角空间法能较为准确地反演中国区域f 。结合绿色植被指数与非光合植被指数（见网络版附表S2），本研究生成了2016–2024年中国区域最大年度f NPV产品，为后续的生态系统碳通量和植被动态研究提供了重要基础。

# 3.2 中国非光合植被的时空分布格局

非光合植被覆盖度的时空变化在不同气候区表现出显著差异，并呈现明显的垂直分带的特征（图2a）。中国的主要气候区包括干旱区（Arid Region，R A）、半干旱至半湿润区（Semi-arid and Sub-humid Region，R S）以及湿润区（Humid Region，R H）。在2016–2024年期间，年度f NPV、f PV（网络版附图S5a）及f BS（网络版附图S5b）被分为五个等级（I–V），分别表示覆盖度变化的从低到高水平（详见网络版附表S3）。

中国年均f 为0.3679，其分布呈现纬度和经度双重梯度特征（图2a）。基于三大主要气候区的分布特点，图2b展示了年均f NPV沿纬度的变化趋势。从湿润区到半干旱至半湿润区，年均f 逐渐上升；而从半干旱至半湿润区到干旱区则逐渐下降，年均值分别为0.3192、0.4235和0.3313（图2c）。如图2d所示，干旱区的主要f 类型为Ⅲ型，占51%。该区域主要为温带沙漠生态系统，植被覆盖度较低。半干旱至半湿润区为干湿气候的过渡带，涵盖温带草原、高山草甸和温带落叶阔叶林等生态系统，其中Ⅲ型f NPV占据最大面积比例（59%），其次为Ⅳ型（23%），共同构成该区域的主要非光合植被覆盖类型。在该区，内蒙古高原、黄土高原和青藏高原东部地区的年 均f NPV显著高于该区平均水平。在湿润区，Ⅱ型与Ⅲ型年均f 类型面积比例相近，占比接近41%。该区主要涵盖华东及华南的季风气候区，典型植被包括常绿阔叶林、热带雨林与季雨林，年均f 表现出由北向南递减的趋势。图2a显示，东北地区的年均f 以Ⅲ型为主，而湿润区Ⅴ型分布较少。整体上，年均f NPV随海拔升高呈现由Ⅲ型向Ⅱ型的变化，表现出明显的垂直带谱特征。年均f 的经度梯度受海拔和季风气候的共同影响，呈现由东向西逐步变化的趋势。

非光合植被覆盖度的动态在森林、草地及农田等主要生态系统中表现出显著的空间异质性。本研究基于MODIS土地覆盖分类对生态系统进行划分，并结合野外调查数据进行了验证，以提高分类的准确性（网络版附图S1c）。我们系统评估了2016–2024年间上述生态系统中非光合植被覆盖度的空间分布特征。其中，森林生态系统的年均f 相对较低，平均值为0.3563，但其分异范围较广，受Ⅱ型和Ⅲ型控制，面积占比分别为35%和38%，反映了森林生态系统跨越多样气候梯度的特点。北方的针叶林年均f 较高，而热带雨林中则显著较低。相比之下，草地生态系统的年均f NPV最高，达0.4425；其次为农田生态系统，为0.4028。两类生态系统的非光合植被覆盖度均主要集中于Ⅲ型，面积占比分别达到59%和68%，说明它们具有较强的凋落物积累与维持能力。草地生态系统的年均f 空间分布与半干旱至半湿润区高度吻合，显示出较强的区域匹配性。与此不同，农田生态系统中的非光合植被覆盖度的空间分布受人为因素影响较大，呈现更强的局地异质性。基于生态系统类型的分层分析加深了我们对非光合植被动态在不同生态系统中的理解。

2016–2024年间，非光合植被覆盖度整体呈上升趋势（图3a），年均增长率（Δf ）为0.0014 a −1（见图3b）。同期，光合植被和裸土覆盖度分别表现出增加和减少的趋势，年均变化率分别为0.0023和−0.0037 a −1（网络版附图S5c，附图S5d）。整体而言，Δf 在半干旱至半湿润区最高，达到0.0075 a −1；湿润区略有负增长，约为−0.0009a −1；而干旱区的Δf 最低，为−0.0066 a −1。中国整体及区域尺度上的f 频率分布直方图表现出显著差异（图3c）。图3d显示，整体上，f NPV存在显著的正增长趋势。从空间分布来看，半干旱至半湿润区的非光合植被显著增长区域（p<0.05）多于干旱区，且在半干旱至半湿润区内，轻微增长的面积比例为37%，显著增长的面积比例为13%，主要集中在内蒙古高原东部、黄土高原东部和青藏高原的中东部地区。在干旱区，非光合植被覆盖度保持稳定或下降的区域主要分布在温带沙漠和塔里木盆地、内蒙古高原西部以及黄土高原西部。湿润区的非光合植被覆盖度轻微增长的区域面积占比为31%，显著增长的面积占比为10%。显著增长的区域主要集中在东北平原、华北平原东北部及胶东半岛，而淮河平原则出现一定的下降趋势。在湿润区南部，非光合植被呈现不显著的正增长，而东南沿海及华东沿海平原则表现出裸土覆盖度显著上升，伴随光合植被的减少，反映出土地利用变化和环境压力的综合影响。

![](images/97613316d93834148c7ebbb02ca614a357360f7a24411087b9250928ae8d36e7.jpg)  
审图号：GS京(2025)1623号  
图 2 2016–2024年中国年均非光合植被的时空分布格局。（a） 中国区域年均f NPV空间分布图，数值范围0–1。图中白色线条标示出三大气候区边界：干旱区（Arid Region，R A）、半干旱至半湿润区（Semi-arid and Sub-humid Region，R S）以及湿润区（Humid Region，R H）。（b） 纬度方向年均f NPV（蓝线）及其增长率Δf NPV （红线）的变化趋势。数据基于对沿纬度带所有陆地栅格进行平均计算，浅蓝色和粉色阴影区域分别表示f NPV和Δf NPV 的置信区间。（c） 不同气候区及主要生态系统（森林、草地、农田）年均f NPV的箱线图。箱体中线为中位数，蓝色方块代表均值，箱线右侧的曲线展示数据分布的密度。（d） 不同地理单元和植被生态系统f 等级的面积百分比分布。依据网络版附表S3，将f 划分为五个等级（I–V），覆盖度由低至高依次排列。图中颜色分别为蓝色（I）、浅蓝色（II）、浅红色（III）、浅黄色（IV）和红色（V）

# 3.3 非光合植被覆盖变化的多因素驱动因素

我们在国家和区域尺度上系统量化了中国非光合植被覆盖度的空间分异。为此，采用BRT算法，驱动因子涵盖气候条件、太阳辐射强度及干旱事件频率等环境变量的地理变化特征，识别影响非光合植被分布的关键环境控制因子及其相对重要性。初步纳入的环境因子包括PRE、TEM、FPAR、MS、SR和SIF。上述因子按时间尺度划分为年尺度（AN）和季度尺度（QU）：其中年尺度指标指全年的平均值，季度尺度指标则提取影像主要获取期的季度均值。此外，还将ASL、SCC、PET和Albedo纳入了驱动因子评价体系。在初步分析阶段，基于国家尺度的BRT模型对上述16个环境因子的相对重要性进行了量化评估。结果显示，MS AN、SR AN、PET、SCC、SIF AN和SIF QU的重要性均低于0.045，因而在后续建模中被剔除。最终，基于对非光合植被空间分布具有较高解释力的变量，构建了高效的驱动因子评价体系。

![](images/d2a80cc1082ff05ebab6280fc7a74cd7a607c012f01b7a421cdf8971327e8d85.jpg)  
审图号：GS京(2025)1623号  
图 3 2016–2024年中国非光合植被覆盖度增长率的空间分布及统计特征。（a） Δf NPV 空间分布图。增长趋势分为五类：显著下降（<−0.04）、轻微下降（−0.04–−0.01）、稳定（−0.01–0.01）、轻微上升（0.01–0.04）和显著上升（>0.04）。显著性检验结果的区域以“×”标示。（b） 中国及其三个气候区内Δf NPV 的分布情况。每个区域中，水平线表示Δf NPV 的分布范围（误差条覆盖第5–95百分位），上方曲线为该增长率的正态分布密度曲线，竖直虚线表示无变化点。（c） 中国全国及各气候分区内年均f NPV的频率分布图，颜色对应直方图的频率，并匹配其频率分布密度曲线。（d） 2016–2024年间中国Δf NPV 的频率分布图，竖直虚线表示无变化点（增长率为0）。其中蓝色代表呈下降趋势，灰色代表保持稳定，橘黄色代表呈上升趋势

中国位于典型的季风气候区，非光合植被覆盖度变化的驱动因子在空间上呈现出显著的区域异质性。在国家尺度上（图4a），TEM 是解释f 空间分异的主要驱动因子（18.92%），其次为FPAR AN（15.94%）、SR QU（10.35%）和TEM QU（10.21%），这四个因子的贡献率均超过10%。在区域尺度上，f 的主控因子因气候带的不同而表现出显著差异。在干旱区（图4b），最重要的驱动因子为PRE QU（21.54%），其次依次为SR QU（11.15%）、FPAR AN（11.07%）和ASL（10.99%）。在半干旱至半湿润区（图4c），f NPV的空间分异主要受MS QU（20.01%）、FPAR AN（13.83%）和ASL（12.41%）的影响。而在湿润区（图4d），TEM QU对f NPV空间分异的贡献率最高，达到29.22%。其次依次为SR QU（13.70%）、ASL（10.93%）和FPAR QU（10.22%）。为进一步揭示关键环境因子对f 的影响，我们继续选取国家尺度及各区域尺度中贡献率最高的两个驱动因子，通过剔除其他因子干扰，开展单变量响应分析，旨在深入解析主导因子的作用机制。

![](images/207f40365ddf451bf778a5051f23392dcebb79b4a112d2140f0191f60ce71c60.jpg)  
图 4 中国非光合植被覆盖度空间分异的环境驱动因子分析。（a–d） 全国尺度及不同气候区（R ：干旱区；R ：半干旱至半湿润区；R ：湿润区）内，基于BRT模型评估的影响非光合植被覆盖度空间变异的环境因子相对重要性结果。柱状图显示各因子的平均相对重要性，误差棒表示标准差。环境因子包括：TEM（气温）、PRE（降水）、MS（土壤湿度）、FPAR（光合有效辐射分量）、SR（太阳辐射）、地形因子ASL（海拔高度）与Albedo（短波黑天反照率）, 其中年尺度（AN）和季度尺度（QU）以下标表示。（e–h） 全国尺度及三大气候区内，解释非光合植被覆盖度空间分异的前两大主导环境因子的偏依赖图。蓝色和红色曲线分别表示第一和第二重要因子对非光合植被覆盖度的平滑响应关系，阴影区域为95%置信区间，反映模型拟合的不确定性。每条垂直虚线对应该因子的平均值位置

在全国范围及湿润区（图4e，4h）中，气温从较低水平开始的上升初期，均引起f 的轻微增加。然而，在全国尺度上，f 于气温达到约0 ℃时开始逐步下降，并持续下降至约10 ℃；而在湿润区，该下降趋势则始于约−10 ℃ ，并延续至约13 ℃。就成像期间的降水而言，全国尺度上f 随降水呈现出先升后降的变化模式；相比之下，干旱区的f 则表现出多阶段的响应过程：在降水量0–5 mm范围内迅速下降，随后在5–27 mm之间趋于平稳，当降水量增加至27–31 mm时出现明显上升，最终在大于31 mm时趋于稳定（图4f）。在FPAR方面，全国与半干旱至半湿润区均表现出f 随FPAR 增加而持续上升的趋势，尤以FPAR 从8提升至10的区间最为显著，f 出现明显跃升；随后，随着FPAR 接近约25，上升速率逐渐减缓（图4g）。此外，在干旱区至湿润区中，f 随SR 的增加而上升，在辐射强度达到约94 W m −2时达到峰值，随后下降，并在超过126 W m −2后趋于稳定平台期。

在全国尺度及不同气候区，非光合植被覆盖度对各类驱动因子的时间响应特征呈现显著的区域异质性（见网络版附图S3）。除干旱区外，全国及其他气候区在年均气温和季节性气温升高的过程中，非光合植被覆盖度普遍呈下降趋势，尽管该趋势在统计上未达到显著性水平。较高的年均气温可能引发热胁迫，抑制光合植被的积累，但过高的季节性气温则可能削弱植被的自然凋萎过程。总体而言，年尺度的干旱通常抑制植被生物量积累，导致非光合植被覆盖度下降；而在季节尺度上，短期干旱往往伴随着植被凋萎过程的加剧，从而促进非光合植被覆盖度的上升。在干旱区，年降水量的增加对非光合植被覆盖度表现出显著的正向影响，主要归因于降水的增加显著提升了该区域的植被初级生产力。在秋冬季节，降水的增加可能提高霜冻发生的概率，进一步加剧植被枯死过程，导致非光合植被覆盖度进一步增加；而在其他气候区，这一效应较为微弱，甚至可能表现为相反的趋势。全年尺度上的太阳辐射和有效辐射增加有助于提升植被的整体生长能力，促进生物量的积累，为非光合植被的转化提供了坚实的基础。因此，不同区域中非光合植被覆盖度的响应差异主要源于植被类型和气候条件的共同作用。此外，各驱动因子在年尺度与季度尺度上的影响效应也表现出不同的模式特征。

# 3.4 非光合植被变化对碳通量的影响

本研究基于长期地面观测数据和多源遥感产品，系统探讨了非光合植被与LC、SOC及SoiR之间的关系。首先，采用线性回归模型拟合PV、NPV和BS与LC、SOC及SoiR的关系。随后，在设定f 为中位数的条件下，绘制二维热力图，进一步分析LC、SOC和SoiR对f NPV与f PV的响应。相关分析分别在全国尺度及不同气候分区进行，以揭示区域差异及其调控机制。

非光合植被在表征凋落物碳方面的能力在不同植被生态系统中存在显著差异，尤其在森林生态系统中，通常需与光合植被共同作用，才能更全面地指示凋落物碳。如图5所示，在国家尺度及各气候区域尺度下，LC与f PV均呈显著正相关，而非光合植被对林下层枯枝、果实等非叶片类凋落物的响应较弱。然而，在湿润区中，随着f NPV的增加，LC同样呈现上升趋势。相比之下，在草地生态系统中，f 的增加却伴随着LC的下降。在其他区域，LC与f NPV和f PV均呈显著正相关。国家尺度下，SOC在森林生态系统中与f NPV呈正相关，而与f PV呈负相关。在干旱区，SOC与f NPV的相关性不显著，但与f PV呈负相关。在半干旱至半湿润区和湿润区中，SOC与f NPV和f PV具有相似的相关关系。在草地生态系统中，湿润区的SOC与f 呈正相关，与f 呈负相关；而在其他气候区，SOC与f NPV普遍呈正相关。在森林生态系统中，非光合植被覆盖度与土壤呼吸之间的关系因区域而异：在全国尺度和半干旱至半湿润区，二者呈现弱正相关，而在湿润区则表现为负相关。相较之下，在干旱区，SoiR与f NPV呈现显著正相关。在草地生态系统中，除湿润区外，SoiR与f NPV整体表现为正相关趋势；在湿润区，该关系则偏离上述模式。总体而言，非光合植被弥补了光合植被在表征凋落物层方面的不足。两者联合使用能够更有效地指示土壤有机碳的空间分布特征（见网络版附图S6）。此外，非光合植被对土壤呼吸的空间异质性表现出高敏感性，尤其在全球干旱化趋势加剧的背景下，非光合植被为土壤呼吸的动态变化提供了更为细致和精准的表征。

非光合植被覆盖度的变化与凋落物碳和土壤有机碳变化呈显著正相关，表明非光合植被覆盖度的动态可能直接调控凋落物碳和土壤有机碳的含量（图6a，6b）。相比之下，非光合植被覆盖度与土壤呼吸的相关性较弱（图6c），这主要是因为土壤呼吸受空气温度、降水等外部环境因素的影响较大，并且表现出明显的空间异质性。基于光合植被、非光合植被和裸土的概念，构建的ECEF指数刻画了植被层与土壤层之间生物量碳转换的关键过程。如图6d所示，ECEF与NEE呈显著负相关（Pearson r=−0.68，p<0.05，R 2 =0.46）（图6d），表明ECEF是评估气候梯度下碳通量变化的有效代理指标。总体而言，中国生态系统表现为碳汇状态，ECEF的平均值为0.30。半干旱至半湿润区两侧的碳通量呈现显著的梯度分布，其中湿润区的碳汇强度较高（0.95），而干旱区则表现为碳源（−0.47），且碳汇强度随着纬度升高逐渐下降（图6e，6f）。在全球尺度上，森林生态系统的碳汇持续增强，强度高于草地生态系统，沙漠生态系统也表现出显著的碳汇潜力。综上所述，ECEF的引入为生物量碳动态评估提供了一个创新性的框架。

![](images/4e6dc388d522138dab9d68ec7fa0baf514b6aca1442eff8068636254521a04fa.jpg)  
图 5 非光合植被覆盖度变化对关键碳通量指标的影响分析。（a–d） 在全国及区域尺度（R ：干旱区；R ：半干旱至半湿润区；R ：湿润区）内，固定f 为中位数时，森林生态系统中各变量与凋落物生产量之间的关系。（e–h） 各变量与对应的草地生态系统凋落物生产关系。（i–l）与（m–p）分别表示森林和草地生态系统中各变量与土壤有机碳关系的空间分布。（q–t）与（u–x）分别表示森林和草地生态系统中各变量与土壤呼吸之间的关系。各图横轴为f ，纵轴为f ，颜色条指示对应的LC、SOC或SoiR数值。所有变量单位均为t ha −1

![](images/32342491ab4fe2cc1113f9844de33155ebec0569a23d1ec26995b57e9f9f1378.jpg)  
图 6 碳通量与非光合植被覆盖度分布模式。（a–c） f NPV的变化率与LC、SOC及SoiR变化速率之间的关系；（d） ECEF与NEE的线性拟合关系；（e） ECEF指数的全国空间分布图，白色线条标示不同气候区边界；（f） 不同气候分区中ECEF的箱线图

# 4 讨论

# 4.1 非光合植被分布格局的调控机制

中国非光合植被覆盖度呈现显著的空间异质性，受气候梯度、生态系统类型及土地管理措施等多重因素的共同影响。总体而言，干旱和半干旱至半湿润地区由于水分供应受限以及土壤微生物活性较低，抑制了有机物的分解过程，因此呈现较高的非光合植被覆盖度（Xu等，2021）。与此相反，湿润地区尽管植被生产潜力较高，但非光合植被的地表覆盖度却相对较低，这主要归因于湿润环境中凋落物分解速率远高于其产生速率。高温和持续湿润的气候条件显著增强了微生物活性，加速了枯死植物组织的分解速率，缩短了其在地表的滞留时间，从而减少了非光合植被的积累。在热带和亚热带生态系统中，频繁的强降雨事件可能导致凋落物的冲刷和搬移；在温带地区，季节性冻融循环则通过机械破碎和生物促解作用加速了凋落物的降解过程，这些因素共同限制了非光合植被在地表的长期存在。

除了气候驱动因素外，生态系统类型对非光合植被动态也起着显著的调控作用。在温带沙漠生态系统中，由于植被稀疏，秋冬季节非光合植被的产生量较低，但其时空分布展现出较强的稳定性和持续性。在此类生态系统中，非光合植被主要由零星的枯草和灌木残留物构成，木本植物的贡献相对较小。相较之下，在温带草原和草甸生态系统（如中国西北和西南地区），季节性草本植物的枯萎以及枯死灌木和落叶在非生长季节大量积累，形成了显著的非光合植被。这些生态系统对气候变化极为敏感，非光合植被的生成主要受降水波动和季节性生长的驱动，表现出明显的时空动态特征。在季风气候主导的湿润区域，如中国南部和东部，非光合植被呈现明显的纬度梯度分布。中纬度地区的针叶林和针阔混交林在秋季落叶期间产生大量非光合植被，而低纬度的常绿阔叶林和热带雨林由于全年持续的凋落物更新和较高的分解速率，地表非光合植被的积累相对较少。尽管这些高生产力生态系统的整体生物量产量较高，但由于有机质循环迅速，它们限制了非光合植被的显著积累。

此外，人类活动因素，如土地利用变化、放牧强度和林地管理等，也对非光合植被的空间分布格局产生了显著影响。过度放牧的草地和经过人工管理的森林区域，通常表现出地表凋落物的减少，即使在气候条件适宜的情况下，地表非光合植被覆盖度仍可能偏低。这些复杂的人为干扰效应凸显了单纯依赖气候变量难以全面解析非光合植被动态的局限性，也强调了在研究非光合植被变化时，必须充分考虑土地利用历史和生态系统特有过程的综合影响。

# 4.2 全球非光合植被制图方法的进展与比较分析

尽管非光合植被在陆地碳循环中发挥着重要作用，但与光合植被相比，全球对非光合植被的系统性监测仍然相对不足。现有的大多数全球植被产品主要侧重于绿色植被的光谱信号，往往忽视了非光合植被独特的光谱特征及其在生态系统中的功能。与此同时，虽然基于机器学习的土地覆盖分类或植被覆盖度模型能够敏感地反映区域差异，但在复杂多变的气候和地表条件下，这些模型往往难以展现出良好的泛化能力，限制了其在大尺度生态系统碳通量监测中的应用。尽管不同传感器的波段配置和光谱响应函数存在差异，需要对端元反射率值进行微调，但三角空间法基于端元驱动框架，充分利用了光谱间的固有关系，降低了对端元值的局部校准依赖，其依然稳健的基本结构在大范围应用中展现出更强的扩展性和适用性。

三角空间法通过区分非光合植被与裸土，在应用中展现出了显著的灵活性。首先，构建的三角空间法结合了NSSI与NDVI，可适用于多种多光谱和高光谱卫星影像数据，包括WorldView-3、ZY-01、高分五号及EO-1Hyperion等，从而实现了对不同传感器数据的广泛兼容。现有研究多集中于局部尺度，缺乏覆盖全球并具备时空连续性的系统性非光合植被监测框架。全球非光合植被覆盖度产品为深入解析非光合植被的空间分布格局及其驱动机制提供了坚实的数据基础与方法支持。因此，基于可见光与近红外波段的光谱形态指数（VNIR SpectralShape Index，SSI）以及MODIS影像数据，本研究开发了2018年全球非光合植被覆盖度数据集（Tian等，2023）。结果表明，在以枯草、灌木残枝及落叶为主的半干旱至半湿润区域，非光合植被覆盖度普遍较高（图7）。值得注意的是，基于SSI与NDVI构建的三角特征空间在高异质性区域中呈现出一定的非线性特征。但是，该方法与MODIS遥感观测数据在整体上仍可保持一致，具备在全球尺度上以500 m空间分辨率反演NPV、PV及BS覆盖度

![](images/8439a5b39811cc85894b295b544f25bf21c74648cd8ee1d5733e857d4bdb4b6c.jpg)  
图 7 2018年全球非光合植被覆盖度的空间分布格局

的可行性与稳健性。

三角空间法框架在中国以外地区（包括萨赫勒干旱带、大平原及澳大利亚中部）的初步应用验证了其优良的可迁移性和适用性。在这些生态系统中，非光合植被的持续存在主要归因于降水稀少、植被稀疏以及微生物分解活性较低，导致凋落物分解缓慢，进而积累明显。相比之下，湿润的热带地区尽管生物量丰富，但由于凋落物周转速度较快，地表非光合植被的含量相对较低。温带及过渡带生态系统则表现出介于两者之间的特征，其非光合植被动态显著受季节性温度与湿度变化的影响，表现出明显的季节性波动。此外，人类活动对非光合植被空间分布的影响日益显著，尤其在脆弱的干旱区生态系统中更加突出。这些现象凸显了非光合植被动态对环境梯度和人为干扰的高度敏感性，强调了在陆地碳循环模型中纳入非光合植被作为关键指标因子的迫切性，尤其对提高全球变化背景下非光合植被影响碳通量预测的准确性具有重要意义。

# 4.3 陆地生态系统中非光合植被对碳通量的贡献

为量化非光合植被对陆地生态系统碳通量的贡献，本研究选取了f NPV 及Δf NPV 作为关键预测变量，系统分析了其与ECEF之间的关系强度与响应特征。结果表明，f NPV与ECEF呈显著正相关（回归斜率为1.1925），表明f NPV较高的区域通常具有更强的碳汇潜力。然而，f 对ECEF的解释力也受到光合植被覆盖度的调节影响。类似地，当采用Δf 作为预测变量时，其与ECEF依然表现出显著正相关，回归斜率达到2.2910，进一步凸显了非光合植被动态变化对生态系统碳通量的重要影响。值得注意的是，不同区域间非光合植被与生物量碳通量指数之间的关系强度存在显著差异：干旱和半干旱地区表现出较强的相关性，反映出这些生态系统对f NPV波动的高度敏感性；而在南方密林覆盖的湿润区，非光合植被对碳通量的解释能力相对较弱，可能是由于该区域光合作用活跃，且冠层植被对碳循环具有主导作用所致。

在半干旱与半湿润地区，凋落物的输入调控时间通常短于生态系统中凋落物的平均滞留时间，导致凋落物积累较为显著。相比之下，热带森林中新鲜凋落物的碳分解与呼吸速率较快，并且被高效转化为矿化态土壤碳。这种空间异质性突显了非光合植被在生态功能上的差异，强调了其作为碳动态关键组成部分的核心作用，尤其是在绿植生物量受限或季节性限制显著的生态系统中更为关键。研究结果支持了非光合植被在维持凋落物生物量、增强土壤有机碳储量及间接稳定生态系统碳平衡中的重要作用，尤其体现在半干旱至半湿润生态过渡区。同时，结果也凸显了在碳通量动态模型中明确纳入非光合植被的必要性，尤其是在气候梯度显著且植被凋谢与土壤碳响应存在明显差异的生态系统中。

# 4.4 全球气候变化对碳通量格局的影响

如图8a–8c所示，半干旱和半湿润地区显著受到夏季季风过渡带的影响，不同区域在干湿动态变化上仍存在显著的空间异质性（Cui和Shi，2021）。这一现象在半湿润地区表现尤为突出。例如，东北亚和北美西部在降水偏少的年份会呈现出半干旱特征，而湿润地区如欧洲和澳大利亚东南部则可能向半湿润区转变（Shen等，2021）。在大陆尺度上，非洲与欧亚大陆呈现出尤为显著的干旱化趋势（图8d）。其中，欧亚大陆的干旱化进程尤为突出，尤其在俄罗斯远东、华北和东北地区，该趋势不仅显著增强，且呈现加速发展态势。全球变暖对植被生长产生了深远影响，尤其在生态敏感区表现尤为明显。这些区域的生态系统脆弱，且对气候变化高度敏感。近年来，夏季季风过渡带的持续扩展使该地区植被同时面临干旱与高温的复合胁迫，这不仅诱发植物根系自我稀疏，还破坏了其原有的代谢平衡，进而影响整体生态稳定性。

![](images/cb9cf8e04759819a1554464c91b30fad032c4f3e377fd2af84d17d1f6aa0c42a.jpg)  
图 8 基于2000–2020年降水分布划分的气候区域。（a–c） 根据年平均最小降水量、年均最大降水量和年均降水量划分的半湿润区和半干旱区；（d） 全球降水趋势图。需注意，该图不包含降水信息较少且植被稀少的南极大陆

草地与森林生态系统在应对全球气候变化过程中表现出显著差异，这种差异源于它们在生态结构、功能特征及适应策略等方面的本质不同。值得注意的是，温度与降水的耦合变化是驱动中国草地生态系统碳汇空间变异的核心因素。长期干旱对草地生态系统产生显著影响。在极端情况下，草地生态系统甚至会从碳汇转变为碳源。这一转变主要源于干旱条件下初级生产力的下降与生态系统呼吸作用的增强。此外，干旱所导致的土壤水分亏缺对植被生长和光合作用产生了显著抑制作用，进一步削弱了生态系统的碳汇功能，从而加剧了碳的呼吸排放过程。近年来，全球森林碳汇总体呈上升趋势，但区域差异依然显著。结合土地覆盖变化数据与全球植被模型的研究表明，北方针叶林与热带森林在增强碳吸收方面发挥了关键作用，是推动全球森林碳汇增长的主要原因。

尤其在高纬度地区，温度升高延长了生长季节，提升了净初级生产力；而部分热带区域则由于再造林与降水改善而增强了碳汇能力。在全球气候变化加剧的背景下，本研究提出的评估框架整合了遥感观测与生态过程建模，能够有效刻画自然生态系统碳通量的空间结构与时间动态，为区域差异识别和碳中和策略的制定提供了科学支撑。

# 4.5 研究局限性与展望

本研究展示了三角空间法框架在非光合植被覆盖度反演及生物量碳通量评估中的显著潜力，但仍存在若干限制，需要引起足够重视。为减少角度效应对遥感反射率的干扰，本研究在影像筛选过程中剔除了太阳天顶角大于60°或卫星观测视角超过20°的Sentinel影像。经过Sen2Cor处理后，Sentinel-2影像生成了经过大气校正和地形校正的2A级表面反射率产品。同时，在影像选择阶段，本研究限定了季节性时间窗口，并采用最大值合成方法对同期多景影像进行了整合。

然而，在复杂地形条件下，尤其是在坡向与太阳-传感器几何关系交互影响显著的区域，仍可能存在地形引发的残余辐射畸变。此外，由于光谱响应函数和波段配置的细微差异，Sentinel-2与Sentinel-3传感器在数据融合过程中可能引入系统性偏差，这凸显了开展更精细的传感器间校正与协调工作的必要性。值得注意的是，并非所有非光合植被都能被遥感传感器有效检测，尤其是在森林生态系统中，浓密冠层下的凋落物由于遮挡和光谱混合效应，常常导致遥感估计的系统性低估。在山区，坡度校正的不完全性可能导致非光合植被覆盖率的高估或低估，从而影响空间分布的准确表征。此外，农田管理、放牧活动及造林工程等局部土地利用变化在迅速改变地表凋落物动态的同时，也对光谱解混方法带来更高的挑战。尽管面临上述挑战，三角空间法框架在理论上具有较好的跨平台适用性，能够扩展应用于其他多光谱卫星传感器，如Landsat 8 OLI、VIIRS及CBERS-4等。这些传感器在红光、近红外及短波红外波段具有相似的光谱覆盖特性，有利于植被指数及端元光谱关系的校准与转换。通过针对不同传感器的波段响应和观测特性进行适当调整，三角空间法有望实现多源遥感数据的融合与协同应用，从而推动非光合植被在全球尺度上的长期动态监测与综合评估。

未来的研究应首先构建一个涵盖多样气候梯度和生态系统类型的全球光谱库，系统反映非光合植被与裸土的光谱特征及其时空变异，从而提升非光合植被数据集的反演精度与适用性。与此同时，应积极探索多角度观测与高光谱遥感数据的融合应用，以弥补传统多光谱数据的不足。结合数据驱动的深度学习方法，有望显著增强端元光谱提取的鲁棒性与自动化水平，实现植被组分估算的高效性。此举将进一步推动全球尺度非光合植被监测及生态碳通量动态研究的深入发展。方法学的进步也将受益于高分辨率、多源连续时间序列遥感数据的融合应用，从而大幅提升非光合植被动态监测的空间和时间精度。合成孔径雷达（SAR）与激光雷达（LiDAR）技术的发展，为捕捉植被结构信息并实现跨传感器数据融合提供了重要支持。最后，将遥感反演的非光合植被覆盖度动态与地面碳通量观测（如涡度协方差系统）深度结合，能够有效验证和优化碳通量代理模型，从而提升生态学的解释力。此类多尺度、多源的综合研究不仅有助于揭示生态系统生物量流动与碳循环的复杂机制，也为全面评估气候变化及人类活动等外部驱动对陆地碳循环过程的影响提供了坚实的科学支撑。

# 5 结论

本研究首次系统评估了中国非光合植被的时空动态及其在气候梯度背景下对陆地碳通量的影响。通过融合Sentinel系列多光谱遥感影像与实地观测数据，生成了2016–2024年间的年最大非光合植被覆盖度产品，空间分辨率为300 m。分析结果表明，非光合植被覆盖度整体呈显著上升趋势，且最高覆盖度及增长率主要集中在半干旱至半湿润气候过渡区。该空间分布格局特别突出了季度气温和降水对非光合植被空间分布与时序变化的关键调控作用。本研究的主要结论如下：（1）中国年均非光合植被覆盖度为0.3679，年增长速率为0.0014 a −1，季度气温和降水是主导NPV空间分异的关键气候因子，分别解释了其变化的19.38%和15.22%；（2）非光合植被通过有机物质输入、调节土壤呼吸及促进土壤碳积累等途径，在陆地碳通量中发挥了关键作用；（3） ECEF作为生态系统碳库结构与动态的综合表征指标，与净生态系统交换通量呈显著负相关（Pearson r=−0.68，p<0.05，R 2 =0.46），体现了ECEF在气候梯度背景下碳通量估算中的稳健代理价值。综上所述，研究结果强调了非光合植被作为植被功能性组成部分的重要生态意义，并验证了结合遥感数据与模型构建框架在捕捉生态系统碳交换双向动态中的有效性。通过在遥感产品与碳通量模型中明确纳入非光合植被，有效解决了现有碳核算体系中的关键结构性不确定性。该方法及其研究成果具有广泛的全球推广价值，为在气候变化背景下，特别是在生态过渡区中改进碳通量估算提供了创新路径。

补充材料 补充材料为作者提供的原始数据，作者对其学术质量和内容负责，详见网络版(http://earthcn.scichina.com)。

数据可用声明 所有用于支持本研究发现的数据均可公开获取。Sentinel表面反射率数据可免费获取自欧洲航天局（European Space Agency ESA；https://dataspace.copernicus.eu）。Google Earth图像可从https://www.google.cn/intl/zh-en/earth/下载。中国生态系统凋落物和土壤的长期动态监测数据库可从国家科技资源共享平台（National Science & Technology Infrastructure，NSTI；http://rs.cern.ac.cn/）获取。1993–2019年中国北方温带草地地上生物量数据集、1981–2019年全球1 km土壤有机碳库数据集、2000–2020年全球0.1°土壤水分数据集、2000–2020年全球1 km土壤呼吸数据集、全球5 km每月碳净生态系统交换数据集、海拔数据集、土壤黏土含量数据集及1901–2023年中国1 km每月潜在蒸散量数据集可从国家地球系统科学数据中心（NationalEarth System Science Data Center，NESDC；http://www.nesdc.org.cn/）获取。2000–2018年青藏高原高山草甸地上生物量数据集、1983–2018年全球高分辨率（3 h，10 km）表面太阳辐射数据集、2000–2022年全球连续空间太阳诱导荧光数据集（基于神经网络）、2002–2020年中国上地下森林生物量碳库数据及1982–2020年中国森林凋落物碳密度数据可从国家青藏高原数据中心（National Tibetan Plateau Data Cen-ter，TPDC；https://data.tpdc.ac.cn/）获取。温度和降水等气象数据集可从https://cds.climate.copernicus.eu/获取。基于GEE平台，可获取500 m的MOD15A2H FPAR产品（MODIS/061/MOD15A2H，“Fpar_500m”波段）提供8天的平均值，5 0 0 m 的 M C D 4 3 A 3 反 照 率 产 品 （ M O D I S / 0 0 6 /MCD43A3，“Albedo_BSA_shortwave”波段）提供16天的平均值。基于MCD12Q1（MODIS/006/MCD12Q1，带有“LC_Type1”波段）获取了不同生态系统数据。最终，数据分析使用了Python 3.8、ArcGIS 10.5、GEE和ENVI 5.6。

# 参考文献

Aitkenhead M J, Black H I J. 2018. Exploring the impact of different input data types on soil variable estimation using the ICRAF-ISRIC global soil spectral database. Appl Spectrosc, 72: 188–198 Bai X, Zhao W, Ji S, et al. 2021. Estimating fractional cover of nonphotosynthetic vegetation for various grasslands based on CAI and DFI. Ecol Indic, 131: 108252 Bai X, Zhao W, Luo W, et al. 2024. Effect of climate change on the seasonal variation in photosynthetic and non-photosynthetic vegetation coverage in desert areas, Northwest China. Catena, 239: 107954 Cao S, Zhang L, He Y, et al. 2022. Effects and contributions of meteorological drought on agricultural drought under different climatic zones and vegetation types in Northwest China. Sci Total Environ, 821:   
153270 Cui L, Shi J. 2021. Evaluation and comparison of growing season metrics in arid and semi-arid areas of northern China under climate change. Ecol Indic, 121: 107055 Dennison P E, Lamb B T, Campbell M J, et al. 2023. Modeling global indices for estimating non-photosynthetic vegetation cover. Remote Sens Environ, 295: 113715 Dhole A, Kadaverugu R, Tomar S, et al. 2023. Impact of land cover classes on surface temperature in the vicinity of urban lakes and vegetation patches: A non-parametric regression analysis over decadal data. Earth Sci Inform, 16: 3947–3961 Dou X, Yang Y. 2018. Estimating forest carbon fluxes using four different data-driven techniques based on long-term eddy covariance measurements: Model comparison and evaluation. Sci Total Environ,   
627: 78–94 Fernandez-Beltran R, Pla F, Plaza A. 2019. Sentinel-2 and Sentinel-3 intersensor vegetation estimation via constrained topic modeling. IEEE Geosci Remote Sens Lett, 16: 1531–1535 Fu Z, Stoy P C, Poulter B, et al. 2019. Maximum carbon uptake rate dominates the interannual variability of global net ecosystem exchange. Glob Change Biol, 25: 3381–3394 Gadedjisso-Tossou A, Adjegan K I, Kablan A K M. 2021. Rainfall and temperature trend analysis by Mann-Kendall test and significance for rainfed cereal yields in northern Togo. Sci, 3: 17 Guerini F M, Kuplich T M, Quadros F L F D. 2020. Estimating natural grassland biomass by vegetation indices using Sentinel 2 remote sensing data. Int J Remote Sens, 41: 2861–2876 Guerschman J P, Hill M J, Renzullo L J, et al. 2009. Estimating fractional cover of photosynthetic vegetation, non-photosynthetic vegetation and bare soil in the Australian tropical savanna region upscaling the EO-1 Hyperion and MODIS sensors. Remote Sens Environ, 113: 928–945 He S, Li J, Wang J, et al. 2022. Evaluation and analysis of upscaling of different land use/land cover products (FORM-GLC30, GLC_FCS30, CCI_LC, MCD12Q1 and CNLUCC): A case study in China. Geocarto Int, 37: 17340–17360   
Hu J, Wang L, Zhang S, et al. 2011. Inhibitory effect of organic carbon on CO fixing by non-photosynthetic microbial community isolated from the ocean. Bioresour Technol, 102: 7147–7153   
Hu X, Ren H, Tansey K, et al. 2019. Agricultural drought monitoring using European Space Agency Sentinel 3A land surface temperature and normalized difference vegetation index imageries. Agric For Meteorol, 279: 107707   
Isson T T, Planavsky N J, Coogan L A, et al. 2020. Evolution of the global carbon cycle and climate regulation on earth. Glob Biogeochem Cycle, 34: e2018GB006061   
Jackson H, Prince S. 2016. Degradation of non-photosynthetic vegetation in a semi-arid rangeland. Remote Sens, 8: 692   
Janse P V, Kayte J N, Agrawal R V, et al. 2018. Standard spectral reflectance measurements for ASD fieldspec spectroradiometer. In: Proceedings of the 2018 Fifth International Conference on Parallel, Distributed and Grid Computing (PDGC). Solan: IEEE. 729–733   
Lees K J, Quaife T, Artz R R E, et al. 2018. Potential for using remote sensing to estimate carbon fluxes across northern peatlands—A review. Sci Total Environ, 615: 857–874   
Li Y, Chen J, Ma Q, et al. 2018. Evaluation of Sentinel-2A surface reflectance derived using Sen2Cor in North America. IEEE J Sel Top Appl Earth Obs Remo Sens, 11: 1997–2021   
Liu J, Fan J, Yang C, et al. 2022. Novel vegetation indices for estimating photosynthetic and non-photosynthetic fractional vegetation cover from Sentinel data. Int J Appl Earth Obs Geoinf, 109: 102793   
Liu L, Xiao X, Qin Y, et al. 2020. Mapping cropping intensity in China using time series Landsat and Sentinel-2 images and Google Earth Engine. Remote Sens Environ, 239: 111624   
Liu S, Liu X, Yu L, et al. 2021. Climate response to introduction of the ESA CCI land cover data to the NCAR CESM. Clim Dyn, 56: 4109–4127   
Ma R, Zhang J, Shen X, et al. 2024. Impacts of climate change on fractional vegetation coverage of temperate grasslands in China from 1982 to 2015. J Environ Manage, 350: 119694   
Meerdink S K, Hook S J, Roberts D A, et al. 2019. The ECOSTRESS spectral library version 1.0 Remote Sens Environ, 230: 111196   
Michopoulos P, Kaoukis K, Karetsos G, et al. 2020. Nutrients in litterfall, forest floor and mineral soils in two adjacent forest ecosystems in Greece. J For Res, 31: 291–301   
Montenbruck O, Hackel S, Jäggi A. 2018. Precise orbit determination of the Sentinel-3A altimetry satellite using ambiguity-fixed GPS carrier phase observations. J Geod, 92: 711–726   
Negash M, Starr M. 2021. Litter decomposition of six tree species on indigenous agroforestry farms in south-eastern Ethiopia in relation to litterfall carbon inputs and modelled soil respiration. Agroforest Syst, 95: 755–766   
Niu Z, He H, Peng S, et al. 2021. A process-based model integrating remote sensing data for evaluating ecosystem services. J Adv Model Earth Syst, 13: e2020MS002451   
Õunapuu-Pikas E, Tullus A, Kupper P, et al. 2025. Foliage development and resource allocation determine the growth responses of silver birch (Betula pendula) to elevated environmental humidity. Tree Physiol, 45: tpae161   
Pillai N D, Nandy S, Patel N R, et al. 2019. Integration of eddy covariance and process-based model for the intra-annual variability of carbon fluxes in an Indian tropical forest. Biodivers Conserv, 28: 2123–2141   
Pugh T A M, Arneth A, Kautz M, et al. 2019. Important role of forest disturbances in the global biomass turnover and carbon sinks. Nat Geosci, 12: 730–735   
Qiu L, Xiao T, Bai T, et al. 2023. Seasonal dynamics and influencing factors of litterfall production and carbon input in typical forest community types in Lushan Mountain, China. Forests, 14: 341   
Ren H, Wen Z, Liu Y, et al. 2023. Vegetation response to changes in climate across different climate zones in China. Ecol Indic, 155: 110932   
Saba G K, Burd A B, Dunne J P, et al. 2021. Toward a better understanding of fish-based contribution to ocean carbon flux. Limnol Oceanogr, 66: 1639–1664   
Schile L M, Byrd K B, Windham-Myers L, et al. 2013. Accounting for nonphotosynthetic vegetation in remote-sensing-based estimates of carbon flux in wetlands. Remote Sens Lett, 4: 542–551   
Shabani S, Pourghasemi H R, Blaschke T. 2020. Forest stand susceptibility mapping during harvesting using logistic regression and boosted regression tree machine learning models. Glob Ecol Conserv, 22: e00974   
Shen X, Liu B, Jiang M, et al. 2021. Spatiotemporal change of marsh vegetation and its response to climate change in china from 2000 to 2019. J Geophys Res-Biogeo, 126: e2020JG006154   
Tian J, Su S, Tian Q, et al. 2021. A novel spectral index for estimating fractional cover of non-photosynthetic vegetation using near-infrared bands of Sentinel satellite. Int J Appl Earth Obs Geoinf, 101: 102361   
Tian J, Zhang Z, Philpot W D, et al. 2023. Simultaneous estimation of fractional cover of photosynthetic and non-photosynthetic vegetation using visible-near infrared satellite imagery. Remote Sens Environ, 290: 113549   
Tsendbazar N E, Tarko A, Li L, et al. 2021. Copernicus global land service: Land cover 100 m: Version 3 Globe 2015–2019: Validation report   
Verrelst J, Halabuk A, Atzberger C, et al. 2023. A comprehensive survey on quantifying non-photosynthetic vegetation cover and biomass from imaging spectroscopy. Ecol Indic, 155: 110911   
Vidal-Macua J J, Nicolau J M, Vicente E, et al. 2020. Assessing vegetation recovery in reclaimed opencast mines of the Teruel coalfield (Spain) using Landsat time series and boosted regression trees. Sci Total Environ, 717: 137250   
Wang G, Wang J, Zou X, et al. 2019. Estimating the fractional cover of photosynthetic vegetation, non-photosynthetic vegetation and bare soil from MODIS data: Assessing the applicability of the NDVI-DFI model in the typical Xilingol grasslands. Int J Appl Earth Obs Geoinf, 76: 154– 166   
Wang J, Li W, Ciais P, et al. 2021. Changes in biomass turnover times in tropical forests and their environmental drivers from 2001 to 2012. Earths Future, 9: 2020EF001655   
Wang S, Huang Y. 2020. Determinants of soil organic carbon sequestration and its contribution to ecosystem carbon sinks of planted forests. Glob Change Biol, 26: 3163–3173   
Wang T, Zhang Y, Yue C, et al. 2025. Progress and challenges in remotely sensed terrestrial carbon fluxes. Geo-spatial Inf Sci, 28: 1–21   
Xu L, Zheng C, Ma Y. 2021. Variations in precipitation extremes in the arid and semi-arid regions of China. Int J Climatol, 41: 1542–1554   
Yu L, Du Z, Dong R, et al. 2022. FROM-GLC Plus: Toward near real-time and multi-resolution land cover mapping. GISci Remote Sens, 59: 1026– 1047   
Zhang M, Zhang L, He H, et al. 2022. Improvement of ecosystem quality in National Key Ecological Function Zones in China during 2000–2015. J Environ Manage, 324: 116406   
Zhang X, Xin X, Yang W, et al. 2021. Soil respiration and net carbon flux response to long-term reduced/no-tillage with and without residues in a wheat-maize cropping system. Soil Tillage Res, 214: 105182   
Zhu C, Tian J, Tian Q, et al. 2023. Using NDVI-NSSI feature space for simultaneous estimation of fractional cover of non-photosynthetic vegetation and photosynthetic vegetation. Int J Appl Earth Obs Geoinf, 118: 103282

（责任编委：丁金枝）