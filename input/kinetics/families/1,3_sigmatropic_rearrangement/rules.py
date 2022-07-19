#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.30791e+26,'s^-1'), n=-3.67984, w0=(664000,'J/mol'), E0=(247189,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4163866947181062, var=128.1927359939506, Tref=1000.0, N=20, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 20 training reactions at node Root
            Total Standard Deviation in ln(k): 23.74425553407489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 23.74425553407489""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 23.74425553407489
sensitivities = [{'dA': 0.17745833756068485, 'dE0': 0.000821558328916846, 'dn': -0.025856364545191697, 'dA_dEa': 0.6098408931727978, 'dE0_dEa': 0.003753691744558703, 'dn_dEa': -0.08932181845701427, 'name': 'C3H6O <=> C3H6O-2'}, {'dA': -0.5553171096437993, 'dE0': -0.0027748209728643692, 'dn': 0.08956055336734534, 'dA_dEa': 19.51794912256803, 'dE0_dEa': 0.13473556654610286, 'dn_dEa': -2.8606177971577424, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': 1.120540320982978, 'dE0': 0.004876473573474558, 'dn': -0.15602964733782462, 'dA_dEa': -45.9151021877326, 'dE0_dEa': -0.1132534490115155, 'dn_dEa': 6.728015675149742, 'name': 'C2H3N3 <=> C2H3N3-2'}, {'dA': -0.635473796865752, 'dE0': -0.003135772313855026, 'dn': 0.1013267763449101, 'dA_dEa': 11.259853563840313, 'dE0_dEa': 0.07634681562407711, 'dn_dEa': -1.6502544959533976, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': 0.9115644888951673, 'dE0': 0.00392562660592811, 'dn': -0.1253923190821723, 'dA_dEa': -27.46609002038927, 'dE0_dEa': -0.04921829702877353, 'dn_dEa': 4.024486767283199, 'name': 'C2H2N2O <=> C2H2N2O-2'}, {'dA': 0.6365881578425804, 'dE0': 0.002667663194955526, 'dn': -0.08510555996744602, 'dA_dEa': -22.7783861320628, 'dE0_dEa': 0.0002287897709565855, 'dn_dEa': 3.33733535249181, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': 0.26830162152438786, 'dE0': 0.000981376151921271, 'dn': -0.031153293975283027, 'dA_dEa': -0.4000838920533042, 'dE0_dEa': 0.055816969880714114, 'dn_dEa': 0.05816025150720751, 'name': 'C2H2N2O-3 <=> C2H2N2O-4'}, {'dA': 0.4750584656144054, 'dE0': 0.0019301060266287517, 'dn': -0.06143431823959668, 'dA_dEa': -10.73461388156834, 'dE0_dEa': 0.036377242462582095, 'dn_dEa': 1.5723839151678882, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': 0.6375431594528171, 'dE0': 0.0026715469648347463, 'dn': -0.08524725740394373, 'dA_dEa': -23.09327519655723, 'dE0_dEa': 0.0004414382177843166, 'dn_dEa': 3.383429036151037, 'name': 'C4H3N3 <=> C4H3N3-2'}, {'dA': -0.6704083842131353, 'dE0': -0.003300398341133044, 'dn': 0.10642654150314106, 'dA_dEa': 43.90059716503231, 'dE0_dEa': 0.29059697512832416, 'dn_dEa': -6.434321168618779, 'name': 'C4H4N2O <=> C4H4N2O-2'}, {'dA': 0.1778364293869768, 'dE0': 0.0008231364475456188, 'dn': -0.025912347479803203, 'dA_dEa': 0.6733002583488488, 'dE0_dEa': 0.0041844999682259755, 'dn_dEa': -0.09862399994827536, 'name': 'CCC=O <=> C=COC'}, {'dA': -0.5540872427723442, 'dE0': -0.0027696305575240832, 'dn': 0.08937872392597608, 'dA_dEa': 11.938055366639482, 'dE0_dEa': 0.08324318962750833, 'dn_dEa': -1.7496842572310527, 'name': 'NC(=N)OC=O <=> O=CNC(=O)N'}, {'dA': 1.1183033815137644, 'dE0': 0.0048671887080274905, 'dn': -0.15569816476737672, 'dA_dEa': -19.020221496673138, 'dE0_dEa': -0.04666759915744495, 'dn_dEa': 2.787092275191335, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': -0.6265705469630924, 'dE0': -0.0030986044882202277, 'dn': 0.1000083378809404, 'dA_dEa': 17.565480549587225, 'dE0_dEa': 0.11796994615013427, 'dn_dEa': -2.5744235621345717, 'name': 'O=CNC=O <=> N=COC=O'}, {'dA': 0.9205179448060666, 'dE0': 0.003962983144938728, 'dn': -0.12671822410265604, 'dA_dEa': -8.741432436569848, 'dE0_dEa': -0.015111756002638052, 'dn_dEa': 1.2808992674623578, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': 0.6406449604200044, 'dE0': 0.002684541329390015, 'dn': -0.08570656458571378, 'dA_dEa': -12.08057802264184, 'dE0_dEa': 0.0005271527611726148, 'dn_dEa': 1.7699876398645678, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.26222920728005805, 'dE0': 0.0009554920720915784, 'dn': -0.030256475557544724, 'dA_dEa': -0.08300832724118327, 'dE0_dEa': 0.017189182840987836, 'dn_dEa': 0.01206799733755204, 'name': 'O=CN1C=N1 <=> c1ncno1'}, {'dA': 0.47543300523150384, 'dE0': 0.0019316620289332466, 'dn': -0.06148981018489072, 'dA_dEa': -5.052177077726428, 'dE0_dEa': 0.0177265785002525, 'dn_dEa': 0.7400941850508452, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.6417853664367353, 'dE0': 0.0026890253143596384, 'dn': -0.08587643130824021, 'dA_dEa': -12.43092922185122, 'dE0_dEa': 0.000585485861267044, 'dn_dEa': 1.821310451198799, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}, {'dA': -0.6666683447847556, 'dE0': -0.0032847653926817958, 'dn': 0.10587251219220878, 'dA_dEa': 49.12002098876841, 'dE0_dEa': 0.32518167503168255, 'dn_dEa': -7.199307632789696, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}]
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.07986e-21,'s^-1'), n=9.62589, w0=(636417,'J/mol'), E0=(33022,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3571800124903484, var=28.092031200167057, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
            Total Standard Deviation in ln(k): 14.035480087290036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 14.035480087290036""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 14.035480087290036
sensitivities = [{'dA': 0.16756508186690125, 'dE0': 0.0, 'dn': -7.090636640066177e-06, 'dA_dEa': -26.42110672869371, 'dE0_dEa': 0.0, 'dn_dEa': 0.17001016862726132, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': 0.1677062872858144, 'dE0': 0.0, 'dn': -8.107103255626465e-06, 'dA_dEa': -16.30278011657717, 'dE0_dEa': 0.0, 'dn_dEa': 0.10490048360582249, 'name': 'O=CN1C=N1 <=> o1cnnc1'}, {'dA': 0.16760486884949868, 'dE0': 0.0, 'dn': -7.3766548081029895e-06, 'dA_dEa': -36.62484114847024, 'dE0_dEa': 0.0, 'dn_dEa': 0.23566467788642104, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.16753637395085688, 'dE0': 0.0, 'dn': -6.879824730379216e-06, 'dA_dEa': -11.551172379357261, 'dE0_dEa': 0.0, 'dn_dEa': 0.07432611459707224, 'name': 'O=CN1C=N1 <=> c1ncno1'}, {'dA': 0.16755096025635366, 'dE0': 0.0, 'dn': -6.988421759815921e-06, 'dA_dEa': -26.832338721152496, 'dE0_dEa': 0.0, 'dn_dEa': 0.172653770076145, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.16740308687703442, 'dE0': 0.0, 'dn': -5.92163594245298e-06, 'dA_dEa': -37.7164355990131, 'dE0_dEa': 0.0, 'dn_dEa': 0.24268834182940127, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 3,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(5.95588e+67,'s^-1'), n=-15.1817, w0=(654062,'J/mol'), E0=(403939,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5544159323717395, var=269.88167642966965, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing
            Total Standard Deviation in ln(k): 36.83950759794208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 36.83950759794208""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 36.83950759794208
sensitivities = [{'dA': -5.436305486782688, 'dE0': -0.017030208170922042, 'dn': -0.10954472770355723, 'dA_dEa': -61.63843613425225, 'dE0_dEa': -0.04315835581645802, 'dn_dEa': -1.213955160255134, 'name': 'C2H3N3 <=> C2H3N3-2'}, {'dA': -5.7271255787305275, 'dE0': -0.01792122214673229, 'dn': -0.1152729248868635, 'dA_dEa': -39.588079170916146, 'dE0_dEa': -0.006124408243060658, 'dn_dEa': -0.7796535786251959, 'name': 'C2H2N2O <=> C2H2N2O-2'}, {'dA': -6.134310950586262, 'dE0': -0.01916850158366542, 'dn': -0.12329331710692674, 'dA_dEa': -34.666401616551475, 'dE0_dEa': 0.05133886676483473, 'dn_dEa': -0.6826724984137218, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': -6.680453879852902, 'dE0': -0.020842236566810574, 'dn': -0.1340501587844639, 'dA_dEa': -7.656347943425023, 'dE0_dEa': 0.06370757733514983, 'dn_dEa': -0.15073304541846777, 'name': 'C2H2N2O-3 <=> C2H2N2O-4'}, {'dA': -6.3665398511581275, 'dE0': -0.019880006394176798, 'dn': -0.1278674557912546, 'dA_dEa': -20.34994329904063, 'dE0_dEa': 0.06677799975949765, 'dn_dEa': -0.4007169751360184, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': -6.135038577966832, 'dE0': -0.019170814723032326, 'dn': -0.12330758327750227, 'dA_dEa': -35.13112178494669, 'dE0_dEa': 0.052429902804557726, 'dn_dEa': -0.6918274353755218, 'name': 'C4H3N3 <=> C4H3N3-2'}, {'dA': -8.00095977648229, 'dE0': -0.024886398956812158, 'dn': -0.16006097129802732, 'dA_dEa': 42.39817974596361, 'dE0_dEa': 0.26625490000416535, 'dn_dEa': 0.8352448846060465, 'name': 'C4H4N2O <=> C4H4N2O-2'}, {'dA': -7.999557345343959, 'dE0': -0.024881861963871273, 'dn': -0.16003357116831263, 'dA_dEa': 48.14265964944828, 'dE0_dEa': 0.30011254129561055, 'dn_dEa': 0.9484142503142143, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}]
""",
)

entry(
    index = 4,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.58597e+12,'s^-1'), n=0.0440307, w0=(704833,'J/mol'), E0=(136609,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06241320838115143, var=8.945969542406907, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing
            Total Standard Deviation in ln(k): 6.152942370306084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 6.152942370306084""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 6.152942370306084
sensitivities = [{'dA': 0.46515933557605543, 'dE0': 0.003666602291272095, 'dn': -0.2461547109202851, 'dA_dEa': 0.6680740245209219, 'dE0_dEa': 0.012459472756141465, 'dn_dEa': -0.3564361213937398, 'name': 'C3H6O <=> C3H6O-2'}, {'dA': 1.1083902431786696, 'dE0': 0.006729766149733058, 'dn': -0.45863825144113257, 'dA_dEa': -7.475505055375577, 'dE0_dEa': 0.2872244538491452, 'dn_dEa': 3.9843246213284806, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': 0.3196410919131051, 'dE0': 0.0006572545061465871, 'dn': -0.037124875704167205, 'dA_dEa': 6.9679893468091905, 'dE0_dEa': 0.2421156653729617, 'dn_dEa': -3.729161195252135, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': 0.4824971794726272, 'dE0': 0.003788839106076549, 'dn': -0.2555156063892486, 'dA_dEa': 0.7028353431231756, 'dE0_dEa': 0.013791199501212863, 'dn_dEa': -0.37508577387714814, 'name': 'CCC=O <=> C=COC'}, {'dA': 1.0995428184089706, 'dE0': 0.006667031502799841, 'dn': -0.45386491974635856, 'dA_dEa': -4.527018509759061, 'dE0_dEa': 0.18234969022918363, 'dn_dEa': 2.4128896106051223, 'name': 'NC(=N)OC=O <=> O=CNC(=O)N'}, {'dA': 0.32947016805454943, 'dE0': 0.0007265505800736362, 'dn': -0.042431421575405956, 'dA_dEa': 10.107388121466391, 'dE0_dEa': 0.3633775224961269, 'dn_dEa': -5.409130880443398, 'name': 'O=CNC=O <=> N=COC=O'}]
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.91531e-14,'s^-1'), n=7.49565, w0=(624125,'J/mol'), E0=(13825.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8129505795286808, var=3.6728302512857196, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
            Total Standard Deviation in ln(k): 5.88458990276278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 5.88458990276278""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 5.88458990276278
sensitivities = [{'dA': 0.25355648892858035, 'dE0': -0.0, 'dn': -1.1711601729139245e-05, 'dA_dEa': -54.93973245712064, 'dE0_dEa': -0.0, 'dn_dEa': 0.15575702329097718, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': 0.25365769698740287, 'dE0': -0.0, 'dn': -1.2032296288179906e-05, 'dA_dEa': -17.332048688333177, 'dE0_dEa': -0.0, 'dn_dEa': 0.04913845034437029, 'name': 'O=CN1C=N1 <=> c1ncno1'}, {'dA': 0.25347392511324024, 'dE0': -0.0, 'dn': -1.1448920072965098e-05, 'dA_dEa': -40.25494908853932, 'dE0_dEa': -0.0, 'dn_dEa': 0.1141261807286992, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.25348957353801843, 'dE0': -0.0, 'dn': -1.1498408989721378e-05, 'dA_dEa': -56.572313170824465, 'dE0_dEa': -0.0, 'dn_dEa': 0.16038361477839652, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 6,
    label = "Root_Ext-2R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.48161e-36,'s^-1'), n=13.8864, w0=(661000,'J/mol'), E0=(11036.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.649252153480784, var=28.6187499376758, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
            Total Standard Deviation in ln(k): 32.45641936565119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 32.45641936565119""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 32.45641936565119
sensitivities = [{'dA': 2.257471507619151, 'dE0': 0.009575627929643626, 'dn': -0.09930738065268699, 'dA_dEa': -20.53382116203699, 'dE0_dEa': 0.320350587967943, 'dn_dEa': 1.1575492138163062, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}, {'dA': -0.09763208606728933, 'dE0': -0.0032779695962516383, 'dn': 0.03372228067413474, 'dA_dEa': 24.602309693285076, 'dE0_dEa': 0.401002413521361, 'dn_dEa': -1.3912580326666755, 'name': 'O=CN1C=N1 <=> o1cnnc1'}]
""",
)

entry(
    index = 7,
    label = "Root_1R!H-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(2.50818e+88,'s^-1'), n=-21.0628, w0=(638000,'J/mol'), E0=(484196,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.168561953451146, var=422.3137326737107, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
            Total Standard Deviation in ln(k): 51.671627485424715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 51.671627485424715""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 51.671627485424715
sensitivities = [{'dA': 3.1906496747925632, 'dE0': 0.008315263125948713, 'dn': 0.07309318369666679, 'dA_dEa': -95.8032716854652, 'dE0_dEa': -0.001999946478719473, 'dn_dEa': -2.3817811153415116, 'name': 'C2H3N3 <=> C2H3N3-2'}, {'dA': 1.8591582660720634, 'dE0': 0.0045603379753041354, 'dn': 0.039988097012384725, 'dA_dEa': -38.80968957191017, 'dE0_dEa': 0.18057716755212797, 'dn_dEa': -0.9647116951925935, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': 1.857167296705802, 'dE0': 0.004554697887057419, 'dn': 0.03993862202197422, 'dA_dEa': -39.43099342317148, 'dE0_dEa': 0.18345484371400358, 'dn_dEa': -0.980165311109279, 'name': 'C4H3N3 <=> C4H3N3-2'}, {'dA': -1.6969047714072354, 'dE0': -0.005465393505294439, 'dn': -0.048429724798739825, 'dA_dEa': 130.63292291427348, 'dE0_dEa': 0.6493169229490718, 'dn_dEa': 3.2482429887000803, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}]
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(4.09681e+60,'s^-1'), n=-13.1585, w0=(670125,'J/mol'), E0=(360582,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5668157718817215, var=547.8562761169217, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
            Total Standard Deviation in ln(k): 50.860213488451016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 50.860213488451016""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 50.860213488451016
sensitivities = [{'dA': -16.923668076346576, 'dE0': -0.055507885029634906, 'dn': -0.23733977142193527, 'dA_dEa': -92.70220623548252, 'dE0_dEa': -0.056663612460129596, 'dn_dEa': -1.2809695747737218, 'name': 'C2H2N2O <=> C2H2N2O-2'}, {'dA': -18.898084005927934, 'dE0': -0.06188748071227258, 'dn': -0.2646273832121722, 'dA_dEa': -30.86080336194981, 'dE0_dEa': 0.08409665519113685, 'dn_dEa': -0.42634199796715644, 'name': 'C2H2N2O-3 <=> C2H2N2O-4'}, {'dA': -18.24720309628193, 'dE0': -0.05978382219948172, 'dn': -0.2556321232716411, 'dA_dEa': -60.0795321660494, 'dE0_dEa': 0.07818405194541825, 'dn_dEa': -0.8300797786329664, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': -21.634507631037078, 'dE0': -0.0707267060393168, 'dn': -0.3024477167792292, 'dA_dEa': 51.99492662663947, 'dE0_dEa': 0.4556475109326278, 'dn_dEa': 0.7188597704858434, 'name': 'C4H4N2O <=> C4H4N2O-2'}]
""",
)

entry(
    index = 9,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.50839e+11,'s^-1'), n=0.136197, w0=(707000,'J/mol'), E0=(134212,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01703312323488117, var=1.3519057502930525, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
            Total Standard Deviation in ln(k): 2.373731974677581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.373731974677581""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.373731974677581
sensitivities = [{'dA': 0.6972490057109639, 'dE0': 0.003487088142014094, 'dn': -0.21580924344845084, 'dA_dEa': -8.23306478287213, 'dE0_dEa': 0.2871016275362843, 'dn_dEa': 3.962065297209422, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': -0.23811244615148788, 'dE0': -0.0037375945989411236, 'dn': 0.2358983308884, 'dA_dEa': 6.87195864334176, 'dE0_dEa': 0.2454886601436714, 'dn_dEa': -3.3205375052184936, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': 0.679356287761909, 'dE0': 0.003377182447382749, 'dn': -0.2069512322451428, 'dA_dEa': -5.266188441794964, 'dE0_dEa': 0.18026829988527984, 'dn_dEa': 2.534822846975313, 'name': 'NC(=N)OC=O <=> O=CNC(=O)N'}, {'dA': -0.11730270405153802, 'dE0': -0.002862705095127671, 'dn': 0.17711915388277064, 'dA_dEa': 10.376321561620193, 'dE0_dEa': 0.37161109584190505, 'dn_dEa': -5.013873513256139, 'name': 'O=CNC=O <=> N=COC=O'}]
""",
)

entry(
    index = 10,
    label = "Root_N-1R!H-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(0.00257114,'s^-1'), n=4.34785, w0=(700500,'J/mol'), E0=(369438,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.092640560837302, 'dn_dEa': 0.0, 'name': 'CCC=O <=> C=COC'}]
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700500,'J/mol'), E0=(384026,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.920203198450264, 'dn_dEa': 0.0, 'name': 'C3H6O <=> C3H6O-2'}]
""",
)

entry(
    index = 12,
    label = "Root_Ext-2R!H-R_5R!H->C_4R!H->N",
    kinetics = ArrheniusBM(A=(7.88104e+10,'s^-1'), n=0.444174, w0=(559500,'J/mol'), E0=(121694,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->N
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.5548165434493835, 'dn_dEa': -0.0, 'name': 'O=CN1C=N1 <=> c1ncno1'}]
""",
)

entry(
    index = 13,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->N",
    kinetics = ArrheniusBM(A=(1.84746e-16,'s^-1'), n=8.14258, w0=(645667,'J/mol'), E0=(64566.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7487509793916722, var=1.4587138791120244, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N
            Total Standard Deviation in ln(k): 4.3025473220224155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N
Total Standard Deviation in ln(k): 4.3025473220224155""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N
Total Standard Deviation in ln(k): 4.3025473220224155
sensitivities = [{'dA': 0.7396004556668705, 'dE0': 0.0015315404614201131, 'dn': -0.03474683742028717, 'dA_dEa': -6.394861423317615, 'dE0_dEa': 0.2505683464572948, 'dn_dEa': 0.5458646447221648, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}, {'dA': -0.05358178808734827, 'dE0': -0.0014412032345504694, 'dn': 0.03310887470879804, 'dA_dEa': 13.763896296266248, 'dE0_dEa': 0.25271810776754344, 'dn_dEa': -1.1783809191443484, 'name': 'O=CN1C=C1 <=> c1ncco1'}, {'dA': 0.7368846893066306, 'dE0': 0.0015207074660007292, 'dn': -0.03451649846972304, 'dA_dEa': -6.525169776943337, 'dE0_dEa': 0.25826475387245373, 'dn_dEa': 0.5569761243397557, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 14,
    label = "Root_Ext-2R!H-R_N-5R!H->C_3R!H->N",
    kinetics = ArrheniusBM(A=(3.19239e+10,'s^-1'), n=0.633646, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->N
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'N=CN1C=N1 <=> [nH]1cnnc1'}]
""",
)

entry(
    index = 15,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N",
    kinetics = ArrheniusBM(A=(7.16673e+09,'s^-1'), n=0.77465, w0=(707000,'J/mol'), E0=(194100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.5713719573767743, 'dn_dEa': -0.0, 'name': 'O=CN1C=N1 <=> o1cnnc1'}]
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(7.79562e-25,'s^-1'), n=11.2893, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0768327727097848, var=36.91907930296372, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N
            Total Standard Deviation in ln(k): 14.886595318028107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 14.886595318028107""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 14.886595318028107
sensitivities = [{'dA': 1.6677854129129759, 'dE0': 0.004556932512330011, 'dn': 0.19838896598819608, 'dA_dEa': -77.10829580984463, 'dE0_dEa': 0.16893698206271696, 'dn_dEa': -11.46494717036242, 'name': 'C2H3N3 <=> C2H3N3-2'}, {'dA': -0.4750035942394061, 'dE0': -0.0027381639380913946, 'dn': -0.12024622547525325, 'dA_dEa': 32.541659470201296, 'dE0_dEa': 0.5769181312670679, 'dn_dEa': 4.842848626912094, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': -0.4668906032208556, 'dE0': -0.002713813669018012, 'dn': -0.11902256939938732, 'dA_dEa': 33.19139880827403, 'dE0_dEa': 0.5865464605115267, 'dn_dEa': 4.939582585696203, 'name': 'C4H3N3 <=> C4H3N3-2'}]
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_2R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.14287e+10,'s^-1'), n=1.07105, w0=(707000,'J/mol'), E0=(428529,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->N
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.0664330387001333, 'dn_dEa': 0.0, 'name': 'O=c1cncc[nH]1 <=> N=c1cncco1'}]
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->N",
    kinetics = ArrheniusBM(A=(3.23202e+11,'s^-1'), n=0.959257, w0=(559500,'J/mol'), E0=(116309,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 2.0079543395483843, 'dn_dEa': 0.0, 'name': 'C2H2N2O-3 <=> C2H2N2O-4'}]
""",
)

entry(
    index = 19,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N",
    kinetics = ArrheniusBM(A=(5.17463e+69,'s^-1'), n=-15.7846, w0=(707000,'J/mol'), E0=(419904,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6020204647519467, var=752.2013288923092, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
            Total Standard Deviation in ln(k): 59.0076206693908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 59.0076206693908""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 59.0076206693908
sensitivities = [{'dA': -4.921800580959799, 'dE0': -0.015016403507650116, 'dn': -0.06616629965281211, 'dA_dEa': -98.36968395070417, 'dE0_dEa': 0.005333169544529679, 'dn_dEa': -1.238351548981489, 'name': 'C2H2N2O <=> C2H2N2O-2'}, {'dA': -6.399637366414618, 'dE0': -0.0192400097884683, 'dn': -0.08477369896238207, 'dA_dEa': -60.325427548171255, 'dE0_dEa': 0.14878615374846796, 'dn_dEa': -0.7593146839145334, 'name': 'C3H3NO <=> C3H3NO-2'}, {'dA': -10.161356652490081, 'dE0': -0.02999286058318679, 'dn': -0.1321362977460014, 'dA_dEa': 70.22107246155747, 'dE0_dEa': 0.5399399252091187, 'dn_dEa': 0.8844097034498359, 'name': 'C4H4N2O <=> C4H4N2O-2'}]
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N",
    kinetics = ArrheniusBM(A=(7.42118e+12,'s^-1'), n=-0.057127, w0=(707000,'J/mol'), E0=(136643,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010222737318967457, var=0.4833412136116934, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
            Total Standard Deviation in ln(k): 1.4194321346238945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
Total Standard Deviation in ln(k): 1.4194321346238945""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
Total Standard Deviation in ln(k): 1.4194321346238945
sensitivities = [{'dA': 1.3537508763975905, 'dE0': 0.0066506426927400815, 'dn': -0.1568988850396585, 'dA_dEa': -16.13212711604639, 'dE0_dEa': 0.5757574752476982, 'dn_dEa': 2.9561117103304286, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}, {'dA': -0.35078083595511655, 'dE0': -0.006590030981614621, 'dn': 0.15635760904123566, 'dA_dEa': 20.365159503102714, 'dE0_dEa': 0.7392996694883667, 'dn_dEa': -3.7477596825324238, 'name': 'O=CNC=O <=> N=COC=O'}]
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N",
    kinetics = ArrheniusBM(A=(7.42131e+10,'s^-1'), n=0.332427, w0=(707000,'J/mol'), E0=(131754,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0006044627176402661, var=1.3355604139234127, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
            Total Standard Deviation in ln(k): 2.318319891761889"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
Total Standard Deviation in ln(k): 2.318319891761889""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
Total Standard Deviation in ln(k): 2.318319891761889
sensitivities = [{'dA': -0.2167625411857682, 'dE0': -0.00564584574657566, 'dn': -0.5521518782862986, 'dA_dEa': 14.033808289736651, 'dE0_dEa': 0.4937703562790749, 'dn_dEa': 10.846842551715733, 'name': 'C2H3NO2 <=> C2H3NO2-2'}, {'dA': 1.4460709670098197, 'dE0': 0.0073753477074844235, 'dn': 0.7302221936281736, 'dA_dEa': -9.961353111411984, 'dE0_dEa': 0.36512956811357866, 'dn_dEa': -7.662954590753998, 'name': 'NC(=N)OC=O <=> O=CNC(=O)N'}]
""",
)

entry(
    index = 22,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(9.35695e+11,'s^-1'), n=0.214198, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.743255396957375, 'dn_dEa': 0.0, 'name': 'N#CC(=N)N1C=C1 <=> N#Cc1ncc[nH]1'}]
""",
)

entry(
    index = 23,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(9.61405e+11,'s^-1'), n=0.233577, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.7382887790244914, 'dn_dEa': 0.0, 'name': 'N=CN1C=C1 <=> c1ncc[nH]1'}]
""",
)

entry(
    index = 24,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(3.83567e+11,'s^-1'), n=0.27432, w0=(707000,'J/mol'), E0=(70700,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.6921455258907361, 'dn_dEa': -0.0, 'name': 'O=CN1C=C1 <=> c1ncco1'}]
""",
)

entry(
    index = 25,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.55603e-17,'s^-1'), n=9.13956, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.73338536715972, var=0.32655979383658124, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C
            Total Standard Deviation in ln(k): 20.576230589316168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 20.576230589316168""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 20.576230589316168
sensitivities = [{'dA': 0.5036844282103048, 'dE0': 1.2799331569540845e-05, 'dn': -0.0009020130914857424, 'dA_dEa': -0.8549218769645481, 'dE0_dEa': 0.6781120226893057, 'dn_dEa': 0.18961739713460712, 'name': 'C3H4N2 <=> C3H4N2-2'}, {'dA': 0.498043182517504, 'dE0': -5.742446855001365e-06, 'dn': 0.00038976710190564664, 'dA_dEa': -0.7299117248643321, 'dE0_dEa': 0.6893749830339604, 'dn_dEa': 0.16092024081801967, 'name': 'C4H3N3 <=> C4H3N3-2'}]
""",
)

entry(
    index = 26,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.92014e+10,'s^-1'), n=1.31782, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'C2H3N3 <=> C2H3N3-2'}]
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.61854e+10,'s^-1'), n=0.947053, w0=(707000,'J/mol'), E0=(429654,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.93992245710974, 'dn_dEa': 0.0, 'name': 'C4H4N2O <=> C4H4N2O-2'}]
""",
)

entry(
    index = 28,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.42792e+11,'s^-1'), n=1.12171, w0=(707000,'J/mol'), E0=(70700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.514512003579724, 'dn_dEa': 0.0, 'name': 'C3H3NO <=> C3H3NO-2'}]
""",
)

entry(
    index = 29,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.48935e+10,'s^-1'), n=1.24936, w0=(707000,'J/mol'), E0=(189635,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.956698770217923, 'dn_dEa': 0.0, 'name': 'C2H2N2O <=> C2H2N2O-2'}]
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.00957e+13,'s^-1'), n=-0.120785, w0=(707000,'J/mol'), E0=(137481,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.3014947348862111, 'dn_dEa': -0.0, 'name': 'C2H4N2O2 <=> C2H4N2O2-2'}]
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.84315e+12,'s^-1'), n=-0.0912511, w0=(707000,'J/mol'), E0=(137560,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330801602, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.782863848537706, 'dn_dEa': -0.0, 'name': 'NC(=N)OC=O <=> O=CNC(=O)N'}]
""",
)

entry(
    index = 32,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.04681e+10,'s^-1'), n=1.21369, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
            Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 1.4040230823618587, 'dn_dEa': 0.0, 'name': 'C4H3N3 <=> C4H3N3-2'}]
""",
)

