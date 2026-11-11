李道诚, 夏迎新, 肖二龙, 宁立新. 基于人类活动因子和随机森林模型改进土壤有机碳密度预测及制图[J]. 中国生态农业 学报 (中英文), 2025, 33(12): 2485−2497 LI D C, XIA Y X, XIAO E L, NING L X. Improvement of soil organic carbon density prediction and mapping based on human activity factors and random forest model[J]. Chinese Journal of Eco-Agriculture, 2025, 33(12): 2485−2497

# 基于人类活动因子和随机森林模型改进土壤有机碳密度预测及制图

李道诚1, 夏迎新1, 肖二龙1, 宁立新1,2\*\*(1. 山东农业大学信息科学与工程学院　泰安　271018; 2. 山东农业大学农业大数据研究中心　泰安　271018)

摘　要: 土壤有机碳 (SOC) 密度是影响粮食安全和农业决策的重要土壤属性。以往 SOC密度预测研究多基于自然环境变量开展。然而, 在农业生产频繁地区, 人类活动也会在一定程度上影响土壤性质。本研究以黄淮海平原为研究区域, 选择 24个环境变量及人口密度、建筑物体积、道路网密度和人类热排放 4个人类活动变量, 探讨人类活动对耕地 SOC密度预测的重要性。结果表明, 环境协变量仅能解释耕地 SOC密度变化的 35%。添加人类活动变量后, 决定系数 (R2) 和林氏一致性相关系数 (Lin’s concordance correlation coefficient, LCCC) 分别提高 37.14% 和19.67%, 平均绝对误差 (MAE) 和均方根误差 (RMSE)分别降低 8.47% 和 9.88%, 显示出更好的模型性能和预测准确性。这说明在黄淮海平原地区, 人类活动对区域 SOC 密度的空间分异具有重要影响。变量重要性分析发现, 白天最高地表温度是最重要的预测因子, 其次是白天地表温度的标准差。人类活动变量中, 人类热排放是最重要的预测变量, 重要性占比为8.25%, 其次是人口密度、建筑物体积和道路网密度。

关键词: 人类活动因子; 土壤有机碳密度; 随机森林; 数字土壤制图; 黄淮海平原

中图分类号: P934

# Improvement of soil organic carbon density prediction and mapping based on human activity factors and random forest model

LI Daocheng1, XIA Yingxin1, XIAO Erlong1, NING Lixin1,2\*\* (1. School of Information Science and Engineering, Shandong Agricultural University, Tai’an 271018, China; 2. Agricultural Big Data Research Center, Shandong Agricultural University, Tai’an 271018, China)

Abstract: Soil organic carbon (SOC) density is a critical soil attribute that not only sustains soil fertility and regulates terrestrial carbon cycles but also influences regional food security and agricultural management decisions. While previous research on SOC density prediction have primarily relied on natural environmental variables, such as climate, topography, and vegetation, they have often overlooked the role of anthropogenic disturbances, especially in heavily human-impacted areas where human activities significantly alter soil properties. This study focuses on the Huang-Huai-Hai Plain (HHH Plain), a major grain-producing region in China characterized by intensive agriculture and urbanization. To improve SOC density prediction accuracy for cultivated land, a random forest (RF) algorithm, integrating 24 environmental covariates (climate, soil parent materials, topography, vegetation, land surface thermal conditions, and soil properties) were integrated with four human activity variables (population density, built-up volume, road network density, and hourly anthropogenic heat flux). Model parameters were optimized using five-fold cross-validation (n_estimators=100 and max_depth=4) and performance was assessed via mean absolute error (MAE), root mean square error (RMSE), coefficient of determination (R2), and Lin’s Concordance Correlation Coefficient (LCCC). The baseline model using only environmental covariates (Model 1) explained 35% of SOC density variation. In contrast, the integrated model (Model 6) incorporating both environmental and all four human activity variables improved prediction performance: R2 and LCCC increased by 37.14% and 19.67%, respectively, while MAE and RMSE decreased by 8.47% and 9.88%, respectively. This model accounted for 48% SOC density variation, highlighting the indispensable role of anthropogenic factors. Among all predictors, daytime land surface temperature was the most influential environmental factor, while hourly anthropogenic heat flux emerged as the most critical human activity factor, contributing 8.25% to prediction importance, surpassing population density (2.90%), built-up volume (0.58%), and road network density (0.06%). These findings demonstrate that integrating human activity factors, particularly hourly anthropogenic heat flux, is essential for accurate SOC density predictions in the HHH Plain. This study provides a scientific basis for regional soil carbon management, sustainable agricultural development, and ecological protection, while offering a reference for similar studies in human-dominated agricultural regions globally.

Keywords: human activity factors; soil organic carbon density; random forest; digital soil mapping; Huang-Huai-Hai Plain

2015年, 联合国发布了《2030年可持续发展议程》, 这项面向全球的话语性政策及其随附的共同战略框架——可持续发展目标 (Sustainable Develop-ment Goals, SDGs)[1] 的 17 个目标中至少有 7 项主题与土壤密切相关, 包括零饥饿、健康、清洁饮水、可持续城市、气候行动、水下生物和陆地生物等[2]。土壤有机碳 (SOC) 作为土壤的重要组成部分, 对于提升土壤肥力、改善土壤性质以及指导农业管理具有重要作用, 在环境保护、粮食安全、农业可持续发展等方面有着重要的意义[3]。SOC不仅是农业生产的基础, 也是陆地生态系统中最大的碳库, 其微小变化对全球碳循环具有显著影响[4]。保护 SOC 和增加土壤碳封存有助于减缓气候变化, 进而更有力地实现“双碳”目标。

获取 SOC准确、高质量的空间信息对于粮食安全、农业可持续发展和减轻气候变化影响具有重要作用。数字土壤制图 (Digital Soil Mapping, DSM) 依赖于土壤样本和环境协变量 (如气候、地形、母质、生物等[5]) 之间的协同变化关系, 利用数学模型算法和现代信息技术来预测土壤属性的空间分布[6]。基于多源变量的 SOC时空变化对理解生态系统碳汇功能和应对气候变化具有重要作用[7]。Jenny[5] 的土壤发生学理论强调了 5个主要因素对土壤形成的影响,这些因素包括气候、生 物、地 形、母质和时间;McBratney 等[8] 的 SCORPAN 理论在 Jenny 提出的土壤发生学理论基础上增加了空间因素, 使得对土壤特性的理解和预测更为全面和精确。何林倩等[9] 基于 DSM 技术, 以济源市南山林场为研究区, 对 6 种地形因子通过模糊 C均值聚类进行土壤碳含量预测制图, 结果表明该方法在 SOC储量估算时精度较高。张晓婷等[10] 以湖北省麻城市乘马岗镇为研究区, 采用 递 归 特 征 消 除 算 法 (recursive feature elimination,RFE)、ReliefF 算法和基于 Tree 的特征选择算法对环境因子进行筛选, 结果表明遥感因子在平原区的SOC 制图中参与程度更高。廖启林等[11] 针对江苏省土壤各元素含量分布展开调查, 重点分析农田施肥、冶金粉尘、燃煤排放、矿业活动等人为活动的作用,结果表明这些人为活动因子对地表土壤元素含量分布具有较大影响。总体而言, 目前在人类活动频繁的地区, 结合人类活动变量、SOC采样数据与实地调查数据进行 SOC及其密度测绘的研究较为匮乏,导致人们对这些因素在 SOC研究中的有效性了解有限, 而实际上在这类地区, SOC 的分布和变化还会受到人类活动因素的影响[12]。

