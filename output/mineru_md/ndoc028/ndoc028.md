# 环长株潭城市群生态系统服务供需变化分析

孙颖¹，杨君1\*，袁淑君²，唐兴隆¹，刘畅¹，王义博¹，孟媛媛¹(1.湖南农业大学 资源学院，湖南 长沙 410128;2.湖南工程职业技术学院，湖南 长沙 410151)

摘要;探析生态系统服务供需关系，有助于推动区域自然资源的有序开发和生态环境管理。基于多源数据，选取碳固持、粮食供应、产水和土壤保持4项生态系统服务，运用InVEST模型、ESDR、局部自相关指数等方法，对比分析2000、2010年和2020年环长株潭城市群生态系统服务供需时空变化及空间匹配特征。结果表明：1)各项生态系统服务总供给>总需求，碳固持供给量下降,粮食供应、产水和土壤保持供给量上升,4项生态系统服务需求量上升。2)碳固持供需比下降，产水供需比上升，粮食供应和土壤保持供需比基本保持不变。城镇建成区的碳固持、粮食供应和产水呈赤字状态，其他区域呈盈余状态;土壤保持赤字区集中在洞庭湖平原。3)除土壤保持以低低空间匹配为主,碳固持、粮食供应、产水服务的空间错位现象突出，高低空间错位主要分布在生态基底较好的山地丘陵区,低高空间错位主要分布在各城区。结合生态系统服务供需和自相关分析结果，提出资源开发与保护建议，全面提升研究区各项生态容量，保护生态环境。

关键词：土地生态与环境；空间匹配;InVEST模型;环长株潭城市群中图分类号：X171.1 文献标志码：A 文章编号：1001-7461(2024)05-0202-08

Changes in the Supply and Demand of Ecosystem Services in the Urban Agglomeration Around Changsha-Zhuzhou-Xiangtan

SUN Ying',YANG Jun1\* ,YUAN Shujun2,TANG Xinglong',LIU Chang' , WANG Yibo’ ,MENG Yuanyuan (1.College of Resources,Hu'nan Agricultural University,Changsha 41ol28,Hunan,China ; 2.Hu'nan Vocatioanal Collegeof Engineering,Changsha 4lol51,Hunan,China)

Abstract:The exploration of the relationship between the supply and demand of ecosystem services (ESs) will help to promote the orderly development of regional natural resources and the management of the ecological environment.Based on multi-source data,this paper selected four ecosystem services,including carbon storage,food supply,water supply and soil conservation,and used the InVEST model,ESDR,and the local indicators of spatial association to comparatively analyze the spatial and temporal changes in the sup-ply and demand of ESs and the spatial matching status of ESs in the Urban Agglomeration Around Changsha-Zhuzhou-Xiangtan in the years of 200o,20l0 and 2020.The results showed that 1） the total supply of all ESs exceeded the total demand.The supply of carbon storage decreased,the supply of food,water and soil conservation increased,and the demand of the four ecosystem services maintained an overall increase. 2）The supply and demand ratio of carbon storage decreased,the supply and demand ratio of water supply increased,and the supply and demand ratio of food supply and soil conservation remained basically unchanged.Carbon storage,food supply and water supply were in deficit in built-up areas of towns and cities and in surplus in other areas.The deficit area of the soil conservation service was concentrated in the Dongting Lake Plain. 3） In addition to soil conservation,which was dominated by low-low spatial matching,the spatial dislocation of carbon storage,food supply and water supply were prominent. The high-low spatial dislocation was mainly distributed in mountainous areas with good ecological base,and the low-high spatial dislocation was mainly distributed in urban areas. Combined with the results of ecosystem service supply and demand and autocorrelation analyses,suggestions are proposed for resource development and protections:to comprehensively enhance the ecological capacity of the study area and protect the ecological environment.

Key words:land ecology and environment;spatial matching;InVEST model; Urban Agglomeration Around Changsha-Zhuzhou-Xiangtan

快速城市化大背景下，社会发展势必会对生态系统造成侵蚀，激化供需矛盾，而生态系统与人类福祉紧密相联，保护生态环境成为当下发展的迫切需求[]。生态系统服务供给是指在一定空间范围内生态系统为人类活动和发展直接或间接提供的所有生态系统服务数量[3]；生态系统服务需求是指在一定空间范围内人类在社会发展中消费和使用的生态系统服务数量[3]。土地利用类型变化和城市扩张导致的生态系统结构改变是出现生态环境问题的根本原因，本质是生态系统服务供给和需求空间分布错位或失衡导致的生态恶化[4]。因此，探析区域生态系统服务供需关系，揭示区域供需空间匹配状况，厘清区域内部之间的生态供给和人们需求之间的关系，为优化区域生态系统综合管理和国土空间规划提供科学依据。

