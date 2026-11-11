# 基于改进S-G滤波和非监督分类局部核回归的中国LAI时序数据融合研究

谢昭颖1，沈润平1\*，黄安奇1，邢雅洁1，王云宇1，刘晓利2  
1. 南京信息工程大学地理科学学院，南京 210044；2. 中国科学院南京土壤研究所，南京，210018

# LAI Time Series Data Fusion in China Based on Improved S-G Filtering and Unsupervised Classification Local Kernel Regression

XIE Zhaoying1 , SHEN Runping1\* , HUANG Anqi1 , XING Yajie1 , WANG Yunyu1 , LIU Xiaoli2 1. School of Geographical Sciences, Nanjing University of Information Science &Technology, Nanjing 210044, China； 2. Institute of Soil Science, Chinese Academy of Sciences, Nanjing 210018, China

Abstract：Leaf Area Index (LAI) is an important parameter for characterizing the canopy structure of vegetation. Remote sensing products of LAI are often affected by factors such as clouds, aerosols, snow, algorithms, and instrument issues, which result in poor data quality or missing data, seriously affecting the application of LAI datasets. In this paper, we propose a LAI time- series data fusion method based on improved S- G filtering and unsupervised classification local kernel regression. The normalized fusion is carried out using MODIS LAI, PROBA- V LAI, and VIIRS LAI products from 2014 to 2020 to improve the consistency, continuity, and accuracy of the products. Results show that the fused LAI shows good consistency in frequency distribution and temporal variation with the source products and other LAI products (MCD15A2H, MOD15A2H, VNP15A2H, PROBA-V), with a R2 of 0.85, 0.77, 0.84, and 0.89, respectively. Compared to other four products, the frequency of data missing is generally reduced, and the temporal continuity is improved. The averaged missing frequency of the fused LAI is reduced to 5.04%, compared to MCD15A2H LAI (19.59% ), MOD15A2H LAI (25.54% ), VNP15A2H LAI (23.33% ), and PROBA-V LAI (9.64% ). Also, the fused LAI shows the strongest correlation with ground measurements, with a R2 of 0.76 ,which is 0.03\~0.20 higher than other products, and a root mean square error (RMSE) of 1.16 m2 /m2 , which is lower than other products (0.10\~0.66 ) m2 /m2 , indicating a higher accuracy.

Key words：Leaf Area Index (LAI); MODIS; PROBA-V; VIIRS; normalization; data fusion; Local Kernel Regression Method

\*Corresponding author: SHEN Runping, E-mail: rpshen@nuist.edu.cn햪튪ꎺ叶面积指数Leaf Area Index(LAI)是表征植被冠层结构的重要参数，其遥感产品常常因云、气溶胶、积雪、算法和仪器问题等因素影响，导致数据质量差或缺失，严重影响LAI数据集的应用。本文提出了一种基于改进S-G滤波和非监督分类局部核回归的LAI时序数据融合方法，并利用2014—2020年MODIS LAI、PROBA-V LAI、VIIRS LAI产品数据，开展归一化融合研究，以提高产品的一致性、连续性和精确性。结果表明，融合LAI与源产品及其他LAI产品(MCD15A2H、MOD15A2H、VNP15A2H、PROBA-V) 的LAI值频率分布、时序变化表现出良好的一致性，并有较好的相关性，R2 分别为0.85、0.77、0.84和0.89，与这4个产品相比，数据缺失频率总体下降，时间连续性有所提高，相较于MCD15A2H LAI(19.59%)、MOD15A2H LAI(25.54%)、VNP15A2H LAI(23.33%)和PROBA-V LAI(9.64%)，融合LAI平均缺失频率降低为5.04%。与其他产品比较，融合LAI与地面实测值的相关性最好，决定系数（R2）达0.76，比其他产品高0.03\~0.2，均方根误差(RMSE)为1.16 m2/m2，比其他产品低（0.1\~0.66）m2 /m2 ，具有较高的精度。

맘볼듊ꎺ叶面积指数(LAI)；MODIS；PROBA-V；VIIRS；归一化；数据融合；局部核回归模型

# 1 引言

叶面积指数(Leaf Area Index，LAI)为单位地表面积内叶组织的单面总面积，是重要的植被结构参数[1]，在生态、农业、林业和气候环境等领域有着广泛应用。遥感反演是获取区域和全球尺度长期LAI数据的有效手段[2]。中等分辨率多个遥感LAI产品，如 MODIS LAI、CYCLOPES LAI、MERIS LAI等[3-5]，已广泛应用于植被物候检测、作物估产、陆表过程建模和全球气候变化等[6-10]研究。然而，研究表明[11]，受云、雪、气溶胶和传感器噪声的影响，遥感LAI产品往往存在时空连续性差和准确性有限等问题，很难提供时空连续的高质量植被信息，限制了其进一步应用。

当前，LAI 产品多由单卫星观测数据生成，仪器故障、云污染和其他因素造成了许多空白或缺失数据[12]。另外，检索过程中的有限信息量会导致数据差异和不一致的出现，尤其是在观测条件较差的情况下，对于任何给定的时间和地点，不同的产品通常具有不同的LAI值，存在较大的不确定性，产品的差异和巨大的不确定性，严重影响数据质量和应用[13]。解决这些问题有多种方案，一是利用辅助信息或多源数据，开发更先进的反演算法[14-15]，二是对当前产品数据进行后处理，如对单传感器产品数据进行重建[16] 或融合多传感器数据[13,17-19] 。

多源数据融合方法可充分利用不同产品数据的优势，实现不同数据间互补，使用来自多个卫星系统的数据，在给定时间段内提供更多潜在的观测结果，提高有昼夜云变化区域的数据可用性[17]。因此，多传感器数据的融合是一种有吸引力的方法，它可以充分利用当前的地球观测任务，提高数据质量、连续性和一致性，揭示每个LAI产品的优劣[20]。数据融合按层次的不同，可分为像元级融合(原始数据的直接融合)、特征级融合(经过特征提取后的数据融合)以及决策级融合(原始数据经解译地物信息后进行融合) [21]，多幅遥感光谱数据的融合往往采用像元级融合，以提高数据的质量。

当前，已有许多学者开展了关于不同传感器LAI 数据融合研究，如 Wang[13] 基于 VEGETATION和 MODIS 传感器的数据，运用最优插值法获得融合LAI，Verger[17]则基于这2个数据应用神经网络和时间滤波(TSGF)技术的创新融合方法来改进 MO-DIS LAI 产品；Munier[18] 利用卡尔曼滤波将 ECO-ClIMAP- II 分解 GEOV19 种植被类型，生成新的LAI 融合产品 LAI-mc(Multi-Cover)。Sadeh[19] 使用线性插值、波段分离分别求平均的方法，对Planet-Scope 和 Sentinel-2 进行融合生成新的 LAI 时间序列数据，综合了 2 种传感器的空间、时间和光谱优势。在LAI融合研究中，大多借助物候特征和周期等辅助信息，应用线性模型进行融合，往往难以精确描述不同传感器的观测值所呈现的非线性模式[22]及多源LAI数据间的复杂关系，大多研究结合叶面积指数的物候特征和周期，基于滤波方法在时间尺度上进行改进，在空间尺度上的数据融合研究，仍有很大的发展空间。然而，不同机构所生产的遥感产品普遍出现可比性较差的问题[23]，Brown[24] 对比分析 MODIS、PROBA-V 和 VIIRS 3 个 LAI 产品在北美地区的差异，结果表明它们在不同土地覆盖类型下存在不同的差异，Fang[25]对中国东北典型农田的EPS、GEOV2、GLASS、GLOBMAP、MODIS、PRO-BA-V和VIIRS 7个全球LAI产品进行了对比验证，产品间存在明显差异，产品质量指标在生长高峰期表现出较大的偏差，如浅层地糅合将会导致其在遥感应用上的局限。如能对多源数据进行归一化，尽可能消除不同源数据的差异，可充分耦合多源遥感观测信息，实现多源数据集成。

为此，本文引入了非参数估计方法中的核回归模型，综合运用改进的S-G滤波和非监督分类方法，提出了基于改进S-G滤波和非监督分类局部核回归的LAI时序数据融合方法，以增强对不同传感器的观测值所呈现的非线性关系描述，并减少人为干扰，提高运算效率，提升LAI数据质量。并将其应用于2014—2020 年中国区域 MODIS，PROBA-V 和 VI-IRS的LAI数据，实现对多源遥感LAI产品数据融合，达到提高LAI产品的估算精度和连续性目的。