黄淮海平原是中国主要农业区之一, 也是中国人口历来最密集的地区之一[13], 受近年来气候变化[14]、化肥施用[15]、农药污染[16]、农业结构变化[17]、不合理的人为活动以及经济增长引起的不合理土地利用[13]等影响, 环境和农业生产面临着干旱、洪涝和土壤肥力退化等问题。在黄淮海平原开展 SOC预测制图研究, 可为土壤资源合理利用、农业可持续发展、生态环境保护和土地管理决策提供科学依据, 同时借助高精度的土壤属性空间分布图, 还能更清晰地解析土壤与作物生长、环境变化及人类活动之间的关联。

鉴于以上情况, 本研究采用多源自然环境变量及人口密度、建筑物体积、道路网密度、人类热排放4 个人类活动因子, 对黄淮海平原耕地表层 SOC 密度预测进行改进。本研究主要目标是: 1)检验人类活动因素对该地区 SOC 密度模拟制图的重要性;2) 识别影响 SOC 密度的重要环境因子和人类活动因子; 3)提供该地区高精度SOC密度空间分布图。

# 1 材料与方法

# 1.1 研究区概况

黄淮海平原 (32°8′15″\~40°23′29″N, 112°29′13″\~122°42′22″E) 是中国东部大平原的重要组成部分[18],涵盖了北京、天津、河北、山东、河南、安徽、江苏等 5 省 2 市, 总面积约为 36.83 万 km2。该区域为暖温带大陆性季风气候, 春冬寒冷干燥, 夏季高温多雨, 年降水量为 500\~900 mm, 降水多集中于夏季[13]。区域内土壤类型以潮土、褐土为主。该地区地势平坦, 交通便利, 经济发达, 是中国重要的农业区域, 尤其以小麦 (Triticum aestivum L.)、玉米 (Zea mays L.)、棉花 (Gossypium hirsutum L.) 等农作物的种植面积较大。研究区位置及采样点如图1所示。

# 1.2 土壤有机碳 (SOC) 密度数据来源