近年来随着人类大规模社会建设活动的开展，人们对美好生态的需求不断增加，使得生态系统服务供需关系及空间匹配状况受到学者们的关注，以此深入研究寻找生态环境与社会发展的平衡点、提升人类福祉具有重要作用。生态系统服务供需研究是从概念的界定等理论方面开始[5]，早期注重生态系统服务供给方面的研究[6-7]。近几年生态系统服务供需研究则集中在供需量化和空间化[8-9]、供需平衡[10-11]、供需分区发展[12]等方面,对生态系统服务供需的评估方法有价值评估法[13]、公众参与法[14]、生态模型法[8]3种。国外学者对生态系统服务供需研究较多，最具代表性的是Burkhard等[15]提出的生态系统服务供需矩阵;Hann 等[16]确定了减少的生态系统服务和提供的生态系统服务之间差异的途径。国内学者也进行了相关研究，张平等[17]对长江经济带的生态系统服务供需价值量进行评估；刘伟等[18]对珠三角城市群 25a间生态系统服务供需均衡关系进行分析;杨宜男等[19]分析了18a间长三角地区城市化对生态系统服务供需的影响。目前研究多关注于生态系统服务供给水平，忽视了生态系统服务需求。通过区域长时序生态系统服务供需分析和空间匹配状况探析，明析供需差异和动态变化趋势，可为政府制定可持续发展战略提供理论参考。

环长株潭城市群作为湖南省经济中心，社会经济活动密集，在城镇快速发展的同时生态空间受挤压，人地矛盾加剧，导致研究区内某些地方逐渐出现大气污染、水体污染等一系列的生态问题。要推动环长株潭城市群高质量发展,实现湖南省十四五规划，迫切需要探索生态服务供需关系。基于此，本研究以环长株潭城市群为研究区，以碳固持、粮食供应、产水和土壤保持服务供需为切入点，探究2000年、2010年、2020年各项生态系统服务供需的空间特征和匹配状况。不仅能促进区域生态结构稳定，进一步优化国土空间开发格局，更为推进生态文明建设提供理论支持。

# 1材料与方法

# 1.1研究区概况

环长株潭城市群，又称"3十5"城市群，以长株潭为中心，以1.5h通勤为半径，包括岳阳、常德、益阳、娄底、衡阳5个城市，总面积9.96万km²。该区域气候为亚热带季风气候，降雨集中在夏季且多暴雨；光热条件充足，年均日照时数在1300一1800 h，无霜期时间长。总体地势较为平坦，处于洞庭湖平原向山区过渡地带，地形多平原、山地和丘陵（图1)。

# 1.2数据来源

研究区30m的LUCC、DEM数据来自中国科学院资源环境科学与数据中心（https://www.res-dc.cn);30 m 的归一化植被指数(NDVI)数据来源于国家生态科学数据中心（https://www.nesdc.org.cn);碳排放数据来自于《中国排放清单和数据集(CEADs)》（https://www.ceads.net);1 km 的土壤数据来源于国家冰川冻土沙漠科学数据中心的中国土壤数据集(2020 年);1km 的年降雨量数据来自于国家地球系统科学数据中心（https://www.geodata.cn);碳密度表主要参考相似区域[20]；1km的人口栅格数据来自于WorldPop（https://hub.worldpop.org)，并用第三次人口普查数据进行修正;1km 的潜在蒸散发数据来自于《全球干旱数和潜在蒸散(ET。)气候数据库v2》(https://figshare.

com);人口数据和粮食产量数据来自于湖南省统计年鉴；用水量数据来自于湖南省水资源公报。

![](images/faf249f2d8f06dc3e2a6b1357af54c5b288752e677cde4cf83b82397b35df02d.jpg)  
图1研究区位置  
Fig.1The location of the research area

# 1.3生态系统服务供需量测算

1.3.1碳固持服务碳固持服务能将大气中的二氧化碳捕获并固定，对生态系统具有重要的调节作用[21]。本研究使用InVEST模型计算供给量，用人均碳排放量、人口密度的乘积为需求量[22],计算公式如下。

