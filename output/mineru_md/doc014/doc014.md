# 华北平原冬小麦—夏玉米轮作区DLM与CLM5模型模拟对比研究

王 菲 1 ，陈报章 1,3\* ，陈 婧 2 ，张慧芳 1 ，郭立峰 1(1. 中国科学院地理科学与资源研究所，资源与环境信息系统国家重点实验室，北京 100101；2. 北京市气象局，北京 100089；3.江苏省地理信息资源开发与利用协同创新中心，南京 210023)

摘 要：作物生长与气候的互馈是当前气候变化研究的热点之一。陆面模型作为一项重要的研究工具，其模型框架、算法设计及参数化方案的不同会直接导致模拟结果的不确定性。为探究陆面模型DLM(dynamic land model)和CLM5(community land model)在作物生长及农田热通量模拟方面的差异及原因，评估2个模型在华北平原作物研究中的适用程度，论文开展了冬小麦—夏玉米轮作站点的模拟对比研究。结果显示，DLM的夏玉米叶面积指数和生态系统总初级生产力的模拟值更高，与观测值更为接近；CLM5模型则在冬小麦模拟中略优。DLM的潜热模拟值与观测值的相关性普遍更高，可能反映了DLM采用的彭曼公式、双叶策略比CLM5采用基于水势梯度质量守恒、大叶策略的潜热计算方法更具优势。对于产量，模型当前的估测能力并不理想。总的来说，在默认设定下，2个模型的模拟结果能基本反映研究区农田站点内夏玉米和冬小麦的生长规律，但与实测值存在一定偏差。模型在该区域的适用性可能需要通过添加农田管理措施、算法优化和参数本地化等方式进一步提高。

关 键 词：夏玉米—冬小麦轮作；DLM模型；CLM5模型；生长模拟；模型对比与评估；华北平原

据联合国粮农组织统计，农田约占全球陆地表面的 11%[1]，人类通过农业活动深刻地改变着地表物质能量格局[2]。农田均一密集的分布方式改变了陆地反照率，影响着大气—陆表间的热流循环；农业耕作改变了土壤中碳氮循环过程，引起温室气体的排放，加剧着全球气候变暖的形势[3]。与此同时，气候的多变性及气候变化反过来又成为影响农业发展的主要原因[4-6]。农业生产，特别是作物种植，受气候变化影响显著。研究证明，温度升高易造成作物物候期提前、生长季缩短，使得作物积累有机质减少，产量下降[7-8]；部分极端天气(高温、干旱)还会给作物生长带来不可逆的影响[9-11]。

为了定量化研究气候变化与农业生产间的相互作用关系，学者们首先利用大气模式，将自然植被替换为简单作物(通常为C3草本植物)，来模拟农业种植对大气和地球系统的扰动[12-14]。随着地球系统模式的进一步发展，陆面模型逐渐有了独立的作物模块[15-18]。这样一来，可实现不同气候条件下的作物生长模拟，及作物对陆表能量流动和物质循环的影响研究。并且，随着模型中农田管理措施的增加与发展，如灌溉和施肥[19]，农业耕作在改变陆地生态系统和气候方面的角色定位将更加准确和清晰。

CLM(community land model)模型是地球系统框架下最新一代的陆面过程模型，较全面地考虑了各项地表过程，完整细致地描述了陆地碳循环、土地覆被变化和植被的动态变化等，近些年得到了广泛关注和应用。Levis等[20] 将Agro-IBIS模型融合到了 CLM 模型 4.0 版本中，由此形成了作物模块。Drewniak 等[3] 在 Levis 等[20] 的基础上发展了单独的CLM4.5-Crop模型，将作物类型由4种扩展为8种，增加了氮的重分配、大豆固氮、施肥和留茬等过程。在最新发展的CLM5模型中[21]，增加了更多的作物类型，如棉花、水稻和甘蔗，总作物类型增加至65种。CLM5-Crop模型还根据纬度改进了某些作物的物候触发机制，调整了部分物候参数值，对施肥速率和灌溉机制进行了比较明显的调整[22-23]。较其他陆面过程模型的作物模块，如LPJ-mL[15,24]、OR-CHIDEE-STICS模型[25]等，CLM考虑了作物的氮循环，包含明确的器官发育和收获留茬过程，能更好地服务于作物的生长模拟及其影响研究。

DLM(dynamic land model) 模 型 是 基 于 EASS(ecosystem- atmosphere simulation scheme) [26- 27] 和CLM4模型发展而来的[28-29]。在继承EASS和CLM4优秀算法的基础上，重新优化了部分植被关键参数，改进了植被冠层和土壤层的水热通量、碳通量和动态植被的部分算法[28-29]，以增强对陆表物理、生物和化学过程的模拟。在冠层尺度的潜热计算上，采用彭曼公式[30]和双叶冠层模型[31-32]代替了CLM中质量守恒算法[33]和大叶模型[34]。对于作物部分，DLM基本延续CLM4模型算法，但以生长季指数模型(growing season index, GSI)[35] 作为判别物候期的方法。相比于CLM中传统的积温模型[36]，GSI能够更为灵活地引入其他物候影响因子(如温度、光照和土壤水分)，从而更为综合地判别植物的物候阶段[37] 。

华北平原是中国第二大平原，人口密集，粮食需求量大；城镇化水平高、进程快。然而后备土地资源不足，耕地占用比例逐渐上升并占主体地位[38]。面对巨大的粮食需求和有限的土地资源，华北平原地区通过发展集约型农业、作物轮作、灌溉和增施肥料等方式来提高粮食产量。当前，华北平原的粮食产量可占全国总产量的20%以上。然而高度发达的农业也给当地的生态环境带来了一定负面效应，如土壤盐渍化、肥力退化、局部气候改变等，这都将影响着华北平原农业的可持续性发展。

虽然较多学者利用CLM作物模型开展了作物生长模拟及农田—大气相互作用等研究[39- 41]，但DLM模型作物模块的应用研究仍比较匮乏。特别是2个模型在植物物候期判别方法、碳氮分配方案、冠层模型和热通量计算方面有着明显差别，可能会影响作物生长和农气相互作用的模拟结果及结论。因此，利用2个模型在中国华北平原开展模拟研究，可探究模型算法、参数化方案等的不同所造成的作物生长模拟差异；同时评估2个模型在华北平原作物研究中的适用程度。根据模型模拟结果，未来可有针对性地对模型做进一步优化和发展，以更好地服务于中国的粮食种植和农业可持续发展。

# 1 研究区域、数据及方法

# 1.1 农田生态站点简介及站点数据概况

本文选择华北平原地区的栾城站(LCA，37.88°N、114.68°E)、禹城站(YCA，36.93°N、116.56°E)和商丘站(SQA，34.52°N、115.58°E)3 个农田生态站[42] ，以及海河流域的怀来站(HLA，40.36°N、115.79°E)[43-44]和馆陶站(GTA，36.52°N、115.13°E)[45- 46] 2 个农田通量站开展模拟研究。栾城、禹城和商丘农田生态站均属于温带季风气候，多年平均气温分别为 12.2、13.1 和 13.9 ℃ ，年 降 水 量 分 别 为 530、582 和 708mm。3个站点的土壤类型基本为潮土，粘土含量较高，砂土含量较低。农作物主要为冬小麦—夏玉米轮作种植。怀来和馆陶农田通量站年均气温分别约 为 10.1、14 ℃ ，年 均 降 水 量 分 别 约 为 370、500mm，主要集中在夏季，怀来站农作物主要为单季夏玉米，馆陶站为冬小麦—夏玉米轮作。