本研究使用的 SOC密度数据来自“国家生态科学 数 据 中 心 ”(http://rs.cern.ac.cn/data/meta id=40579)“2010s中国陆地生态系统碳密度数据集”。该数据集覆盖了黄淮海平原森林、草地、农田、湿地和灌丛等主要生态系统类型, 包含了植被地上碳密度、植被地下碳密度和不同深度 (0\~20 cm 和 0\~100 cm)SOC密度。该数据集中的数据来自实地采样与文献获取, 文献中深度≤100 cm的样点按实际深度推算

0\~100 cm 密度, >100 cm 的取 0\~100 cm 数据; 实地采样数据参照第二次全国土壤调查的要求开展, 为确保样本能反映土壤的真实属性特征, 采用了多土层采样方式, 从而提升采样数据的代表性与可靠性。本研究结合研究区边界进行空间裁剪和数据筛选,从已有数据集中选择 151 个样点的 0\~20 cm 表层SOC 密度数据 (图 1), 可较好反映区域 SOC 密度空间分布特征。

# 1.3 环境协变量数据及来源

用于 SOC密度预测的环境变量共有 24个, 包括气候、母质、地形、植被、土壤等。环境变量的具体信息如表 1 所示。

地形数据来源于美国地质调查局 (USGS)的数字高程模型 (DEM), 从中计算得到 7 个地形变量 [ 高程、坡度、sin方位(与北方的角度距离)、平面曲率、剖面曲率、地形湿度指数、地形位置指数 ]。地形分类根据USGS的全球生态土地单元图得出。

气 候 数 据 均 来 源 于 “Global Climate and WeatherData”(https://www.worldclim.org/data/worldclim21.html), 用于计算年平均气温。降水量数据来自“科学数 据 银 行 ”(https://www.scidb.cn/en/detail dataSetId=ff7ee051d2d44ab4a221cd810bf37251), 用 于 计 算 平 均年降水量和降水标准差。年平均太阳辐射量和风速数据来自“WorldClim Verson2”(https://www.worldclim.org/data/worldclim21.html)。

土壤母质中风化层厚度数据来自文献 [19]。数据基于中国地质调查局的地质钻探数据库 (NIGBD)

![](images/d08d60c653471265295f16482130ac8412d3c54cc7b2930730bb242f878dde8f.jpg)  
图 1 研究区位置及观测土壤有机碳 (SOC) 密度采样点分布

Fig. 1 Location of the research area and distribution of soil organic carbon (SOC) density sampling points for observation 钻探资料, 通过解析这些钻探资料剖面图来确定风 化层的厚度。

表 1 研究中使用的环境协变量  
Table 1 Environmental covariates used in research   

<table><tr><td>类别Category</td><td>变量Variant</td><td></td><td>简写 Abbreviation 分辨率 Resolution</td></tr><tr><td>气候条件 Climate condition</td><td>年平均气温 Mean annual air temperature</td><td>MAAT</td><td>1 km</td></tr><tr><td></td><td>平均年降水量 Mean annual precipitation</td><td>MAP</td><td>1 km</td></tr><tr><td></td><td>降水标准差 Precipitation standard deviation</td><td>PSD</td><td>1 km</td></tr><tr><td></td><td>年平均太阳辐射量 Mean annual solar radiation</td><td>MASR</td><td>1 km</td></tr><tr><td></td><td>风速Wind speed</td><td>WS</td><td>1 km</td></tr><tr><td>土壤母质 Soil parent material</td><td>风化层厚度Regolith thickness</td><td>RT</td><td>100 m</td></tr><tr><td>地形条件 Topographic condition</td><td>高程 Elevation above sea level</td><td>DEM</td><td>250m</td></tr><tr><td></td><td>坡度 Slope gradient</td><td>SG</td><td>250m</td></tr><tr><td></td><td>Sin方位(与北方的角度距离) Sin aspect (angle distance from north)</td><td>SA</td><td>250m</td></tr><tr><td></td><td>平面曲率 Planform curvature</td><td>PLC</td><td>250m</td></tr><tr><td></td><td>剖面曲率 Profile curvature</td><td>PRC</td><td>250m</td></tr><tr><td></td><td>地形湿度指数 Topographic wetness index</td><td>TWI</td><td>250m</td></tr><tr><td></td><td>地形位置指数 Topographic position index</td><td>TPI</td><td>250m</td></tr><tr><td>植被Vegetation</td><td>平均归一化植被指数 Mean normalized difference vegetation index</td><td>MNDVI</td><td>500m</td></tr><tr><td></td><td>归一化植被指数的标准差 Standard deviation of normalized difference vegetation</td><td>SDNDVI</td><td>500 m</td></tr><tr><td>地表热条件 Land surface thermal conditions</td><td>白天最高地表温度 Daytime maximum land surface temperature</td><td>HDLST</td><td>1 km</td></tr><tr><td></td><td>平均白天地表温度 Daytime average land surface temperature</td><td>MDLST</td><td>1 km</td></tr><tr><td></td><td>白天地表温度的标准差 Standard deviation of daytime land surface temperature</td><td>SDDLST</td><td>1 km</td></tr><tr><td></td><td>夜间最高地表温度 Nighttime maximum land surface temperature</td><td>HNLST</td><td>1 km</td></tr><tr><td></td><td>平均夜间地表温度 Nighttime average land surface temperature</td><td>MNLST</td><td>1 km</td></tr><tr><td></td><td>夜间地表温度的标准差 Standard deviation of nighttime land surface temperature</td><td>SDNLST</td><td>1 km</td></tr><tr><td>土壤 Soil</td><td>地下水深度 Groundwater table depth</td><td>GWTD</td><td>1 km</td></tr><tr><td></td><td>平均土壤湿度 Mean of soil moisture</td><td>MSM</td><td>5km</td></tr><tr><td>人类活动因子</td><td>土壤水分标准偏差 Standard deviation of soil moisture</td><td>SDSM</td><td>5km</td></tr><tr><td>Humanactivity factor</td><td>人口密度 Population density</td><td>PD</td><td>1 km</td></tr><tr><td></td><td>建筑物体积 Built-up volume</td><td>BUV</td><td>100 m</td></tr><tr><td></td><td>道路网密度 Road network density</td><td>RD</td><td>1 km</td></tr><tr><td></td><td>人类热排放Hourly anthropogenic heat flux</td><td>HAHF</td><td>1 km</td></tr></table>

从“美国地质勘探局”(https://e4ftl01.cr.usgs.gov/)下 载 MODIS2004—2023 年 MOD13Q1 数 据 , 提 取250 m分辨率植被指数 16天合成产品, 并计算平均归一化植被指数 (MNDVI)。

2003—2018年的月平均土壤湿度数据来源于文献 [20], 用于计算平均土壤湿度及土壤水分标准差。地下水位深度数据来源于文献 [21]。

使用地表热条件的 6 个指标, 从“资源环境科学数据平台”获取了基于 MODIS 地表温度数据 LST每 8天 1 km数据产品, 并计算获取这些指标的 LST数据, 数据空间分辨率为 1 km, 时间分辨率为 2004—2023 年逐年度。

对于人类活动因子, 结合该地区经济和农业发展特点及考虑数据可获得性, 选取人口密度、建筑物体积、道路网密度和人类热排放 4 个因子。2019年 人 口 密 度 数 据 来 源 于“资 源 环 境 科 学 数 据 平台”[22]。2010 年建筑物体积数据来源于“GHSL-GlobalHuman Settlement Layer” (https://ghsl.jrc.ec.europa.eu/download.php ds=builtV)。 2022 年 道 路 网 密 度 数 据集来源于“全球变化科学研究数据出版系统”(https://www.geodoi.ac.cn/WebCn/doi.aspx?Id=752)。 2010 年人类热排放数据集由文献 [23] 获取。

使用最邻近方法将不同分辨率的类型协变量重新采样到 250 m, 使用 CUBIC 法将不同分辨率的数值协变量重新采样到 250 m[24]。

# 1.4 数据预处理

通过批量裁剪与重投影、重采样和统计计算等步骤, 将矢量格式的原始 SOC密度数据集转换为分辨率为 250 m 的栅格格式数据集。数据集叠加了 28个协变量, 包括更新了投影变换和重采样后的环境因子和人类活动因子。所有的数据处理和模型预测工作均在 Python环境中完成, 而地理空间分析则借

助 ArcGIS 软件实现。

# 1.5 建模与评估

本研究使用 RF构建基于环境协变量的 SOC密度预测模型。具体技术路线如图 2 所示。先进行数据准备, 检测清洗原始数据中异常值, 对环境协变量数据集、人类活动数据及采样点数据做归一化处理,消除量纲影响, 用 GridSearchCV 方法[25] 优化随机森林关键参数, n_estimator 的取值范围为 (50, 75, 100,125, 150, 200), max_depth 的 取 值 范 围 为 (3, 4, 5, 6),确定最优参数组合为 n_estimators=100、max_depth=4,其余参数保持默认, 平衡模型性能与计算效率。模型训练采用五折交叉验证。最后用平均绝对误差(MAE)、均方根误差 (RMSE)、决定系数 (R2)、林氏一致性相关系数 (LCCC)多维度评估模型性能, 计算五折交叉验证预测值标准差量化空间预测不确定性。

![](images/b36a87b5ce24b0d330db1896aa388881565f7e2fca0fe91cc087fb4bccd0b895.jpg)

![](images/a7f536c0337399a2809258b15a8fbace8b1a4de86852dee83908474d52e3af84.jpg)

![](images/8aa5ed8e364239e4a5a988fa16e3beda4da0f2905d426c7aa3f3579b49e30dcd.jpg)

![](images/ab0283ef42bbbe693e88b10b677016f0eeb258f41dee36a30eb69647214026f3.jpg)

![](images/31f6f8d11af3612943fa42a0b2d185bbe98e73cb630e8d377799942e7c41b704.jpg)

式中: h为预测的个数, r为皮尔逊相关系数, P 为 h点观测到的 SOC 密度值, Qh 为 h 点预测的 SOC 密度Qh值, 为Qh 的平均值,∂P 和∂Q 为Ph 和Qh 的方差。Nfolds=5Q(五折交叉验证), Q 表示第 i折的预测值, 表示所有折预测值的均值, σpred表示最终输出的不确定性度量。在模型建立过程中, 通过 RF模型计算每个特征在所有树中的平均不纯度减少量来评估其重要性[26]

为研究加入人类活动因子是否能改善 SOC密度的预测, 导出了 6 个不同类别的协变量池, 如表 2 所示。池 1只包含 24个环境变量。池 2\~5由 24个环境协变量, 再分别加人口密度、建筑物体积、道路网密度和人类热排放组成。池 6由 24个环境协变量和 4个人类活动协变量共同组成。针对这 6个协变量池, 建立了6个预测模型, 即模型1\~6。

# 2 结果与分析

# 2.1 土壤有机碳(SOC) 密度描述性统计

本研究共采用 151个 SOC密度样本点, SOC 密度 范 围 为 0.33\~11.55 kg·m‒2, 平 均 值 为 2.43 kg·m‒2,SOC 密度的标准差为 1.82 kg·m‒2, 表明数据有一定程

![](images/357509eae97f82b1a2e53cbe9cc3005cbe62ff80c4c09a0f01da3f0b6e418c00.jpg)  
图 2 基于随机森林模型的黄淮海平原耕地土壤有机碳(SOC)密度预测操作流程图  
Fig. 2 Operational flowchart of soil organic carbon (SOC) density prediction in cultivated land of Huang-Huai-Hai Plain based on random forest model

表 2 用于土壤有机碳 (SOC) 密度预测的 6 个不同协变量组合池 (含环境变量与人类活动因子)Table 2 Six covariate combination pools (including environmental variables and human activity factors) for soil organic carbon(SOC) density prediction  

<table><tr><td>池Pool</td><td>协变量 Covariate</td></tr><tr><td>池1 Pool 1</td><td>环境变量(表1)Environment variables (Table 1)</td></tr><tr><td>池2 Pool 2</td><td>环境变量(表1)+人口密度 Environment variables (Table 1) +population density</td></tr><tr><td>池3 Pool 3</td><td>环境变量(表1)+建筑物体积 Environment variables (Table 1)+built-up volume</td></tr><tr><td>池4 Pool 4</td><td>环境变量(表1)+道路网密度 Environment variables (Table1)+road network density</td></tr><tr><td>池5Pool 5</td><td>环境变量(表1)+人类热排放 Environment variables (Table 1)+ hourly anthropogenic heat flux</td></tr><tr><td>池6 Pool 6</td><td>环境变量(表1)+人口密度+建筑物体积+道路网密度和人类热排放 Environment variables (Tablel)+population density+built-upvolume+road network density+hourlyanthropogenic heat flux</td></tr></table>

度的离散性。偏度系数为 1.81, 显示数据分布右偏,存在少量高值样本点。变异系数为 74.66%, 表明样本点间的相对变动较大, 数据分布的波动性较强。

# 2.2 环境协变量特征相关性分析

为检验涵盖人为因子在内的所有协变量之间的相关性, 图 3 显示了 28 个协变量之间的偏相关系数矩阵, 其数值范围从‒0.82\~0.86; 同时通过双尾检验的显著性水平 (P 值) 对相关性强度进行验证, 进一步提升结果的可信度。从图中的具体关联特征可进一步观察到: 气候类因子间表现出较强的正向协同性, 例如年平均气温 (MAAT) 与年平均降水量 (MAP)、年平均太阳辐射量 (MASR) 与风速 (WS) 之间, 均呈现出高度显著正相关 (P<0.01); 而部分指数间则存在 明 显 的 负 向 关 联, 以 白 天 地 表 温 度 的 标 准差(SDDLST) 与平均土壤湿度 (MSM) 为例, 二者表现出高度显著负相关 (P<0.01); 值得注意的是, 人为因子中人类热排放 (HAHF) 也与高程 (DEM) 和地形湿度指数 (TWI) 等环境变量存在不同程度的显著相关,这一结果直观体现了人为活动与环境协变量之间的相互作用与关联特征。

# 2.3 协变量描述性统计

表3展示了所有采样点在28个协变量中的均值、标准差等统计特性。环境变量如高程 (DEM), 均值23.80 m、标准差 22.11 m, 反映研究区海拔起伏大,

![](images/900e9e5bf07f87844df1a8b2a0fa06a0a0408f2eb685948bea8f0efe92a7b4e1.jpg)  
图 3 协变量之间的偏相关性结果及显著性水平 (P 值)

\*表示 Pearson 相关分析中 P<0.05, 相关性具有统计学显著性; \*\*表示 P<0.01, 相关性具有高度统计学显著性 (双侧检验)。图中变量含义详见表 1。\* indicates statistical significance of correlation (P<0.05) in Pearson correlation analysis; \*\* indicates high statistical significance of correlation (P<0.01)(two-tailed test). The meanings of variables in the figure are detailed in Table 1.

Fig. 3 Results of partial correlation between covariates and level of significance (P value)

表 3 黄淮海平原耕地土壤有机碳(SOC)密度预测所用28个协变量的描述性统计 Table 3 Descriptive statistics of 28 covariates for soil organic carbon (SOC) density prediction in cultivated land of Huang-Huai-Hai Plain   

<table><tr><td rowspan="2">协变量Covariate</td><td rowspan="2">最大值 Maximum value Average value Minimum value Standard deviation</td><td rowspan="2">平均值</td><td rowspan="2">最小值</td><td>标准差</td></tr><tr><td></td></tr><tr><td>年平均气温 Mean annual air temperature/C</td><td>15.13</td><td>13.24</td><td>10.40</td><td>0.79</td></tr><tr><td>平均年降水量 Mean annual precipitation /mm</td><td>871.82</td><td>617.86</td><td>474.20</td><td>79.85</td></tr><tr><td>降水标准差 Precipitation standard deviation /mm</td><td>152.40</td><td>112.05</td><td>73.99</td><td>16.33</td></tr><tr><td>年平均太阳辐射量 Mean annual solar radiation /(J·m2-a-1)</td><td>16 411.00</td><td>15 864.96</td><td>14 789.00</td><td>297.01</td></tr><tr><td>风速Wind speed /(m·s-1)</td><td>4.29</td><td>3.20</td><td>2.20</td><td>0.79</td></tr><tr><td>风化层厚度 Regolith thickness /mm</td><td>470.12</td><td>139.06</td><td>16.11</td><td>87.68</td></tr><tr><td>高程 Elevation above sea level /m</td><td>113.00</td><td>23.80</td><td>5.00</td><td>22.11</td></tr><tr><td>坡度 Slope gradient /()</td><td>17.91</td><td>2.24</td><td>-0.31</td><td>2.64</td></tr><tr><td>Sin方位(与北方的角度距离)Sin aspect (angle distance from north)/()</td><td>389.40</td><td>150.96</td><td>-18.86</td><td>96.17</td></tr><tr><td>平面曲率Planform curvature</td><td>20 076 400 640.00</td><td>916 342 780.69</td><td>-7942 519 808.00 7942 519 808.00</td><td></td></tr><tr><td>剖面曲率 Profile curvature</td><td>8 155 319 808.00</td><td>385354</td><td>-10 921 600</td><td>2 900 322 618.86</td></tr><tr><td>地形湿度指数 Topographic wetness index</td><td>5 057 590.00</td><td>605.10 311 249.56</td><td>000.00 -222 214.00</td><td>937 171.25</td></tr><tr><td>地形位置指数 Topographic position index</td><td>22.36</td><td>-0.05</td><td>-7.12</td><td>3.77</td></tr><tr><td>平均归一化植被指数 Mean normalized difference vegetation index</td><td>0.87</td><td>0.61</td><td>0.06</td><td>0.24</td></tr><tr><td>归一化植被指数的标准差 Standard deviation of normalized difference vegetation</td><td>0.20</td><td>0.05</td><td>0.02</td><td>0.03</td></tr><tr><td>index 白天最高地表温度 Highest daytime land surface temperature /K</td><td>16 000.00</td><td>15 611.53</td><td>15 287.00</td><td></td></tr><tr><td>平均白天地表温度 Mean daytime land surface temperature /K</td><td>14 547.80</td><td>13 810.53</td><td>10 631.90</td><td>177.17</td></tr><tr><td>白天地表温度的标准差 Standard deviation of daytime land surface temperature /K</td><td>6 699.46</td><td>3260.69</td><td>1 770.85</td><td>601.23</td></tr><tr><td>夜间最高地表温度Highest nighttime land surface temperature /K</td><td>15 235.00</td><td>15 048.29</td><td>14 889.00</td><td>1050.82</td></tr><tr><td>平均夜间地表温度 Mean nighttime land surface temperature /K</td><td>13 936.20</td><td>13 026.38</td><td>11 102.20</td><td>57.69</td></tr><tr><td>夜间地表温度的标准差 Standard deviation of nighttime land surface temperature /K</td><td>6 147.68</td><td>3 616.93</td><td>1593.09</td><td>757.51</td></tr><tr><td>地下水深度 Groundwater table depth /m</td><td>51.59</td><td>2.36</td><td>-0.25</td><td>1 237.43</td></tr><tr><td>平均土壤湿度 Mean of soil moisture /(mm-)</td><td>0.59</td><td>0.35</td><td>0.03</td><td>8.07</td></tr><tr><td>土壤水分标准偏差 Standard deviation of soil moisture/(m·m-)</td><td>0.20</td><td>0.11</td><td>0.01</td><td>0.25</td></tr><tr><td>人口密度 Population density /(persons:km-2)</td><td>28 938.90</td><td>2 970.94</td><td>71.71</td><td>0.08</td></tr><tr><td>建筑物体积 Built-up volume /m</td><td>131 080.00</td><td>5010.44</td><td>0.00</td><td>7 901.32 20 540.63</td></tr><tr><td>道路网密度 Road network density/(m·km-2)</td><td>1593.00</td><td>49.26</td><td>-76.00</td><td>240.57</td></tr><tr><td>人类热排放Hourlyanthropogenic heatflux/(W·m-2)</td><td>2 231130.00</td><td>113 862.69</td><td>18935.00</td><td>315 465.78</td></tr></table>

水热、植被等差异会影响 SOC 积累; 人类活动类变量如人类热排放 (HAHF), 均值 113 862.69 W·m−2,最大值、最小值分别为 2 231 130.00 W·m−2、189 335W·m−2, 表明不同区域人类活动干扰程度不同。这些为后续分析协变量对 SOC 密度的影响提供基础。

# 2.4 协变量的重要性

图 4展示了 6个模型池中每个变量的相对重要性, 6个池中相同协变量的排名略有差异。这是因为在某个模型中给定变量的相对重要性取决于与其他变量的相关性[26]。

总体来看, 白天最高地表温度 (HDLST)、白天地 表 温 度 的 标 准 差 (SDDLST) 和 年 平 均 降 水 量(MAP)是 最 重 要的 3个 变 量, 相 对 重 要 性 合 计占SOC密度变化的 42.95%。对于人类活动因子来说,人口密度 (PD) 的相对重要性在模型 2 中排名第 9,相对重要性为 3.86% (图 4b); 建筑物体积 (BUV) 在模型 3 中排名第 24, 相对重要性为 0.79% (图 4c); 道路网密度 (RD) 在模型 4中排名第 25, 相对重要性为0.12% (图 4d); 人类热排放 (HAHF) 在模型 5 中排名第 4, 相对重要性为 8.46% (图 4e)。在包含全部 28 个协变量的模型 6 (图 4f) 中, 4 类人类活动因子的重要性差异显著, 其中人类热排放 (HAHF)虽位列第 4(8.25%), 却是最关键的人为驱动因子, 其相对重要性较排名第 11 位的人口密度 (PD, 2.90%) 高出 5.35 个百 分 点, 二 者 展 现 出 重 要 预 测 能 力; 建 筑 物 体积(BUV, 第 27 位, 0.58%)、道路网密度 (RD, 第 28 位,0.06%) 则排名靠后。

基于图 4f 单个环境变量的重要性排序, 本研究进一步量化了各变量类别对 SOC密度预测精度的相对贡献 (图 4g)。结果显示, 地表热条件类因子占比38.90%, 居主导地位; 其次为气候类因子, 占 比为17.12%; 人类活动类因子占 11.80%, 位列第 4。

![](images/c73d200ea06168fbaa27b863f80231ffff1649b8f09d83d800682878b364a0fc.jpg)

![](images/3b36f6708a7c8a4964e2ee93fc995ef046c7a4b2f44d4ff170229bf03d3f3a2e.jpg)  
各类别协变量的重要性 Importance of covariates by category   
图 4 通过随机森林(RF)计算6个模型的每个变量的相对重要性

图中变量符号表示的含义详见表 1。(a)、(b)、(c)、(d)、(e)、(f) 分别表示模型 1、2、3、4、5、6 中每个变量的相对重要性; (g) 表示各类别协变量的重要性。The meanings of variable symbols in the figure are detailed in Table 1. (a), (b), (c), (d), (e), and (f) respectively represent the relative im-portance of each variable in models 1, 2, 3, 4, 5, and 6; (g) indicates the importance of covariates in each category.

Fig. 4 Calculates the relative importance of each variable in six models using random forest (RF)

# 2.5 模型性能和空间差异

6个模型分别代表了 6种不同的协变量的组合,其 SOC 密度预测精度的量化指标如表 4 所示, 预测值与实测值的匹配特征则通过图 5 直观呈现。

由表 4 结果看出, 单个人类活动因子的加入均能提升预测精度, 人口密度 (PD)、建筑物体积 (BUV)、道路网密度 (RD) 和人类热排放 (HAHF) 分别使 R2提高 17.14%、11.43%、14.29%、28.57%。对比模型 6和模型 1, 模型 6 的 R2 提升 37.14%, 平均绝对误差降低 8.47%, 均方根误差降低 9.88%, LCCC 提高 19.67%。结合图 5的散点图可见: 随着人类活动因子的逐步加入 (图 5a-5f), 预测值与实测值的散点分布逐渐向1∶1 参考线 (实线) 靠拢, 拟合回归线 (虚线) 也更接近参考线, 尤其是模型 6 的散点集中程度最高、与参

表 4 黄淮海平原耕地土壤有机碳 (SOC) 密度预测中 6 种协变量组合模型的性能对比 Table 4 Performance comparison of six covariate combination models for soil organic carbon (SOC) density prediction in croplands of the Huang-Huai-Hai Plain   

<table><tr><td>模型 Model</td><td>协变量 Covariate</td><td>平均绝对误差 Mean absolute error</td><td>均方根误差 Root mean square error</td><td>决定系数R Coefficient of determination</td><td>林氏一致性相关系数 Lin&#x27;s concordance correlation coefficient (LCCC)</td></tr><tr><td>1</td><td>环境变量 Environment variable</td><td>1.18</td><td>1.72</td><td>0.35</td><td>0.61</td></tr><tr><td>2</td><td>环境变量+人口密度 Environment variable + population density</td><td>1.11</td><td>1.60</td><td>0.41</td><td>0.69</td></tr><tr><td>3</td><td>环境变量+建筑物体积 Environment variable + built-up volume</td><td>1.12</td><td>1.67</td><td>0.39</td><td>0.67</td></tr><tr><td>4</td><td>环境变量+道路网密度 Environment variable + road network density</td><td>1.14</td><td>1.59</td><td>0.40</td><td>0.67</td></tr><tr><td>5</td><td>环境变量+人类热排放 Environment variable + hourly anthropogenic heat flux 环境变量+人口密度+建筑物体积、</td><td>1.09</td><td>1.56</td><td>0.45</td><td>0.71</td></tr><tr><td>6</td><td>道路网密度和人类热排放 Environment variable + population density + built-up volume + road network density + hourly anthropogenic heat flux</td><td>1.08</td><td>1.55</td><td>0.48</td><td>0.73</td></tr></table>

![](images/6bbb1aa198b2793c2fc80dfae3288aedb6002bab00dba575427c61f92ca7c987.jpg)  
SOC 密度实测值 Measured SOC density /(kg·m−2)   
图 5 不同模型下土壤有机碳 (SOC) 密度实测值与预测值散点图

(a)、(b)、(c)、(d)、(e)、(f) 分别表示模型 1、2、3、4、5、6 的预测精度散点图。实线是 1∶1 参考线 (y=x 线), 虚线是预测值和实测值的拟合回归线。MAE: 平均绝对误差; RMSE: 均方根误差; LCCC: 林氏一致性相关系数。(a), (b), (c), (d), (e), and (f) represent the prediction accuracy scat-ter plots for models 1, 2, 3, 4, 5, and 6, respectively. The solid line represents the 1∶1 reference line (y=x line), and the dashed line represents the fitted regres-sion line between predicted values and measured values. MAE: mean absolute error; RMSE: root mean square error; LCCC: Lin’s concordance correlation coef-ficient.

Fig. 5 Scatter plots of measured and predicted soil organic carbon (SOC) densities under different models 考线的偏差最小, 进一步验证了 4 种人类活动因子结 合环境变量对黄淮海平原 SOC 密度的良好预测能力。

本研究从空间维度对比了未包含人类活动因子的模型 1 和全量纳入的模型 6。图 6a、6b 显示, 两模型预测的 SOC密度不确定性均呈现“北、中、东部低, 西北、东南部高”的特征, 但加入人类活动因子后, 模型 6在中部、南部地区的预测表现改善更显著, 这可能与该区域土地利用方式、农业活动强度等人类干扰特征密切相关。图 7a、7b 分别展示了模型1和模型6预测的SOC密度均值的空间分布情况。

模型 1显示, 研究区北部、中部及东部 SOC密度较低, 西北部和南部则为高值区且分布较广; 纳入人类活动因子后, 模型 6的预测分布整体趋势与模型 1一致, 但西北、西南地区的 SOC密度呈明显上升趋势。

# 3 讨论

# 3.1 环境协变量的相对重要性

SOC密度制图研究中, 地形、气候及植被等要素通常具有较高解释力, 被广泛用于 SOC 密度的预测和制图[27-29]。这些变量对 SOC 密度的影响因研究

![](images/28eefbfd37d64198d4269af94409dc5fee98da5e942dc3ebfe6921253bffa301.jpg)  
图 6 模型 1 (a) 和模型 6 (b) 预测的土壤有机碳 (SOC) 密度不确定性的空间分布情况

![](images/dd00e4506c007bffeaac456d74f8fcfa8c8787ad769bf5c2f373542d3b363377.jpg)  
Fig. 6 The spatial distribution of soil organic carbon (SOC) density uncertainty predicted by model 1 (a) and model 6 (b)   
图 7 模型 1 (a) 和模型 6 (b) 预测的土壤有机碳 (SOC) 密度均值的空间分布情况

Fig. 7 The spatial distribution of mean soil organic carbon (SOC) density predicted by model 1 (a) and model 6 (b)

区域与尺度的不同而变化, 因此其重要性分析受到广泛关注。

海拔是最重要的地形协变量。海拔与坡度等地形特征通过调控地表气候、水文循环 (如水流路径、速度[30] 及土壤水分保持[31]) 影响 SOC 输入与循环,进而间接作用于植被生长和土壤发育。气候作为土壤形成的核心因子显著影响 SOC 的空间变化[32]。研究表明, 降水和温度是影响 SOC空间变化的两个关键气候变量, 这一点在多个类似地区的研究中得到了证实[33]。本研究中, 平均年降水量对 SOC 密度的预测重要性远超年平均气温。二者都是通过调控碳输入与分解过程来影响 SOC 密度, 平均年降水量通过影响净初级生产力进而增加或减少碳输入, 同时高湿度环境还能促进母岩风化、增强土壤碳稳定性,进而减少 SOC分解[34], 年平均气温主要通过改变土壤微生物代谢活性与酶活性, 直接调控 SOC的分解速率[35]。平均归一化植被指数因能有效反映植被生长状况与生物量, 成为常用指标[36]。

# 3.2 人类活动因子的相对重要性

人类活动因素对土壤性质也有一定的影响。过去的 10年中, 许多研究分析了人类活动对 SOC密度预测的重要性[37]。其中, 城市化进程中产生的热排放对土壤性质的影响尤为显著。城市热岛效应不仅影响城市气候和生态系统, 还会改变土壤温度、水分状况和微生物活性, 进而影响土壤有机碳的动态[38]。李宇等[39] 基于 1960—2017年逐日气温数据的研究显示, 我国北部地区城市平均热岛强度显著高于南部, 其中华北地区最强, 年均强度达 (1.4±1.4)℃, 而升温会加快微生物代谢速率, 进而加剧土壤有机碳分解。与此同时, 人类活动引发的不透水地表扩张, 既降低水分保持能力与渗透性, 也能加速土壤水分蒸发、减少湿度, 直接影响 SOC的积累与稳定性。此外, 人类活动导致的土壤压实与结构破坏会缩减土壤孔隙度, 阻碍水分与空气交换, 进一步干扰 SOC的储存与转化过程。作为人类热排放的重要衍生效应,上述变化共同构成了城市环境中 SOC动态的关键驱动因素。人口密度、建筑物体积、道路网密度等会不同程度地影响 SOC 密度的空间变异。人口密度确定了人类对土壤的压力, 与前人的研究一致[40]。建筑物体积作为城市化进程中的一个重要组成部分, 通过改变地表覆盖影响地表和土壤温度, 还可通过改变地表径流和土壤水分状况等途径间接影响 SOC 的稳定性。道路网可能会改变地表水的流向, 增加径流速度, 导致土壤侵蚀, 进而影响 SOC的分布和稳定性。在研究道路网密度对 SOC密度影响方面需后期深入研究。

# 3.3 模型性能

表 4数据显示, 纳入人类活动因子的模型 6在SOC密度分布预测中显著优于仅含环境变量的模型1。 模 型 6 的 MAE (1.08) 和 RMSE (1.55) 分 别 较 模型 1 (1.18、1.72) 降低约 8.47% 和 9.88%, 预测误差更小; 其 R2 与 LCCC 也更高, 预测可靠性更强; 同时, 模型6对SOC密度变异的解释比例从模型1的35.00%提升至 48.00%, 充分证明人类活动因子是提升模型预测与解释能力的关键变量。

在进行 SOC密度预测时, 本研究的准确度结果(R2=0.48) 具有一定的可信度。例如, Wadoux 等[41] 对澳大利亚猎人山谷地区土壤总碳进行预测研究, 使用随机森林得到的 R2 为 0.35, 使用卷积神经网络(CNN) 得到的 R2 为 0.46。Zhao 等[42] 通过使用残差最大似然 (REML) 拟合的混合线性模型和回归克里金法 (RK) 对江苏省西北部农田区的 SOC 进行预测,得到了 R2=0.53 的结果。Qi 等[43] 使用 10 个协变量和随机森林方法对辽宁省的 SOC进行预测, 得到了R2=0.58 的结果。上述对比表明, 不同研究区、不同预测模型及不同协变量组合, 导致最终预测准确度出现合理差异, 但本研究的 R2=0.48处于已发表研究的合理结果区间内, 这证明了本研究预测模型的可靠性与结果的可信度。本研究在模型中纳入人类活动因子, 模型能达到与未纳入该因子的研究相近, 甚至更优的预测准确度, 进一步证实了人类活动因子对提升SOC密度分布解释力的积极作用。

# 3.4 局限与展望

本研究选取地下水深度、平均土壤湿度等参数作为 SOC密度预测变量, 存在一定局限性。黄淮海平原作为典型冲积平原, 土壤性质空间异质性显著,除水分外, 土壤 pH 值等关键理化性质对 SOC 空间分布亦有重要调控作用——其可通过影响微生物群落结构与酶活性, 直接改变有机质分解速率及稳定性。但目前区域内土壤 pH数据多来自离散采样点,存在空间分布不均、密度不足等问题, 难以全面表征区域尺度的空间变异特征; 即便通过统计学或机器学习方法进行空间预测, “以点代面”的模式仍难以捕捉精细格局。未来需系统探究土壤 pH 与其他理化性质的交互作用对 SOC 空间格局的影响机制, 以更全面揭示区域SOC密度的分布特征及驱动因素。

受数据获取限制, 农业管理措施、土壤扰动强度等重要人类活动数据未纳入预测模型, 而这类因子(如耕作方式、施肥制度等) 对 SOC密度动态变化影响显著, 其量化不足可能削弱模型的解释能力与预测精度; 同时, 现有人类活动数据时空分辨率偏低,难以准确反映其时空变异特征。未来研究需从 3方面强化: 1)系统收集农业管理、土地利用变化等人类活动数据; 2) 开发高精度的人类活动强度量化指标; 3)构建融入人类活动时空异质性的 SOC预测模型, 以提升模型性能并深化对 SOC密度动态变化的理解。

# 4 结论

为评估人类活动对黄淮海平原耕地表层 SOC密度分布的影响, 本研究选取人类热排放、人口密度、建筑物体积和道路网密度 4个人类活动因子展开分析,结果如下: 1)相较于仅用环境协变量的模型 1, 纳入4个人类活动因子的模型6预测性能显著提升。R2 提高 37.14%、一致性相关系数提高 19.67%, 平均绝对误差、均方根误差分别降低 8.47%、9.88%, 表明结合 4 类人类活动因子可有效优化该区域 SOC 密度制图精度。2)模型 6对SOC密度分布变异的解释率达48.00%, 较模型 1提升明显, 凸显人类活动因子对SOC 密度预测的补充价值。3) 4 个人类活动因子中,人类热排放重要性最高(总排名第 4, 相对重要性8.25%), 人口密度次之 (第 11 位, 2.90%); 建筑物体积(第 27 位, 0.58%) 与道路网密度 (第 28 位, 0.06%) 贡献较小。

