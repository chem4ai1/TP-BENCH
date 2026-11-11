# 天山中段土壤有机碳空间预测及主控因子分析

何戩兰¹，闫庆武'，陈奕云²，李珂頎¹，白俊平³，吴子豪'(1.中国矿业大学公共管理学院,江苏 徐州221116；2.武汉大学资源与环境科学学院,湖北 武汉 430079;3.新疆送变电有限公司,新疆 乌鲁木齐830063)

摘要：精准刻画天山中段土壤有机碳(SoilOrganic Carbon,SOC)的空间格局并揭示其主要影响因子,对于评估土壤质量、实现固碳增汇和保障生态安全具有重要意义。然而,由于天山地区内,尤其是近天山地区和远离天山地区的地形、降雨量、蒸发量、植被覆盖和土壤pH差异显著,整体生态条件复杂,导致区域SOC存在高度空间异质性,这为利用数字土壤制图技术实现SOC精确制图带来了极大的挑战。本文基于463个土壤采样数据,结合极限梯度提升树（eXtreme Gradient Boosting,XGB)等多种机器学习模型获取了SOC的空间分布图,并使用 SHAP(Shapley Addi-tive exPlanations)算法揭示了SOC空间分异的主要影响因子。结果表明:XGB模型的拟合效果最优,其拟合R达到0.716、LCCC达到0.824,而RMSE仅为1.554g·kg"。该地区SOC的空间分布呈现出北高南低的特征。通过 SHAP算法进一步发现,该地区SOC含量主要受到pH、海拔与年均降水量的影响。且偏依赖图结果表明,环境变量与SOC均存在阈值效应。当pH高于7.8、年均蒸发量高于620mm,或年均降雨量低于300mm、植被净初级生产力低于130gC·m2·a时,SOC 含量骤降,这表明控制土壤pH蒸散量、植被的生长情况有利于区域土壤固碳增汇。应该通过使用酸性改良剂、施用有机肥、保证农业灌溉等手段调节该地区影响 SOC的关键变量的取值,进而实现提升SOC含量的目标。本研究证实了考虑土壤pH、海拔、年均降水量等变量的重要性,研究成果为天山中段土壤碳汇管理提供了数据支撑，也为其他干旱半干旱地区的SOC数字制图提供了参考。

关键词：土壤有机碳；干旱半干旱地区；空间制图；主控因子；天山中段