# 2 研究方法

# 2.1 技术路线

研究源LAI产品尽可能来自不同传感器，参考前人LAI融合研究，考虑产品的成熟度和应用广泛性来选取源数据集。MCD15A2H LAI产品被公认为全球主流的LAI产品[26]，且在以往的LAI融合研究中大多融合其与CYCLOPES LAI产品，CYCLO-PES LAI产品来自VEGETATION传感器，PROBA-V的研发旨在为VEGETATION传感器提供延续性，两者LAI产品算法相似，且PROBA-V的算法有所简化，VNP15A2H LAI则源自VIIRS传感器。因此，研究选取 MCD15A2H、PROBA-V 和 VNP15A2H 3个LAI产品开展融合研究。为了能达到更好地融合效果，解决数据质量偏低和异常值存在的问题，研究首先对 LAI 数据产品进行重建。然后再以MCD15A2H为参考，利用非监督分类的局部核回归归一化方法，对PROBA-V和VNP15A2H产品进行归一化处理，消除产品之间的差异。考虑到PROBA-V LAI与MCD15A2H LAI时间分辨率不一致，研究参考时空融合方法地面覆盖和系统误差不变的假设[27-28]，对这2种产品重合日期影像进行融合，即MCD15A2H LAI每年第5、10、15、20、25、30、35、40、45 幅影像与 PROBA-V LAI 第 4、8、12、16、20、24、28、32、36幅影像进行融合。由于所选融合的8天MCD15A2HLAI影像时间范围包含在10天PROBA-V LAI影像时间范围，8天和10天对应的日期气候条件较为相似，短期气候相似条件下，LAI变化较小，融合的两幅影像具有较高的相关性。最后，对归一化处理后的产品进行平均，并进一步利用同期像元代替、窗口平均填补缺失值，得到多源LAI融合产品，具体技术流程如图1所示。

![](images/1c4807480663c0ffd4188e54211458f36340feed94be2aefdf34e03d40aea7b1.jpg)  
图1 基于改进S-G滤波和非监督分类局部核回归融合的技术流程  
Fig. 1 Technical process of local kernel regression fusion based on improved S-G filtering and unsupervised classification

# 2.2 基于像元质量分析的S-G滤波重建

因大气条件等因素影响，LAI产品存在数据缺失、质量较低等问题，严重影响LAI数据集的应用，时序数据集重建算法被广泛用于有效解决这一问题[29]，目前常用的重建方法有S-G滤波、DL拟合(双逻辑)、AG 拟合(非对称高斯)和 HANTS 模型(时间序列谐波分析)等。与其它算法相比，S-G滤波算法能更好地拟合时间序列数据的上包络线，对于大气和传感器等因素影响产生的LAI低值，具有很好的修复作用[29]。且从时间间隔角度考虑，相较于DL拟合方法和HANTS重构模型，S-G滤波模型对8 天及以上间隔时间序列的重构效果较好，表现最为稳定[30]。同时，LAI时序数据重建研究表明[31]，滤波前利用地学和生态规律，对低质量或缺值像素进行填充，有利于提高低质量或缺值像素质量，为进一步提高 LAI 时序数据重建质量打下了坚实的基础。因此，研究选择了改进的S-G滤波方法，即基于像元质量分析的S-G滤波重建方法。利用质量控制数据集，从像元质量分析出发，考虑植被变化的地理相邻影响，针对低质量数据进行重建。首先对选定的融合源LAI产品，依据产品的像元质量标识进行 重 建 ，当 像 元 为 高 质 量 时 (MCD15A2H、VNP15A2H反演算法为三维辐射传输模型，反演结果好为高质量，PROBA-V无缺失值为高质量)，保留原始LAI值；当像元不为高质量时，逐像元寻找质量控制评价标准下低质量的像元点，并以此作为像元中心点，在其周围建立一个9×9的滑动窗口。根据相应的土地覆盖数据，在窗口内寻找同类植被的高质量像元，利用地理相近同类地物有很大的相似性的特点，将窗口内符合条件的高质量像元均值替换该低质量中心像元。若该像元中心周围无法找到高质量像元点，则该像元值仍然为原始值。

然后，使用 S-G 滤波进行平滑，S-G滤波是基于局域的多项式最小二乘法拟合的滤波。S-G 滤波不仅可以滤除噪声，提高数据的平滑度，同时也可以使得数据的规律性不发生变化[32]。不同数据可根据其特点调整合适的滤波参数、设定滑动窗口的大小，使 S-G 滤波进行迭代运算，模拟时序数据的变化趋势，实现时序数据重建。其公式如下：

![](images/344f8522b393d008ed8ddd9a18fd6bdf8069f353ea6eb923d3f9179149c2f902.jpg)

式中：Y \* 表示经过 S-G 滤波后的叶面积指数数值；C 表示滤波时所设定的系数；Y 表示原始叶面积指数数值；m为滑动窗口的大小；N代表滤波所用长度，为了防止过度拟合及引入异常值，多项式拟合次数选在2\~4之间较为合适。

# 2.3 基于非监督分类的局部核回归融合

受大气状态、观测几何和仪器平台等多方面因素影响，不同传感器的数据存在不一致和可比性差等问题。为解决上述问题，更好地实现多源LAI数据融合，研究参考基于粗分辨率参考数据的多源数据归一化模型，对源LAI数据进行归一化，该方法最早可追溯到 Olthof 等[33] 用 SPOT VEGETATION10天合成数据，对Landsat ETM+的反射率数据进行辐射归一化。Gao[34]在此基础上进行了拓展，采用MODIS的标准产品对不同传感器的中分辨率反射率数据进行归一化，Gan[35]以MODIS 产品为参考，对Landsat ETM+ 和 Terra ASTER 传感器的ND-VI进行归一化处理。基本思路是以粗分辨率数据作为标准数据，将整个影像分成不同的集群建立关系模型，以消除其它数据与标准数据之间的偏差，从而间接消除数据间的差异。该方法的基础为无论斑块大小，相同土地覆盖类型的均匀像元具有相同的地表反射率，且在不同斑块大小的情况下，每一种土地覆盖类型在短时间内不分裂为两种或两种以上类型(1到n)的情况下，这些像元的季节性和双向反射率变化也应相同。与基于若干同步数据建立通用模型的方法相比，基于参考的归一化方法对待归一化数据寻找相应同步参考数据，实时性更好，更贴合待归一化数据的实际情况。其流程如下：

（1）获得待归一化数据对应的分类类别图(本文为LAI分类类别图)。可从已有分类数据如土地覆盖分类数据，或基于原始时序影像(本文为LAI时序影像)无监督分类获得相应的分类类别图。为了避免在此过程中，根据经验人为地设置相似度阈值，研究选用无监督分类方法。

（2）使用同质像元构建传感器间转换模型。基于待归一化时序影像对应的分类类别图搜索参考数据（本文为MCD15A2H LAI数据），以当前像元为中心的a×a窗口内的同类像元(本研究使用的是9×9的大小)，同时搜索待归一化数据相对应同类像元构建模型。

（3）从左到右、从上到下按块逐像素处理，得到归一化结果。

常见的非监督分类方法主要有K-Means、ISO-DATA[36]、链状方法等。以往利用某一数据为参考，实现多源遥感数据归一化的研究中，往往通过已有分类数据[33（] 如土地覆盖分类数据）人为设定阈值来寻找相似像元，而非监督分类的优势就在于区分影像像元的不同类别，基于这种思想，将非监督分类用于确定相似像元，可以很大程度上排除人为干扰，并提高运算效率。本研究采用K-Means方法[37]，它通过计算距离的相似性，来对物体进行分类，如果2个目标之间的距离越近，计算出的相似度越大。

考虑到不同传感器的观测值表现为难以精确描述的非线性模式[22]及多源LAI数据之间关系的复杂性，研究选择非参数估计方法中的核回归模型进行归一化。核回归是一种非参数估计的局部加权平均方法，它赋予接近估计点的数据更多的权重。该方法广泛应用于模式识别、图像去噪、超分辨率重建和图像插值等领域[38] 。Nadaraya-Watson 估计[39-40] 是一种常用的核估计方法，它是一个局部自适应线性滤波器，表达式如下:

![](images/fb36f3a34ebe471e9cf5c72101d9af0b434803c441ab47ce53a92b7d00eb2544.jpg)

![](images/9c04a195445309188e6f46835581f21709e980c89c9055d26caa18e701416bb2.jpg)