综上, 黄淮海平原耕地 SOC密度预测需重点关注贡献度高的人类活动因子 (如人类热排放、人口密度), 同时可保留低贡献因子的潜在研究价值。未来可进一步探索各因子与 SOC 密度的交互作用及对土壤有机碳动态的联合影响。

# 参考文献 References

张军泽, 王帅, 赵文武, 等. 可持续发展目标关系研究进展[J].[1] 生态学报, 2019, 39(22): 8327−8337 ZHANG J Z, WANG S, ZHAO W W, et al. Research progress on the interlinkages between the 17 Sustainable Development Goals and their implication for domestic study[J]. Acta Ecologica Sinica, 2019, 39(22): 8327−8337   
张甘霖, 朱阿兴, 史舟, 等. 土壤地理学的进展与展望[J]. 地理[2] 科学进展, 2018, 37(1): 57−65 ZHANG G L, ZHU A X, SHI Z, et al. Progress and future prospect of soil geography[J]. Progress in Geography, 2018, 37(1): 57−65   
[3] 黄昌勇. 土壤学[M]. 北京: 中国农业出版社, 2000 HUANG C Y. Soil Science[M]. Beijing: China Agriculture Press, 2000   
[4] 赵明松, 张甘霖, 王德彩, 等. 徐淮黄泛平原土壤有机质空间 变异特征及主控因素分析[J]. 土壤学报, 2013, 50(1): 1−11 ZHAO M S, ZHANG G L, WANG D C, et al. Spatial variability of soil organic matter and its dominating factors in Xu-Huai alluvial plain[J]. Acta Pedologica Sinica, 2013, 50(1): 1−11   
JENNY H. Factors of soil formation[J]. Soil Science, 1941,[5] 52(5): 415   
ZHU X L, HELMER E H, GAO F, et al. A flexible[6] spatiotemporal method for fusing satellite images with different resolutions[J]. Remote Sensing of Environment, 2016, 172: 165−177   
杨阳, 王宝荣, 窦艳星, 等. 植物源和微生物源土壤有机碳转[7] 化与稳定研究进展[J]. 应用生态学报, 2024, 35(1): 111−123 YANG Y, WANG B R, DOU Y X, et al. Advances in the research of transformation and stabilization of soil organic carbon from plant and microbe[J]. Chinese Journal of Applied Ecology, 2024, 35(1): 111−123   
MCBRATNEY A B, MENDONÇA SANTOS M L, MINASNY[8] B. On digital soil mapping[J]. Geoderma, 2003, 117(1/2): 3−52   
何林倩, 刘倩, 王德彩, 等. 基于数字土壤制图技术的土壤有[9] 机碳储量估算[J]. 应用生态学报, 2021, 32(2): 591−600 HE L Q, LIU Q, WANG D C, et al. Estimation of soil organic carbon storage based on digital soil mapping technique[J]. Chinese Journal of Applied Ecology, 2021, 32(2): 591−600   
张晓婷, 黄魏, 傅佩红, 等. 基于特征筛选算法的数字土壤制[10] 图研究[J]. 土壤学报, 2024, 61(3): 635−647 ZHANG X T, HUANG W, FU P H, et al. Research on digital soil mapping based on feature selection algorithm[J]. Acta Pedologica Sinica, 2024, 61(3): 635−647   
廖启林, 华明, 张为, 等. 人为活动对江苏土壤元素含量分布[11] 的影响[J]. 地质学刊, 2012, 36(2): 147−156 LIAO Q L, HUA M, ZHANG W, et al. Influence of human activities on soil element distributions in Jiangsu[J]. Journal of Geology, 2012, 36(2): 147−156   
王高起, 袁丹, 吴萍, 等. 深层土壤有机碳储量、稳定性以及[12] 对人类活动响应的研究进展[J]. 中国生态农业学报 (中英文), 2025, 33(3): 435−448 WANG G Q, YUAN D, WU P, et al. Research advances on deep soil organic carbon storage, stability and responses to human activities[J]. Chinese Journal of Eco-Agriculture, 2025, 33(3): 435−448   
洪舒蔓, 郝晋珉, 艾东, 等. 基于人地关系的黄淮海平原土地[13] 整治策略[J]. 农业工程学报, 2013, 29(24): 251−259 HONG S M, HAO J M, AI D, et al. Land consolidation strategies in Huang-Huai-Hai Plain based on man-earth relationship[J]. Transactions of the Chinese Society of Agricultural Engineering, 2013, 29(24): 251−259   
刘冉, 孙劭, 鞠蕾, 等. 黄淮海平原气象干旱的演化特征与时[14] 空规律[J]. 农业工程学报, 2023, 39(19): 85−92 LIU R, SUN S, JU L, et al. Evolutionary characteristics and spatiotemporal trend of meteorological drought in the Huang-Huai-Hai Plain[J]. Transactions of the Chinese Society of Agricultural Engineering, 2023, 39(19): 85−92   
吴凯, 谢贤群. 黄淮海平原化肥用量的时间序列分析及其对[15] 农业发展的正负效应[J]. 农业环境科学学报, 2002, 21(6): 516−518, 523 WU K, XIE X Q. Time series analysis of applied fertilizer and its positive and negative effects on agricultural development in the Huang-Huai-Hai Plain[J]. Journal of Agro-Environmental Science, 2002, 21(6): 516−518, 523   
赵炳梓, 张佳宝, 周凌云, 等. 黄淮海地区典型农业土壤中六[16] 六六 (HCH) 和滴滴涕 (DDT) 的残留量研究Ⅰ. 表层残留量 及其异构体组成[J]. 土壤学报, 2005, 42(5): 761−768 ZHAO B Z, ZHANG J B, ZHOU L Y, et al. Residues of HCH and DDT in typical agricultural soils of Huang-Huai-Hai Plain, China Ⅰ. Residues in surface soils and their isomeric composition[J]. Acta Pedologica Sinica, 2005, 42(5): 761−768   
侯满平, 郝晋珉, 李新波, 等. 黄淮海平原农业结构调整及其[17] 模式探讨[J]. 农业工程学报, 2004, 20(3): 286−291 HOU M P, HAO J M, LI X B, et al. Agricultural structure adjustment and mode in Huang-Huai-Hai Plain[J]. Transactions of the Chinese Society of Agricultural Engineering, 2004, 20(3): 286−291   
任频频, 黄峰, 李保国. 黄淮海平原旱作农田土壤有机质含量[18] 的空间分异特征[J]. 土壤学报, 2022, 59(2): 440−450 REN P P, HUANG F, LI B G. Spatial differentiation characteristics of soil organic matter in dry farmland in the Huang-Huai-Hai Plain[J]. Acta Pedologica Sinica, 2022, 59(2): 440−450   
YAN F P, SHANGGUAN W, ZHANG J, et al. Depth-to-[19] bedrock map of China at a spatial resolution of 100 meters[J]. Scientific Data, 2020, 7: 2   
MENG X J, MAO K B, MENG F, et al. A fine-resolution soil[20] moisture dataset for China in 2002–2018[J]. Earth System Science Data, 2021, 13(7): 3239−3261   
FAN Y, LI H, MIGUEZ-MACHO G. Global patterns of[21] groundwater table depth[J]. Science, 2013, 339(6122): 940−943   
VENTER O, SANDERSON E W, MAGRACH A, et al. Global[22] terrestrial human footprint maps for 1993 and 2009[J]. Scientific Data, 2016, 3: 160067   
VARQUEZ A C G, KIYOMOTO S, KHANH D N, et al. Global[23] 1-km present and future hourly anthropogenic heat flux[J]. Scientific Data, 2021, 8: 64   
NING L X, CHENG C X, LU X, et al. Improving the prediction[24] of soil organic matter in arable land using human activity factors[J]. Water, 2022, 14(10): 1668   
ZHI J J, ZHANG G L, YANG F, et al. Predicting mattic[25] epipedons in the northeastern Qinghai-Tibetan Plateau using Random Forest[J]. Geoderma Regional, 2017, 10: 1−10   
SHI J J, YANG L, ZHU A X, et al. Machine-learning variables[26] at different scales vs. knowledge-based variables for mapping multiple soil properties[J]. Soil Science Society of America Journal, 2018, 82(3): 645−656   
ADHIKARI K, HARTEMINK A E, MINASNY B, et al. Digital[27] mapping of soil organic carbon contents and stocks in Denmark[J]. PLoS One, 2014, 9(8): e105519   
STUMPF F, KELLER A, SCHMIDT K, et al. Spatio-temporal[28] land use dynamics and soil organic carbon in Swiss agroecosystems[J]. Agriculture, Ecosystems & Environment, 2018, 258: 129–142   
SONG X D, YANG F, JU B, et al. The influence of the[29] conversion of grassland to cropland on changes in soil organic carbon and total nitrogen stocks in the Songnen Plain of Northeast China[J]. Catena, 2018, 171: 588−601   
[30] WIESMEIER M, URBANSKI L, HOBLEY E, et al. Soil organic carbon storage as a key function of soils — A review of drivers and indicators at various scales[J]. Geoderma, 2019, 333: 149−162   
ZHOU Y, HARTEMINK A E, SHI Z, et al. Land use and[31] climate change effects on soil organic carbon in North and Northeast China[J]. Science of the Total Environment, 2019, 647: 1230−1238   
MALLICK J, ALMESFER M K, SINGH V P, et al. Evaluating[32] the NDVI–rainfall relationship in Bisha watershed, Saudi Arabia using non-stationary modeling technique[J]. Atmosphere, 2021, 12(5): 593   
WANG S, ZHUANG Q L, WANG Q B, et al. Mapping stocks[33] of soil organic carbon and soil total nitrogen in Liaoning Province of China[J]. Geoderma, 2017, 305: 250−263   
CHAPLOT V, BOUAHOM B, VALENTIN C. Soil organic[34] carbon stocks in Laos: Spatial variations and controlling factors[J]. Global Change Biology, 2010, 16(4): 1380−1393   
CONANT R T, RYAN M G, ÅGREN G I, et al. Temperature[35] and soil organic matter decomposition rates-synthesis of current knowledge and a way forward[J]. Global Change Biology, 2011, 17(11): 3392−3404   
WANG Y, WANG S, ADHIKARI K, et al. Effect of cultivation[36] history on soil organic carbon status of arable land in northeastern China[J]. Geoderma, 2019, 342: 55−64   
GRUNWALD S, THOMPSON J A, BOETTINGER J L. Digital[37] soil mapping and modeling at continental scales: Finding solutions for global issues[J]. Soil Science Society of America Journal, 2011, 75(4): 1201−1213   
卞韬, 任国玉, 刘思廷, 等. 石家庄城市热岛效应: 从冠层、表[38] 层到土壤深层[J]. 气候与环境研究, 2023, 28(4): 409−419 BIAN T, REN G Y, LIU S T, et al. Urban heat island effect in Shijiazhuang: From the canopy to the surface and deep layers of soil[J]. Climatic and Environmental Research, 2023, 28(4): 409−419   
李宇, 周德成, 闫章美. 中国 84 个主要城市大气热岛效应的[39] 时 空 变 化 特 征 及 影 响 因 子 [J]. 环 境 科 学 , 2021, 42(10): 5037−5045 LI Y, ZHOU D C, YAN Z M. Spatiotemporal variations in atmospheric urban heat island effects and their driving factors in 84 major Chinese cities[J]. Environmental Science, 2021, 42(10): 5037−5045   
LIU X, HERBERT S J, HASHEMI A M, et al. Effects of[40] agricultural management on soil organic matter and carbon transformation — A review[J]. Plant, Soil and Environment, 2006, 52(12): 531−543   
WADOUX A M J, PADARIAN J, MINASNY B. Multi-source[41] data integration for soil mapping using deep learning[J]. Soil, 2019, 5(1): 107−119   
ZHAO M S, ROSSITER D G, LI D C, et al. Mapping soil[42] organic matter in low-relief areas based on land surface diurnal temperature difference and a vegetation index[J]. Ecological Indicators, 2014, 39: 120−133   
QI L, WANG S, ZHUANG Q L, et al. Spatial-temporal changes[43] in soil organic carbon and pH in the Liaoning Province of China: A modeling analysis based on observational data[J]. Sustainability, 2019, 11(13): 3569