土壤有机碳(Soil Organic Carbon,SOC)是指土壤中所有有机碳的总和,它对于维系土壤的肥沃度、保持土壤水分和改善土壤质量发挥着关键作用[2]。我国陆地生态系统土壤有机碳库中，约有12.24%的储量位于干旱半干旱地区[3]。然而干旱半干旱地区植被覆盖稀疏、土壤侵蚀严重，其生态较为脆弱，这直接影响了该地区碳汇功能的表现,容易造成SOC的流失。而在地形复杂的干旱半干旱地区，地形起伏导致水热资源分布不均,影响到区域土壤属性、植被覆盖情况，进而导致SOC空间格局复杂多变。这不仅加剧了生态脆弱性和SOC流失风险，更使得此类地区SOC的高精度空间数字化制图长期面临严峻挑战。通过分析影响SOC空间分异的因素，明确其影响机理,不仅可以为区域生态恢复和土地管理提供重要参考，还有利于提升研究区SOC的预测精度。诸多大尺度研究表明，气温和降水量等气候因子是SOC的主控因子。例如,Zhuo等[4的研究指出，在中国东北和华北地区,年均气温与年均降水量对不同土壤深度的土壤有机碳(SOC)密度具有显著的调控作用。类似的,缪琦等[5]发现,在大区域尺度上,年均气温与年均降水量共同影响中国西南地区森林SOC密度。但是干旱半干旱区，蒸发量大，并且土壤质地较粗,保水保肥能力差，导致土壤含水量低,盐分含量高,植被难以生长。因此,土壤水分和盐分含量成为制约SOC积累的关键因子。Yang等[通过研究验证了祁连山森林草原SOC与土壤pH呈显著负相关;常帅等[的研究揭示了内蒙古锡林郭勒草原SOC与pH呈极显著负相关关系，而与土壤含水量呈极显著正相关关系。尽管现有研究发现水分和盐度相关因子可能是SOC的主要影响因子，但它们还较少被用于干旱半干旱地区SOC空间制图。

在以往的研究中，学者们通常选取地理加权回归（Geographically Weighted Regression,GWR)或多尺度地理加权回归（Multiscale Geographically WeightedRegression,MGWR)去探索变量的局部空间关系与空间异质性。例如,韩雅等[8利用GWR揭示气候因子对NDVI影响的空间异质性;宋颖等[9利用MGWR探究了环境因子与土壤盐渍化之间的空间非平稳特征。虽然,这两种空间回归模型都能够灵活地捕捉和分析空间数据的局部异质性,但是仍有两个缺点。首先,这两种模型假定自变量与因变量之间为线性关系[1],然而诸多实验证明,SOC及其潜在影响因子之间的关系是更为复杂的非线性关系[1I-13]。并且GWR和MGWR高度依赖空间相关性，而当样点密度不足时，其结果的可靠性大大降低。近年来，随机森林（Random Forest,RF）、支持向量机（SupportVectorMachine,SVM）、神经网络（ArtificialNeuralNetwork,ANN)等模型因其强大的预测能力在土壤学相关的研究中被广泛运用[14-15]。但由于机器学习模型具有"黑盒"的特性,使得模型预测的直接解释性受限。为了解析这些模型在SOC空间分异预测中的关键影响因子,研究者越来越多地依赖于例如

SHAP这类可解释性方法进行事后推断分析。将机器学习或深度学习模型与SHAP可解释性算法相结合，可以有效揭示局部主控因子，为理解和分析模型的预测结果提供强有力的支撑。

天山中段位于新疆中部，属于温带大陆性气候,是典型的干旱半干旱地区。因此,本研究以天山中段为研究区，使用可解释机器学习模型获取SOC空间分布图,并揭示其局部主控因子。首先对比传统的空间回归模型GWR以及机器学习模型RF、梯度提升决策树（Gradient Boosting DecisionTree,GBDT）、XGB、深度神经网络(Deep Neural Net-works,DNN）、卷积神经网络（ConvolutionalNeuralNetworks,CNN)的预测性能,并通过模型训练与变量筛选,选择出表现最佳的模型与环境变量进行空间制图,最后结合SHAP算法,探索分析影响研究区域的主要环境变量及其影响机理,并给出有针对性的土壤管理建议。

# 1材料与方法

# 1.1研究区概况

天山中段位于新疆中部（75°31'\~9154'E,3934'\~4612'N)(图1),总面积达56.86×10km²。该地区整体地势呈现出南部高、北部低的特点。天山注：底图采用国家地理信息公共服务平台标准地图制作,审图号为GS(2024)0650,对底图边界无修改。下同。

![](images/6fbc2c986c775a0e34d6a4276d486caefdfa009259c41e681fd3850f054d6502.jpg)  
图1研究区位置及采样点分布  
Fig.1 Location of study area and distribution of sampling points

中段地处亚欧大陆中部,远离海洋。但来自大西洋的部分水汽抵达此处时，会受到天山山脉的阻挡。这使得天山北坡降水量相对丰富，而南坡则降水量较少。但总体而言，该地区的降水量仍然有限，且该区域蒸发作用强烈。这些因素共同作用，导致天山中段的植被覆盖度相对较低,土壤盐碱化情况严重。天山中段土壤质地较粗,土壤中砾石含量较高，土壤结构相对松散,保水保肥能力较弱。

# 1.2土壤样品采集及化学分析

利用随机抽样方法于2005年从研究区内采集了463个土壤样本(0\~30cm)。土壤样品在实验室自然干燥,研磨,筛选,然后使用Walkley-Black湿氧化法测定SOC含量。

# 1.3环境变量及预处理

依据SCORPAN模型以及结合研究区实际情况,共选取了20个可能对研究区SOC含量产生影响的环境变量，具体变量名称、所属类别、空间分辨率及数据来源见表1,各变量的空间分布见图2。其中，高程数据来源于ASTERGDEM数据,根据高程计算出坡度。对全部环境变量数据,利用ArcGIS重采样为1km分辨率。此外,在模型拟合前,将类别变量通过独热编码转换为哑变量。

# 1.4研究方法

1.4.1随机森林(RF）RF是一种基于bagging的集成学习算法，它以决策树作为基学习器,通过组合各棵决策树的预测结果来提升预测的准确性[16-17]。它在多个自助采样得到的子集上独立构建决策树，并在每个节点随机选择特征进行分裂,然后将多个决策树的预测结果进行平均或加权平均得到最终预测的结果。RF擅长处理高维度或大规模的数据、能够捕捉到数据间的非线性关系,并且它具有优异的泛化能力，能够有效降低过拟合的风险。

在本研究中，采用了Python语言平台中"scikit-learn”库内的“RandomForestRegressor"来实现随机森林模型。本研究随机森林模型中设置决策树的数量为50,决策树最大深度为5,并且设置"max_fea-tures='sqrt'"以确保决策树分裂时考虑的特征数量为输入特征总数的平方根。

1.4.2梯度提升决策树(GBDT）GBDT是一种基于boosting的集成学习算法，它同样以决策树作为基学习器[18-19]。它构建了损失函数,并且以损失函数的梯度作为提升方向,每一轮迭代过程中,都会在已有的决策树模型基础上增加新的决策树,以此最小化损失函数。GBDT可以灵活处理不同类型的数据，并且对于异常值、缺失值具有一定鲁棒性,其预测精度相对较高。

表1环境变量信息  
Tab.1 Information pertaining to environmental variables   

<table><tr><td>类别</td><td>影响因子</td><td>空间分辨率</td><td>数据来源</td></tr><tr><td>土壤属性(S)</td><td>土壤类型</td><td>1 km</td><td>国家地球系统科学数据中心(https://www.geodata.cn)</td></tr><tr><td></td><td>粉粒含量 砂粒含量</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>黏粒含量</td><td></td><td></td></tr><tr><td></td><td>全氮</td><td>90m</td><td></td></tr><tr><td></td><td>全磷</td><td></td><td></td></tr><tr><td></td><td>全钾</td><td></td><td></td></tr><tr><td></td><td>pH</td><td></td><td></td></tr><tr><td></td><td>砾石含量</td><td></td><td></td></tr><tr><td></td><td>土壤厚度</td><td></td><td></td></tr><tr><td></td><td>土壤湿度</td><td>0.05°</td><td>国家生态科学数据中心(https://www.nesdc.org.cn/)</td></tr><tr><td>气候因子(C)</td><td>年均气温</td><td>1 km</td><td>国家青藏高原科学数据中心(http://data.tpdc.ac.cn)</td></tr><tr><td></td><td>年均降水量</td><td></td><td></td></tr><tr><td></td><td>年均蒸发量</td><td></td><td></td></tr><tr><td>有机体(0)</td><td>土地利用类型</td><td>1 km</td><td>资源环境科学与数据平台(https://www.resdc.cn/)</td></tr><tr><td></td><td>最大NDVI</td><td></td><td>国家生态科学数据中心(https://www.nesdc.org.cn/)</td></tr><tr><td></td><td>植被净初级生产力</td><td></td><td>国家地球系统科学数据中心(https://www.geodata.cn)</td></tr><tr><td></td><td>人口密度</td><td>1 km</td><td>WorldPop(https://hub.worldpop.org/)</td></tr><tr><td>地形因子(R)</td><td>海拔</td><td>1 km</td><td>地理空间数据云(https://www.gscloud.cn）</td></tr><tr><td></td><td>坡度</td><td></td><td></td></tr></table>

![](images/c9dc160277faebcc76d3f7126ec430c4e09fe7f6e9fe4881dc97ffbf3c151f19.jpg)  
图2环境变量空间分布  
Fig.2 Spatial distribution of environment variables

在本研究中,采用了Python语言平台中"scikit-learn”库内的“GradientBoostingRegressor”来实现GBDT模型。经过多次实验尝试,GBDT模型中决策树的棵数设置为150,决策树最大深度为6,决策树分裂时考虑的特征数量为输入特征总数的平方根（max_features=‘sqrt'）,并且该模型的学习率设置为0.01。

1.4.3极限梯度提升树（XGB）XGB同样是一种基于boosting的集成学习算法，它是GBDT的一种提升[20-21]。XGB相对于GBDT,引人了正则化项,能够有效防止过拟合。并且XGB可以并行计算,进而提升了算法的效率。

在本研究中,采用了Python 语言平台中的"xg-boost"库实现了XGBoost模型。对模型的关键参数进行了细致的调整，以优化其性能。在模型中，设置决策树的棵数设置为30,决策树最大深度为3,学习率为0.1。并且将类别数据指定为"category”,这样就无需对其进行额外的独热编码处理。

1.4.4深度神经网络(DNN）DNN是一种深度学习模型。相对于传统的人工神经网络,它具有更多的隐藏层,并且DNN相邻层间的神经元两两相连[22]。通过采用这种神经网络架构,DNN能够高效地整合大量参数、自动提取特征并进行学习,这一特点减少了它对手工特征工程的依赖。DNN具有非常强大的学习能力,通过学习复杂的数据模式,解决一些复杂的非线性问题。

在本研究中，采用Python语言设计了DNN模型，它包含4个全连接层，每层后接批量归一化和Dropout层,以增强模型的泛化能力。模型中使用了ReLU激活函数来引入非线性;设置Dropout率为0.2以减少过拟合;设置模型训练的epoch数为100,以确保模型充分学习。

1.4.5卷积神经网络（CNN）CNN同样是一种深度学习架构，它适合用于处理图像等具有网格结构的数据,在处理非图像数据时同样有良好的应用表现[23]。CNN通过卷积层自动提取局部特征,并通过池化层降低特征的空间维度，能够有效捕捉局部特征的层次结构和空间相关性,进而提升预测的准确性。

在本研究中,使用Python语言构建了一个CNN模型,包含2个卷积层,每个卷积层后接批量归一化和最大池化层。模型使用3×1的卷积核,第一个卷积层有64个滤波器，第二个有128个。池化层使用2×2的窗口，步长为2。卷积层输出通过全连接层映射到64维,再通过Dropout层减少过拟合。最终,输出层将特征映射到1维,用于回归预测。

1.4.6 SHAP SHAP是一种基于博弈论的用于解释机器学习预测结果的算法[24]。SHAP利用Shapley值来量化模型的全局或局部解释,Shapley值代表了机器学习模型中每个特征的边际贡献,即体现出该特征对预测结果的影响。在回归分析中，如果一个特征的SHAP值为零,这意味着该特征的存在与否并未改变模型的预测，即它对预测结果没有显著作用。若SHAP值为正值，则意味着该特征的存在推动了预测值超出平均预测的水平;若为负值,则表示该特征拉低了预测值,使其低于平均预测的水平。

在本研究中,采用了Python 语言平台中的 shap库来计算每个变量的SHAP值，同时绘制了特征的相对重要性图、变量间的偏依赖图等。

# 1.5模型评估与不确定性分析

在本研究中，利用bootstrap方法评估SOC 的含量以及进行不确定性分析。463个研究样本被随机划分为校正集(70%,n=324)与验证集(30%,n=139)两个部分。

模型评估使用了3个指标,分别是R、RMSE以及LCCC。

![](images/56e25cc62900587a8348dcf961c783a868cf7367de42555970a86db40806f0a9.jpg)

![](images/5238b10c4e77dbc4b7bcf1e7a2d429a82300a124f832ffef549002fc20d4ffe1.jpg)

![](images/502c4ad191e45fe97819d3aec34537664b13db0157c924345854e0d6d32a4591.jpg)

式中：n代表样本的数量；A代表第i个样本中SOC含量的测量值；A代表所有样本SOC含量的平均值；B代表第i个样本中SOC含量的预测值。LCCC全称是一致性相关系数,通常用于表示两组数据之间的相关性，它的取值为-1\~1,当LCCC的绝对值越接近于1时,证明数据间的一致性越强。r代表测量值与预测值之间的皮尔逊相关系数；0A与θB分别代表第n个样本测量值与预测值的变异系数；A与B分别代表所有样本SOC测量值与预测值的平均值。对于大部分模型,如果它拥有更高的R、LCCC以及更低的RMSE,则说明这个模型的性能更好。

不确定性图通常用于展示模型预测的置信区间。在本文中，从6种不同的预测模型中选出表现最优者,利用该模型重复训练100次得到100个训练好的模型。再利用100个模型对每个像素的预测值、标准差进行了计算,并以预测的平均值来确定最终SOC预测图像。

# 2结果与分析

# 2.1 描述性统计

图3展示了研究区内采样点的分布情况及各点SOC 含量。在采样点中，SOC的含量范围为0.05\~24.33g·kg−1,平均值为2.11g·kg1,标准差为2.86g

![](images/1228cd2b153bf7d0d2dacb00cadcea1490237b039a30ea54420dce8b95593e91.jpg)  
图3研究区SOC描述性统计结果  
Fig. 3 SOC descriptive statistical results of the study area

kg-。偏度为4.08,表明采样点的S0C含量分布具有明显的正偏；峰度为19.35,表明数据呈现尖峰态分布。

# 2.2模型性能比较

GWR、RF、GBDT、XGB、DNN、CNN模型分别结合特征选择方法，筛选出最优特征,并进行预测的结果如表2所示。GWR在校正集的表现尚可，其拟合R达到0.746,而在验证集中,GWR性能极低，预测R为负值，并且其RMSE和LCCC的值分别是所有模型中最高与最低的，证明GWR在本实验中无法提供可靠的预测结果。3个机器学习模型拟合R均大于0.9,而深度学习模型DNN与CNN的拟合优度分别为0.725与0.716,其在校正集的表现不如机器学习模型,但二者的拟合R与预测R更接近。尽管如此,DNN与CNN在验证集上的预测表现仍略低于3个机器学习模型。

表2模型性能表现  
Tab.2 Evaluation of model performance   

<table><tr><td>模型</td><td>拟合R</td><td>预测R</td><td>RMSE</td><td>LCCC</td></tr><tr><td>GWR</td><td>0.746</td><td>-0.827</td><td>3.702</td><td>-0.018</td></tr><tr><td>CNN</td><td>0.716</td><td>0.668</td><td>1.673</td><td>0.782</td></tr><tr><td>DNN</td><td>0.725</td><td>0.680</td><td>1.616</td><td>0.800</td></tr><tr><td>GBDT</td><td>0.920</td><td>0.682</td><td>2.507</td><td>0.778</td></tr><tr><td>RF</td><td>0.905</td><td>0.688</td><td>1.576</td><td>0.808</td></tr><tr><td>XGB</td><td>0.903</td><td>0.716</td><td>1.554</td><td>0.824</td></tr></table>

在5个模型中，XGB具有最高的预测R、LCCC以及最低的RMSE,它是6个模型中综合表现最佳的。在本数据集中,XGB模型最重要的12个环境变量分别是：土地利用类型、植被净初级生产力、年均蒸发量、年均降水量、年均气温、人口密度、全钾、pH、全氮、粉粒含量、砂粒含量、海拔。

# 2.3 S0C全局和局部主控因子研究

如图4所示，基于变量筛选后保留的12个变量中,pH是影响SOC空间分异的核心主导因子,其平均绝对 Shapley值超过0.5g·kg"1,显著高于其他变量。海拔作为第二重要的环境变量，其平均绝对Shapley值在0.35g·kg-1左右。年均降水量与植被净初级生产力贡献程度相近，介于0.23\~0.25g·kg-区间内。人口密度与年均蒸发量的平均绝对Shapley值略高于0.1g·kg"1,贡献程度有限。剩余的6个变量全钾、全氮、土地利用类型、粉粒含量、年均气温与砂粒含量的平均绝对Shapley值均小于0.1g·kg"1,证明这些变量对SOC变异的解释贡献相对微弱。

基于各采样点环境变量的平均绝对 Shapley值进行排序，识别出主导SOC空间变异的前两位影响因子，分别如图5a、图5b所示。由图5a可知，各采样点中的首要影响因子共有7类,分别是pH、植被净初级生产力、人口密度、海拔、年均降水量、全氮、全钾。其中，采样点中以pH作为首要影响因子的有337个，占采样点总数的72.79%;以植被净初级生产力为首要影响因子的有61个，占采样点总数的13.17%。以另外5个变量作为首要影响因子的采样点数量均≤20个。pH属于土壤属性,而植被净初级生产力归属于有机体类别。根据图5b可知,各采样点中的第二影响因子共有9个类别,相较于首要影响因子,第二影响因子新增了粉粒含量、年均蒸发量、土地利用类型3个环境变量，缺少了全钾。其中以海拔、年均降水量、pH作为第二影响因子的采样点最多，分别有165个、159个、92个，属于上述三者的采样点占到总数的89.85%。有92.66%的采样点以pH作为首要或第二影响因子,证明pH对于SOC含量的影响十分显著。

![](images/2167894fe3834059084cc378d89bdee1ac6009b536a4cecda9261170510300f4.jpg)  
图4环境变量的相对重要性

![](images/3d4699e987c48ada6c76d0187c7c5889254e8a99f2c42c7dac1c2d9a95f16dd1.jpg)  
Fig. 4 The significance of environmental variables in relative terms   
图5各采样点SOC的主要及次要影响因子  
Fig. 5Primary and secondary impact factors of SOC at each sampling point

# 2.4非线性关系和阈值效应分析

图6揭示了8个数值型变量pH、海拔、年均降水量、植被净初级生产力、人口密度、年均蒸发量、全钾、全氮以及类别变量土地利用类型与Shapley/SOC值之间的非线性关系。分析表明,海拔、年均降水量、植被净初级生产力、人口密度、全氮与SOC含量总体上呈现出正相关关系,而pH、年均蒸发量、全钾与SOC含量总体上则呈现出负相关关系,但所有变量均表现出显著的非线性特征。

根据图6a可知,pH位于6.5\~7.8时,其 Shapley值逐渐减少,但均大于0g·kg"',表明此时pH对于SOC 的累积具有促进作用。而当pH超过7.8时，随着pH的增加,其Shapley值稳定在-0.5g·kg"1左右，则此时pH对SOC含量产生了负面影响。如图6g所示,全钾的情况与pH相似,但全钾在12\~14g·kg"1时,其Shapley值同样随着全钾含量的增大而减小,在14g·kg-'之后,Shapley值在0g·kg-上下波动。年均蒸发量(图6f)与pH、全钾略有不同的是,在400\~500 mm时，年均蒸发量的Shapley值呈现出上升的趋势,在此之后,年均蒸发量的Shapley值逐渐减少，在年均蒸发量等于650 mm之后，年均蒸发量的Shapley值稳定在-0.1 g·kg−1。

根据图6b可知，当海拔由0增至1400m时，Shapley值相对稳定地处于0g·kg-1以下，表明此时海拔对SOC含量的影响倾向于负面或者影响十分微弱。而当海拔>1400 m时,Shapley值随海拔的增加而增加，此时海拔对SOC含量的影响是正面的。这种情况的出现可能与天山的积雪融水有关。年均降水量、植被净初级生产力、人口密度、全氮的情况与海拔类似(图6c、图6d、图6e与图6h),它们的阈值分别为300 mm、130 g C·m2.a−1、150人·km2、2.4 g·kg-1。

土地利用类型是最重要的9个环境变量中唯一一个类别变量。观察图6i可以发现,未利用地、旱地的平均Shapley值为负数,而草地与林地的平均Shapley值均为正数,并且草地在4种土地利用类型中具有最高的平均Shapley值。因此,当研究区内土地类型为草地或林地时，它们对于SOC的累积能够

起到促进作用。

综合分析结果可知,SHAP依赖图以直观的方式展现了SOC含量与各种环境因素之间的复杂非线性关系。它不仅能够揭示环境因素对SOC含量的阈值效应，还明确了这些因素对SOC含量产生显著影响的特定取值范围。在本研究区中，当pH为7.0、海拔为2200m、年均降水量为390mm、植被净初级生产力为180gC·m-2·a-、年均蒸发量为460 mm、全钾含量为12.3g·kg、全氮含量为3.0g·kg"、人口密度为200人·km左右时，更有助于SOC积累。

# 2.5 S0C空间分布和不确定性

图7a揭示了研究区中SOC的空间分布趋势，其空间分辨率为1km。预测结果显示,SOC含量的最高值达到16.63g·kg−1,最低值仅为0.99g·kg−1。从分布趋势来看,SOC含量呈现出明显的北高南低格局。此外,西北部及中部地区的SOC含量显著高于其他区域。值得注意的是,SOC含量较高的区域与此处水体分布情况类似,二者均呈现出了“V"形分布。综合SOC的空间分布趋势与各环境变量的空间分布图可以发现,SOC的空间分异与区域环境因子存在显著关联。其中,pH值与年均蒸发量的低值区在空间上呈现显著集聚性,其分布与SOC高值区的"V"形空间模式高度吻合。同样地,海拔、年均降水量、植被净初级生产力及全氮含量的高值带同样沿该"V"形轴线延伸。微酸性的土壤、较低的蒸发，较高的海拔、降水量、全氮含量以及更为茂密的植被,最终塑造出该地区SOC的空间分异格局。

![](images/71d3ff43cb2f2ea47c3300a82648b3e07138164dacc1efc2e641d583f8d34ac2.jpg)  
图6 Shapley值与环境变量的偏依赖图  
Fig. 6 Partial dependence of Shapley/SOC values on environmental variables

![](images/14ba148b4f12fb6f681691075abd9dfc746159b2326488ba5528a88772608552.jpg)  
图7 SOC空间分布及不确定性  
Fig.7 SOC spatial distribution and uncertainty

SOC含量预测的不确定性如图7b所示。预测的不确定性介于0.088\~2.948之间，在研究区南部，其不确定性较高，这可能与该地区部分数据的缺失有关。

# 3讨论

# 3.1可解释机器学习模型的优越性分析

在本研究中，对比了局部空间回归模型与基于算法的机器学习及深度学习模型在处理复杂数据集时的性能差异。结果表明,后者在预测精度上具有明显优势,尤其是在捕捉数据中复杂的非线性关系方面，而这恰恰是传统的空间回归模型所难以实现的。

机器学习模型和深度学习模型因其算法的复杂性和结构的灵活性，能够从大规模数据集中提取数据的特征和模式[25-27]。这种能力同样在本研究的实验结果中得到了体现,无论是机器学习模型还是深度学习模型,其预测的R、RMSE和LCCC 指标上均优于GWR模型。Shao等[28曾利用多种机器学习模型与GWR分别进行中国新冠肺炎疫情的空间预测,发现机器学习模型的性能表现均优于GWR。

值得注意的是,尽管深度学习模型因其深度结构而被普遍认为具有更高的预测精度,但在本研究中,表现最佳的模型是XGB这一机器学习模型。这一现象可能与本研究所使用的数据集规模较小且为表格型数据有关。例如,Anding等[29]的研究就发现只提供部分数据时,未经预训练的神经网络模型比经典分类器的预测结果要差;Shwartz-Ziv等[30]证明,XGBoost在处理表格型数据时，用更少的参数调优却得到了比一些深度学习模型更好的预测表现,这与我们的发现一致。因此，在数据量相对有限的情况下，传统的机器学习模型可能因其较低的数据依赖性和较好的泛化能力而表现更优。而对于表格类型数据,基于树的模型具有更稳定且强大的表现。

此外，我们观察到2个深度学习模型DNN 和CNN的拟合R与预测R在数值上非常接近，这表明它们在未知数据上的泛化能力较强[31-33]。这种泛化能力的优势可能源于深度学习模型在处理复杂非线性关系时的内在能力。尽管在本研究中,深度学习模型并未展现出最高的预测性能,但它们在泛化能力上的表现仍然值得进一步关注。

综上，可解释性机器学习模型相较于传统的空间回归模型，能够捕捉多环境因子间的非线性交互效应,进而实现有效的SOC空间分异情况预测。

# 3.2环境变量对SOC空间格局的影响分析

研究结果表明，pH、海拔与气候因子是研究区SOC 分布的主要影响因子。pH能够影响土壤中微生物及酶的活性,适宜的土壤pH能够抑制微生物的生长，进而降低SOC的分解速率，促进SOC的积累。在偏碱性的环境下,pH通常与SOC呈负相关。本文研究区土壤pH位于6.34\~9.24区间内，pH低值区与 SOC含量的高值区表现出相似的空间分布规律，这与冯锦等[34]和马辉英等[35]的研究结果是一致的。

以往的部分研究中发现,随着海拔的升高,SOC含量呈现出增加的趋势[36-38]。在本研究中,同样观测到了类似的现象。这可能归因于气候的垂直地带性特征的影响。随着海拔的升高，气温逐渐下降，这种低温环境对微生物活性构成了抑制作用，进而减缓了SOC的分解速率。并且通过对比研究区的海拔分布与降水格局，推测SOC含量较高的区域可能位于山体中部,即半山腰位置。这一区域相较于山脚及山顶,降水量更为充沛。更为丰富的降水条件为植物生长提供了更为优越的环境,促进了植物生长,进而促进了SOC的累积。此外,由于研究区高海拔处存在积雪，积雪融水或许也是促进SOC 累积的原因之一。

气候因子对于SOC的影响是显著的，这与聂祥琴等[39]、李景等[40]、潘依依等[41]的研究结果一致。来自大西洋的水汽跟随西风气流穿越中亚地区抵达天山。这些水汽在天山的迎风坡，即天山北坡处,受地形的阻挡形成降雨。这就导致天山北坡地区的气候环境相较于南坡会更加湿润。根据偏依赖图，当研究区的年均降水量超过300mm时，该因素对于SOC的累积起到了明显的促进作用。合适的降水量有助于植物的生长,进而促进植物通过光合作用,实现生物固碳[42-43]。而蒸发量通常对 SOC的累积起到了相反的作用,如果蒸发量过高，土壤含水量降低,土壤呼吸增强,消耗土壤中的有机物并释放COzo

# 3.3研究区固碳建议

根据变量重要性及采样点的首要、次要影响因子的可视化结果，可以发现pH对于研究区的 SOC影响是最大的。并且结合偏依赖图可知,当土壤pH在7左右时，最利于SOC 累积。可以发现研究区土壤更偏向于碱性，为了让研究区内的土壤保持在一个接近于中性的pH水平，施用合适的肥料或其他改良剂是一种可行性较高的解决措施。Tavakkoli等[44]发现在表土含钠量高的地区使用石膏并且增加豆类产量有助于降低pH值，进而提升了SOC含量;Zuo等[45]对比分析了醋糟、污泥等多种有机材料,发现它们对于SOC的积累与作物产量的提升都有积极的作用;Zhang等[46]通过实验发现对于轻度碱性土壤,农家肥、秸秆、绵羊粪便能有效增加 SOC以及改善土壤团聚体。这些改善措施都具有一定的借鉴意义,但值得注意的是,本研究区的土壤pH整体位于弱酸性至碱性的区间，尚未达到强碱性水平，因此，在选择施用的改良剂时,需要着重注意施放的剂量与浓度。

同样地,气候因子作为SOC的主控因子同样需要重视。同样地,在一定范围内增加土壤湿度、减少蒸发有助于SOC的累积。鉴于直接改变降水量与蒸散量的可行性较低，故可以在研究区内保护、恢复植被,进而有效地提升土壤的保水能力。还注意到,在采样点中，土地利用类型为草地的区域SOC含量最高，同时考虑到研究区的蒸发量远大于降水量,种植一些耐干旱、耐盐碱的植物,如在合适的区域铺设人工草地也可以作为一种改善土壤状况、促进SOC 累积的手段。

# 3.4不足与展望

天山中段最高海拔可达7000m以上，而本研究的采样点中，最高海拔仅为3084m,甚至不足最高海拔的一半。这就表明对于高海拔地区的制图结果可能存在一定误差。考虑到实地采样的可行性，在后续研究中，应该尽可能补充较高海拔的采样数据,从而进一步完善该地区SOC的空间预测图。

本研究所依赖的核心土壤数据采集于2005年，数据现时性不足，因此，基于2005年数据所揭示的SOC空间格局及其驱动机制，可能无法充分代表当前的研究区状况,对近期变化趋势的推断也存在不确定性。在未来的研究中，期望纳入并整合时效性更强的数据使研究内容进一步拓展,在探明研究区SOC 主控因子的同时，获取更接近当前情况的SOC分布图。

# 4结论

本研究通过模型比较,确定了XGB是研究区最优预测模型,并揭示了SOC北高南低的空间分布格局。在此基础上,使用SHAP算法确定了pH、海拔、年均降水量是研究区SOC的主控因子。偏依赖图结果揭示了环境变量与SOC存在阈值效应，其中pH、年均蒸发量、年均降雨量、植被净初级生产力的阈值分别为7.8、620 mm、300 mm以及130gC·m2·a,当各变量取值超过相应阈值，则会导致SOC含量显著下降。借助施用有机肥、酸性改良剂以及保证灌溉等手段有利于该地区SOC的累积。本研究证实了土壤属性、地形及气候因子的重要性,为天山中段土壤碳汇的精准管理提供了科学依据和可操作的调控路径,对于其他干旱半干旱地区的土壤固碳增汇研究与实践亦提供了重要参考。

# 参考文献(References):

[1]Chappell E,Easher TH, Saurette D,et al. Soil Organic Carbon: Past,Present,and Future Research[M]. Germany: Springer,2021: 35-48.   
[2] Kuht J,Eremeev V,Talgre L,et al.Changes in the soil microbial hydrolytic activity and the content of organic carbon and total nitrogen by growing spring barley undersown with red clover in different farming systems[J]. Agriculture, 2019,9(7): 146.   
[3] 张杰,李敏,敖子强,等.中国西部干旱区土壤有机碳储量估 算[J].干旱区资源与环境,2018,32(9):132-137.[Zhang Jie,Li Min,Ao Ziqiang,et al.Estimation of soil organic carbon storage of terrestrial ecosystem in arid western China[J]. Journal of Arid Land Resources and Environment ,2018,32(9): 132-137.]   
[4] Zhuo Z, Chen Q, Zhang X,etal.Soil organic carbon storage,distribution,and influencing factors at different depths in the dryland farming regions of Northeast and North China[J]. Catena,2022, 21005934Z: Doi: 10.1016/j.catena.2021.105934.   
[5] 缪琦,史学正,于东升,等.气候因子对森林土壤有机碳影响的 幅度效应研究[J].土壤学报,2010,47(2):270-278.[Liao Qi,Shi Xuezheng, Yu Dongsheng, et al. Scale effect of climatic factors on forest soil organic carbon[J].Acta Pedologica Sinica,2010,47(2): 270-278.]   
[6] Yang L,Jia W,Shi Y,et al. Spatiotemporal differentiation of soil organic carbon of grassland and its relationship with soil physicochemical properties on the northern slope of Qilian Mountains, China[J]. Sustainability,2020,12(22): 9396.   
[7] 常帅,于红博,曹聪明,等.锡林郭勒草原土壤有机碳分布特征 及其影响因素[J].干旱区研究,2021,38(5):1355-1366.[Chang Shuai,Yu Hongbo, Cao Congming,et al. Distribution characteristics of soil organic carbon in Xilin Gol steppe and its influencing factors[J]. Arid Zone Research,2021,38(5): 1355-1366.]   
[8] 韩雅,朱文博,李双成.基于GWR模型的中国NDVI与气候因 子的相关分析[J].北京大学学报(自然科学版),2016,52(6): 1125-1133.[Han Ya, Zhu Wenbo,Li Shuangcheng. Modeling relationship between NDVIand climatic factors in China: Using geographically weighted regression[J].Acta Scientiarum Naturalium Universitatis Pekinensis,2016,52(6): 1125-1133.]   
[9] 宋颖,高明秀,王佳凡,等.基于MGWR的滨海区土壤盐渍化 分布空间预测及影响因素分析[J].环境科学,2024,45(7): 4293-4301.[Song Ying,Gao Mingxiu,Wang Jiafan,et al. Spatial prediction and influencing factors analysis of soil salinization in coastal area based on MGWR[J]. Environmental Science,2024,45 (7): 4293-4301.]   
[10]Hagenauer J, Helbich M.A geographically weighted artificial neural network[J]. International Journal of Geographical Information Science,2022,36(2): 215-235.   
[11]Wu Z,Chen Y,Yang Z,et al. Mapping soil organic carbon in lowrelief farmlands based on stratified heterogeneous relationship[J]. Remote Sensing,2022,14(15): 3575.   
[12] Zhang C,Chen YY,Wei YJ,et al. Unraveling the threshold and interaction effects of environmental variables on soil organic carbon mapping in plateau watershed[J]. Geoderma, 2024,450: 117032.   
[13] Zheng Y T,Zhao X N,Li XY,et al. Mapping soil organic carbon density via geographically weighted regression with smooth terms: A case study in Shanxi Province[J]. Ecological Indicators,2024, 166: 112588.   
[14] Chakraborty S K, Chandel N S,Jat D,et al. Deep learning approaches and interventions for futuristic engineering inagriculture[J]. Neural Computing & Applications,2022,34(23): 20539-20573.   
[15]Padarian J, Minasny B, Mcbratney A B.Machine learning and soil sciences:A review aided by machine learning tools[J]. Soil,2020, 6(1): 35-52.   
[16] Biau G,Scornet E.A random forest guided tour[J]. Test,2016,25 (2): 197-227.   
[17]Breiman L. Random forests[J]. Machine Learning,2001,45(1): 5- 32.   
[18]Friedman JH.Greedy function aproximation: A gradientbosting machine[J]. Annals of Statistics,2001,29(5): 1189-1232.   
[19]Liang W,Luo S, Zhao G,etal.Predicting hard rock pillar stability using GBDT,XGBoost,and LightGBM algorithms[J].Mathematics,2020,8(5): 765.   
[20] Chen T Q,Guestrin C. XGBoost: A scalable tree boosting system [C]//Assoc Comp M. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discoveryand Data Mining (KDD).San Francisco,CA:Assoc Computing Machinery,2016: 785-794.   
[21]Pathy A,Meher S,Balasubramanian P.Predicting algal biochar yield using eXtreme Gradient Boosting (XGB)algorithm of machine learning methods[J].Algal Research- Biomass Biofuels and Bioproducts,2020,50: 102006.   
[22] Passafaro TL,Lopes FB,Dórea JRR,et al.Would large dataset sample size unveil the potential of deep neural networks for improved genome-enabled prediction of complex traits?The case for body weight in broilers[J].Bmc Genomics,2020,21(1): 771.   
[23]Shruti P,Rekha R.A review of convolutional neural networks,its variants and applications[Cl//2O23 International Conference on Intelligent Systems for Communication,IoT and Security (ICISCoIS), 2023,31-36.   
[24]Lundberg S M, Lee S-I.A unified approach to interpreting model predictions[C//Proceedings of the 31st Annual Conference on Neural Information Processing Systems (NIPS). Long Beach, CA: Neural Information Processing Systems (NIPS),2017: 4768-477.   
[25] Islam M T, Xing L. Deciphering the feature representation of deep neural networks for high-performance AI[J]. Ieee Transactions on Pattern Analysis and Machine Intelligence,2024,46(8): 5273- 5287.   
[26] Liu Q,Wang X D. Designing an efficient framework for large-scale data processing and analysis based on deep learning technology [C]//Assoc Comp M. Proceedings of the 3rd International Conference on Cyber Security,Artificial Intelligence and Digital Economy (CSAIDE). Nanjing: Assoc Computing Machinery,2024: 269- 274.   
[27]Wang S, Zhang Z, Geng S,et al. Research on optimization of random forest algorithm based on Spark[J]. Cmc-Computers Materials & Continua,2022,71(2):3721-3731.   
[28]Shao Q,Xu YM,Wu HY.Spatial prediction of COVID-19 in China based on machine learning algorithms and geographically weighted regression[J]. Computational and Mathematical Methods in Medicine,2021,2021: 7196492.   
[29] Anding K, Haar L,Polte G,et al. Comparison of the performance of innovative deep learning and classical methods of machine learning to solve industrial recognition tasks[C]//Proceedings of the Joint TC1-TC2 International Symposium on Photonics and Education in Measurement Science. Germany: Spie-Int SOC Optical Engineering,2019: UNSP111440R.   
[30]Shwartz-Ziv R,Armon A. Tabular data: Deep learning is not äal you need[J]. Information Fusion,2021,81: 84-90.   
[31] 洪岩,袁琳,李梦雪,等.产品生命周期视域下人工智能技术在 服装产业中的应用进展[J].丝绸,2024,61(12):1-22.[Hong Yan,Yuan Lin,Li Mengxue,etal.Progressintheapplicationof artificial intelligence technology in the garment industry from the perspectiveof productlifecycle[J]. Journal ofSilk,2024,61(12):22.]   
[32] 李升波,关阳,侯廉,等.深度神经网络的关键技术及其在自动 驾驶领域的应用[J].汽车安全与节能学报,2019,10(2):119- 145.[Li Shengbo, Guan Yang,Hou Lian,et al. Key technique of deep neural network and its applications in autonomous driving[J]. Journal of Automotive Safety and Energy,2019,10(2): 119-145.]   
[33] 田芳,周孝信,史东宇,等.基于卷积神经网络的电力系统暂态 稳定预防控制方法[J].电力系统保护与控制,2020,48(18):1- 8.[Tian Fang, Zhou Xiaoxin, Shi Dongyu,et al.A preventive control method of power system transient stability based on a convolutional neural network[J].Power System Protection and Control, 2020,48(18): 1-8.]   
[34] 冯锦,崔东,孙国军,等.新疆土壤有机碳与土壤理化性质的相 关性[J].草业科学,2017,34(4):692-697.[Feng Jin, Cui Dong, Sun Guojun,et al. Soil organic carbon in relation to soil physicochemical properties in Xinjiang[J].Pratacultural Science,2017,34 (4): 692-697.]   
[35] 马辉英,李昕竹,马鑫钰,等.新疆天山北麓中段不同植被类型 下土壤有机碳组分特征及其影响因素[J]. 生态环境学报, 2022,31(6): 1124-1131.[Ma Huiying,Li Xinzhu,Ma Xinyu,et al. Characteristics and driving factors of soil organic carbon fractions under different vegetation types of the mid-northern piedmont of the Tianshan Mountains,Xinjiang[J].Ecology and Environmental Sciences,2022,31(6): 1124-1131.]   
[36] 傅华,陈亚明,王彦荣,等.阿拉善主要草地类型土壤有机碳特 征及其影响因素[J].生态学报,2004,24(3):469-476.[Fu Hua, Chen Yaming,Wang Yanrong,et al. Organic carbon content in ma-jor grassland types in Alex,Inner Mongolia[J].Acta Ecologica Sinica,2004,24(3): 469-476.]   
[37] 何志斌,赵文智,刘鹄,等.祁连山青海云杉林斑表层土壤有机 碳特征及其影响因素[J].生态学报,2006,26(8):2572-2577. [He Zhibin,Zhao Wenzhi,Liu Hu,et al.Characteristic of Picea crassifolia forest soil organic carbon and relationship with environment factors in the Qilian Mountain[J].Acta Ecologica Sinica, 2006,26(8): 2572-2577.]   
[38] 刘伟,程积民,高阳,等.黄土高原草地土壤有机碳分布及其影 响因素[J].土壤学报,2012,49(1): 68-76.[Liu Wei, Cheng Jimin, Gao Yang,et al. Distribution of soil organic carbon in grassland on the Loess Plateau and its influencing factors[J].Acta Pedologica Sinica,2012,49(1): 68-76.]   
[39] 聂祥琴,陈瀚阅,牛铮,等.基于时序影像的农业活动因子提取 与闽西耕地 SOC 数字制图[J].地球信息科学学报,2022,24(9): 1835-1852.[Nie Xiangqin,Chen Hanyue,Niu Zheng,etal.Digital SOC mapping in croplands using agricultural activity factors derived from time-series data in western Fujian[J]. Journal of Geoinformation Science,2022,24(9): 1835-1852.]   
[40] 李景,吴会军,武雪萍,等.长期免耕和深松提高了土壤团聚体 颗粒态有机碳及全氮含量[J].中国农业科学,2021,54(2):334- 344.[Li Jing,Wu Huijun, Wu Xueping,et al.Long-term conservation tillage enhanced organic carbon and nitrogen contents of particulate organic matter in soil aggregates[J]. Scientia Agricultura Sinica,2021,54(2): 334-344.]   
[41] 潘依依,何云峰,单立楠,等.沙漠化土壤有机碳研究进展[J].土 壤通报,2011,42(6):1515-1521.[Pan Yiyi,He Yunfeng,Shan Linan,et al.A review on soil organic carbon during desertification progresses[J]. Chinese Journal of Soil Science,2011,42(6):1515- 1521.]   
[42]Iversen C,Norby RJS N.Global Environmental Change[M].Germany: Springer Reference,2014: 297-316.   
[43] 李玉露,吴雪晴,袁野,等.黑龙江省植被碳-水利用效率时空 演变及其驱动机制[J].应用生态学报，2024,35(12):3349- 3358.[Li Yulu,Wu Xueqing,Yuan Ye,et al. Spatial-temporal variation and driving mechanism of vegetation carbon and water use efficiency in Heilongjiang Province,China[J]. Chinese Journal of Applied Ecology,2024,35(12): 3349-3358.]   
[44] Tavakkoli E,Uddin S,Rengasamy P,et al.Field applications of gypsum reduce pH and improve soil C in highly alkaline soils in

southern Australia's dryland cropping region[J]. Soil Use and Management,2022,38(1): 466-477. [45] Zuo W,Xu L, Qiu M,et al. Effects of different exogenous organic materials on improving soil fertility in Coastal Saline-alkali soil[J].

# Spatial prediction and master factors of soil organic carbon in the middle section of Tianshan Mountains

HE Jianlan'，YAN Qingwu'，CHEN Yiyun²，LI Keqi'，BAI Junping³，WU Zihao' (1.School of Public Policyand Management,China Universityof Mining and Technology,Xuzhou 221116,Jiangsu, China; 2.Schoolof Resource and Environmental Sciences,Wuhan University,Wuhan 430079,Hubei, China; 3. Xinjiang Power Transmission and Transformation Co.,Ltd., Urumqi 830063, Xinjiang, China)

Abstract: Accurately mapping the spatial paterns of soil organic carbon (SOC) in the middle section of Tianshan Mountains, Xinjiang, is esential for evaluating soil quality,enhancing carbon sequestration,and ensuring ecological security.However,significant variations interrain,precipitation,evaporation,vegetationcover,andsoilpH, particularly between areas close to and distant from the mountains,result in complex ecological conditions. This complexity leads to high spatial heterogeneity in regional SOC,creating substantial chalenges for precise SOC mapping using digital soil mapping techniques.To addressthis,this study utilized 463 soil samples and applied multiple machine learning models, including eXtreme gradient boosting (XGBoost, XGB), to generate a spatial distribution map of SOC.In addition, the Shapley Additive exPlanations (SHAP) algorithm was employed to identify the primary factors influencing SOC spatial variation.Results indicated that the XGB model outperformed others,achieving a fting R² of 0.716,a liquid chromatography at critical conditions of 0.824,and a root mean square error of 1.554 g·kg"1.The spatial distribution of SOC exhibited higher values in the northern region and lower values in the southern.Further SHAP analysis showed that SOC content is primarily affected by soil pH,elevation,and mean annual precipitation.Partial dependence plots identified threshold effects in the relationships between environmental variables and SOC.Notably, SOC content declined sharply when pH exceeded 7.8, mean annual evaporation surpassed 620 mm, mean annual precipitation fellbelow 300 mm, or net primary productivity dropped below 130 g C·m2·a'.These findings suggest that managing soil pH, evapotranspiration,and vegetation growth is beneficial for regional soil carbon sequestration. Implementing strategies such as applying acid amendments,organic fertilizers,and ensuring agricultural irigation can help regulate the key variables affecting SOC and increase SOC content.This study reinforces the importance of considering factors such as soil pH,elevation,and mean annual precipitation.The results provide valuabledata support for soil carbon sink management in the middle section of Tianshan Mountains and serve as a significant reference for digital SOC mapping in other arid and semi-arid regions.

Keywords: soil organic carbon;arid and semi-arid areas； spatial mapping; dominant factors； the middle sec-tion of Tianshan Mountains