农田生态站数据从国家生态科学数据中心获取(http://www.nesdc.org.cn)，分为气象数据和农田数据。气象数据的时间分辨率为0.5 h，包括气温、短波辐射、降水、相对湿度、风速和大气压等，为驱动模型的大气强迫场数据。农田数据包含作物物候记录(用于模型播种时间、收获时间和种植时长等参数的设定)、叶面积指数(leaf area index, LAI)和作物产量数据(用于模型模拟结果的验证)。

受仪器或人为因素的影响，站点气象数据容易存在缺失或者异常的问题。对于异常数据，予以剔除。缺失时间段在2 h之内的数据，利用分段线性插值法进行填补。缺失时间较长的数据：气温和辐射数据采用正弦函数插值；相对湿度采用余弦函数插值；降水和风速数据则仍采用分段线性插值方法

处理。

农田通量站数据从国家青藏高原科学数据中心获取(https://data.tpdc.ac.cn/zh-hans/)，分为气象数据和通量数据。气象数据的分辨率、内容及用途与农田生态站数据一致。通量数据的时间分辨率为0.5 h，包含碳通量——生态系统总初级生产力(gross primary production，GPP)和热通量——潜热通量(latent heat flux, LE)。此外，禹城站点也有部分GPP和LE的通量观测数据，均将用于模型模拟结果的验证与分析。

由于仪器无法直接测量GPP通量，因此本文利用 REddyProcWeb 线 上 工 具 (https://www.bgc- jena.mpg.de/bgi/index.php/Services/REddyProcWeb)，对 观测得到的净生态系统碳交换量(NEE)和生态系统呼吸量(Re)进行异常峰值剔除、摩擦风速校正、插补等处理，再用NEE减去Re得到GPP数据。

本文所使用的站点数据来源较多，站点种类不同，包含的观测数据有较大差异，且不同站点或同一站点内不同数据覆盖时间范围不同，因此，对本文中所用站点数据内容和时间进行统计，具体如表1所示。

# 1.2 模型运行设置及结果评价指标

模拟实验前，首先利用各站点大气强迫数据使模型在加速模式下运行，运行时长为1 a，运行次数设置为400次；然后转为正常模式继续运行，运行时长也为1 a，运行次数设置为200次，使模型达到平衡态[47]。平衡态时的变量值将作为模型模拟的初始值。

模型运行所用的物候参数、播种日期及种植时长，严格按照站点的物候记录设置(不再考虑2个模型物候期判别方式不同所造成的差异)，避免因模型估算的生长时间与作物实际生长时间不一致而在结果验证时造成较大误差。除物候参数外，其他参数均为模型默认值，暂不考虑灌溉和施肥过程。

DLM和CLM5作物相关算法的详细介绍及模型其他参数设定可详见模型技术手册，获取途径为：http://www.cesm.ucar.edu/models/。

在模拟结果的验证对比中，本文采用决定系数(R2 )和均方根误差(root mean square error，RMSE)来定量描述模拟值和观测值之间的差异，根据R2 和RMSE数值高低评估模型模拟精度。通常，R2 越接近1、RMSE越小，模拟结果相对于观测值的准确性越高。决定系数和均方根误差计算公式详见参考文献[48]。

# 2 结果与分析

# 2.1 LAI模拟结果及验证对比

由于仅禹城站、栾城站和商丘站有LAI观测数据(表1），因此只对3个站点在模型运行年份的LAI模拟结果进行验证分析。

总体上，DLM的夏玉米LAI模拟值高于CLM5的模拟结果(图1)。在禹城站，DLM的LAI模拟值基本高于或等于同时间的观测数据，仅2006年的LAI最高值低于观测记录值；CLM5则对LAI普遍低估。在商丘站，2014年2个模型的LAI模拟值均低于观测值。2015—2017年间，DLM的LAI最高值可达5 m2·m-2 以上，高于现有观测值。相比之下，CLM5的LAI模拟值虽低于DLM，但与LAI观测值更接近。

栾城站 2007—2010 年间，DLM 模拟的 LAI 与玉米生长前期的LAI观测值吻合度较好，但模拟最高值低于实测值。然而，栾城站2009年和2010年的模型模拟值较实测值严重偏低。特别是CLM5，模拟最高值仅为0.6 m2·m-2 左右，这可能与站点的气象驱动数据有关。对比栾城站2007—2010年夏玉米生长季(6—9月)的气温、辐射和相对湿度月平均数据(图2)可以发现，2009年和2010年的气温和注：DOY(day of the year)表示一年中的天数。

表1 站点数据内容及观测时间  
Tab.1 Type of data and observation time at agricultural stations   

<table><tr><td>农田站点</td><td>气象数据</td><td>通量数据</td><td>农田作物物候数据</td><td>农田作物LAI数据</td><td>农田作物产量数据</td></tr><tr><td>栾城站</td><td>2007—2010年</td><td>无</td><td>2007—2010年</td><td>2007—2010年</td><td>2007—2010年</td></tr><tr><td>商丘站</td><td>2014—2017年</td><td>无</td><td>2006—2017年</td><td>2006—2017年</td><td>2006—2017年</td></tr><tr><td>禹城站</td><td>2006—2010年</td><td>2006—2010年</td><td>2006—2010年</td><td>2006—2010年</td><td>2006—2010年</td></tr><tr><td>怀来站</td><td>2015年</td><td>2015年</td><td>无</td><td>无</td><td>无</td></tr><tr><td>馆陶站</td><td>2009年11月—2010年12月2009年11月—2010年12月</td><td></td><td>无</td><td>无</td><td>无</td></tr></table>

注：表中栾城站、商丘站和禹城站为农业生态站点；禹城站、怀来站和馆陶站为农田通量站点；表中数值为各数据时间覆盖范围。

![](images/d4b14a4c2e901d3dbb47cb0a4ff97f20f0669dd7cf1fa0100b4c23b3f11bacc3.jpg)  
图1 禹城站、栾城站和商丘站CLM5和DLM夏玉米LAI模拟结果对比 Fig.1 Comparison of simulated and observed summer maize LAI using the CLM5 and DLM at Yucheng, Luancheng and Shangqiu stations

短波辐射与其他年份相差不大，并且9月气温明显高于前两年，辐射在6月也更高。但2009年和2010年的相对湿度却总体偏低(图2c)，特别是在生长季前期、作物快速生长的6、7月。相对湿度影响着气孔的闭合，相对湿度过低会造成气孔变小或关闭，CO2无法通过气孔进入叶肉或进入叶肉的CO2量减少，光合作用减弱，作物生长变缓。由此可见，气象驱动数据的准确性直接影响到模拟结果的准确性。

DLM和CLM5的冬小麦叶面积指数模拟结果如图3所示。与夏玉米模拟结果不同的是，CLM5的LAI模拟值高于DLM。禹城站2006—2007年和2008—2009年期间，2个模型的LAI模拟值低于已有观测值，2007—2008年的模拟值则高于观测值。栾城站2008—2009年的冬小麦模型估算结果明显错误(同夏玉米，气象数据原因)，2007—2008年LAI估算较观测值偏低，2009—2010年的CLM5模型结果与验证数据最高值基本匹配。在商丘站，模型的LAI模拟值普遍低于LAI实测值，后者最高值在8m2 ·m-2 左右，而CLM5的最高值仅为约5 m2 ·m-2 。

导致DLM和CLM5模型LAI模拟值偏低可能有2个方面原因：一方面，本文的模拟试验并未考虑作物施肥和灌溉，可能会对作物LAI的模拟结果产生一定影响。氮素和水分在作物生长中起重要作用。在DLM和CLM5模型中，植物的碳同化过程受氮素限制。在植物氮素不足的情况下，光合作用中的最大羧化速率(Vcmax)将会减小，导致光合速率降低，碳同化量减少。而CLM5模型针对氮素不足的情况，还将消耗一部分同化碳量(如利用该部分碳量来促进根系生长等)，用于吸收环境中的可获取氮素，缓解植物的氮素胁迫。碳同化总量小的情况下，分配给叶片的碳量也会减少。叶面积指数为叶片碳量与作物冠层顶部比叶面积(specific leaf ar-ea, SLA)参数值的乘积。在SLA一定的情况下，叶片碳较小则会导致 LAI 较小。施肥能在一定程度上提高植物体内的氮素含量，减小氮素对Vcmax的限制，提高碳同化量，从而增大作物LAI。

![](images/b2f197a455b503754fa089cff204246027af61b725fc15065a3e25ce46603760.jpg)  
图 2 栾城站点2007—2010 年 6—9 月气温(a)、短波辐射(b)和相对湿度(c)月平均数据  
Fig.2 Monthly temperature (a), shortwave radiation (b) and relative humidity (c) from June to September during 2007-2010 at Luancheng Station

![](images/49aa164b4ffd5d15cb2cfcc5bf5e918c4c73c6fa18bf7adc823eb744aec24f24.jpg)  
图3 禹城站、栾城站和商丘站CLM5和DLM冬小麦LAI模拟结果对比  
Fig.3 Comparison of simulated and observed winter LAI using CLM5 and DLM at Yucheng, Luancheng and Shangqiu stations

当存在水分胁迫时，植物则会通过减小或关闭气孔的方式来降低水分流失。与此同时，由气孔进入叶片内部的CO2也会减少，使得光合作用中暗反应所需要的“原料”供应不足，碳同化总量减小，LAI也将随之变小。植物缺水时，灌溉能够有效缓解水分胁迫，利于叶面积指数的提高。综上，在后续研究中，应考虑施肥和灌溉的作用。

另一方面，模型当前的参数值通常是根据一些国外站点观测数据校正得到，或直接根据作物过程计算公式或文献数据确定，可能并不适用于本文研究的华北平原。如，在碳同化总量一定的情况下，LAI 高低还受碳分配系数的影响。在 DLM 和CLM5模型中，用于叶片生长的碳量由碳同化总量乘以叶分配系数得到。作物在展叶期到灌浆期之间是叶片生长最迅速(即LAI增长最快)的阶段，若在此阶段分配给叶片碳库的碳量不足，则易造成LAI模拟值偏低。因此，根据研究区实际情况对模型中的关键参数进行本地化和优化，可能对改善模型的模拟精度有重要作用。

尽管由于上述原因，造成了 DLM 和 CLM5 的LAI模拟值低于观测值，但2个模型的夏玉米和冬小麦模拟结果却相反，即DLM的夏玉米LAI模拟值更高，而 CLM5 的冬小麦 LAI 模拟值更高。首先，DLM和CLM5在植物氮素限制上有所区别。DLM在碳氮过程方面主要借鉴了CLM早期版本。陆面过程模型早期的地球生物化学循环主要是通过 Ball-Berry 气孔导度模型和 Faquhar 光合模型来模拟叶片与大气间的气体交换及植物生产力[49]。

该类模型通常被认为是一种“Carbon-only”模型，即氮限制表征不足，易夸大陆地的碳汇作用[50-51](即模拟的碳同化量偏高)。CLM早期版本及DLM即为该种“Carbon-only”模型，氮限制主要限于上文提到的对光合作用 Vcmax的影响。CLM5 模型还包含氮素不足时消耗植物碳以缓解氮素限制[52]，由此将降低最终的碳同化总量，理论上LAI模拟值会略低。

然而，在冬小麦LAI模拟中，DLM的模拟值却低于CLM5。这可能与2个模型在作物播种时设置的由种子向叶片转移的碳量(crop_seedc_to_leaf)有关。对于所有作物，DLM模型将该值统一设定为1gC·m-2 ·s-1 ，CLM5 则设定为 3 gC·m-2 ·s-1 。叶片初始碳量决定了初始 LAI 的高低。由于植物冠层尺度的碳同化总量由叶片净光合速率与LAI计算得到，由此初始LAI也决定了碳同化的基础值。夏玉米因生长季内温度和辐射高，自然降水较充足，光合作用旺盛，碳同化量大。因此叶片碳可以迅速积累，LAI增长比较明显。但在冬小麦生长初期，华北平原秋冬季节的光照和水热条件较弱，光合速率低而植物碳积累缓慢。这时种子转移到叶片的基础碳量就尤为重要。若无法在一个较高的基础碳量(或叶面积指数)上进行光合作用和碳积累，则易造成冬小麦的LAI模拟值偏低。因此在DLM模型中，应尝试修改冬小麦的crop_seedc_to_leaf设定值。

# 2.2 GPP模拟结果及验证分析

本文还对有GPP验证数据的禹城站点2006—2010年、怀来站2015年(仅包含夏玉米，无冬小麦)以及馆陶站2010年的结果进行了验证分析。

夏玉米模拟结果显示(图4)，禹城站2009年和2010 年期间，DLM 和 CLM5 在生长季初期和末期的GPP模拟值高于实测值；2006—2008年，模型模拟值与该时间段的观测值吻合度较高。在夏玉米生长季中期，2个模型的GPP模拟值均低于观测值，特别是2006年和2007年，最高观测值与同时间模拟值分别相差了 8.02×10-5 和 2.49×10-4 gC·m-2 ·s -1 。总体上，2个模型对GPP都存在着不同程度的低估，但DLM模拟的夏玉米GPP数值显著高于CLM5结果，与观测值线性拟合R2 也更优(表2)。然而DLM拟合结果的RMSE却显著高于CLM5。这可能是因为，虽然DLM的GPP模拟值与观测值的相关性较高，但可能极端值(极高值或极低值)也较多，由此造成了均方根误差偏大。

![](images/b92365613bb3287d4ad40f0025761520dd8e8babb1103790e4533bb1db4d950c.jpg)  
图4 禹城站、怀来站和馆陶站CLM5和DLM模型的夏玉米GPP模拟结果对比 Fig.4 Comparison of simulated and observed summer maize GPP using CLM5 and DLM at Yucheng, Luancheng, and Shangqiu stations

怀来站点DLM和CLM5的GPP模拟效果总体不佳，两者与观测值的线性拟合R2 仅分别为0.49和0.38，RMSE 分别为 2.58×10-7 和 7.51×10-8 gC·m-2 ·s-1 。在玉米生长前期，2个模型的GPP结果与验证数据较吻合；随着玉米的生长，CLM5模型的光合作用并未明显提升，使得GPP都维持在一个较低的水平。相比之下，DLM的GPP模拟值在生长季中期达到最大，与观测值较为接近。但在作物衰退期，光合速率仍较高，GPP估算量偏高。此外，近第200天和约 220 天时，2 个模型的 GPP 数值出现明显的波动。这可能与该时间段内气象数据缺失有关。虽然对气象缺失数据也进行了插补，但插补数据可能无法代表该站点当时真实的气象状况，由此造成了较大的模拟偏差。

馆陶站点DLM和CLM5的GPP模拟值变化趋势较为一致。DLM在夏玉米生长季中期的模拟值与观测值的吻合度较好，但前期偏低，后期偏高。CLM5的模拟值则在中期显著低于实测值，前期和后期模拟结果与观测值更为接近。由此，CLM5模拟结果与观测值的线性拟合R2 更高，为0.75；DLM的R2 为0.68，且均方根误差也更大(表2)。

然而，值得注意的是，在怀来站和馆陶站夏玉米生长季中，部分时间点的观测值异常偏低(图4)。这可能与NEE的通量观测数据缺失有关。NEE将直接影响GPP的数值高低。如馆陶站2010年第236 天，GPP 数值仅为 4.23×10-6 gC·m-2 ·s-1 ，在数量级方面与前后两天的验证值相差10倍。而在当天的NEE观测记录中，0:00\~16:00的数据均为缺失状态。虽然在数据处理过程中，EddyProcWeb工具对缺失数据进行了插值，但插补数据可能与实际情况仍存在一定偏差，导致了观测值的异常偏低。观测值的异常情况在一定程度上也拉低了模型模拟结果与实测值的拟合优度。因此，在今后研究中需加强对数据的筛选和质量的控制。

总的来说，DLM和CLM5模型对夏玉米生长前期的GPP变化捕捉较准确。DLM会随着夏玉米的发育逐步提升光合作用水平，使得生长季中期GPP与观测值比较接近，但DLM对作物衰退并不敏感，后期GPP模拟值偏高。相比之下，CLM5可以很好地模拟玉米衰退期的光合过程，但生长季中期并无明显提升，GPP低估严重。

冬小麦的模拟结果显示(图5)，2个模型的模拟结果差异较小。禹城站内，CLM5的GPP模拟值与观测值的线性拟合 R2 为 0.57，DLM 为 0.55，RMSE分 别 为 8.81 × 10- 7 和 7.48 × 10- 7 gC · m- 2 · s - 1 。 由 于DLM在2006—2007年的拟合曲线严重偏低，拉低了整体的拟合效果。若剔除2006—2007年的结果，DLM的GPP模拟效果则优于CLM5，R2 可以达到0.62(未在图表中显示)。馆陶站内，CLM5 和 DLM模拟结果的R2 则分别为0.57和0.56，RMSE分别为4.85×10-8 和5.32×10-8 gC·m-2 ·s-1 ，以CLM5略优。

表2 DLM和CLM5的夏玉米和冬小麦GPP和LE模拟值与实测值的线性拟合统计结果  
Tab.2 Statistical results of a linear fitting between simulated and observed summer maize and winter wheat GPP and LE using DLM and CLM5   

<table><tr><td rowspan="2">变量</td><td rowspan="2">站点</td><td rowspan="2">指标</td><td colspan="2">夏玉米</td><td colspan="2">冬小麦</td></tr><tr><td>DLM</td><td>CLM5</td><td>DLM</td><td>CLM5</td></tr><tr><td>GPP</td><td>禹城站</td><td>RMSE/(gC·m2·s-1)</td><td>1.10E-07</td><td>2.82E-08</td><td>8.81E-07</td><td>7.48E-07</td></tr><tr><td></td><td></td><td>R</td><td>0.61</td><td>0.52</td><td>0.55</td><td>0.57</td></tr><tr><td></td><td>怀来站</td><td>RMSE/(gC·m2·s1)</td><td>2.58E-07</td><td>7.51E-08</td><td></td><td></td></tr><tr><td></td><td></td><td>R²</td><td>0.49</td><td>0.38</td><td></td><td></td></tr><tr><td></td><td>馆陶站</td><td>RMSE/(gC·m²·s-1)</td><td>1.10E-07</td><td>2.82E-08</td><td>4.85E-08</td><td>5.32E-08</td></tr><tr><td></td><td></td><td>R²</td><td>0.68</td><td>0.75</td><td>0.56</td><td>0.57</td></tr><tr><td>LE</td><td>禹城站</td><td>RMSE/(W·m2)</td><td>522693</td><td>260048</td><td>522693</td><td>260048</td></tr><tr><td></td><td></td><td>R²</td><td>0.54</td><td>0.51</td><td>0.59</td><td>0.56</td></tr><tr><td></td><td>怀来站</td><td>RMSE/(W·m2)</td><td>97331</td><td>35700</td><td></td><td></td></tr><tr><td></td><td></td><td>R²</td><td>0.57</td><td>0.55</td><td></td><td></td></tr><tr><td></td><td>馆陶站</td><td>RMSE/(W·m)</td><td>54166</td><td>18509</td><td>115665</td><td>72452</td></tr><tr><td></td><td></td><td>R</td><td>0.80</td><td>0.78</td><td>0.54</td><td>0.47</td></tr></table>

![](images/e16fe311946d771d50077d6acf706c3be979a0f3349a7268cc2acd6953e69acc.jpg)  
图5 禹城站和馆陶站CLM5和DLM模型的冬小麦GPP模拟结果对比  
Fig.5 Comparison of simulated and observed winter wheat GPP using CLM5 and DLM at Yucheng and Guantao stations

图5还显示，在冬小麦生长季内，GPP有2个比较明显的波峰，这一特征与其越冬过程有关。冬小麦播种后，随着叶片的萌发，GPP逐渐增长；进入越冬期后，冬小麦生长变缓，GPP增长率趋近于0；越冬期后，小麦又进入了快速发育阶段，GPP增加迅速；后随着作物的灌浆成熟，GPP逐渐下降。总体上，DLM和CLM5对冬小麦越冬前的GPP模拟效果普遍较好；但经历越冬期后，2个模型对GPP的拟合能力稍显不足，发育中期存在低估的现象；进入衰退期后，模型结果又与观测值匹配较好。

进一步由验证数据可知，禹城站2006—2007年的冬小麦GPP最高值最大，其次为2008—2009、2007—2008、2009—2010 年。GPP 最高值次序与小麦越冬期前的初级生产力高低密切相关。通常越冬期前GPP较高的年份，冬小麦在越冬期后的生产力表现更高，GPP最高值更大。这主要是因为越冬前光合作用强使得碳同化量多，进而用于分配的碳量高，LAT也就更大，利于后期冬小麦的发育。

# 2.3 潜热通量模拟结果及验证分析

该部分同样仅对有潜热验证数据的禹城站2006—2010年、怀来站2015年(仅包含夏玉米，无冬小麦)以及馆陶站 2010 年的模型结果进行验证分析。

夏玉米模拟结果表明(图 6)，DLM 与 CLM5 的LE模拟精度比较接近，线性拟合R2 均可达到0.5以上，整体上模拟效果较好。在禹城站，DLM的LE模拟值总体上高于CLM5，但易在生长季前期出现不合理的高估。相比之下，CLM5更能捕捉到现实中LE较低时的情况，但对高值的模拟能力略显不足。DLM和CLM5的LE模拟与观测值线性拟合R2分 别 为 0.54 和 0.51，但 RMSE 分 别 为 522692 和260048 W·m-2 ，DLM均方根误差明显偏高。

怀来站DLM和CLM5的LE模拟值与观测值的变化趋势较为一致，线性拟合R2 分别为0.57和0.55，DLM 模拟结果的 RMSE 同样较高，为 97331W·m-2。在上述的近第200天和220天左右，由于气象数据问题，2个模型的结果均无法与观测数据对应。

馆陶站的LE模拟效果在3个站点中最好，DLM和CLM5模拟结果与观测值的线性拟合R2 可分别达 0.80 和 0.78；RMSE 分别为 54166 和 18508W·m-2。在夏玉米生长初期和末期，CLM5与观测值变化趋势较为吻合，但作物生长中期，CLM5的潜热低估现象非常明显，此时 DLM 能更好地捕捉作物迅速生长阶段的潜热变化。

冬小麦的潜热模拟结果如图7所示。除馆陶站CLM5结果外，其余模拟结果与观测值的线性拟合

![](images/c50ad522b502deeb2ca7403895734d8b6972e457d659feda3d25bc51b5d2976f.jpg)  
图6 禹城站、怀来站和馆陶站CLM5和DLM模型的夏玉米潜热通量模拟结果对比

![](images/df25d99f65e003856df5bfcfa30a7a152e13a94ab07b252ea7cb1afe2ecd9b96.jpg)  
ig.6 Comparison of simulated and observed summer maize LE using CLM5 and DLM at Yucheng, Huailai and Guantao statio   
图7 禹城站和馆陶站CLM5和DLM模型的冬小麦潜热通量模拟结果对比  
Fig.7 Comparison of simulated and observed winter wheat LE using CLM5 and DLM at Yucheng and Guantao stations

R2 均在0.5以上。就相关性而言，DLM的模拟效果优于CLM5。其中，禹城站的DLM模拟值与观测值的线性拟合R2 为0.59，CLM5为0.56；馆陶站2个模型的R2 分别为0.54和0.47。然而，DLM模型结果的

RMSE也普遍更高(表2)。

与冬小麦GPP的模拟结果类似，2个模型对越冬期前的潜热估算效果优于越冬期后。在冬小麦发育中期，模型对潜热的低估比较明显。而CLM5的LE模拟结果易在作物生长中后期较早衰退(如禹城站 2006—2007 年、2009—2010 年和馆陶站)，造成较大的模拟偏差。

综合GPP和LE的模拟结果，可以发现当前模型结果普遍低于实际情况。事实上，DLM和CLM5模型的GPP和LE模拟效果与LAI的模拟结果有一定联系。一般来说，LAI是一个核心变量，会直接影响到碳吸收、光能利用、热量传输和水分耗散等一系列碳循环、能量及水量平衡过程。因此，LAI模拟值的可靠性将影响到一系列其他过程模拟结果的可靠性。由于本文中LAI模拟值偏低，可能也导致了GPP和LE模拟值偏低。并且2个模型对2种作物的GPP和LE模拟差异规律(即DLM的夏玉米生长模拟更优，CLM5 反之)也与 LAI 结果基本一致，除冬小麦潜热外。

DLM和CLM5在潜热模拟方面的差异主要是因为 DLM 采用 Penman-Monteith 方程和双叶模型分别计算阳叶和阴叶的蒸腾潜在热通量，同时用地表阻抗取代Penman-Monteith中的叶片气孔阻抗来估算地表潜热通量。CLM则采用基于水势梯度的质量守恒算法和大叶模型计算潜在热通量。Gao等[53]通过研究发现，农田土壤蒸发和作物蒸腾与植物捕获的净辐射有密切关系。在实际蒸散发过程中，太阳辐射提供了植被/土壤水分由液态转换为气态的能量[54]。但CLM质量守恒算法中缺乏太阳辐射相关变量，由此易造成蒸散发估算误差，进而最终影响潜热模拟的准确性。另一方面，DLM采用的双叶模型能够充分考虑冠层阳叶和阴叶在接触和获取环境因子上的差异性(如阳叶捕获的光合有效辐射更多，或表面温度更高)[55]，相比大叶模型，可更为准确地估算冠层碳通量和热通量[32,56]。因此本文中的DLM潜热估算效果更优。Chen等[28]也通过研究证实，相比于CLM，DLM方案对多种下垫面类型的净辐射和热通量的模拟精度可提高约 10%。在后续发展中，CLM5模型可以考虑吸收DLM模型优秀的热通量计算方案。

综上，为改善作物模型对GPP和LE的模拟效果，首先可以尝试利用参数优化和考虑施肥灌溉的方式改善模型的LAI模拟结果；其次，可以互相吸收模型中更好的参数化方案和算法。

# 2.4 产量模拟结果及验证分析

由于DLM模型无作物产量的计算过程，因此本小节仅利用CLM5模型进行产量的模拟和验证。模拟结果显示(图8)，总体上，CLM5模型的产量模拟效果并不理想，模拟值与实际产量间存在不同程度的偏差。如禹城站2006年夏玉米的产量估算值严重低于实际产量，前者为2491 kg·hm-2 ，后者为5836kg·hm-2，模拟值仅约为验证值的1/2。栾城站2008年的夏玉米产量模拟值与实际产量较为接近。估算产量为 8412 kg·hm-2 ，验证值为 9215 kg·hm-2 ，两者相差 803 kg·hm-2 。商丘站 2014—2017 年间的夏玉米产量模拟值均低于实测值，其中2014年模拟结果与实测值差距最大，为5619 kg·hm-2 ，2017年模拟结果与实测值差距最小，为1398 kg·hm-2 。

冬小麦的产量模拟结果显示，多数情况下CLM5 模型的产量估算值低于实际产量(禹城站2009年除外)。其中，商丘站2016年的冬小麦模拟产量严重低于实测值，前者为2063 kg·hm-2，后者则为 9787 kg·hm-2 ，模拟值仅约为验证值的 21%。禹城站2007年和2008年的模拟结果与实际产量的偏差则相对较小，差值分别为1351和967 kg·hm-2 。其余产量估算结果与实测值之间的偏差介于1500\~5000 kg·hm-2 之间。

CLM5模型产量估测效果较差可能存在两方面原因。一方面，并未考虑施肥和灌溉的作用。在不添加施肥和灌溉的条件下，可能部分研究站点的土壤氮素含量和自然降水量无法满足作物的氮素和水分需求。正如2.1节所述，会产生一定的氮素和水分胁迫，导致作物光合速率低，碳同化量小，有机物积累少，模型的产量估算值往往低于实测产量。

另一方面，在碳同化总量一定的前提下，果实碳库的分配系数将直接影响最终产量。CLM5模型中的产量计算方法为：果实碳库总量乘以收获系数0.85，再经单位转换得到最终产量。若果实碳库的分配量占碳同化总量的比例过低，产量估测值则低。在CLM5作物模型中，果实碳库的分配发生在作物灌浆期后。果实分配系数受叶片和茎分配系数的影响(三者的总和为1)。因此，可以通过参数优化的方法来合理调整不同器官间碳分配比例的参数值，以达到提高果实分配碳量的目的。

此外，由于产量的积累发生在灌浆期至收获之间。收获日期固定的前提下，灌浆期开始时间将影响着果实碳的积累时长和总量。一般来说，在CLM5作物模型中，触发灌浆期的方法有2种：一是播种后的积温达到模型设定的灌浆期积温；二是LAI 模拟值达到模型设定的最大 LAI 参数值。CLM5模型关于玉米和小麦设定的最大LAI值分别为5 m2 m-2 和7 m2 m-2 。事实上，LAI的实测值显示(图1和图3)，夏玉米和冬小麦的最大LAI可分别达到约 7 m2 ·m-2 和 9 m2 ·m-2 。模型设定的最大 LAI 参数值较小，易使灌浆期开始时间较早。虽然灌浆期时间长利于产量的提高，但由此也会造成叶片发育时间较短(LAI在展叶期至灌浆期内增长最快，进入灌浆期后则逐渐下降)，LAI模拟值偏低。因此，需要调整最大LAI参数的数值，确保叶片生长和产量积累时间的合理分配。

![](images/1e78bf979bd4eaf22b9a7f03d7b362da38a9a1db3e29fccb09eb46b387b9e0ea.jpg)  
图8 禹城站、栾城站和商丘站夏玉米和冬小麦CLM5模拟产量与实际产量对比 Fig.8 Comparison between yields simulated by CLM5 and observations for summer maize at Yucheng, Luancheng and Shangqiu stations

总的来说，当前CLM5模型的产量估算方法仍较简略。事实上，一些专业的农学作物模型在进行产量估测时，会综合考虑包括种植密度、作物品种质量、病虫害、自然灾害(如大风、暴雨)等与产量相关的管理措施或胁迫因素[57-59]，以实现较为精准的预测。农学作物模型通常应用于田间尺度，该尺度下的农田及作物管理数据相对较为充分和详尽，有利于模型的不断完善和发展，使产量预测更加准确。陆面过程模型(包括CLM5模型)的应用尺度更多样(站点、区域或全球)，但其农业模块发展尚处于起步阶段：受农业相关格网数据匮乏的影响，缺乏对作物种植密度、病虫害、突发自然灾害等农业数据的表述。未来，随着农业数据的丰富，陆面过程模型中的产量估算过程将会进一步发展和完善。

# 3 结论

本文应用 2 大优秀陆面过程模型 DLM 和CLM5，开展了华北平原农田站点内夏玉米和冬小麦的生长模拟。通过对叶面积指数、总初级生产力、潜热通量和作物产量进行验证对比，评估了2个模型的模拟效果，探究其模拟差异的原因。主要结论如下：

(1) DLM和CLM5两个模型的LAI模拟值普遍低于实测值。这可能与本文中未考虑施肥灌溉及未进行参数本地化(优化)有关，后续应加强这两方面工作。从作物种类来看，DLM的夏玉米LAI模拟值更高，更接近观测值；CLM5 的冬小麦模拟值更高。这可能主要与2个模型对氮限制的表征和叶片基础碳量的设置不同有关。在冬小麦模拟中，DLM模型应提高作物的基础碳量。

(2) 2 个模型的 GPP 模拟结果差异与 LAI 结果相似，即多数情况下模型模拟值低于实测值。其中，以DLM的夏玉米模拟值更高，与观测值的相关性更好；CLM5的冬小麦模拟值略高，与观测值的相关性略高。然而，DLM 模型结果的均方根误差总体更大，模拟精度并不高。造成2个模型GPP模拟偏差的原因可能与LAI相同。除此之外，也应该在DLM模型中完善氮素限制的表征，避免因氮限制不足而出现 GPP 模拟值异常偏高，导致 RMSE偏大。

(3) DLM模型的潜热模拟值与观测值之间的相关性普遍高于CLM5模型结果，展现了DLM更为优越的潜热模拟能力。CLM5模型可以借鉴DLM双叶策略和 Penman-Monteith 算法的优势，改善模型的热通量模拟能力。

(4) CLM5模型的产量估算效果总体较差。产量的高低与灌浆期内的作物碳同化总量、果实碳库分配量及果实碳积累时长等密切相关。因此，可通过添加农田管理措施、模型参数优化等方法，提高灌浆期内碳同化模拟结果的准确性；再调整模型中关于果实库碳积累速率与时长的设定，以提高模型的产量预测能力。

# 参考文献(References)

[1] Food and Agricultural Organization (FAO). FAOSTAT database [DB/OL]. 2020-09-14 [2021-11-05]. http: //www. fao.org/faostat/en/#data/.   
[2] Hurtt G C, Frolking S, Fearon M G, et al. The underpinnings of land- use history: Three centuries of global gridded land-use transitions, wood-harvest activity, and resulting secondary lands [J]. Global Change Biology, 2006, 12 (7): 1208-1229.   
[3] Drewniak B, Song J, Prell J, et al. Modeling agriculture in the community land model [J]. Geoscientific Model Development, 2013, 6(2): 495-515.   
[4] 赵俊芳, 郭建平, 张艳红, 等. 气候变化对农业影响研究 综 述 [J]. 中 国 农 业 气 象, 2010, 31(2): 200- 205. [Zhao Junfang, Guo Jianping, Zhang Yanhong, et al. Advances in research of impacts of climate change on agriculture. Chinese Journal of Agrometeorology, 2010, 31(2): 200- 205. ]   
[5] Lobell D B, Schlenker W, Costa-Roberts J. Climate trends and global crop production since 1980 [J]. Science, 2011, 333: 616-620.   
[6] Zhu X, Troy T J. Agriculturally relevant climate extremes and their trends in the world's major growing regions [J]. Earth's Future, 2018, 6(4): 656-672.   
[7] Li Z G, Tang H J, Yang P, et al. Spatio-temporal responses of cropland phenophases to climate change in Northeast China [J]. Journal of Geographical Sciences, 2012, 22(1): 29-45.   
[8] 张学珍, 李侠祥, 张丽娟, 等. RCP 8.5 气候变化情景下 21 世纪印度粮食单产变化的多模式集合模拟 [J]. 地理学 报, 2019, 74(11): 2314- 2328. [Zhang Xuezhen, Li Xiaxiang, Zhang Lijuan, et al. Multi-model ensemble projection of crop yield of India under RCP8.5 climate change scenario during the 21st century. Acta Geographica Sinica, 2019, 74(11): 2314-2328. ]   
[9] Battisti D S, Naylor R L. Historical warnings of future food insecurity with unprecedented seasonal heat [J]. Science, 2009, 323: 240-244.   
[10] Hlavinka P, Trnka M, Semerádová D, et al. Effect of drought on yield variability of key crops in Czech Republic [J]. Agricultural and Forest Meteorology, 2009, 149(3/ 4): 431-442.   
[11] Deryng D, Conway D, Ramankutty N, et al. Global crop yield response to extreme heat stress under multiple climate change futures [J]. Environmental Research Letters, 2014, 9(3): 034011. doi: 10.1088/1748-9326/9/3/034011.   
[12] Hodges T, Botner D, Sakamoto C, et al. Using the CE-RES- Maize model to estimate production for the US Cornbelt [J]. Agricultural and Forest Meteorology, 1987, 40(4): 293-303.   
[13] Xue Y K, Fennessy M J, Sellers P J. Impact of vegetation properties on US summer weather prediction [J]. Journal of Geophysical Research: Atmospheres, 1996, 101(D3): 7419-7430.   
[14] Pitman A J, de Noblet-Ducoudré N, Cruz F T, et al. Uncertainties in climate responses to past land cover change: First results from the LUCID intercomparison study [J]. Geophysical Research Letters, 2009, 36(14): L14814. doi: 10.1029/2009GL039076.   
[15] Bondeau A, Smith P, Zaehle S, et al. Modelling the role of agriculture for the 20th century global terrestrial carbon balance [J]. Global Change Biology, 2007, 13(3): 679-706.   
[16] Osborne T M, Lawrence D M, Challinor A J, et al. Development and assessment of a coupled crop-climate model [J]. Global Change Biology, 2007, 13(1): 169-183.   
[17] Stehfest E, Heistermann M, Priess J A, et al. Simulation of global crop production with the ecosystem model Day-Cent [J]. Ecological Modelling, 2007, 209: 203-219.   
[18] Osborne T, Gornall J, Hooker J, et al. JULES- crop: A parametrisation of crops in the Joint UK Land Environment Simulator [J]. Geoscientific Model Development, 2015, 8(4): 1139-1155.   
[19] McDermid S S, Mearns L O, Ruane A C. Representing agriculture in earth system models: Approaches and priorities for development [J]. Journal of Advances in Modeling Earth Systems, 2017, 9(5): 2230-2265.   
[20] Levis S, Bonan G B, Kluzek E, et al. Interactive crop management in the community earth system model (CESM1): Seasonal influences on land-atmosphere fluxes [J]. Journal of Climate, 2012, 25(14): 4839-4859.   
[21] Lawrence D M, Fisher R A, Koven C D, et al. The community land model version 5: Description of new features, benchmarking, and impact of forcing uncertainty [J]. Journal of Advances in Modeling Earth Systems, 2019, 11(12): 4245-4287.   
[22] Badger A M, Dirmeyer P A. Climate response to Amazon forest replacement by heterogeneous crop cover [J]. Hydrology and Earth System Sciences, 2015, 19(11): 4547- 4557.   
[23] Levis S, Badger A, Drewniak B, et al. CLMcrop yields and water requirements: Avoided impacts by choosing RCP 4.5 over 8.5 [J]. Climatic Change, 2018, 146(3): 501-515.   
[24] Sitch S, Smith B, Prentice I C, et al. Evaluation of ecosystem dynamics, plant geography and terrestrial carbon cycling in the LPJ dynamic global vegetation model [J]. Global Change Biology, 2003, 9(2): 161-185.   
[25] Smith P C, De Noblet-Ducoudré N, Ciais P, et al. European-wide simulations of croplands using an improved terrestrial biosphere model: Phenology and productivity [J]. Journal of Geophysical Research: Biogeosciences, 2010, 115(G1): G01014. doi: 10.1029/2008JG000800.   
[26] Chen B Z, Chen J M, Mo G, et al. Modeling and scaling coupled energy, water, and carbon fluxes based on remote sensing: An application to Canada's landmass [J]. Journal of Hydrometeorology, 2007, 8(2): 123-143.   
[27] Chen B Z, Chen J M, Ju W M, et al. Remote sensingbased ecosystem-atmosphere simulation scheme (EASS): Model formulation and test with multiple- year data [J]. Ecological Modelling, 2007, 209: 277-300.   
[28] Chen J, Chen B Z, Black T A, et al. Comparison of terrestrial evapotranspiration estimates using the mass transfer and Penman ‐ Monteith equations in land surface models [J]. Journal of Geophysical Research: Biogeosciences, 2013, 118(4): 1715-1731.   
[29] Chen J, Zhang H F, Liu Z R, et al. Evaluating parameter adjustment in the MODIS gross primary production algorithm based on eddy covariance tower measurements [J]. Remote Sensing, 2014, 6(4): 3321-3348.   
[30] Monteith J L. Environmental physics [J]. Physics Education, 1976, 11(3): 147. doi: 10.1088/0031-9120/11/3/004.   
[31] Wang Y P, Leuning R. A two-leaf model for canopy conductance, photosynthesis and partitioning of available energy I: Model description and comparison with a multilayered model [J]. Agricultural and Forest Meteorology, 1998, 91(1/2): 89-111.   
[32] Chen J M, Liu J, Cihlar J, et al. Daily canopy photosynthesis model through temporal and spatial scaling for remote sensing applications [J]. Ecological Modelling, 1999, 124(2/3): 99-119.   
[33] Singh V P, Xu C Y. Evaluation and generalization of 13 mass‐transfer equations for determining free water evaporation [J]. Hydrological Processes, 1997, 11(3): 311-323.   
[34] De Pury D G G, Farquhar G D. Simple scaling of photosynthesis from leaves to canopies without the errors of big‐leaf models [J]. Plant, Cell & Environment, 1997, 20 (5): 537-557.   
[35] Jolly W M, Nemani R, Running S W. A generalized, bioclimatic index to predict foliar phenology in response to climate [J]. Global Change Biology, 2005, 11(4): 619- 632.   
[36] Lawrence D M, Oleson K W, Flanner M G, et al. Parameterization improvements and functional and structural advances in version 4 of the community land model [J]. Journal of Advances in Modeling Earth Systems, 2011, 3 (1). doi: 10.1029/2011MS00045.   
[37] 车明亮. 集成陆面过程模式物候模型的发展及其应用 研究 [D]. 北京: 中国科学院大学, 2015. [Che Mingliang. Development and application of phenology module in an integrated dynamic land surface model. Beijing, China: University of Chinese Academy of Sciences, 2015. ]   
[38] 许丽丽, 李宝林, 袁烨城, 等. 2000—2010 年中国耕地变 化与耕地占补平衡政策效果分析 [J]. 资源科学, 2015, 37(8): 1543-1551. [Xu Lili, Li Baolin, Yuan Yecheng, et al. Changes in China's cultivated land and the evaluation of land requisition- compensation balance policy from 2000 to 2010. Resources Science, 2015, 37(8): 1543- 1551. ]   
[39] Ren X L, Weitzel M, O'Neill B C, et al. Avoided economic impacts of climate change on agriculture: Integrating a land surface model (CLM) with a global economic model (iPETS) [J]. Climatic Change, 2018, 146(3): 517-531.   
[40] Chen M, Griffis T J, Baker J M, et al. Comparing crop growth and carbon budgets simulated across AmeriFlux agricultural sites using the Community Land Model (CLM) [J]. Agricultural and Forest Meteorology, 2018, 256/257: 315-333.   
[41] Franke J A, Müller C, Elliott J, et al. The GGCMI Phase 2 experiment: Global gridded crop model simulations under uniform changes in CO2, temperature, water, and nitrogen levels (protocol version 1.0) [J]. Geoscientific Model Development, 2020, 13(5): 2315-2336.   
[42] 国家生态系统观测研究网络/中国生态系统研究网络. 国家生态系统观测研究网络科技资源服务系统 [DB/ OL]. 2015 [2019- 07- 16]. http://www.cnern.org.cn. [National Ecosystem Research Network of China/Chinese Ecosystem Research Network. 2015 [2019-07-16]. http:// www.cnern.org.cn. ]   
[43] 杨光超, 朱忠礼, 谭磊, 等. 怀来地区蒸渗仪测定玉米田 蒸 散 发 分 析 [J]. 高 原 气 象, 2015, 34(4): 1095- 1106. [Yang Guangchao, Zhu Zhongli, Tan Lei, et al. Analysis on evapotranspiration of maize field measured by Lysimeters in Huailai. Plateau Meteorology, 2015, 34(4): 1095- 1106. ]   
[44] 刘绍民, 徐自为, 肖青. 海河流域多尺度地表通量与气 象要素观测数据集: 怀来站—自动气象站(40 m 塔): 2016 [DS]. 国家青藏高原科学数据中心, 2019. [Liu Shaomin, Xu Ziwei, Xiao Qing. Multi-scale surface flux and meteorological elements observation dataset in the Hai River Basin (Huailai station- automatic weather station- 40 m tower, 2016). National Tibetan Plateau Data Center, 2019. ]   
[45] Jia Z Z, Liu S M, Xu Z W, et al. Validation of remotely sensed evapotranspiration over the Hai River Basin, China [J]. Journal of Geophysical Research: Atmospheres, 2012, 117(D13). doi: 10.1029/2011JD017037.   
[46] 刘绍民, 徐自为. 海河流域多尺度地表通量与气象要素 观测数据集: 馆陶站—自动气象站(2008—2010) [DS]. 国家青藏高原科学数据中心, 2016. [Liu Shaoming, Xu Ziwei. Multi- scale surface flux and meteorological elements observation dataset in the Haihe River Basin (Guantao site- automatic weather station) (2008- 2010). National Tibetan Plateau Data Center, 2016. ]   
[47] Wieder W R, Lawrence D M, Fisher R A, et al. Beyond static benchmarking: Using experimental manipulations to evaluate land model assumptions [J]. Global Biogeochemical Cycles, 2019, 33(10): 1289-1309.   
[48] Willmott C J, Ackleson S G, Davis R E, et al. Statistics for the evaluation and comparison of models [J]. Journal of Geophysical Research: Oceans, 1985, 90: 8995-9005.   
[49] Bonan G B. Ecological climatology: Concepts and applications [M]. 3rd Edition. New York, USA: Cambridge University Press, 2016.   
[50] Hungate B A, Dukes J S, Shaw M R, et al. Nitrogen and climate change [J]. Science, 2003, 302: 1512-1523.   
[51] Shi M J, Fisher J B, Brzostek E R, et al. Carbon cost of plant nitrogen acquisition: Global carbon cycle impact from an improved plant nitrogen cycle in the Community Land Model [J]. Global Change Biology, 2016, 22(3): 1299-1314.   
[52] Zaehle S, Jones C D, Houlton B, et al. Nitrogen availability reduces CMIP5 projections of twenty- first- century land carbon uptake [J]. Journal of Climate, 2015, 28(6): 2494-2511.   
[53] Gao Y, Duan A W, Qiu X Q, et al. Modeling evapotranspiration in maize/soybean strip intercropping system with the evaporation and radiation interception by neighboring species model [J]. Agricultural Water Management, 2013, 128: 110-119.   
[54] Allan R, Pereira L, Smith M. Crop evapotranspiration-Guidelines for computing crop water requirements [R]. FAO Irrigation and Drainage Paper No. 56. Rome, Italy, 1998.   
[55] 申双和, 张雪松, 欧阳竹. 双叶模型在冬小麦田冠层CO2 通 量 多 层 模 拟 中 的 应 用 [J]. 气 象 学 报, 2011, 69(5): 819-829. [Shen Shuanghe, Zhang Xuesong, Ouyang Zhu. An application of the two-leaf model in multilayer simulation for winter wheat canopy CO2 fluxes. Acta Meteorologica Sinica, 2011, 69(5): 819-829. ]   
[56] Leuning R, Dunin F X, Wang Y P. A two-leaf model for canopy conductance, photosynthesis and partitioning of available energy. II. Comparison with measurements [J]. Agricultural and Forest Meteorology, 1998, 91: 113-125.   
[57] 谢云, Kiniry J R. 国外作物生长模型发展综述 [J]. 作物 学报, 2002, 28(2): 190-195. [Xie Yun, James R Kiniry. A review on the development of crop modeling and its application. Acta Agronomica Sinica, 2002, 28(2): 190- 195. ]   
[58] 林忠辉, 莫兴国, 项月琴. 作物生长模型研究综述 [J]. 作 物 学 报, 2003, 29(5): 750- 758. [Lin Zhonghui, Mo Xingguo, Xiang Yueqin. Research advances on crop growth models. Acta Agronomica Sinica, 2003, 29(5): 750-758. ]

[59] 张建平, 赵艳霞, 王春乙, 等. 气候变化情景下东北地区玉米产量变化模拟 [J]. 中国生态农业学报, 2008, 16(6): 1448- 1452. [Zhang Jianping, Zhao Yanxia, Wang

Chunyi, et al. Simulation of maize production under climate change scenario in northeast China. Chinese Journal of Eco-Agriculture, 2008, 16(6): 1448-1452. ]

# Comparative study of DLM and CLM5 model simulations at winter wheat-summer maize rotation stations in the North China Plain

WANG Fei1 , CHEN Baozhang1,3\* , CHEN Jing2 , ZHANG Huifang1 , GUO Lifeng1 (1. State Key Laboratory of Resources and Environment Information System, Institute of Geographic Sciences and Natural Resources Research, CAS, Beijing 100101, China; 2. Beijing Meteorological Service, Beijing 100089, China; 3. Collaborative Innovation Center of Geographical Information Resources Development and Utilization in Jiangsu Province, Nanjing 210023, China)

Abstract: The interaction between crop growth and climate is one of the key issues in climate change studies. As an important research tool, land surface models can be used for distinct simulations with different model frameworks, algorithms, or parameterization schemes. In order to investigate the differences of the Dynamic Land Model (DLM) and Community Land Model (CLM5) in estimating crop growth and farmland heat flux and the causes of the differences, model comparisons were conducted at the agricultural stations with summer maize and winter wheat rotation in the North China Plain (NCP). The results show that the estimated leaf area index and gross primary production of DLM for summer maize were better, while for winter wheat, the opposite results were obtained. Nonetheless, DLM performed better in simulating latent heat flux, which may reflect that the Penman formula and two- leaf strategy in DLM is better than the mass conservation algorithm based on water potential gradient and big- leaf strategy in CLM5. However, the capacity of yield prediction was poor. In conclusion, with the default settings, the simulations of the two models can basically reflect the growth characteristics of summer maize and winter wheat in the study area, but there remains certain deviation from the observations. The applicability of the models for the NCP may need to be further improved through the addition of farmland management measures, algorithm optimization, and parameter localization.

Keywords: summer maize and winter wheat rotation; DLM model; CLM5 model; growth simulation; model comparison and evaluation; North China Plain