需求：Dx=DpcXρxpop (1)式中：D为碳固持服务需求量(t/ʰm²);Dp为人均碳排放量(t);ρxpop 为栅格x 的人口密度(人/hm²）。1.3.2粮食供应服务粮食供应服务是保证当地居民生活的物质基础。粮食产量与NDVI之间有线性关系[23]。将粮食总产量用栅格NDVI值和耕地总NDVI值比值结果分配为供给量，用人口密度和人均粮食需求量的乘积确定需求量，人均粮食需求量则采用已有研究[24],计算公式如下。

NDVI 供给：Gx=Gsum> + NDVI sum 需求:Dip =DpefeXρxpop

式中：G，为粮食供给量(t/hm²);Gsum为粮食总产量(t);NDVI,为每个栅格上的 NDVI值;NDVIsum为耕地NDVI值之和;Df为粮食需求量(t/hm²）;ρxpop为栅格人口密度(人/hm²）;Dpcfc为人均粮食需求量(t)。

1.3.3产水服务环长株潭城市群是长江中下游城市群的重要组成部分，境内河网密集，水资源丰富，评估产水服务供给和需求状况，对防止区域水资源污染具有现实意义。本研究采用InVEST模型计算供给量，用人口密度、人均耗水量的结果为需求量[25],计算公式如下。

需求：Dwp =Dpeweρxpop

![](images/16b7ef82a74cb1c628f4252401e0cb85961fd2e3451225b872202ac0226c523f.jpg)

式中：Dwp为需水量(m/hm²);Dpcwc为人均耗水量(m²）;ρxpop 为栅格x的人口密度(人/hm²）;D为用水总量(m）,包括农业、工业、居民生活、城镇公共、生态环境用水;o为研究区的年末人口数。

1.3.4土壤保持服务土壤保持是生态系统服务和功能的重要部分之一。土壤保持服务需求量是人类希望治理好的实际土壤侵蚀量，本研究用In-VEST 模型的 SDR 模块计算土壤保持量与实际土壤侵蚀量[26]。

# 1.4生态系统服务供需比

生态系统服务供需比(ESDR)能真实反映生态系统服务供需状况[27]，计算公式如下。

![](images/f9498c0c7fedb963d095cf7ee9eca3fdeac25f9b22697e30a90f5b75660ce179.jpg)

式中：ESDR为生态系统服务供需比;D为生态系统服务的需求量;S为生态系统服务的供给量；Dmax为需求量的最大值;Smax为供给量的最大值;ESDR<O表示供小于求;ESDR=0表示供求平衡;ESDR>O表示生态系统服务供大于求。

# 1.5生态系统服务供需匹配

双变量局部空间自相关指数(LISA)反映出空间单元的属性值与相邻单元上相同属性值的相关性和空间聚集程度[28],利用双变量局部自相关指数分析区域内生态系统服务供需的空间匹配特征。

# 2结果与分析

# 2.1环长株潭城市群生态系统服务供需特征

2000－2020年环长株潭城市群碳固持服务供给量逐年小幅下降，从7.82×10°t降至7.65×10"t,单位面积碳固持量从80.71t/hm²降至78.94t/hm²。单位面积碳供给量最高的地区为株洲，次之为长沙和湘潭，其中长沙碳供给量较湘潭的下降速度快，逐渐少于湘潭。从空间分布上来看，碳供给量整体上呈现出南北耕地低，中间丘陵高的分布特征（图2-a)。20a间，环长株潭城市群碳需求量逐年上升，从4.81×10t增至19.32×10t,单位面积固碳需求量从4.96t/hm²增至19.94t/hm²，增长约3倍，长沙和株洲的增幅尤为明显，增长约4倍。在空间上呈点状分布，整体来看是中间高，四周较低（图3-a)。

![](images/b6d1516f24789443ff89c44e06c286f397ea977c55496e09b8955447892954ea.jpg)  
图22000一2020年研究区生态系统服务供给量的空间分布  
Fig.2Spatial distribution of ESs supply in research area from 2ooo to 2020

2000－2020年环长株潭城市群粮食供应服务供给量波动上升，从5.11×10t增至5.34×10t,单位面积粮食供给量从2000 年的5.28t/hm²增至2010 年的5.53 t/hm²，2010 年到 2020 年小幅下降，降至5.51t/hm²。除益阳和岳阳两市单位面积粮食供给量小幅减少外，其他城市仍然保持正向变化态势(图2-b)。20a间环长株潭城市群粮食服务总需求量逐年上升，从1.26×10t增至1.33×10t,单位面积粮食需求量从1.31t/hm²增至1.4t/hm²。长沙单位面积粮食需求量变化最大，从1.72t/hm²增至2.14t/hm²。在空间上呈点状分布，整体南高北低(图3-b)。

2000－2020年环长株潭城市群产水服务供给量逐年上升，从6.1×10l°m增至7.8×10l°m，单位面积产水服务供应量从6940.36m/hm²增至8 945.26m/hm²。在空间分布上，因受降雨分布影响每年有所差别(图2-c)。20a间环长株潭城市群产水服务需求量先增后减，2010年的单位面积需求量为2243.58m/hm²，较2000 年有小幅增长，但2020年单位面积需水量较2010年略有下降，为2144.18m/hm²，主要是受经济活动减少所致。空间上呈点状分布，整体上为东高西低。总的来说，除长沙、株洲、岳阳外，其他地区的产水需求量有所下降(图3-c)。

2000－2020年环长株潭城市群土壤保持服务供给量波动上升，其中 2000 年至 2010 年从17.96×10°t增至20.5×10t，而2020年降至19.52×10t,单位面积土壤保持量先从185.44t/hm²增至211.60 t/hm²，后降至 201.54t/hm²。空间分布上表现为两侧高，中间低，高值区集中在湘中丘陵等山地(图2-d),20a间土壤侵蚀量从2.88×10°t上升至3.11×10t,单位面积土壤侵蚀量从29.7t/hm²增至32.17t/hm²，除株洲和衡阳的单位面积土壤侵蚀量下降外，其他城市保持上升。空间特征上，土壤侵蚀量与土壤保持服务供给量分布基本一致（图3-d)。

![](images/7c044912f5408040496e3d4b216b8714968d5cb1f27a10efe6b9c339958e64b0.jpg)  
图32000一2020年研究区生态系统服务需求量的空间分布  
Fig.3Spatial distribution of ESs demand in research area from 2Ooo to 2020

# 2.2环长株潭城市群生态系统服务供需数量匹配分析

2000－2020年环长株潭城市群碳固持服务供需比下降，从0.104降至0.022，降幅为78%，空间分布上，赤字范围在长株潭等城市周围扩大，赤字程度不断加深，盈余范围则集中在湘中丘陵和东部罗霄山脉;粮食服务供需比基本保持不变，主城区供不应求范围扩大，其他地区点状分布增加;产水服务供需比小幅上升，从0.174增至0.203，升幅为24%，赤字范围在城镇建成区扩大，在盈余区增加点状分布；土壤保持服务供需比在波动中小幅上升，供需比低值区集中在洞庭湖区和研究区中部(表1、图4)。

表12000一2020年研究区生态系统服务供需比  
Table 1The ratio of ES supply and demand in research area from 2Ooo to 2020   

<table><tr><td rowspan="2">地区</td><td colspan="3">碳固持服务供需比</td><td colspan="3">粮食服务供需比</td><td colspan="3">产水服务供需比</td><td colspan="3">土壤保持服务供需比</td></tr><tr><td>2000年</td><td>2010年</td><td>2020年</td><td>2000年</td><td>2010年</td><td>2020年</td><td>2000年</td><td>2010年</td><td>2020年</td><td>2000年</td><td>2010年</td><td>2020年</td></tr><tr><td>益阳</td><td>0.106</td><td>0.031</td><td>0.023</td><td>0.024</td><td>0.028</td><td>0.023</td><td>0.172</td><td>0.188</td><td>0.210</td><td>0.099</td><td>0.096</td><td>0.086</td></tr><tr><td>娄底</td><td>0.105</td><td>0.030</td><td>0.022</td><td>0.023</td><td>0.025</td><td>0.024</td><td>0.186</td><td>0.209</td><td>0.249</td><td>0.137</td><td>0.124</td><td>0.114</td></tr><tr><td>衡阳</td><td>0.099</td><td>0.028</td><td>0.020</td><td>0.020</td><td>0.021</td><td>0.022</td><td>0.174</td><td>0.203</td><td>0.155</td><td>0.080</td><td>0.070</td><td>0.060</td></tr><tr><td>岳阳</td><td>0.108</td><td>0.091</td><td>0.024</td><td>0.022</td><td>0.026</td><td>0.021</td><td>0.151</td><td>0.190</td><td>0.224</td><td>0.070</td><td>0.072</td><td>0.060</td></tr><tr><td>湘潭</td><td>0.105</td><td>0.084</td><td>0.021</td><td>0.020</td><td>0.022</td><td>0.021</td><td>0.177</td><td>0.207</td><td>0.194</td><td>0.065</td><td>0.060</td><td>0.051</td></tr><tr><td>株洲</td><td>0.121</td><td>0.107</td><td>0.028</td><td>0.026</td><td>0.028</td><td>0.027</td><td>0.203</td><td>0.240</td><td>0.198</td><td>0.141</td><td>0.130</td><td>0.101</td></tr><tr><td>长沙</td><td>0.108</td><td>0.081</td><td>0.019</td><td>0.022</td><td>0.022</td><td>0.019</td><td>0.179</td><td>0.229</td><td>0.239</td><td>0.071</td><td>0.095</td><td>0.067</td></tr><tr><td>常德</td><td>0.090</td><td>0.080</td><td>0.021</td><td>0.025</td><td>0.029</td><td>0.024</td><td>0.170</td><td>0.184</td><td>0.250</td><td>0.071</td><td>0.070</td><td>0.067</td></tr><tr><td>环长株潭</td><td>0.104</td><td>0.030</td><td>0.022</td><td>0.023</td><td>0.025</td><td>0.023</td><td>0.174</td><td>0.204</td><td>0.216</td><td>0.092</td><td>0.088</td><td>0.095</td></tr></table>

![](images/1ba3ca0d617883eb85e304ba557032a47ff3a866c7c31d25d965f1323e9ba300.jpg)  
图42000一2020年研究区生态系统服务供需比空间分布  
Fig.4Spatial distribution of supply and demand ratio of ESs in research area from 2ooo to 2020

# 2.3环长株潭城市群生态系统服务供需空间匹配特征

为揭示生态系统服务供需空间特征，利用Geo-Da 软件识别不同的匹配类型，即高高型(简称HH)空间匹配、低低型(简称LL)空间匹配、低高型(简称LH)空间错位和高低型(简称HL)空间错位。

碳固持服务以 HL空间错位为主，面积占比由23%降至21%，主要分布在山地丘陵区，远离城镇人为干扰少；LL空间匹配面积占比在8%左右，与HL空间错位交错分布，为偏远城镇，碳固持能力弱且碳排放量低;HH空间匹配面积占比在6%左右，分布在各主城区周边，为公园等城市休闲区，虽然碳固持能力强，但靠近城市碳排放量也较高;LH空间错位面积占比在2%左右，分布在各个城区，生态用地少且人口积聚，碳固持能力弱且碳排放量高（图5-a）。

粮食供应服务以HL空间错位为主，面积占比从28%增至30%，主要分布在经济发展较慢、人口较少、偏远的农村，粮食供给量多而需求量少;LH空间错位面积占比从8%增至11%，按城镇块状分布，人口聚集，粮食需求量大而供给量小;LL空间匹配面积占比在6%左右，呈块状分布，一部分为湖区，一部分为小县城城区，供给量和需求量均低；HH空间匹配面积占比在3%左右，点状分布于城市周边，地势平坦，农田水利设施完备，粮食产量高且粮食需求也较高(图 5-b)。

产水服务以HL空间错位为主，面积占比从27%降至22%，主要集中在研究区东西两侧，受年降雨影响略有变化;LL空间匹配面积占比从4%增至8%，一方面是因社会活动导致地表植被破坏,另一方面是受年降雨的影响;LH空间错配面积占比在5%左右，按城市块状分布，地面硬化面积多，雨水下渗减少，产水量少且需水量大;HH空间匹配面积占比在3%左右，为城市发展区，植被覆盖较主城区好，且人口较多,产水和需水量高(图 5-c)。

土壤保持服务以LL空间匹配为主，面积占比从45%升至47%，分布于洞庭湖、长株潭及衡阳中部,区域内地势平坦，水土保持措施较好，土壤保持量低且土壤侵蚀量也低;HH空间匹配面积占比在25%左右，分布于偏远的山地丘陵区，虽坡度较大，但林地郁闭度高，因此土壤保持量较高且土壤侵蚀量也较高;LH空间错位面积占比在3%左右，点状分布在HH型区域周边，这些地区因植被覆盖遭到破坏，故土壤保持量低而土壤侵蚀量高;HL空间错位面积占比在3%左右，点状分布于LL型区域周边,这些地区地势较平坦，有较好的植被覆被，能有效防止暴雨对土壤的冲刷作用，土壤保持量较高而土壤侵蚀量较低(图5-d)。

![](images/84007e58ae64155748c83d2efc12d8d77002c198e556eb5c09a3565b6a5dc332.jpg)  
图52000一2020年研究区生态系统服务空间匹配情况  
Fig.5Spatial matching of ESs in research area from 2ooo to 2020

# 3讨论

本研究综合分析了2000－2020 年环长株潭城市群4项生态系统服务供需变化特征，发现粮食供应、产水和土壤保持服务供给量上升，碳固持服务供给量下降,4项生态系统服务需求量增加，这与以往的研究结论基本一致[3,29]。碳固持方面，随着经济社会发展，建设用地需求量增加以及化石燃料使用量上升，使得碳供给量下降而需求量上升;粮食供应方面,农业技术发展带动供给量上升，但随着农村劳动力流失和老龄化、退耕还湿等政策影响使得供给量受到影响，期间需求量持续上升；产水方面，环长株潭城市群属于亚热带季风气候，降雨充沛，且研究区内有洞庭湖及其4大支流，另外建设用地扩大和工业发展等使得雨水下渗减少，故产水服务供给量和需求量上升；土壤保持方面,研究区处于湖南地势较为平整的区域，随着湖南省生态修复、生态保护等政策实施，水土保持功能显著提高。

整体来说，4项生态系统服务供给高值区集中在武陵山脉，湘中丘陵，湘、赣交界处的幕阜-罗霄山脉，与湖南主体功能区划分的生态保护区基本一致。区域内森林群落发育良好,水土资源丰富，包括壶瓶山生态区、花岩溪、大熊山、北罗霄等众多国家森林公园，生态基底良好，是湖南4水重要的生态屏障。生态系统服务需求高值区大体呈现“大集聚，小分散"的分布特征，“大集聚”是指长沙株洲湘潭3市，“小分布"是指其余城市的城镇建成区，与湖南主体功能区划分的开发区分布保持一致。随着城市化进程加快，高强度的人类活动使得对自然资源的开发程度不断加深，也使得土地利用类型发生转变，社会发展对生态系统索取的需求增加。

在生态系统服务供需空间匹配方面，环长株潭城市群除土壤保持以LL空间匹配为主外，其他3项生态系统服务都以HL空间错位为主。高供给低需求区集中在中小型乡镇，这些地方人类活动对生态环境干扰较小,在良好生态基底优势下,未来要对耕地进行统一整合，有序引导耕地流转，加强耕地高标准建设，提高耕地利用效率，避免因劳动力的流失而导致耕地畧荒，同时积极应用农业技术，提高粮食单产。低供给高需求区集中分布在各城市人口稠密区，区域内社会经济活动频繁，未来一方面要控制城市无序扩张,严守城镇开发边界,严格监管土地利用转变，增加绿化面积,提高城市生态容量，另一方面要促进产业绿色升级，实现湖南制造向湖南智造的转变。高供给高需求区集中在城市郊区，靠近城市，地势平坦开阔，自然条件优越，但未来应多开展农田水利设施建设,提高土壤肥力，增设生态用地，防止生态环境恶化。低供给低需求区集中在大片水体或偏远山地丘陵处，未来应以区域生态保护为主，降低人类活动强度，全面提升环长株潭城市群各项生态容量。

本研究致力于环长株潭城市群内部生态系统服务供给和需求的数量、空间特征及空间匹配状况，区域内生态系统服务供需整体处于盈余状态，但供需匹配的空间失衡现象明显。生态系统服务供需之间的变化能反映生态环境与社会发展之间的动态联系，当某一区域的供给量大于需求量时就会往外溢出，但生态系统服务受诸多因素的影响，生态系统服务的流动过程十分复杂，供给和需求的边界难以明确界定。未来研究要深入分析生态系统服务供需的内部原理和变化的驱动机制，明确生态系统服务溢出效应的流向、流速、流量，为生态系统综合管理、生态文明建设提供理论支持。

# 4结论

本研究基于多源数据，从生态环境协调发展视角出发，选取了碳固持、粮食供应、产水和土壤保持4项生态系统的供给和需求，利用局部自相关等多种研究方法进行评估分析，结论如下。

1)环长株潭城市群各项生态系统服务供需在空间分布上各有其特点，碳供给量南北低中间高，粮食供给量北高南低，产水供给量高值区因降雨差异而不断变化，2000年在湘中丘陵，2010年在研究区东部,2020年在研究区北部，土壤保持量两侧高，中间低;生态系统服务需求量除土壤侵蚀量与土壤保持量分布基本保持相同外，碳、粮食和产水需求量受城市扩张影响而呈点状摊开分布。

2)环长株潭城市群在供需数量上的特征表现为粮食供应、产水和土壤保持服务供给量上升，碳固持服务供给量下降，4项生态系统服务需求量总体保持上升，各项生态系统服务皆供大于需，粮食供应和土壤保持服务供需比基本保持不变，产水服务因地表水增加而供需比上升，但碳固持因需求量的大幅上升导致其供需比下降，未来要严格土地利用类型用途管制，提高研究区各项生态容量，促进社会与生态环境协调发展。

3)环长株潭城市群有 HH匹配、LL匹配、LH错配和HL错配4种匹配类型，除土壤保持服务以LL空间匹配为主外，碳固持、粮食供应、产水服务都以HL空间错位为主，HL空间错位主要分布在生态基底较好的山地丘陵地区，LH空间错位主要分布在各市城区，主要是区域生态与经济发展不均衡所致，未来要增加城区绿化面积，提高城市生态容量，防止生态环境恶化。

# 参考文献：

[1]朱佩娟，王学栋，谢雨欣,等.基于主体功能区划的湖南省生态系统服务供需关系演变[J].生态学报，2023，43（15)：6182-6193.ZHU PJ,WANG XD,XIE Y X,et al.Evolution of supply anddemand relationship of ecosystem services in Hu'nan Provincebased on main function zoning[J].Acta Ecologica Sinica,2023,43(15):6182-6193.(in Chinese)  
[2] 马国强,李秋洁,张蓉,等.抚仙湖流域景观格局及生态系统服务价值的动态变化[J].西北林学院学报，2023,38(2)：265-272.MAG Q,LIQJ,ZHANG R,et al.Dynamic changes of land-scape pattern and ecosystem service value in the Fuxian Lakebasin[J]. Journal of Northwest Forestry University,2023,38(2):265-272.(in Chinese)  
[3] 王盈丽，徐新良，庄大春，等.湖南省生态系统服务供需格局演变[J].生态学杂志,2021,40(10):3268-3277.WANGYL,XUXL,ZHUANGDC,et al.Evolution of thesupply and demand pattern of ecosystem services in HunanProvince[J].Chinese Journal of Ecology,2021,40(10):3268-3277.(in Chinese)  
[4] 李倩，吴雅华，李佳芯，等.基于生态系统服务供需关系的福州绿地生态网络构建分区[J].西北林学院学报，2022,37（2)：238-247.LIQ,WU Y H,LIJX,et al.Construction zoning of urbangreen space ecological network based on ecosystem service sup-ply and demand in Fuzhou[J].Journal of Northwest ForestryUniversity,2022,37(2):238-247.(in Chinese)  
[5] ZHAI T,WANG J,JING Z,et al.Did improvements of ecosys-tem services supply-demand imbanlance change environmentalspatial injustices?［J]．Ecological Indicators，2020，111:106068.  
[6] 张自正，张蕾，孙桂英，等.清江流域生态系统服务权衡时空效应及驱动因素[J].应用生态学报，2023，34（4)：1051-1062.ZHANG ZZ,ZHANGL,SUNG Y,et al.Spatial and temporaleffect and driving factors of ecosystem service trade-off in theQingjiang River Basin China[J].Chinese Journal of Applied E-cology,2023,34(4):1051-1062.(in Chinese)  
[10]赵泾峰，冯德君，张文辉，等.陕西不同天然类型栓皮栎软木的主要化学组分及其利用分析[J].西北农林科技大学学报（自然科学版)，2014，42(9)：78-82，90.ZHAOJF,FENGDJ,ZHANGWH,etal.Mainchemical com-ponents and utilization analyses of different natural Quercus vari-abilis corks in Shaanxi[J].Journal of Northwest A&FUniversity(Nat.Sci.Ed.),2014,42(9):78-82,90.(in Chinese)  
[11] 陈慧，苑一丹，宋孝周.初生和再生软木特性及化学组成对比分析[J].木材加工机械，2016，27(4)：40-44.  
[12] 张英杰，赵泾峰，冯德君.4种不同类型栓皮栎软木物理力学性能研究[J].广西林业科学，2020，49(1)：135-138.  
[13] 张守兵，杨瑾.栓皮采剥技术[J].特种经济动植物，2010，13(3):30-31.  
[14] MIRANDA I,GOMINHO J,PEREIRA H.Cellular structureand chemical composition of cork from the Chinese cork oak(Quercus variabilis）[J].Journal of Wood Science,2013,59(1)：1-9.  
[15] HOOKE R,MARTYN J,ALLESTRY J.Micrographia,or somephysiological descriptions of minute bodies made by magnif-ying glasses? with observations and inquiries thereupon[M].London:the Royal Society,1665.  
[16] PRASETIAD,PURUSATAMABD,KIMJH,etal.Quan-titative anatomical characteristics of virgin cork in Quercusvariabilis grown in Korea[J].Forests,2022,13(10):1-14.  
[17] PEREIRA H.The cellular structure of cork from QuercussuberL[J].IAWAJournal,1987,8(3):213-218.  
[18] SENA,QUILHO T,PEREIRA H.The cellular structure ofcork from Quercus cerris var.cerris bark in a materials’per-spective[J].Industrial Crops and Products,2011,34(1):929-936.  
[19] 臧小榕，母军，张新宇.软木细胞壁化学组分及软木材料应用探析[J].林产工业，2019，46(8)：47-52.  
[20] 夏敬清.不同水热条件下树木形成层活动及径向生长监测研究[D].兰州：兰州大学，2022.  
[21］张军周.祁连山树木形成层活动及年内径向生长动态监测研究[D].兰州：兰州大学，2018.

# （上接第209页）

[7]王茹，张先平，张晓玲，等.2000一2020年山西省宁武县生态系统服务价值时空动态研究[J].西北林学院学报，2024，39（1)：264-272.WANGR,ZHANG XP,ZHANG XL,et al.Spatiotemporaldynamics of ecosystem service value in Ningwu County,ShanxiProvince from 2000 to 202o[J].Journal of Northwest ForestryUniversity，2024,39(1):264-27.(in Chinese)  
[8] 占活，于洋，吴秀芹.湟水流域生态系统服务供需匹配关系[J].生态学报，2021,41(18)：7260-7272.  
[9] 陈泓文，巩杰.陕北黄土高原生态系统服务供需格局及其演变[J].水土保持研究，2021,28(6):226-232.  
[10] WANG J,ZHAI T,LIN Y,et al.Spatial imbalance and change insupply and demand of ecosystem services in China[J].Science ofthe Total Environment,2019,659:781-791.  
[11] 陈立恒，龚健，王雄，等.长江中游地区生态系统服务平衡与城镇化的空间关系[J].生态学报,2021,41(14)：5546-5556.  
[12] GUANQ,HAOJ,RENG,etal.Ecological indexesforthe a-nalysis of the spatial-temporal characteristics of ecosystemservice supply and demand:a case study of the major grain-producing regions in Quzhou,China[J].Ecological Indicators,2020,108:105748.  
[13] 谢高地，张彩霞，张雷明，等.基于单位面积价值当量因子的生态系统服务价值化方法改进[J].自然资源学报，2015，30（8)：1243-1254.  
[14] DVARRSKAS A.Mapping ecosystem services supply chainsfor coastal Long Island communities:implications for resili-ence planning[J].Ecosystem Services,2018,30:14-26.  
[15] BURKHARDB,KROLLF,NEDKOVS,etal.Mapping eco-system service supply，demand and budgets[J].Ecologicallndicator,2012,21：17-29.  
[16] HANNDEL,ROUXDJ,CURRIEB,etal.Identifying path-ways to reduce discrepancies between desired and provided ecosys-tem services[J].Ecosystem Services,2020,43:101119.  
[17]张平，朱翔，贺清云，等.长江经济带生态系统服务供需时空分异与平衡格局分析[J].生态科学，2020,39(6)：155-166.  
[18] 刘伟，张帆，魏云浩，等.珠三角城市群区域生态系统服务供需均衡关系分析[J].生态学报,2023,43(1)：4461-4472.  
[19] 杨宜男，李敬，王立，等.长三角地区城市化对典型生态系统服务供需的影响[J].自然资源学报，2022，37(6)：1555-1571.  
[20] 戴云哲.湖南省土地生态服务功能演化特征及优化路径研究[D].中国地质大学,2020.  
[21] 赵宇豪，罗宇航，易腾云，等.基于生态系统服务供需匹配的深圳市生态安全格局构建[J].应用生态学报，2022，33（9)：2475-2484.  
[22] 刘春芳，王韦婷，刘立程，等.西北地区县域生态系统服务的供需匹配：以甘肃古浪县为例[J].自然资源学报,2020,35（9)：2177-2190.  
[23] PANEK E,GOZDOWSKI D.Analysis of relationship between ce-real yield and NDVI for selected regions of central Europe basedon MODIS satelite data[J].Remote Sensing Applications:Societyand Environment,2020,17:100286.  
[24] 唐华俊，李哲敏.基于中国居民平衡膳食模式的人均粮食需求量研究[J].中国农业科学，2012,45(11):2315-2327.  
[25] 胡昂，吴俣思，黄莹，等.高空间异质性区域生态系统服务供需与驱动力分析：以四川省为例[J].长江流域资源与环境，2022，31(5):1062-1076.  
[26]朱月华,侯宗东,徐彩仙,等.基于生态系统服务供需关系的甘肃白龙江流域生态风险识别与管理[J].地理科学，2023，43(3):423-433.  
[27] 王晓峰，尧文洁，冯晓明，等.青藏高原生态系统服务供需变化及其驱动因素[J].生态学报，2023，43(17)：1-15.  
[28] 刘立程，刘春芳，王川，等.黄土丘陵区生态系统服务供需匹配研究：以兰州市为例[J].地理学报，2019，74(9)：1921-1937.  
[29] 朱佩娟，王学栋，谢雨欣，等.基于主体功能区划的湖南省生态系统服务供需关系演变[J].生态学报，2023，43（15)：6182-6193.