式中：z(x)为样本点的LAI估计值；K( )为用来控制每个样本的权值的核函数，；h为用来控制核大小的平滑参数，h越大，估计结果越平滑；X为当前待归一化的像元；x，⋯ ，x 为在当前待归一化数据的数据块中的同类像元；y ，⋯，y 为对应的参考数据。

本研究选用较为常用的高斯核函数作为核函数，优点是计算量较小，表达式如下：

![](images/798dfb77af44a2eea90f33dd4fdf6331f3f8b2633c736e13cb3865602cabcc5b.jpg)

式中：exp 是指数函数；σ 是核参数，用来控制核函数的灵活性。

本文引入 K- Means 方法和核回归方法，以MCD15A2H 为参考，对滤波重建后的 VNP15A2HLAI和PROBA-V LAI产品进行归一化融合。首先用K-Means算法生成待归一化LAI时序影像对应的 LAI 分类类别图，然后对每个待归一化的像元，根据LAI分类类别图搜索窗口内的同质像元，建立核回归方程，计算归一化结果。如果当前像素所在的窗口缺乏同质像元，无法求解转换关系，则采用备用模型得到不同土地覆盖类型的线性模型。

# 2.4 评价方法

为了与站点观测值比较，利用双线性插值[41]方

法将遥感产品栅格数据内插到站点，再与站点数据对比分析。

本研究采用决定系数(R2)、和均方根误差(RMSE)2个指标定量地分析融合LAI的精度，计算公式如下：

![](images/e61ac780dd073e9329dfc80a062b15cd550219c057dcf602e7da63fab0c80406.jpg)

![](images/6ca4139bdf7dce390df5cf766ae10d5722e7553169cbbb2799701d9471b79061.jpg)

式中：N为样本总数，站点验证时 N 代表筛选得到的站点数量；X 和 Y 分别为第 i 个对应点的LAI产品值和站点观测值；Xˉ 是观测值平均值。在融合LAI与其它产品进行一致性分析时，N 代表产品完成匹配所得到的像元数量，X 和Y 分别是第i个对应点的用于验证的LAI产品值和融合LAI值，Xˉ 是融合LAI值平均值。

# 3 数据来源

本文数据包括 LAI 产品数据、土地覆盖数据、地面观测数据等，具体信息如表1所示。

# 3.1 LAI 产品数据

# 3.1.1 MODIS LAI

研究采用的MODIS LAI为MCD15A2H第6版本数据集和MOD15A2H第6版本数据集，前者由Terra和Aqua的采集数据组合生成，后者则源自Ter-ra星。产品的反演算法除了采用三维辐射传输模型算法模拟生成查找表的主算法[42]外，还根据不同植被类型建立LAI与归一化植被指数（NDVI）的经验回归方程来构建备用算法[43]。MCD15A2H第6版本数据集在本研究中作为融合源数据，MOD15A2H第6版本数据集则用于融合LAI的验证。

表1 文中所用数据及基本信息  
Tab. 1 Data and basic information used in the paper   

<table><tr><td>类型</td><td>产品名称</td><td>来源</td><td>空间分辨率</td><td>时间分辨率</td><td>投影方式</td></tr><tr><td rowspan="4">LAI产品数据</td><td>MCD15A2H</td><td>https://earthdata.nasa.gov/</td><td>500m</td><td>8天(2000年至今)</td><td>正弦曲线投影</td></tr><tr><td>MOD15A2H</td><td>https://earthdata.nasa.gov/</td><td>500m</td><td>8天(2000年至今)</td><td>正弦曲线投影</td></tr><tr><td>PROBA-V</td><td>http://land.copernicus.eu/global/products/lai</td><td>300m</td><td>10天(2014年至今)</td><td>简易圆柱投影</td></tr><tr><td>VNP15A2H</td><td>https://earthdata.nasa.gov/</td><td>500m</td><td>8天(2012年至今)</td><td>正弦曲线投影</td></tr><tr><td>土地覆盖数据</td><td>MCD12Q1</td><td>https://earthdata.nasa.gov/</td><td>500 m</td><td>1年</td><td>正弦曲线投影</td></tr><tr><td rowspan="2">地面观测数据</td><td rowspan="2">1</td><td>中国生态系统网络(CERN)</td><td>1</td><td></td><td>1</td></tr><tr><td>(http://www.cnern.org/index.action)</td><td></td><td></td><td></td></tr></table>

# 3.1.2 PROBA-V LAI

PROBA-V LAI由哥白尼全球土地服务中心(CGLS)制作。该数据集源自Proba-V卫星。此产品的反演算法以蓝光、红光和近红外波段的反射率（及其相关的观察和照明几何形状）作为输入数据，及 CYCLOPES V3.1 和 MODIS C5 的加权平均值，使用神经网络（ANN）得到每日估计值，最后应用时间合成、平滑和间隙填充程序[44]，得到最终的产品。

# 3.1.3 VIIRS LAI

VIIRS LAI 为 VNP15A2H V1 产品[45]。该数据集源自 Suomi 国家极地轨道合作伙伴(SNPP)卫星。产品的反演算法与MODIS LAI产品类似，但由于传感器之间的差异，需专门调整参数来修正算法。

# 3.2 土地覆盖数据

研究所采用的土地覆盖数据为MCD12Q1产品[46]，由每年Terra和Aqua观测所得的数据经监督决策树分类处理所得。产品有5个土地覆盖分类方案，本研究采用基于叶面积和光合有效辐射的土地覆盖分类方案（LAI/fPAR Biome scheme），该方案的划分基于Myneni等[43]根据冠层结构分析，并与LAI/FAPAR算法兼容的六大生物群落方案，本文LAI融合研究仅在植被覆盖区域进行，具体仅涉及分类方案中的如下类别，草地/谷类作物用地(覆盖主要为一年生小于2 m的草本植物，包括玉米、小麦等谷类作物)、灌木林地（1\~2 m高的灌木，覆盖超过10%）、阔叶作物用地（高度小于2 m的一年生草本阔叶作物（如棉花））、稀树草原（树高大于 2m树木，覆盖介于10%\~60%）、常绿阔叶林（树高大于2 m的常绿阔叶树木，覆盖率大于60%）、落叶阔叶林（树高大于2 m的落叶阔叶树木，覆盖率大于60%）、常绿针叶林（树高大于2 m常绿针叶林，树木覆盖率大于60%）和落叶针叶林（树高大于2m落叶针叶林树木，覆盖率大于60%）8种土地覆盖类型，原分类方案的水体、城市、无植被覆盖区和未分类统一划分成非植被区。2016年中国区域的土地覆盖分类图如图2所示，植被覆盖分布空间特征表现为草地/谷类作物用地在我国分布很广，主要集中于中高纬地区，灌木林地主要分布于西北、西南、河北和内蒙古地区，阔叶作物用地主要分布于东北、华北地区，稀树草原主要分布于华东、东北、西南和西北地区，常绿阔叶林主要分布于南

注：白色为非植被区。该图基于自然资源部标准地图服务网下载的审图号为GS（2020）4632号的标准地图制作，底图无修改。该数据源于https://earthdata.nasa.gov/。

![](images/8ecd6ea177d070f74bbd8cc28f5a560b28a89360f607ab0f4aaa6453a4c6a86d.jpg)  
图2 2016年中国土地覆盖分类  
Fig. 2 Regional land cover classification map of China in 2016

方山地丘陵区域，落叶阔叶林主要分布于中部及东北地区、常绿针叶林主要分布于西南地区，落叶针叶林主要分布在东北地区。2014—2020年间植被覆盖类型变化主要表现为草地/谷类作物用地、落叶阔叶林和常绿针叶林等先减后增加，灌木林地先减后增再减少，阔叶作物用地、稀树草原和落叶针叶林减少，常绿阔叶林增加。

# 3.3 地面观测数据

本文的数据来源于国家科技基础条件平台-国家生态科学数据中心(http://www.nesdc.org.cn)、江西鹰潭农田生态系统国家野外科学观测研究站（http://ww.yingtan.cerm.ac.cn）。中国生态系统网络(CERN)以地面网络式观测、实验为主，对各生态系统类型进行长期、全面的监测，到目前为止分布在中国不同区域已有52个生态系统定位研究站(其中农业站18个，森林站18个，草地站7个，荒漠站2个，沼泽站1个，湖泊站3个，海湾站3个)，其中只有22个站点在研究年限内（2014—2020年）有LAI数据，研究获取了其中15个站点，包括9个农业站、1个草地站和5个森林站。CERN严格按照陆地生态系统生物观测指标和规范进行监测[47]，作物叶面积观测采用样方法，选择具有代表性、生长较一致的样方，按照标准株采样法，选取一定的代表株进行测定，以得到样方值，进而得到群体特征值。采用直接测定法，如叶面积仪测定法，观测时间为每年随生育期进行动态观测。对同一时间的观察数据进行平均处理，得到用于验证的站点观测数据。森林叶面积观测主要采用冠层分析仪和称重法，由于冠层分析仪基于光学模型测定的冠层叶面积指数，忽略树干、树枝对计算结果的影响，应用叶片称重法进行校正[47]。数据按照以下步骤进行质量控制：① 与历史观测数据对比，看数据是否处于正常状态和符合观测结果的变化规律，剔除异常值；② 参考数据阈值范围，如果有严重偏离则剔除。表2列出了观测站点数据相关信息。

# 4 结果与分析

# 4.1 源LAI数据差异分析

融 合 前 源 数 据 产 品 PROBA- V LAI、MCD15A2H LAI 和 VNP15A2H LAI 存 在 一 定 差异，2014—2020 年春季 LAI 平均值分别为 1.88、2.15和 2.00 m2 /m2 ，夏季平均值分别为 3.04、3.62 和 3.42m2 /m2 ，秋季平均值分别为 1.98、2.48 和 2.25 m2 /m2 ，冬季平均值分别为 0.72、1.15 和 0.86 m2 /m2 。从整体上看 PROBAV LAI 平均值小于 MCD15A2H LAI值，在中国东北、西南和东南地区显示较大差异（图3），结合土地覆盖分类图分析可知，其地表类型大多为森林。从整体上看，VNP15A2H LAI平均值稍低于MCD15A2H LAI值（图3），与PROBAV LAI和MCD15A2H LAI间的差值空间分布比较，则其差值分布相对均匀，特别是春季和夏季，但秋季和冬季东北地区差值相对较大。

产品差值分布频率分析表明（图4），PROBAVLAI、VNP15A2H LAI与MCD15A2H LAI像元差值主要集中分布于（ 1.00\~1.00）m2 /m2 之间，其中，超过60%的像元差值分布在（-0.50\~0.50）m2 /m2 范围，峰值都为0.00 m2 /m2 ，其频率均超过35.00%，说明不同 产 品 间 有 较 好 的 一 致 性 。 春 季 和 冬 季VNP15A2H LAI与MCD15A2H LAI的差值分布较为均匀，春季主要分布于（-1.50～1.50）m2 /m2 之间，冬季主要分布于（-1.00～1.00）m2 /m2 。夏季和秋季VNP15A2H LAI与MCD15A2H LAI负差值频率则略大于正差值频率，负差值主要分布于（-2.00\~0.00）m2 /m2 。PROBA-V LAI与MCD15A2H LAI的差值表现为春季正差值分布频率小于负差值分布频率，正差值主要分布于（0.00\~2.00）m2 /m2 ，夏季和秋季负差值大于正差值频率，负差值主要分布于（-2.00\~0.00）m2 /m2 ，冬季正负差值频率分布相当，主要分布于（-1.00\~1.00）m2 /m2 ，说明不同LAI产品间

表2 观测站点的基本信息  
Tab. 2 asic information about the observation site   

<table><tr><td>站点</td><td>代码</td><td>土地覆盖类型</td><td>经度/E</td><td>纬度/oN</td><td>集中月份</td><td>年份</td></tr><tr><td>甘肃临泽站</td><td>LZD</td><td>草地/谷类作物用地</td><td>100.13</td><td>39.35</td><td>5、7月</td><td>2014—2016</td></tr><tr><td>陕西安塞站</td><td>ASA</td><td>草地/谷类作物用地</td><td>109.31</td><td>36.86</td><td>6、7、8月</td><td>2014—2018</td></tr><tr><td>内蒙古奈曼站</td><td>NMD</td><td>草地/谷类作物用地</td><td>120.70</td><td>42.93</td><td>6、7、9月</td><td>2014—2018</td></tr><tr><td>辽宁沈阳站</td><td>SYA</td><td>草地/谷类作物用地</td><td>123.37</td><td>41.52</td><td>5、6、7、9月</td><td>2014—2018</td></tr><tr><td>江西鹰潭站</td><td>YTA</td><td>草地/谷类作物用地</td><td>116.93</td><td>28.21</td><td>6、7、8月</td><td>2014—2018</td></tr><tr><td>黑龙江海伦站</td><td>HLA</td><td>草地/谷类作物用地</td><td>126.93</td><td>47.45</td><td>5、6、7、8月</td><td>2014-2018</td></tr><tr><td>新疆策勒站</td><td>CLD</td><td>草地/谷类作物用地</td><td>80.44</td><td>37.01</td><td>5、6、7、9、10月</td><td>2014—2018</td></tr><tr><td>四川盐亭站</td><td>YGA</td><td>草地/谷类作物用地</td><td>105.46</td><td>31.27</td><td>2、3、6、7、8月</td><td>20142015</td></tr><tr><td>新疆阿克苏站</td><td>AKA</td><td>阔叶作物用地</td><td>80.83</td><td>40.62</td><td>5、6、7、8月</td><td>2014-2018</td></tr><tr><td>陕西长武站</td><td>CWA</td><td>阔叶作物用地</td><td>107.68</td><td>35.24</td><td>3、4、5、11月</td><td>2014—2018</td></tr><tr><td>内蒙古大兴安岭站</td><td>DXF</td><td>稀树草原</td><td>121.51</td><td>50.94</td><td>7、8月</td><td>2016、2018</td></tr><tr><td>广东鼎湖山站</td><td>DHF</td><td>常绿阔叶林</td><td>112.54</td><td>23.17</td><td>1月</td><td>2015</td></tr><tr><td>云南西双版纳站</td><td>BNF</td><td>常绿阔叶林</td><td>101.20</td><td>21.96</td><td>全年</td><td>2014-2018</td></tr><tr><td>黑龙江帽儿山站</td><td>MEF</td><td>落叶阔叶林</td><td>127.67</td><td>45.42</td><td>7、8、9、10月</td><td>2014—2018</td></tr><tr><td>四川贡嘎山站</td><td>GGF</td><td>常绿针叶林</td><td>101.99</td><td>29.57</td><td>6、7、8、9、10月</td><td>2015、2016</td></tr></table>

注：非植被区域和缺失区域都采用白色表示。该图基于自然资源部标准地图服务网站下载的审图号为GS(2020)4632号的标准地图制作，底图无修改。

![](images/0ba942b8960eb746486c5d782506b8ace1b72fcbc67ce6736e06a1d151699929.jpg)  
图3 2014—2020年不同季节PROBAV LAI、VIIRS LAI和MODIS LAI差值中国空间分布  
Fig. 3 Spatial distribution of Difference values of PROBAV LAI，VIIRS LAI and MODISLAI in China in different seasons from 2014 to 2020

![](images/ef2dfbe8099b03e1b42d8cc2d92eb562d602875572de7a12f33128280817e5bb.jpg)  
图4 2014—2020年不同季节PROBAV LAI、VIIRS LAI与MODIS LAI差值的频率分布图Fig. 4 Frequency distribution diagram of differences between PROBAV LAI，VIIRS LAI and MODISLAI indifferent seasons from 2014 to 2020

还存在一定的差异性。

# 4.2 融合数据一致性和连续性分析

# 4.2.1 不同产品数据LAI值频率分布一致分析

研究利用2014—2020年不同产品有效像元，分析了不同季节（按气象季节划分，3—5月为春季，6—8月为夏季，9—11月为秋季，12月—次年2月为冬季）每一种产品的LAI变化范围和频率分布（图5），以评价融合数据与其他产品在空间上的一致性 。 结 果 表 明 MCD15A2H、MOD15A2H 和VNP15A2H 在四季不同 LAI 值频率分布几乎趋于一致，这是由于MCD15A2H与MOD15A2H的算法相同，而VNP15A2H的传感器(VIIRS)是MODIS系列的拓展和改进，是为了继续MODIS 时间序列，调整MODIS的查找表(LUT)算法而生成的[45]。在春、夏、秋季可明显看出在融合LAI值域范围内LAI和PROBA- V LAI 曲线平滑度稍好于 MCD15A2H、MOD15A2H 和 VNP15A2H，且 LAI 在 6\~7（/ m2 /m2）区间内出现频率上升，这可能是因为这3个产品的有效范围为0\~10（/ m2 /m2），而PROBA-VLAI利用时间滤波器进行异常值剔除，以及平滑和间隙填充将范围限定在 0\~7（/ m2 /m2）。融合 LAI 显然保留了PROBA-V LAI这一特点，从季节上看，它与其他4个产品LAI值的频率分布走势大致相同，符合我国植被生长特征。在冬季，融合LAI低值频率略高，与融合前对产品进行了重建，填充了空值区有关。

![](images/2f995ddcfbb3b46f19e4eaecb94fc8c3fd8508c2338d3aea188a2833e9ba6f0f.jpg)  
图5 2014—2020年不同季节LAI频率分布  
Fig. 5 LAI frequency distribution map of different seasons from 2014 to 2020

# 4.2.2 不同LAI产品数据时间一致性分析

为分析不同 LAI 产品的时间一致性，首先对2014—2020年各个LAI产品进行最大值月合成处理，然后选择代表不同土地覆盖类型的CERN站点，提取相应的月合成数据，生成LAI时间序列图（图6）。图6（a）为辽宁沈阳站LAI变化曲线，其土地覆盖类型为草地/谷类作物用地，不同产品时间序列曲线变化明显，符合当地生长季节特征。PRO-BA-V LAI的值高于其它产品值，特别是在生长季尤为明显，MCD15A2H、MOD15A2H和VNP15A2H三者的值较为接近，融合LAI的值则介于PROBA-V LAI和三者值之间。与站点的观测值比较，融合LAI的值与站点值更为接近，且趋势一致。图6(b)新疆阿克苏站的LAI变化曲线，其土地覆盖类型为阔叶作物用地，5种LAI产品整体差异不大，融合LAI 与 PROBA-V LAI 相似度更为接近，且与站点数据比较，PROBA-V LAI和融合LAI较其它产品，与观测值具有更好的一致性。图6（c）为内蒙古大兴安岭站LAI时间序列曲线，其土地覆盖类型为稀树草原，所有产品的曲线变化趋势都相似，并且年际间变化较低。PROBA-V LAI曲线在非生长季存在缺失；融合LAI在非生长季的值较其它产品高，这可能与融合前对产品中低质量值进行重建处理，提高了中低质量像元值有关。图6(d)为云南西双版纳站的LAI时间序列曲线，其土地覆盖类型为常绿阔叶林，MOD15A2H 和 VNP15A2H 的时间序列曲线波动较大，存在明显的波谷，融合LAI上下波动的范围较小，与站点观测值也拟合得较好。图6（e）为黑龙江帽儿山站的LAI时间序列曲线，其土地覆盖类型为落叶阔叶林，MCD15A2H、MOD15A2H和VNP15A2H的年际间变化较大，在某些年份融合LAI和PROBA-V LAI的峰值存在不一致的情况，但与站点观测值的一致性上表现良好。图6（f）为四川贡嘎山站LAI时间序列曲线，其土地覆盖类型为 常 绿 针 叶 林 ，MCD15A2H、MOD15A2H、VNP15A2H和融合LAI呈现出相似的曲线变化趋势，没有明显的年际变化和季节变化，LAI数值差异也较小。总的来看，融合LAI在不同土地覆盖类型中，与其它产品有较好的时间一致性，时序曲线较为平滑，噪点较少，变化趋势与其它产品较为一致，且与站点观测值有较好的一致性，符合我国植被的生长规律。

# 4.2.3 融合LAI与其他产品数据的一致性分析

图 7 为 2014—2020 年基于 CERN 站点的融合LAI与其他LAI产品关系的散点图，融合LAI与源数据 MCD15A2H LAI、VNP15A2H LAI 和 PROBA-VLAI呈现良好的相关性，R2 分别为0.85、0.84和0.89，P 值均小于 0.000 1，均方根误差分别为 0.72 m2 /m2 、0.74 m2 /m2 和 0.58 m2 /m2 。其中，融合 LAI 与 PRO-

BA-VLAI相关关系最好，回归方程较为接近1：1的连线状态，可能与融合数据过程中，利用基于像元质量的滤波对MODIS数据进行处理，提高数据质量有关，另外，与MODIS和VIIRS相比，研究表明PROBA-V LAI产品数据有更高的精度[24]，归一化过程中，进一步融合了该数据，使得融合LAI与质量更高的PROBA-V LAI产品数据有更高的相关性。与非融合源LAI产品MOD15A2H LAI也有较好的相关性，R2 为0.77，P<0.000 1，RMSE为0.89 m2 /m2 。4.2.4 不同LAI产品数据时空连续性分析

图8左列为2014—2020年不同LAI产品数据的 LAI 年 均 值 空 间 分 布 图 。 MCD15A2H LAI、MOD15A2H LAI、VNP15A2H LAI、PROBA-V LAI

![](images/1b9a8f64ad14ff90986b27c1a7b5b7e0097eaa4346cc16745374afa57c2d744a.jpg)  
(a)CERN-辽宁沈阳-草地/谷类作物用地

![](images/eb0819d93e74a2a60d905cdafeff963d2fc1a11c937ab83266015bf8774feec0.jpg)  
(b)CERN-新疆阿克苏-阔叶作物用地

![](images/07404f5b08f73e0d92bc191185e85d64653de9a2f8eff606f35d52e84c936f58.jpg)  
(c)CERN-内蒙古大兴安岭-稀树草原

（续上页）

![](images/032a5c170d4c80aeca986461c699533d3724abd1120616e4577231171cc2608f.jpg)  
图6 2014—2020年不同土地覆盖类型不同LAI产品时间序列  
Fig. 6 Time series of LAI products of different land cover types from 2014 to 2020

和融合 LAI 的年均值分别为 1.52 m2 /m2 、1.43 m2 /m2 、1.40 m2 /m2 、0.99 m2 /m2 和 1.50 m2 /m2 。 图 8 右 列2014—2020年不同LAI产品数据缺失情况分布图，参考 Weiss 和 Fang 等的分析方法[48-50] ，根据各产品的像元质量标识，将有云雪使用备用算法的植被覆盖像元标记为缺失值计算年均缺失率。从图中可见，中国区域缺失值区域主要集中于我国东北、西南地区。PROBAV LAI和融合LAI相较研究中其它LAI产品数据，表现出更好的空间完整度，PRO-BAVLAI使用神经网络（ANN）得到反演结果，虽在反演时应用间隙填充程序，但仍存在缺失的现象。融合 LAI 由于重建工作及多源传感器使其在空间分布上较为完整，但仍有小部分受云雨天气、传感器观测角度等多重因素影响存在缺失情况。

图 9 为 2014—2020 年不同 LAI 产品在中国区域15个CERN站点的缺失情况和分布频率。整体上看，LAI产品在夏季和冬季受云雨雪等不良天气条件的影响，与春季和秋季比较，缺失频率较高。MCD15A2H LAI、MOD15A2H LAI、VNP15A2HLAI、PROBA-V LAI和融合LAI平均缺失频率分别为 19.59%、25.54%、23.33%、9.64%和 5.04%，其中代表 西 南 地 区 的 平 均 缺 失 频 率 分 别 为 24.49% 、39.59%、29.80%、10.09%、7.21%，相较于其他产品，融合LAI缺失频率大大降低；由于MCD15A2H LAI数据源于2个传感器，与MOD15A2H LAI数据源于单个传感器相比，缺失频率有所降低，可以看出多传感器数据的组合使用，可以有效提高LAI的时间连续性。PROBA-V LAI缺失频率低于其它源LAI产品，这可能是使用CYCLOPE和第5版本MOD15A2产品的同期LAI进行训练，并应用缺口填充程序的结果，多个传感器可以收集更多有效的LAI以丰富细节[15]，PROBA-V LAI的验证报告[51] 也显示，它在通常受云覆盖影响的地区有非常好的完整性。

![](images/6085bb0d787ffc8a0589753a6f375185100c0d7b069c1c897d55758400e618cd.jpg)  
图7 2014—2020年基于CERN站点融合LAI与其它LAI产品关系的散点图  
Fig. 7 Scatter diagram of fusion LAI and other LAI products based on CERN site during 2014—2020

# 4.3 融合数据精度分析

利用2014—2020年CERN站点的地面观测数据，对融合生成的LAI直接验证，结果如图10所示。实线为观测数据与各 LAI 数据所建立的回归方程，中间虚线为1：1线，两侧的虚线表示偏差为±1.00m2 /m2 的回归线。相较其它源 LAI 产品数据，PROBA-V LAI与地面观测数据表现出更高的相关性，这与Brown[24]的研究结果一致，同时Camacho和Weiss的研究表明[11,52]，共享类似检索方案的相关GEOV1 产品在与验证数据的一致性上优于其它LAI产品。与融合前源LAI产品比较，融合LAI与地面观测数据的相关性最高(R2 =0.76，P<0.000 1)，均方根误差(RMSE)为 1.16 m2 /m2 ，具有较高的数据精度，其中，融合 LAI 偏差范围为-1.00 m2 /m2 到1.00 m2 /m2 的数据约占 73.00%。不同 LAI 数据在不同覆盖类型站点的表现分析表明（表3），融合LAI表现均好于其它产品，其中，在草地与谷类作物用地类型上，融合 LAI 的 R2 为 0.71（P<0.000 1），比其它产品的 R2 值高 0.05\~0.26，RMSE 为 0.73 m2 /m2 ，比其它产品的 RMSE 值低（0.07\~0.42）m2 /m2 。在阔叶作物用地类型上融合LAI的R2 为0.48（P<0.000 1），

![](images/6e62850f9b11b4cec83ab8b6b4050d2dbde80f17ef2ce9fdc6693c56693f219a.jpg)  
注：非植被区域和缺失区域都采用白色表示。该图基于自然资源部标准地图服务网站下载的审图号为GS(2020)4632号的标准地图制作，底图无修改。  
图8 2014—2020年不同LAI产品的年均值图及缺失情况分布

![](images/ce74498ab136467d82c7328c0ac2f968773929911a1a3575e67e0435d318e494.jpg)  
Fig. 8 Annual mean maps and missing distribution maps of different LAI products from 2014 to 2020   
图9 基于CERN站点2014—2020年不同LAI产品缺失频率分布

Fig. 9 Based on the missing frequency distribution diagram of different LAI products at CERN site from 2014 to 2020比其它产品的R2 值高0.04\~0.12，RMSE为1.19 m2 /m2 ，比其它产品的 RMSE 值低 0.00\~0.37（m2 /m2）。在森林类型上融合 LAI 的 R2 为 0.53（P<0.000 1），比其它产品的 R2 值高 0.10\~0.25，RMSE 为 1.33 m2 /m2 ，比其它产品的RMSE值低0.20\~0.93（m2 /m2）。

表3 不同产品在森林和非森林类型站点的对比结果  
Tab. 3 Comparative results of products of different land cover types   

<table><tr><td></td><td colspan="3">MCD15A2H</td><td colspan="3">MOD15A2H</td><td colspan="3">VNP15A2H</td><td colspan="3">PROBA-V</td><td colspan="3">融合LAI</td></tr><tr><td>土地覆盖类型</td><td>R</td><td>RMSE</td><td>n</td><td>R</td><td>RMSE</td><td>n</td><td>R</td><td>RMSE</td><td>n</td><td>R</td><td>RMSE</td><td>n</td><td>R</td><td>RMSE</td><td>n</td></tr><tr><td>草地/谷类作物用地</td><td>0.60</td><td>0.91</td><td>53</td><td>0.45</td><td>1.15</td><td>53</td><td>0.59</td><td>1.14</td><td>53</td><td>0.66</td><td>0.80</td><td>53</td><td>0.71</td><td>0.73</td><td>53</td></tr><tr><td>阔叶作物用地</td><td>0.44</td><td>1.31</td><td>32</td><td>0.42</td><td>1.40</td><td>32</td><td>0.36</td><td>1.56</td><td>32</td><td>0.39</td><td>1.19</td><td>32</td><td>0.48</td><td>1.19</td><td>32</td></tr><tr><td>森林</td><td>0.31</td><td>1.99</td><td>81</td><td>0.28</td><td>2.26</td><td>81</td><td>0.36</td><td>2.05</td><td>81</td><td>0.43</td><td>1.53</td><td>81</td><td>0.53</td><td>1.33</td><td>81</td></tr></table>

# 5 讨论

目前，对于不同卫星传感器反演的LAI时间序列产品，由于连续性和质量问题，极大地阻碍了应用[11]，长时序数据重建和多传感器数据的融合，可为其提供解决有效的方案，在不同传感器数据融合研究中，结合物候特征及周期，应用线性模型进行融合[13,15,19,35] ，往往难以精确描述非线性模式[22] 及多源LAI数据间的复杂关系，本研究引入非参数估计方法中的核回归模型进行归一化融合，同时在融合前采用改进的S-G滤波算法进行重建，以提升融合源单传感器LAI时间序列数据质量。并在归一化过程中，引入非监督分类方法确定相似像元，克服了过去多源遥感数据归一化研究中，通过分类数据（如土地覆盖分类数据），人为设定阈值[35]来寻找相似像元的不足，极大地排除人为干扰，提高了运算效率。本研究表明，基于改进S-G滤波和非监督分类局部核回归的融合方法，对2014—2020年MCD15A2H、PRO-BA-V和VNP15A2H的LAI产品进行归一化融合，得到的中国区LAI数据，整体上既保持了与源数据较好的相关性和时间变化上的一致性，同时减少了数据缺失率，提高了产品数据的连续性，并降低了数据误差，提高了产品数据精度。

融合前LAI数据重建，研究选用了基于像元质量分析的S-G滤波重建方法，不同滤波方法可能对最后融合产生较大影响。在归一化框架中，参考数据是影响精度的重要因素，参考数据的质量在某种程度上决定着最后的融合结果，因此，不同参考数据可能会带来不同的融合结果，应尽可能选择较高时间分辨率和较大幅宽的传感器数据，并考虑产品数据的成熟度和应用广泛性。

另外，目前LAI观测数据集仍十分有限，给不同区域不同覆盖类型融合LAI产品定量分析和验证带来一定的局限性和不确定性，特别是本文研究期限内，落叶针叶林和灌木林覆盖区域没有合适的验证观测站点数据，有待于长期LAI观测网的建立和数据共享。

在验证阶段，研究使用了站点观测数据，尽管研究采取质量控制来保证其精确性，但由于粗分辨率像元存在异质性，不可避免会存在一定的不确定性，这也是卫星LAI产品被普遍低估的原因之一[16]。

随着遥感卫星平台和传感器的发展，如何充分利用不同传感器LAI产品的优势，克服其不足，融合更多不同来源LAI产品和更多的不同时空分辨率、不同时序长度产品数据，使得遥感数据产品具有更好的物理意义一致性，在时间和空间上有较好的一致性，并提高数据精度，以更好的满足陆面模式模拟对地表参数的需求，更好的服务于多种应用，仍是当前遥感数据应用的重要挑战和难题。本文探讨了多传感器LAI数据归一化融合，该方法不仅适用于不同传感器LAI长时序数据处理，同时也为其它指标或参数，如归一化植被指数的归一化融合提供了参考，但不同滤波方法对融合产生的影响、归一化过程的更多人工智能和机器学习算法的比较和应用、不同时序长度和不同分辨率数据融合，以及地表观测数据的同化等仍有待深入研究。

# 6 结论

（1）研究提出了一种不同传感器平台LAI时序数据归一化融合方法。该方法引入了局部核回归模型，以更精确描述非线性模式及多源LAI数据之间的复杂关系，进行 LAI 归一化融合，同时在融合前采用改进的S-G滤波算法进行数据重建，提升融合源单传感器LAI时间序列数据质量，并在归一化过程中引入非监督分类方法确定相似像元，并极大地排除人为干扰，提高了运算效率和客观性，达到充分利用多源遥感数据的优势，提高产品的连续性、一致性和精确性的目的。

![](images/3056324b1ba163604a807ff3c0aeb03395df9b443515b13b7fba433662348007.jpg)  
图10 LAI产品与地面观测结果比较  
Fig. 10 Comparison of LAI products and ground measurements

（2）研究利用本文融合方法，以MCD15A2H为参考，对 2014—2020 年 PROBA-V 和 VIIRS 的 LAI数据开展了归一化融合研究，在中国区域，整体上源 数 据 产 品 PROBA- V LAI 平 均 值 小 于MCD15A2H LAI，在中国东北、西南、东南地区表现较 大 差 异 ，VNP15A2H LAI 平 均 值 也 稍 低 于MCD15A2H LAI，与PROBA-V LAI和MCD15A2HLAI的差值比较，其差值空间分布较为均匀。PRO-BA-V LAI、VNP15A2H LAI 与 MCD15A2H LAI 的像元差值集中分布于(-1.00\~1.00）m2 /m2 区间，超过60.00% 的 像 元 差 值 分 布 在（- 0.50\~0.50）m2 /m2 。VNP15A2H LAI与MCD15A2H LAI的差值分布频率在春、冬季较为均匀，夏、秋季负差值频率则略大于正差值频率，PROBA-V LAI与MCD15A2H LAI春、夏和秋正差值分布频率小于负差值分布频率，冬季正负差值频率分布相当，不同LAI产品间存在一定的差异性。

（3）与 MCD15A2H、MOD15A2H、VNP15A2H和 PROBA-V 等 LAI 产品比较，融合 LAI 数据与该四个产品有较好的数值频率分布一致性和时间变化一致性，LAI值各季节频率分布变化趋势一致，时序曲线较为平滑，噪点较少，变化趋势与其它产品较为一致，且与站点观测值有较好的一致性，符合我国植被的生长规律。在空间连续性上，融合LAI相较其它产品在空间分布上较为完整，但仍有小部分受云雨天气、传感器观测角度等多重因素影响存在缺失情况。在时间连续性上，融合LAI平均缺失频率为 5.04%，相较于 MCD15A2H LAI(19.59% )、MOD15A2H LAI (25.54% )、 VNP15A2H LAI(23.33%)和 PROBA-V LAI(9.64%)，数据缺失频率最低，多传感器数据融合使用在提高LAI时间连续性上具有重要作用。

（4）融合LAI数据与CERN站点观测值验证决定 系 数 R2 为 0.76，RMSE 为 1.16 m2 /m2 ，优 于MCD15A2H、MOD15A2H、VNP15A2H 和 PROBA-V等LAI产品，融合LAI数据偏差在（-1.00～1.00）m2 /m2 范围的数据约占 73.00%。同时，融合 LAI 与源产品和其它LAI产品(MCD15A2H、MOD15A2H、VNP15A2H、PROBA-V)整体上表现出良好的相关性，R2 分别为0.85、0.77、0.84和0.89。

# 参考文献(References)：

[ 1 ] Watson D J. Comparative physiological studies on the growth of field crops: I. variation in net assimilation rate and leaf area between species and varieties, and within and between years[J]. Annals of Botany, 1947,11(1):41- 76. DOI:10.1093/oxfordjournals.aob.a083148

[2] 刘洋,刘荣高,陈镜明,等.叶面积指数遥感反演研究进展 与展望[J].地球信息科学学报,2013,15(5):734-743. [ Liu Y, Liu R G, Chen J M, et al. Current status and perspectives of leaf area index retrieval from optical remote sensing data[J]. Journal of Geo-Information Science, 2013,15 (5):734-743. ] DOI:10.3724/SP.J.1047.2013.00734

[ 3 ] Huang D, et al. Stochastic transport theory for investigating the three- dimensional canopy structure from space measurements[J]. Remote Sensing of Environment, 2008, 112(1):35-50. DOI:10.1016/j.rse.2006.05.026

[ 4 ] Baret F. LAI, fAPAR and fCover CYCLOPES global products derived from VEGETATION[J]. Remote Sensing of Environment, 2007,110(3):275-286. DOI:10.1016/j. rse.2007.02.018

[ 5 ] Tum M, Günther K, Böttcher M, et al. Global gap- free MERIS LAI time series (2002-2012)[J]. Remote Sensing, 2016,8(1):69. DOI:10.3390/rs8010069

[ 6 ] Che M L, et al. Spatial and temporal variations in the end date of the vegetation growing season throughout the Qinghai- Tibetan Plateau from 1982 to 2011[J]. Agricultural and Forest Meteorology, 2014,189/190:81- 90. DOI: 10.1016/j.agrformet.2014.01.004

[7] 黄健熙,武思杰,刘兴权,等.基于遥感信息与作物模型集 合卡尔曼滤波同化的区域冬小麦产量预测[J].农业工程 学报,2012,28(4):142-148. [ Huang J X, Wu S J, Liu X Q, et al. Regional winter wheat yield forecasting based on assimilation of remote sensing data and crop growth model with Ensemble Kalman method[J]. Transactions of the Chinese Society of Agricultural Engineering, 2012,28(4): 142-148. ] DOI:10.3969/j.issn.1002-6819.2012.04.023

[8] 陈洪萍,贾根锁,冯锦明,等.气候模式中关键陆面植被参 量遥感估算的研究进展[J].地球科学进展,2014,29(1): 56-67. [ Chen H P, Jia G S, Feng J M, et al. Remote sensing estimates of key land surface vegetation variables used in climate model: A review[J]. Advances in Earth Science, 2014,29(1):56- 67. ] DOI:10.11867/j.issn.1001- 8166.2014.01.0056

[9] 侯吉宇,周艳莲,刘洋.不同叶面积指数遥感数据模拟中 国总初级生产力的时空差异[J].遥感技术与应用,2020, 35(5):1015-1027. [ Hou J Y, Zhou Y L, Liu Y. Spatial and temporal differences of GPP simulated by different satellite- derived LAI in China[J]. Remote Sensing Technology and Application, 2020,35(5):1015-1027. ]

[10] Zeng Z Z, Piao S L, Li L Z X, et al. Climate mitigation

from vegetation biophysical feedbacks during the past three decades[J]. Nature Climate Change, 2017,7(6):432- 436. DOI:10.1038/nclimate3299   
[11] Camacho F, et al. GEOV1: LAI, FAPAR essential climate variables and FCOVER global time series capitalizing over existing products. Part 2: Validation and intercomparison with reference products[J]. Remote Sensing of Environment, 2013,137:310- 329. DOI:10.1016/j.rse.201 3.02.030   
[12] Zhou X J, et al. Reconstruction of time series leaf area index for improving wheat yield estimates at field scales by fusion of Sentinel-2,-3 and MODIS imagery[J]. Computers and Electronics in Agriculture, 2020,177:105692. DOI:10.1016/j.compag.2020.105692   
[13] Wang D D, Liang S L. Improving LAI mapping by integrating MODIS and CYCLOPES LAI products using optimal interpolation[J]. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2014,7 (2):445-457. DOI:10.1109/JSTARS.2013.2264870   
[14] Ma H, et al. Development of the GLASS 250-m leaf area index product (version 6) from MODIS data using the bidirectional LSTM deep learning model[J]. Remote Sensing of Environment, 2022,273:112985. DOI:10.1016/j. rse.2022.112985   
[15] Liu Q, et al. Retrieval of leaf area index using temporal, spectral, and angular information from multiple satellite data[J]. Remote Sensing of Environment, 2014,145:25- 37. DOI:10.1016/j.rse.2014.01.021   
[16] Huang A Q, et al. A methodology to reconstruct LAI time series data based on generative adversarial network and improved Savitzky- Golay filter[J]. International Journal of Applied Earth Observation and Geoinformation, 2021, 105:102633. DOI:10.1016/j.jag.2021.102633   
[17] Verger A, et al. A multisensor fusion approach to improve LAI time series[J]. Remote Sensing of Environment, 2011,115(10):2460-2470. DOI:10.1016/j.rse.2011.05.006.   
[18] Munier S, Carrer D, Planque C, et al. Satellite leaf area index: Global scale analysis of the tendencies per vegetation type over the last 17 years[J]. Remote Sensing, 2018, 10(3):424. DOI:10.3390/rs10030424   
[19] Sadeh Y, et al. Fusion of Sentinel-2 and PlanetScope timeseries data into daily 3 m surface reflectance and wheat LAI monitoring[J]. International Journal of Applied Earth Observation and Geoinformation, 2021,96:102260. DOI: 10.1016/j.jag.2020.102260   
[20] Fang H L, Baret F, Plummer S, et al. An overview of global leaf area index (LAI): Methods, products, validation, and applications[J]. Reviews of Geophysics, 2019,57(3): 739-799. DOI:10.1029/2018rg000608   
[21] 张良培,沈焕锋.遥感数据融合的进展与前瞻[J].遥感学 报,2016,20(5):1050-1061. [ Zhang L P, Shen H F. Progress and future of remote sensing data fusion[J]. Journal of Remote Sensing, 2016,20(5):1050-1061. ] DOI:10.118 34/jrs.20166243   
[22] Miura T, et al. An empirical investigation of cross-sensor relationships of NDVI and red/near- infrared reflectance using EO- 1 Hyperion data[J]. Remote Sensing of Environment, 2006,100(2):223- 236. DOI:10.1016/j.rse.2005. 10.010   
[23] Jiang N, Zhu W Q, Zheng Z T, et al. A comparative analysis between GIMSS NDVIg and NDVI3g for monitoring vegetation activity change in the Northern Hemisphere during 1982- 2008[J]. Remote Sensing, 2013,5(8):4031- 4044. DOI:10.3390/rs5084031   
[24] Brown L A, et al. Evaluation of global leaf area index and fraction of absorbed photosynthetically active radiation products over North America using Copernicus Ground Based Observations for Validation data[J]. Remote Sensing of Environment, 2020,247:111935. DOI:10.1016/j.rs e.2020.111935   
[25] Fang H L, et al. Validation of global moderate resolution leaf area index (LAI) products over croplands in northeastern China[J]. Remote Sensing of Environment, 2019, 233:111377. DOI:10.1016/j.rse.2019.111377   
[26] Song B W, Liu L Y, Zhao J J, et al. Validation of four coarseresolution leaf area index products over croplands in China using field measurements[J]. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing,14: 9372-9382. DOI:10.1109/JSTARS.2021.3108172   
[27] Houborg R. A Spatio-Temporal Enhancement Method for medium resolution LAI (STEM- LAI) [J]. International Journal of Applied Earth Observation and Geoinformation, 2016,47:15-29. DOI:10.1016/j.jag.2015.11.013   
[28] Zhu X L, Cai F Y, Tian J Q, et al. Spatiotemporal fusion of multisource remote sensing data: Literature survey, taxonomy, principles, applications, and future directions[J]. Remote Sensing, 2018,10(4):527. DOI:10.3390/rs10040527   
[29] 张慧芳,高炜,施润和.基于背景库的高质量LAI时间序 列数据重建[J].遥感学报,2012,16(5):986-999. [ Zhang H F, Gao W, Shi R H. Reconstruction of high- quality LAI time-series product based on long-term historical database [J]. Journal of Remote Sensing, 2012,16(5):986-999. ]   
[30] 周惠慧,王楠,黄瑶,等.不同时间间隔下的遥感时间序列 重构模型比较分析[J].地球信息科学学报,2016,18(10): 1410-1417. [ Zhou H H, Wang N, Huang Y, et al. Comparison and analysis of remotely sensed time series of reconstruction models at various intervals[J]. Journal of Geo-Information Science, 2016,18(10):1410-1417. ] DOI: 10.3724/SP.J.1047.2016.01410   
[31] 周旻悦,沈润平,陈俊,等.基于像元质量分析和异常值检 测的LAI时序数据S-G滤波重建研究[J].遥感技术与应 用,2019,34(2):323-330. [ Zhou M Y, Shen R P, Chen J, et al. Filtering and reconstruction of LAI time series data by S-G filter based on pixel quality analysis and outlier detection [J]. Remote Sensing Technology and Application, 2019,34 (2):323-330. ] DOI:10.11873/j.issn.1004-0323.2019.2.0323.   
[32] Steinier J, Termonia Y, Deltour J. Smoothing and differentiation of data by simplified least square procedure[J]. Analytical Chemistry, 1972,44(11):1906-1909. DOI:10.1021/ ac60319a045   
[33] Olthof I, et al. Landsat- 7 ETM + radiometric normalization comparison for northern mapping applications[J]. Remote Sensing of Environment, 2005,95(3):388-398. DOI: 10.1016/j.rse.2004.06.024   
[34] Gao F, Masek J G, Wolfe R E, et al. Building a consistent medium resolution satellite data set using moderate resolution imaging spectroradiometer products as reference [C]//2010:043526. DOI:10.1117/1.3430002   
[35] Gan W X, Shen H F, Zhang L P, et al. Normalization of medium-resolution NDVI by the use of coarser reference data: Method and evaluation[J]. International Journal of Remote Sensing, 2014,35(21):7400- 7429. DOI:10.1080/ 01431161.2014.968684   
[36] 田振坤,傅莺莺,刘素红,等.基于无人机低空遥感的农作 物快速分类方法[J].农业工程学报,2013,29(7):109-116, 295. [ Tian Z K, Fu Y Y, Liu S H, et al. Rapid crops classification based on UAV low- altitude remote sensing[J]. Transactions of the Chinese Society of Agricultural Engineering, 2013,29(7):109- 116,295. ] DOI:10.3969/j.iss n.1002-6819.2013.07.014   
[37] Napoleon D, Pavalakodi S. A new method for dimensionality reduction using KMeans clustering algorithm for high dimensional data set[J]. International Journal of Computer Applications, 2011,13(7):41- 46. DOI:10.5120/ 1789-2471   
[38] Zhang K B, Gao X B, Tao D C, et al. Single image superresolution with non- local means and steering kernel regression[J]. IEEE Transactions on Image Processing: a Publication of the IEEE Signal Processing Society, 2012, 21(11):4544-4556. DOI:10.1109/TIP.2012.2208977   
[39] Nadaraya E A. On estimating regression[J]. Theory of Probability & Its Applications, 1964,9(1):141- 142. DOI: 10.1137/1109020   
[40] Watson G S. Smooth regression analysis[J]. Sankhyā: the Indian Journal of Statistics, Series A (1961- 2002), 1964, 26(4):359-372.   
[41] 龙柯吉,师春香,韩帅,等.中国区域高分辨率温度实况融 合格点分析产品质量评估[J].高原山地气象研究,2019, 39(3):67-74. [ Long K J, Shi C X, Han S, et al. Quality assessment of high resolution temperature merged grid analysis product in China[J]. Plateau and Mountain Meteorology Research, 2019,39(3):67- 74. ] DOI:10.3969/j.issn. 1674-2184.2019.03.011   
[42] Knyazikhin Y, Martonchik J V, Diner D J, et al. Estimation of vegetation canopy leaf area index and fraction of absorbed photosynthetically active radiation from atmosphere- corrected MISR data[J]. Journal of Geophysical Research: Atmospheres, 1998,103(D24):32239- 32256. DOI:10.1029/98jd02461   
[43] Myneni R B, Ramakrishna R, Nemani R, et al. Estimation of global leaf area index and absorbed par using radiative transfer models[J]. IEEE Transactions on Geoscience and Remote Sensing, 1997,35(6):1380- 1393. DOI:10.1109/ 36.649788   
[44] Lacaze R, Smets B, Baret F, et al. Operational 333m biophysical products of the Copernicus global land service for agriculture monitoring[J]. The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 2015,XL-7/W3:53-56. DOI:10.5194/ isprsarchives-xl-7-w3-53-2015   
[45] Yan K, Park T, Chen C, et al. Generating global products of LAI and FPAR from SNPP- VIIRS data: Theoretical background and implementation[J]. IEEE Transactions on Geoscience and Remote Sensing, 2018,56(4):2119- 2137. DOI:10.1109/TGRS.2017.2775247   
[46] MCD12Q1 数 据 [EB/OL]. https://earthdata.nasa.gov/. [MCD12Q1 data(2019) [EB/OL]. https://earthdata.nasa. gov/. ]   
[47] 吴冬秀,张琳,宋创业.陆地生态系统生物观测指标与规 范[M].北京:中国环境出版集团,2019. [ Wu D X, Zhang L, Song C Y. Protocols for standard biological observation and measurement in terrestrial ecosystems[M]. Beijing: China Publishing Group Environment, 2019. ]   
[48] Weiss M, et al. LAI and fAPAR CYCLOPES global products derived from VEGETATION. Part 2: Validation and comparisonw ith MODIS collection 4 products[J]. Remote Sensing of Environment, 2007,110(3):317- 331. DOI:10.1016/j.rse.2007.03.001   
[49] Fang H L, et al. Validation of MODIS and CYCLOPES LAI products using global field measurement data[J]. Remote Sensing of Environment, 2012,119:43- 54. DOI:10. 1016/j.rse.2011.12.006   
[50] Fang H L, Jiang C Y, Li W J, et al. Characterization and intercomparison of global moderate resolution leaf area index (LAI) products: Analysis of climatologies and theoretical uncertainties[J]. Journal of Geophysical Research: Biogeosciences, 2013,118(2):529- 548. DOI:10.1002/jgr g.20051   
[51] Fuster B, Sánchez- Zapero J, Camacho F. Copernicus Global Land Operations“Vegetation and Energy”[J]. Scientific ouality evaluation, 2020.   
[52] Weiss M, Baret F, Block T, et al. On line validation exercise (OLIVE): A web based service for the validation of medium resolution land products. application to FAPAR products[J]. Remote Sensing, 2014,6(5):4190-4216. DOI: 10.3390/rs6054190