#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(110.988,'m^3/(mol*s)'), n=1.49988, w0=(576945,'J/mol'), E0=(15465.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.019948822720939917, var=2.246162810883263, Tref=1000.0, N=137, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 137 training reactions at node Root
    Total Standard Deviation in ln(k): 3.0546600095204206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 137 training reactions at node Root
Total Standard Deviation in ln(k): 3.0546600095204206""",
    longDesc = 
"""
BM rule fitted to 137 training reactions at node Root
Total Standard Deviation in ln(k): 3.0546600095204206
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(884.82,'m^3/(mol*s)'), n=1.24215, w0=(548704,'J/mol'), E0=(56327.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.036618929375089385, var=2.71253636296974, Tref=1000.0, N=76, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 76 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 3.393761825367252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 76 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.393761825367252""",
    longDesc = 
"""
BM rule fitted to 76 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.393761825367252
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(62.2141,'m^3/(mol*s)'), n=1.57163, w0=(612131,'J/mol'), E0=(14423.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008043428188145867, var=2.314465408330227, Tref=1000.0, N=61, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 61 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 3.0700867008716486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 61 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 3.0700867008716486""",
    longDesc = 
"""
BM rule fitted to 61 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 3.0700867008716486
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_Ext-4R-R",
    kinetics = ArrheniusBM(A=(132.852,'m^3/(mol*s)'), n=1.44355, w0=(543092,'J/mol'), E0=(57130.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1162669490050592, var=14.438136852385156, Tref=1000.0, N=49, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R',), comment="""BM rule fitted to 49 training reactions at node Root_1R!H->C_Ext-4R-R
    Total Standard Deviation in ln(k): 10.422192642076714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 49 training reactions at node Root_1R!H->C_Ext-4R-R
Total Standard Deviation in ln(k): 10.422192642076714""",
    longDesc = 
"""
BM rule fitted to 49 training reactions at node Root_1R!H->C_Ext-4R-R
Total Standard Deviation in ln(k): 10.422192642076714
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(5.06544e+13,'m^3/(mol*s)'), n=-1.60273, w0=(548808,'J/mol'), E0=(41081,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30974673560266636, var=41.007441680777, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 13.615990787317209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 13.615990787317209""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 13.615990787317209
""",
)

entry(
    index = 6,
    label = "Root_1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(922.64,'m^3/(mol*s)'), n=1.24025, w0=(568250,'J/mol'), E0=(53979.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004274848215638861, var=2.5390685203379473, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 14 training reactions at node Root_1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 3.205176886553694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.205176886553694""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.205176886553694
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_4R->H",
    kinetics = ArrheniusBM(A=(5402.83,'m^3/(mol*s)'), n=1.15458, w0=(596938,'J/mol'), E0=(64951.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0477072866231589, var=0.2458225151096127, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H->C_4R->H
    Total Standard Deviation in ln(k): 1.1138250617471301"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H->C_4R->H
Total Standard Deviation in ln(k): 1.1138250617471301""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H->C_4R->H
Total Standard Deviation in ln(k): 1.1138250617471301
""",
)

entry(
    index = 8,
    label = "Root_N-1R!H->C_N-4R->H",
    kinetics = ArrheniusBM(A=(34.3465,'m^3/(mol*s)'), n=1.61756, w0=(614425,'J/mol'), E0=(1788.56,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008156786388511824, var=2.270092214989918, Tref=1000.0, N=53, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H',), comment="""BM rule fitted to 53 training reactions at node Root_N-1R!H->C_N-4R->H
    Total Standard Deviation in ln(k): 3.0409937357817585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 53 training reactions at node Root_N-1R!H->C_N-4R->H
Total Standard Deviation in ln(k): 3.0409937357817585""",
    longDesc = 
"""
BM rule fitted to 53 training reactions at node Root_N-1R!H->C_N-4R->H
Total Standard Deviation in ln(k): 3.0409937357817585
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R",
    kinetics = ArrheniusBM(A=(2.17275e+24,'m^3/(mol*s)'), n=-4.64023, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5439384364017564, var=461.36737115577336, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R
    Total Standard Deviation in ln(k): 44.42731429286764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R
Total Standard Deviation in ln(k): 44.42731429286764""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R
Total Standard Deviation in ln(k): 44.42731429286764
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R",
    kinetics = ArrheniusBM(A=(107.54,'m^3/(mol*s)'), n=1.46921, w0=(543359,'J/mol'), E0=(56674,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2305786571017787, var=13.892198757189893, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R',), comment="""BM rule fitted to 46 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R
    Total Standard Deviation in ln(k): 10.564002870689814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R
Total Standard Deviation in ln(k): 10.564002870689814""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R
Total Standard Deviation in ln(k): 10.564002870689814
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_2R!H->C_4R->O",
    kinetics = ArrheniusBM(A=(6.63496e+27,'m^3/(mol*s)'), n=-5.30481, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.758006596954966, var=32.81185557181099, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_4R->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_4R->O
    Total Standard Deviation in ln(k): 13.387989221432699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_4R->O
Total Standard Deviation in ln(k): 13.387989221432699""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_4R->O
Total Standard Deviation in ln(k): 13.387989221432699
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_2R!H->C_N-4R->O",
    kinetics = ArrheniusBM(A=(2.69338e+07,'m^3/(mol*s)'), n=0.0426318, w0=(542500,'J/mol'), E0=(-2245.15,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.781690410563489, var=7.000377717954332, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O
    Total Standard Deviation in ln(k): 9.780782631156653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O
Total Standard Deviation in ln(k): 9.780782631156653""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O
Total Standard Deviation in ln(k): 9.780782631156653
""",
)

entry(
    index = 13,
    label = "Root_1R!H->C_N-2R!H->C_4R->H",
    kinetics = ArrheniusBM(A=(14210.3,'m^3/(mol*s)'), n=1.06643, w0=(583375,'J/mol'), E0=(48221.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006942402741823475, var=0.9857268348599192, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_4R->H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H
    Total Standard Deviation in ln(k): 2.0078199239458105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H
Total Standard Deviation in ln(k): 2.0078199239458105""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H
Total Standard Deviation in ln(k): 2.0078199239458105
""",
)

entry(
    index = 14,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H",
    kinetics = ArrheniusBM(A=(938.023,'m^3/(mol*s)'), n=1.18864, w0=(562200,'J/mol'), E0=(67591,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06901648213777242, var=1.5775585667210101, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H
    Total Standard Deviation in ln(k): 2.6913735133923913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H
Total Standard Deviation in ln(k): 2.6913735133923913""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H
Total Standard Deviation in ln(k): 2.6913735133923913
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H->C_4R->H_2R!H->O",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(612000,'J/mol'), E0=(63724.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O",
    kinetics = ArrheniusBM(A=(3303.78,'m^3/(mol*s)'), n=1.21177, w0=(594786,'J/mol'), E0=(57012.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.010733409560458679, var=0.2404019501332996, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O
    Total Standard Deviation in ln(k): 1.0099060432727496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O
Total Standard Deviation in ln(k): 1.0099060432727496""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O
Total Standard Deviation in ln(k): 1.0099060432727496
""",
)

entry(
    index = 17,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O",
    kinetics = ArrheniusBM(A=(310.459,'m^3/(mol*s)'), n=1.41075, w0=(622808,'J/mol'), E0=(3985.41,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00217738532084826, var=1.3491820820665785, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O
    Total Standard Deviation in ln(k): 2.3340567626636806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O
Total Standard Deviation in ln(k): 2.3340567626636806""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O
Total Standard Deviation in ln(k): 2.3340567626636806
""",
)

entry(
    index = 18,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O",
    kinetics = ArrheniusBM(A=(2.10947,'m^3/(mol*s)'), n=1.87841, w0=(606352,'J/mol'), E0=(16427.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.019916682266462694, var=1.7387102091896054, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O',), comment="""BM rule fitted to 27 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O
    Total Standard Deviation in ln(k): 2.6934888184225336"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O
Total Standard Deviation in ln(k): 2.6934888184225336""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O
Total Standard Deviation in ln(k): 2.6934888184225336
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.68562e+33,'m^3/(mol*s)'), n=-6.96034, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-8.90375239702533, var=455.6672244412005, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R
    Total Standard Deviation in ln(k): 65.1650403812006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R
Total Standard Deviation in ln(k): 65.1650403812006""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R
Total Standard Deviation in ln(k): 65.1650403812006
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S",
    kinetics = ArrheniusBM(A=(3.12126e-13,'m^3/(mol*s)'), n=4.70087, w0=(527000,'J/mol'), E0=(17509.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=10.238614422136449, var=279.3313223037818, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S
    Total Standard Deviation in ln(k): 59.23071623718318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S
Total Standard Deviation in ln(k): 59.23071623718318""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S
Total Standard Deviation in ln(k): 59.23071623718318
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S",
    kinetics = ArrheniusBM(A=(392.285,'m^3/(mol*s)'), n=1.32323, w0=(544102,'J/mol'), E0=(62532.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9012089140319229, var=6.136519187941537, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S',), comment="""BM rule fitted to 44 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S
    Total Standard Deviation in ln(k): 7.230473474978894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S
Total Standard Deviation in ln(k): 7.230473474978894""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S
Total Standard Deviation in ln(k): 7.230473474978894
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.21372e+27,'m^3/(mol*s)'), n=-5.08888, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7330773293589598, var=62.91070125951379, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R
    Total Standard Deviation in ln(k): 17.74271299662356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R
Total Standard Deviation in ln(k): 17.74271299662356""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R
Total Standard Deviation in ln(k): 17.74271299662356
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H",
    kinetics = ArrheniusBM(A=(1.80766e+06,'m^3/(mol*s)'), n=1.76405e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3986168174433896e-07, var=1.078433666146626, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H
    Total Standard Deviation in ln(k): 2.081870835278338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H
Total Standard Deviation in ln(k): 2.081870835278338""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H
Total Standard Deviation in ln(k): 2.081870835278338
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H",
    kinetics = ArrheniusBM(A=(1.03965e+08,'m^3/(mol*s)'), n=0.0639478, w0=(539000,'J/mol'), E0=(-26025.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6545330186471228, var=49.63337137115906, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H
    Total Standard Deviation in ln(k): 18.280668318879233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H
Total Standard Deviation in ln(k): 18.280668318879233""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H
Total Standard Deviation in ln(k): 18.280668318879233
""",
)

entry(
    index = 25,
    label = "Root_1R!H->C_N-2R!H->C_4R->H_Ext-2NOS-R",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(46201.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_4R->H_Ext-2NOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Ext-2NOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Ext-2NOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Ext-2NOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(23588.5,'m^3/(mol*s)'), n=1.06552, w0=(609250,'J/mol'), E0=(60925,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6761713695632989, var=0.41113237262952895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C
    Total Standard Deviation in ln(k): 2.984351249045606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C
Total Standard Deviation in ln(k): 2.984351249045606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C
Total Standard Deviation in ln(k): 2.984351249045606
""",
)

entry(
    index = 27,
    label = "Root_1R!H->C_N-2R!H->C_4R->H_N-Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(55750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_4R->H_N-Sp-2NOS-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_N-Sp-2NOS-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O",
    kinetics = ArrheniusBM(A=(1014.95,'m^3/(mol*s)'), n=1.27928, w0=(578600,'J/mol'), E0=(57860,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04934108255245285, var=1.2460831670347177, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O
    Total Standard Deviation in ln(k): 2.361820152834982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O
Total Standard Deviation in ln(k): 2.361820152834982""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O
Total Standard Deviation in ln(k): 2.361820152834982
""",
)

entry(
    index = 29,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O",
    kinetics = ArrheniusBM(A=(113.479,'m^3/(mol*s)'), n=1.35003, w0=(545800,'J/mol'), E0=(36533.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.051923422251300824, var=0.39032015757806815, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O
    Total Standard Deviation in ln(k): 1.3829312852404396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O
Total Standard Deviation in ln(k): 1.3829312852404396""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O
Total Standard Deviation in ln(k): 1.3829312852404396
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1",
    kinetics = ArrheniusBM(A=(1937.55,'m^3/(mol*s)'), n=1.2703, w0=(604833,'J/mol'), E0=(54671.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.018956926636315957, var=0.21812069796588607, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1
    Total Standard Deviation in ln(k): 0.9839097840348989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1
Total Standard Deviation in ln(k): 0.9839097840348989""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1
Total Standard Deviation in ln(k): 0.9839097840348989
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_N-2CN-u1",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_N-2CN-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_N-2CN-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_N-2CN-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_N-2CN-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi",
    kinetics = ArrheniusBM(A=(183.784,'m^3/(mol*s)'), n=1.53352, w0=(616900,'J/mol'), E0=(3825.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.020934905525660494, var=0.4342346152673807, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 1.3736501260715168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi
Total Standard Deviation in ln(k): 1.3736501260715168""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi
Total Standard Deviation in ln(k): 1.3736501260715168
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi",
    kinetics = ArrheniusBM(A=(233807,'m^3/(mol*s)'), n=0.440784, w0=(642500,'J/mol'), E0=(107629,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6128014920471064, var=3.3112778589447784, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 5.18770200907973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi
Total Standard Deviation in ln(k): 5.18770200907973""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi
Total Standard Deviation in ln(k): 5.18770200907973
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C",
    kinetics = ArrheniusBM(A=(42.92,'m^3/(mol*s)'), n=1.42345, w0=(627423,'J/mol'), E0=(17160.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09684615220645305, var=0.8640800788185798, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C
    Total Standard Deviation in ln(k): 2.1068517301700886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C
Total Standard Deviation in ln(k): 2.1068517301700886""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C
Total Standard Deviation in ln(k): 2.1068517301700886
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.37469,'m^3/(mol*s)'), n=1.94332, w0=(586786,'J/mol'), E0=(16559.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00666421519637062, var=1.9699416352685581, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C
    Total Standard Deviation in ln(k): 2.830482344730366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 2.830482344730366""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C
Total Standard Deviation in ln(k): 2.830482344730366
""",
)

entry(
    index = 36,
    label = "Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_Sp-5R!H#4R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(515000,'J/mol'), E0=(39525.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0",
    kinetics = ArrheniusBM(A=(276.39,'m^3/(mol*s)'), n=1.37219, w0=(537375,'J/mol'), E0=(64280.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0040884181099603, var=4.329900964940567, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0',), comment="""BM rule fitted to 32 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0
    Total Standard Deviation in ln(k): 6.694370982345792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0
Total Standard Deviation in ln(k): 6.694370982345792""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0
Total Standard Deviation in ln(k): 6.694370982345792
""",
)

entry(
    index = 39,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0",
    kinetics = ArrheniusBM(A=(0.523029,'m^3/(mol*s)'), n=1.96149, w0=(562042,'J/mol'), E0=(-2713.15,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3860685190007465, var=20.13255742655902, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0',), comment="""BM rule fitted to 12 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0
    Total Standard Deviation in ln(k): 9.965131074099705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0
Total Standard Deviation in ln(k): 9.965131074099705""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0
Total Standard Deviation in ln(k): 9.965131074099705
""",
)

entry(
    index = 40,
    label = "Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(4.86796e+38,'m^3/(mol*s)'), n=-8.5123, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-11.615596275987219, var=19.48985781656424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 38.03528317888868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 38.03528317888868""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 38.03528317888868
""",
)

entry(
    index = 41,
    label = "Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(19.2398,'m^3/(mol*s)'), n=2.50102, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.27916e+06,'m^3/(mol*s)'), n=-3.7648e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9639738002758667, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R
    Total Standard Deviation in ln(k): 1.9682923503688117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R
Total Standard Deviation in ln(k): 1.9682923503688117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R
Total Standard Deviation in ln(k): 1.9682923503688117
""",
)

entry(
    index = 43,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.83511e+08,'m^3/(mol*s)'), n=-0.444996, w0=(539000,'J/mol'), E0=(19251.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12991208638309779, var=25.84400843057048, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R
    Total Standard Deviation in ln(k): 10.517884530659062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R
Total Standard Deviation in ln(k): 10.517884530659062""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R
Total Standard Deviation in ln(k): 10.517884530659062
""",
)

entry(
    index = 44,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_4C-u1",
    kinetics = ArrheniusBM(A=(2.64758,'m^3/(mol*s)'), n=2.9919, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_N-4C-u1",
    kinetics = ArrheniusBM(A=(0.011478,'m^3/(mol*s)'), n=3.34181, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_2NOS->N",
    kinetics = ArrheniusBM(A=(720,'m^3/(mol*s)'), n=1.5, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_2NOS->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_2NOS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_2NOS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_2NOS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_N-2NOS->N",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(642000,'J/mol'), E0=(64200,'J/mol'), Tmin=(300,'K'), Tmax=(1000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_N-2NOS->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_N-2NOS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_N-2NOS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_4R->H_Sp-2NOS-1C_N-2NOS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1",
    kinetics = ArrheniusBM(A=(228.987,'m^3/(mol*s)'), n=1.42089, w0=(577333,'J/mol'), E0=(57733.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05487466182504174, var=0.6944264733105656, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1
    Total Standard Deviation in ln(k): 1.8084669826740656"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1
Total Standard Deviation in ln(k): 1.8084669826740656""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1
Total Standard Deviation in ln(k): 1.8084669826740656
""",
)

entry(
    index = 49,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(9471.03,'m^3/(mol*s)'), n=1.06688, w0=(580500,'J/mol'), E0=(58050,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.44786487945355996, var=2.3276605709388356, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1
    Total Standard Deviation in ln(k): 4.183847303032689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1
Total Standard Deviation in ln(k): 4.183847303032689""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1
Total Standard Deviation in ln(k): 4.183847303032689
""",
)

entry(
    index = 50,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=1.87, w0=(566000,'J/mol'), E0=(56600,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_Sp-2NOS-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_Sp-2NOS-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(100.519,'m^3/(mol*s)'), n=1.35508, w0=(540750,'J/mol'), E0=(26523.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.052107872471350736, var=0.5035092234267061, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C
    Total Standard Deviation in ln(k): 1.553451913472127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 1.553451913472127""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 1.553451913472127
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N",
    kinetics = ArrheniusBM(A=(587.901,'m^3/(mol*s)'), n=1.41727, w0=(618000,'J/mol'), E0=(45060,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06640401910100215, var=0.26094188700249565, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N
    Total Standard Deviation in ln(k): 1.190912488846253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N
Total Standard Deviation in ln(k): 1.190912488846253""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N
Total Standard Deviation in ln(k): 1.190912488846253
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N",
    kinetics = ArrheniusBM(A=(10114.1,'m^3/(mol*s)'), n=1.0662, w0=(591667,'J/mol'), E0=(59166.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04115737528167287, var=0.520316344789736, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N
    Total Standard Deviation in ln(k): 1.5494851767639202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N
Total Standard Deviation in ln(k): 1.5494851767639202""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N
Total Standard Deviation in ln(k): 1.5494851767639202
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C",
    kinetics = ArrheniusBM(A=(1882.2,'m^3/(mol*s)'), n=1.22788, w0=(650357,'J/mol'), E0=(31983.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07003934365378406, var=3.360364171739336, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C
    Total Standard Deviation in ln(k): 3.850917483522595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C
Total Standard Deviation in ln(k): 3.850917483522595""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C
Total Standard Deviation in ln(k): 3.850917483522595
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C",
    kinetics = ArrheniusBM(A=(127.957,'m^3/(mol*s)'), n=1.58109, w0=(598885,'J/mol'), E0=(2223.86,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09597807114861825, var=0.626058882528767, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C
    Total Standard Deviation in ln(k): 1.8273751651076473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C
Total Standard Deviation in ln(k): 1.8273751651076473""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C
Total Standard Deviation in ln(k): 1.8273751651076473
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1",
    kinetics = ArrheniusBM(A=(387365,'m^3/(mol*s)'), n=0.299183, w0=(653000,'J/mol'), E0=(107293,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8258682422240214, var=2.717875821208586, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1
    Total Standard Deviation in ln(k): 5.380048350868628"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1
Total Standard Deviation in ln(k): 5.380048350868628""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1
Total Standard Deviation in ln(k): 5.380048350868628
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 58,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(4.36359e+07,'m^3/(mol*s)'), n=-0.0300002, w0=(655500,'J/mol'), E0=(42573.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9951627558956904, var=8.207568253226448, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 8.243745152850435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 8.243745152850435""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 8.243745152850435
""",
)

entry(
    index = 59,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(34.4305,'m^3/(mol*s)'), n=1.44661, w0=(533833,'J/mol'), E0=(29064.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.040007632077037274, var=0.3494806738783088, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 1.285658728542547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.285658728542547""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.285658728542547
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N",
    kinetics = ArrheniusBM(A=(29.5049,'m^3/(mol*s)'), n=1.59245, w0=(592750,'J/mol'), E0=(19598.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.069596137450727, var=1.5113316212548111, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N
    Total Standard Deviation in ln(k): 2.6394103572058367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N
Total Standard Deviation in ln(k): 2.6394103572058367""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N
Total Standard Deviation in ln(k): 2.6394103572058367
""",
)

entry(
    index = 61,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N",
    kinetics = ArrheniusBM(A=(0.615829,'m^3/(mol*s)'), n=1.96425, w0=(571875,'J/mol'), E0=(75296.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3104586047403263, var=0.9595215316593622, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N
    Total Standard Deviation in ln(k): 2.743788397345642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N
Total Standard Deviation in ln(k): 2.743788397345642""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N
Total Standard Deviation in ln(k): 2.743788397345642
""",
)

entry(
    index = 62,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6258.48,'m^3/(mol*s)'), n=0.685875, w0=(535413,'J/mol'), E0=(9457,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0809408668346672, var=9.167145411090761, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R',), comment="""BM rule fitted to 23 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 8.785727189536344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.785727189536344""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.785727189536344
""",
)

entry(
    index = 63,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R",
    kinetics = ArrheniusBM(A=(1.20181e+06,'m^3/(mol*s)'), n=0.0278834, w0=(539000,'J/mol'), E0=(40020.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3317664383097431, var=0.19245514395310417, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R
    Total Standard Deviation in ln(k): 1.7130554769296356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R
Total Standard Deviation in ln(k): 1.7130554769296356""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R
Total Standard Deviation in ln(k): 1.7130554769296356
""",
)

entry(
    index = 64,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_2R!H->S",
    kinetics = ArrheniusBM(A=(979000,'m^3/(mol*s)'), n=0, w0=(537500,'J/mol'), E0=(38210.6,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_2R!H->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_2R!H->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_2R!H->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_2R!H->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S",
    kinetics = ArrheniusBM(A=(7.84834,'m^3/(mol*s)'), n=1.90173, w0=(545400,'J/mol'), E0=(35453.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.038120461078776126, var=0.259461760369396, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S
    Total Standard Deviation in ln(k): 1.1169397588469092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S
Total Standard Deviation in ln(k): 1.1169397588469092""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S
Total Standard Deviation in ln(k): 1.1169397588469092
""",
)

entry(
    index = 66,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.20565,'m^3/(mol*s)'), n=2.49959, w0=(563000,'J/mol'), E0=(2828.85,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(45.1779,'m^3/(mol*s)'), n=1.37765, w0=(563000,'J/mol'), E0=(20495.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14386814426607, var=17.63223221601489, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 8.77951101926173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.77951101926173""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.77951101926173
""",
)

entry(
    index = 68,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(92345.7,'J/mol'), Tmin=(700,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Sp-2R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(2.6e+09,'m^3/(mol*s)'), n=-1.26, w0=(551500,'J/mol'), E0=(34913.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_N-Sp-2R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.34628,'m^3/(mol*s)'), n=2.68412, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_4CHN->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.02e+06,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(9.86819e+12,'m^3/(mol*s)'), n=-1.83383, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.910329122522753, var=17.605006546960293, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 15.723916408732457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 15.723916408732457""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 15.723916408732457
""",
)

entry(
    index = 74,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(0.352401,'m^3/(mol*s)'), n=2.99533, w0=(539000,'J/mol'), E0=(47279.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(3.6,'m^3/(mol*s)'), n=2, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_Sp-2NOS-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_Sp-2NOS-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(178.214,'m^3/(mol*s)'), n=1.42089, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 77,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(500,'m^3/(mol*s)'), n=1.5, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_Sp-2NOS-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_Sp-2NOS-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_N-Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_N-Sp-2NOS-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_N-Sp-2NOS-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_N-4O-u1_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R",
    kinetics = ArrheniusBM(A=(1713.08,'m^3/(mol*s)'), n=1.04631, w0=(540750,'J/mol'), E0=(61802.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6075970314782776, var=0.6553537765114736, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R
    Total Standard Deviation in ln(k): 3.149537412505626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R
Total Standard Deviation in ln(k): 3.149537412505626""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R
Total Standard Deviation in ln(k): 3.149537412505626
""",
)

entry(
    index = 80,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_4CN->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_4CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_4CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_4CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_4CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_N-4CN->N",
    kinetics = ArrheniusBM(A=(0.81,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(54700,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_N-4CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_N-4CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_N-4CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_N-4CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1367.9,'m^3/(mol*s)'), n=1.28344, w0=(602750,'J/mol'), E0=(60275,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3312627342341653, var=0.027192120539529588, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 1.1628999139155172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 1.1628999139155172""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 1.1628999139155172
""",
)

entry(
    index = 83,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(648500,'J/mol'), E0=(59319.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi",
    kinetics = ArrheniusBM(A=(13116.2,'m^3/(mol*s)'), n=1.06552, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009683765652408772, var=0.10971138960797763, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 0.6883536488758378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi
Total Standard Deviation in ln(k): 0.6883536488758378""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi
Total Standard Deviation in ln(k): 0.6883536488758378
""",
)

entry(
    index = 85,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_N-Sp-2C-1BrClFINOPSSi",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(545000,'J/mol'), E0=(54500,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_N-Sp-2C-1BrClFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_N-Sp-2C-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_N-Sp-2C-1BrClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_N-Sp-2C-1BrClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1",
    kinetics = ArrheniusBM(A=(266.42,'m^3/(mol*s)'), n=1.41367, w0=(659100,'J/mol'), E0=(15617.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.476047800147832, var=3.882590597283919, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1
    Total Standard Deviation in ln(k): 7.6588510262119085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1
Total Standard Deviation in ln(k): 7.6588510262119085""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1
Total Standard Deviation in ln(k): 7.6588510262119085
""",
)

entry(
    index = 87,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1",
    kinetics = ArrheniusBM(A=(12844.6,'m^3/(mol*s)'), n=1.04554, w0=(628500,'J/mol'), E0=(62850,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6337605004670377, var=7.489199349058056, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1
    Total Standard Deviation in ln(k): 9.591164397569802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1
Total Standard Deviation in ln(k): 9.591164397569802""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1
Total Standard Deviation in ln(k): 9.591164397569802
""",
)

entry(
    index = 88,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R",
    kinetics = ArrheniusBM(A=(15.1785,'m^3/(mol*s)'), n=1.91136, w0=(603700,'J/mol'), E0=(2803.92,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4660309461628993, var=0.6705461821263063, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R
    Total Standard Deviation in ln(k): 2.8125471189925215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R
Total Standard Deviation in ln(k): 2.8125471189925215""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R
Total Standard Deviation in ln(k): 2.8125471189925215
""",
)

entry(
    index = 89,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1",
    kinetics = ArrheniusBM(A=(211.933,'m^3/(mol*s)'), n=1.42089, w0=(595875,'J/mol'), E0=(59587.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05487466192466684, var=0.2135346724240081, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1
    Total Standard Deviation in ln(k): 1.0642603451673014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1
Total Standard Deviation in ln(k): 1.0642603451673014""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1
Total Standard Deviation in ln(k): 1.0642603451673014
""",
)

entry(
    index = 90,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1",
    kinetics = ArrheniusBM(A=(2341.31,'m^3/(mol*s)'), n=1.23375, w0=(595875,'J/mol'), E0=(53086.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07415205097242003, var=0.2919329859412488, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1
    Total Standard Deviation in ln(k): 1.2694865518499208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1
Total Standard Deviation in ln(k): 1.2694865518499208""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1
Total Standard Deviation in ln(k): 1.2694865518499208
""",
)

entry(
    index = 91,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R",
    kinetics = ArrheniusBM(A=(7.0481e+12,'m^3/(mol*s)'), n=-1.90371, w0=(684500,'J/mol'), E0=(124001,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5179182833961141, var=17.419168698346834, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R
    Total Standard Deviation in ln(k): 9.668320194682368"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R
Total Standard Deviation in ln(k): 9.668320194682368""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R
Total Standard Deviation in ln(k): 9.668320194682368
""",
)

entry(
    index = 92,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->N",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->N",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1",
    kinetics = ArrheniusBM(A=(5.06664e+07,'m^3/(mol*s)'), n=-0.0312498, w0=(655500,'J/mol'), E0=(47727,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.992383990457577, var=7.28007565550926, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1
    Total Standard Deviation in ln(k): 7.902526180397997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1
Total Standard Deviation in ln(k): 7.902526180397997""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1
Total Standard Deviation in ln(k): 7.902526180397997
""",
)

entry(
    index = 97,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_N-4CNS-u1",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_N-4CNS-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_N-4CNS-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_N-4CNS-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_N-4CNS-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N",
    kinetics = ArrheniusBM(A=(34.41,'m^3/(mol*s)'), n=1.44661, w0=(544000,'J/mol'), E0=(54400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43780050013999694, var=0.5999111817527254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N
    Total Standard Deviation in ln(k): 2.6527474307051118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N
Total Standard Deviation in ln(k): 2.6527474307051118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N
Total Standard Deviation in ln(k): 2.6527474307051118
""",
)

entry(
    index = 99,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->N",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(513500,'J/mol'), E0=(42507.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R",
    kinetics = ArrheniusBM(A=(44.6712,'m^3/(mol*s)'), n=1.62801, w0=(610875,'J/mol'), E0=(25269,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.619295161377688, var=5.687851574571153, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R
    Total Standard Deviation in ln(k): 6.337154207222094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R
Total Standard Deviation in ln(k): 6.337154207222094""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R
Total Standard Deviation in ln(k): 6.337154207222094
""",
)

entry(
    index = 101,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1",
    kinetics = ArrheniusBM(A=(116.606,'m^3/(mol*s)'), n=1.35374, w0=(594500,'J/mol'), E0=(42446.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07505693938603511, var=0.5657537030769392, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1
    Total Standard Deviation in ln(k): 1.6964788544158005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1
Total Standard Deviation in ln(k): 1.6964788544158005""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1
Total Standard Deviation in ln(k): 1.6964788544158005
""",
)

entry(
    index = 102,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_N-2NO-u1",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1",
    kinetics = ArrheniusBM(A=(0.000312293,'m^3/(mol*s)'), n=2.90354, w0=(587833,'J/mol'), E0=(53849,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1230320030307755, var=0.5384824975894967, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1
    Total Standard Deviation in ln(k): 1.7802276338704983"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1
Total Standard Deviation in ln(k): 1.7802276338704983""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1
Total Standard Deviation in ln(k): 1.7802276338704983
""",
)

entry(
    index = 104,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_N-2NO-u1",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C",
    kinetics = ArrheniusBM(A=(277.167,'m^3/(mol*s)'), n=1.45641, w0=(539000,'J/mol'), E0=(56513.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15946548885041142, var=3.4605667761100647, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C
    Total Standard Deviation in ln(k): 4.129995267655812"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C
Total Standard Deviation in ln(k): 4.129995267655812""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C
Total Standard Deviation in ln(k): 4.129995267655812
""",
)

entry(
    index = 106,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C",
    kinetics = ArrheniusBM(A=(7332.53,'m^3/(mol*s)'), n=0.657806, w0=(534417,'J/mol'), E0=(7098.69,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4974942151411073, var=12.206531220215924, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C',), comment="""BM rule fitted to 18 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C
    Total Standard Deviation in ln(k): 10.766660931338013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C
Total Standard Deviation in ln(k): 10.766660931338013""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C
Total Standard Deviation in ln(k): 10.766660931338013
""",
)

entry(
    index = 107,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(0.000446327,'m^3/(mol*s)'), n=2.98472, w0=(539000,'J/mol'), E0=(26976,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(2.86e+09,'m^3/(mol*s)'), n=-1.1, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R",
    kinetics = ArrheniusBM(A=(7.68278,'m^3/(mol*s)'), n=1.90504, w0=(547000,'J/mol'), E0=(35905.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3190536272635911, var=0.21442568177902221, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R
    Total Standard Deviation in ln(k): 1.729957324969327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R
Total Standard Deviation in ln(k): 1.729957324969327""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R
Total Standard Deviation in ln(k): 1.729957324969327
""",
)

entry(
    index = 110,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_N-Sp-5CO-4R",
    kinetics = ArrheniusBM(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_N-Sp-5CO-4R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_N-Sp-5CO-4R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_N-Sp-5CO-4R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_N-Sp-5CO-4R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(86.8554,'m^3/(mol*s)'), n=1.32534, w0=(563000,'J/mol'), E0=(4758.22,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.020959504917343545, var=17.395798088654246, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C
    Total Standard Deviation in ln(k): 8.41406531530701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 8.41406531530701""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 8.41406531530701
""",
)

entry(
    index = 112,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_N-Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(602200,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(40463,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_N-Sp-6R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_N-Sp-6R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_4C-u1",
    kinetics = ArrheniusBM(A=(1.15e+07,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_N-4C-u1",
    kinetics = ArrheniusBM(A=(0.191068,'m^3/(mol*s)'), n=2.28136, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-4R->O_N-4CHN->H_Ext-1C-R_Sp-5R!H-1C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C_Ext-2NOS-R",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C_Ext-2NOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C_Ext-2NOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C_Ext-2NOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_4CNO->O_4O-u1_N-Sp-2NOS-1C_Ext-2NOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_4CN->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_4CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_4CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_4CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_4CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_N-4CN->N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(47358.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_N-4CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_N-4CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_N-4CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-Sp-2NOS-1C_Ext-2NOS-R_N-4CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_Sp-2N-1N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_Sp-2N-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_Sp-2N-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_Sp-2N-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_Sp-2N-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_N-Sp-2N-1N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(671000,'J/mol'), E0=(67100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_N-Sp-2N-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_N-Sp-2N-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_N-Sp-2N-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->N_1BrClFINOPSSi->N_N-Sp-2N-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(400,'m^3/(mol*s)'), n=1.5, w0=(564000,'J/mol'), E0=(56400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(666000,'J/mol'), E0=(66600,'J/mol'), Tmin=(295,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->N_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.41468e+08,'m^3/(mol*s)'), n=-0.287748, w0=(679500,'J/mol'), E0=(39776.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8677516935997125, var=3.3515988232698968, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 5.85042378949206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 5.85042378949206""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 5.85042378949206
""",
)

entry(
    index = 124,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(9.04e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(573833,'J/mol'), E0=(21511.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03872283658228287, var=0.003687235162771551, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 0.2190263021681399"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 0.2190263021681399""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 0.2190263021681399
""",
)

entry(
    index = 127,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(3.06823e-33,'m^3/(mol*s)'), n=11.5608, w0=(648500,'J/mol'), E0=(-37786,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1311443344629586, var=3.4442370952847847, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 9.075152857245785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 9.075152857245785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 9.075152857245785
""",
)

entry(
    index = 128,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(200.038,'m^3/(mol*s)'), n=1.42089, w0=(573833,'J/mol'), E0=(57383.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054874661098006004, var=0.36033975866889256, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 1.3412845505876048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 1.3412845505876048""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 1.3412845505876048
""",
)

entry(
    index = 129,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(662000,'J/mol'), E0=(66200,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1",
    kinetics = ArrheniusBM(A=(940.642,'m^3/(mol*s)'), n=1.34001, w0=(611833,'J/mol'), E0=(50491.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15971084273790068, var=0.37565381576566487, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1
    Total Standard Deviation in ln(k): 1.6299977651045376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1
Total Standard Deviation in ln(k): 1.6299977651045376""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1
Total Standard Deviation in ln(k): 1.6299977651045376
""",
)

entry(
    index = 131,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_N-2NO-u1",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_5R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_5R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=-0.34, w0=(684500,'J/mol'), E0=(61174.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_N-5R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(1.80446e+07,'m^3/(mol*s)'), n=-0.0937499, w0=(655500,'J/mol'), E0=(-21178.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.980224981662296e-09, var=3.2252654385801245, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R
    Total Standard Deviation in ln(k): 3.600308546438853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R
Total Standard Deviation in ln(k): 3.600308546438853""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R
Total Standard Deviation in ln(k): 3.600308546438853
""",
)

entry(
    index = 135,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_Sp-2C-1N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(553500,'J/mol'), E0=(55350,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_N-Sp-2C-1N",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_N-Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_N-Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_5R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(24711.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(24.3822,'m^3/(mol*s)'), n=1.74624, w0=(615000,'J/mol'), E0=(4836.05,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06763263468134857, var=0.8943979206627513, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N
    Total Standard Deviation in ln(k): 2.0658615974961876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N
Total Standard Deviation in ln(k): 2.0658615974961876""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N
Total Standard Deviation in ln(k): 2.0658615974961876
""",
)

entry(
    index = 139,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi",
    kinetics = ArrheniusBM(A=(97.18,'m^3/(mol*s)'), n=1.38035, w0=(581125,'J/mol'), E0=(36551.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11740613771597475, var=0.9685448374036849, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi
    Total Standard Deviation in ln(k): 2.2679438188850685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi
Total Standard Deviation in ln(k): 2.2679438188850685""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi
Total Standard Deviation in ln(k): 2.2679438188850685
""",
)

entry(
    index = 140,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(648000,'J/mol'), E0=(64800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(0.00010394,'m^3/(mol*s)'), n=3.02774, w0=(562750,'J/mol'), E0=(47277.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8568478925825855, var=0.083327900484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 2.73158245570468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 2.73158245570468""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 2.73158245570468
""",
)

entry(
    index = 142,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(638000,'J/mol'), E0=(77381.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R",
    kinetics = ArrheniusBM(A=(2.76483,'m^3/(mol*s)'), n=1.98276, w0=(539000,'J/mol'), E0=(-8474.87,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04521652769004133, var=1.8376785452849425, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R
    Total Standard Deviation in ln(k): 2.8312483384361813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R
Total Standard Deviation in ln(k): 2.8312483384361813""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R
Total Standard Deviation in ln(k): 2.8312483384361813
""",
)

entry(
    index = 144,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_N-Sp-5CO-4R",
    kinetics = ArrheniusBM(A=(0.0055536,'m^3/(mol*s)'), n=2.98335, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_N-Sp-5CO-4R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_N-Sp-5CO-4R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_N-Sp-5CO-4R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_N-Sp-5CO-4R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(138228,'m^3/(mol*s)'), n=0.328051, w0=(533000,'J/mol'), E0=(53300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09427738490050666, var=1.5003652371786114, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.6924657587950356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6924657587950356""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6924657587950356
""",
)

entry(
    index = 146,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C",
    kinetics = ArrheniusBM(A=(13001,'m^3/(mol*s)'), n=0.616156, w0=(537833,'J/mol'), E0=(22742.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7394739601311657, var=2.987848711249721, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C
    Total Standard Deviation in ln(k): 5.323238489269965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C
Total Standard Deviation in ln(k): 5.323238489269965""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C
Total Standard Deviation in ln(k): 5.323238489269965
""",
)

entry(
    index = 147,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_N-4R->C",
    kinetics = ArrheniusBM(A=(7.19e-07,'m^3/(mol*s)'), n=3.13, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O",
    kinetics = ArrheniusBM(A=(7.72436,'m^3/(mol*s)'), n=1.90406, w0=(555000,'J/mol'), E0=(55500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24698307808363243, var=0.05025213467874637, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O
    Total Standard Deviation in ln(k): 1.0699617175486948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O
Total Standard Deviation in ln(k): 1.0699617175486948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O
Total Standard Deviation in ln(k): 1.0699617175486948
""",
)

entry(
    index = 149,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O",
    kinetics = ArrheniusBM(A=(0.923506,'m^3/(mol*s)'), n=2.28841, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7318907322076494, var=0.49165066501919524, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O
    Total Standard Deviation in ln(k): 3.2445976803590875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O
Total Standard Deviation in ln(k): 3.2445976803590875""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O
Total Standard Deviation in ln(k): 3.2445976803590875
""",
)

entry(
    index = 150,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.36084e+07,'m^3/(mol*s)'), n=-0.614171, w0=(563000,'J/mol'), E0=(39269.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07593134585196257, var=21.253437688878638, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 9.432901836334837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 9.432901836334837""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 9.432901836334837
""",
)

entry(
    index = 151,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.77931,'m^3/(mol*s)'), n=2.03017, w0=(563000,'J/mol'), E0=(15146.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4563200164724831, var=6.162975822039156e-33, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.1465327047047316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.1465327047047316""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.1465327047047316
""",
)

entry(
    index = 152,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R",
    kinetics = ArrheniusBM(A=(1.89499e+08,'m^3/(mol*s)'), n=-0.346565, w0=(679500,'J/mol'), E0=(38476.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1578984580421725, var=4.595591047124435, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R
    Total Standard Deviation in ln(k): 7.206909289886282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R
Total Standard Deviation in ln(k): 7.206909289886282""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R
Total Standard Deviation in ln(k): 7.206909289886282
""",
)

entry(
    index = 153,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(548000,'J/mol'), E0=(31955.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0426036023134155, var=0.11276809873671895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N
    Total Standard Deviation in ln(k): 3.2928163591177713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 3.2928163591177713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 3.2928163591177713
""",
)

entry(
    index = 154,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(625500,'J/mol'), E0=(26705.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_2NO->N",
    kinetics = ArrheniusBM(A=(0.0294,'m^3/(mol*s)'), n=2.69, w0=(662000,'J/mol'), E0=(33464.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(635000,'J/mol'), E0=(6270.39,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N",
    kinetics = ArrheniusBM(A=(178.214,'m^3/(mol*s)'), n=1.42089, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 158,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(625500,'J/mol'), E0=(55947.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(323.865,'m^3/(mol*s)'), n=1.46107, w0=(586750,'J/mol'), E0=(42728,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23284945485790864, var=0.6476388655306268, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 2.1983797414238784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 2.1983797414238784""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 2.1983797414238784
""",
)

entry(
    index = 160,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(662000,'J/mol'), E0=(47976.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS",
    kinetics = ArrheniusBM(A=(7.38113e+07,'m^3/(mol*s)'), n=-8.07774e-08, w0=(655500,'J/mol'), E0=(1088.46,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06280608228446091, var=6.8952486502763435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS
    Total Standard Deviation in ln(k): 5.421999069670699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS
Total Standard Deviation in ln(k): 5.421999069670699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS
Total Standard Deviation in ln(k): 5.421999069670699
""",
)

entry(
    index = 162,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS",
    kinetics = ArrheniusBM(A=(1.12829e+07,'m^3/(mol*s)'), n=-0.125, w0=(655500,'J/mol'), E0=(6223.54,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.020226109195674993, var=1.3477513771929206, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS
    Total Standard Deviation in ln(k): 2.3781703435775885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS
Total Standard Deviation in ln(k): 2.3781703435775885""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS
Total Standard Deviation in ln(k): 2.3781703435775885
""",
)

entry(
    index = 163,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4N",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(13374.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N",
    kinetics = ArrheniusBM(A=(30.945,'m^3/(mol*s)'), n=1.66369, w0=(623250,'J/mol'), E0=(10593.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1931314392317747, var=7.293392619087761, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N
    Total Standard Deviation in ln(k): 10.924424563505077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N
Total Standard Deviation in ln(k): 10.924424563505077""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N
Total Standard Deviation in ln(k): 10.924424563505077
""",
)

entry(
    index = 165,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(81.7183,'m^3/(mol*s)'), n=1.38035, w0=(550250,'J/mol'), E0=(14285.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6204493662846748, var=3.9540263770573922, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 5.545280338111078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 5.545280338111078""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 5.545280338111078
""",
)

entry(
    index = 166,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1222.75,'m^3/(mol*s)'), n=1.08731, w0=(612000,'J/mol'), E0=(51891.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.880107590500096, var=0.27344860374733626, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 3.2596479531592055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 3.2596479531592055""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 3.2596479531592055
""",
)

entry(
    index = 167,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_2NO->N",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(601500,'J/mol'), E0=(75336.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->N_2NO-u1_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(0.00384267,'m^3/(mol*s)'), n=2.98197, w0=(539000,'J/mol'), E0=(32080.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-5CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(18531.3,'m^3/(mol*s)'), n=0.90285, w0=(539000,'J/mol'), E0=(70355,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48292031656078577, var=0.03443159742027864, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R
    Total Standard Deviation in ln(k): 1.5853613214113713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R
Total Standard Deviation in ln(k): 1.5853613214113713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R
Total Standard Deviation in ln(k): 1.5853613214113713
""",
)

entry(
    index = 171,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_5CO->O",
    kinetics = ArrheniusBM(A=(241000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O",
    kinetics = ArrheniusBM(A=(127675,'m^3/(mol*s)'), n=0.374915, w0=(532143,'J/mol'), E0=(53214.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10774558719433884, var=1.1417378960158642, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O
    Total Standard Deviation in ln(k): 2.4128198063882467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O
Total Standard Deviation in ln(k): 2.4128198063882467""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O
Total Standard Deviation in ln(k): 2.4128198063882467
""",
)

entry(
    index = 173,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_Sp-5CCOO=4C",
    kinetics = ArrheniusBM(A=(4.47472e-06,'m^3/(mol*s)'), n=2.9381, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_Sp-5CCOO=4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_Sp-5CCOO=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_Sp-5CCOO=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_Sp-5CCOO=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C",
    kinetics = ArrheniusBM(A=(12936.9,'m^3/(mol*s)'), n=0.61869, w0=(537688,'J/mol'), E0=(25042,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5395986851008143, var=2.162290357556704, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C
    Total Standard Deviation in ln(k): 4.303684062760698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C
Total Standard Deviation in ln(k): 4.303684062760698""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C
Total Standard Deviation in ln(k): 4.303684062760698
""",
)

entry(
    index = 175,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_2CN->N",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_2CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_2CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_2CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_2CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_N-2CN->N",
    kinetics = ArrheniusBM(A=(2.89e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_N-2CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_N-2CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_N-2CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_5CO->O_N-2CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.00205123,'m^3/(mol*s)'), n=3.00966, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_N-2R!H->S_Sp-5CO-4R_N-5CO->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(416.476,'m^3/(mol*s)'), n=0.963194, w0=(563000,'J/mol'), E0=(15659.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2888722218320057, var=87.3358806715488, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 19.460794242494874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 19.460794242494874""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 19.460794242494874
""",
)

entry(
    index = 179,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(2.11547e+08,'m^3/(mol*s)'), n=-0.313028, w0=(679500,'J/mol'), E0=(76755.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12167865343175763, var=0.6437215165799257, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0
    Total Standard Deviation in ln(k): 1.914169472146607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 1.914169472146607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 1.914169472146607
""",
)

entry(
    index = 180,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(5.7209e+06,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(20296,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_N-5R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(39565.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_2N-u1",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_2NO->N",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(625500,'J/mol'), E0=(52128.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_5R!H->C",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56853,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_Sp-5R!H=4CCNNSS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.85561e+07,'m^3/(mol*s)'), n=-0.375, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.06912283083491383, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.5270693322083513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513
""",
)

entry(
    index = 190,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56999.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS",
    kinetics = ArrheniusBM(A=(3.40826e+06,'m^3/(mol*s)'), n=-2.28069e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 192,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_N-Sp-5R!H-4CNS",
    kinetics = ArrheniusBM(A=(1.20333e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_N-Sp-5R!H-4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_N-Sp-5R!H-4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_N-Sp-5R!H-4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_N-Sp-5R!H-4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(648000,'J/mol'), E0=(54170.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_N-1BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(17330.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_N-1BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_N-1BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_Ext-4N-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4N_N-1BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_2NO->N",
    kinetics = ArrheniusBM(A=(0.46,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(589000,'J/mol'), E0=(45404.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_2NO->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(625500,'J/mol'), E0=(51859.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(35268.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->N_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(85952.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_Sp-6R!H=1C_Sp-5CO-4R_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R",
    kinetics = ArrheniusBM(A=(472376,'m^3/(mol*s)'), n=0.0899387, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.957511192532731, var=0.3089571360946666, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R
    Total Standard Deviation in ln(k): 3.520117213485219"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R
Total Standard Deviation in ln(k): 3.520117213485219""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R
Total Standard Deviation in ln(k): 3.520117213485219
""",
)

entry(
    index = 201,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R",
    kinetics = ArrheniusBM(A=(41408.2,'m^3/(mol*s)'), n=0.611132, w0=(527000,'J/mol'), E0=(52700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1446833650040144, var=1.680093987116231, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R
    Total Standard Deviation in ln(k): 2.9620323671368127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R
Total Standard Deviation in ln(k): 2.9620323671368127""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R
Total Standard Deviation in ln(k): 2.9620323671368127
""",
)

entry(
    index = 202,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_N-Sp-5C-4R",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_N-Sp-5C-4R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_N-Sp-5C-4R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_N-Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_N-Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C",
    kinetics = ArrheniusBM(A=(16290.2,'m^3/(mol*s)'), n=0.587889, w0=(529750,'J/mol'), E0=(25497.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8178611799476728, var=1.4361448244290624, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C
    Total Standard Deviation in ln(k): 4.457387270098513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C
Total Standard Deviation in ln(k): 4.457387270098513""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C
Total Standard Deviation in ln(k): 4.457387270098513
""",
)

entry(
    index = 204,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.12706e-06,'m^3/(mol*s)'), n=3.71421, w0=(561500,'J/mol'), E0=(18079.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7523711856842638, var=55.256481060022864, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C
    Total Standard Deviation in ln(k): 16.79251856912071"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C
Total Standard Deviation in ln(k): 16.79251856912071""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C
Total Standard Deviation in ln(k): 16.79251856912071
""",
)

entry(
    index = 205,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(0.194584,'m^3/(mol*s)'), n=2.48511, w0=(563000,'J/mol'), E0=(20721.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_N-5CO-u0_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(55695.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->N_Ext-4O-R_5R!H-u0_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(3.47e+08,'m^3/(mol*s)'), n=-0.75, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.82e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_1BrClFINOPSSi->O_4CNS-u1_Ext-4CNS-R_N-Sp-5R!H=4CCNNSS_Sp-5R!H-4CNS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(7142.24,'m^3/(mol*s)'), n=0.763389, w0=(527000,'J/mol'), E0=(52700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.763373789700657, var=0.001161348087431578, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R
    Total Standard Deviation in ln(k): 1.9863430770259898"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R
Total Standard Deviation in ln(k): 1.9863430770259898""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R
Total Standard Deviation in ln(k): 1.9863430770259898
""",
)

entry(
    index = 213,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_4R->C",
    kinetics = ArrheniusBM(A=(0.00241424,'m^3/(mol*s)'), n=2.70017, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_N-4R->C",
    kinetics = ArrheniusBM(A=(0.00163749,'m^3/(mol*s)'), n=2.84871, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_5CO->O",
    kinetics = ArrheniusBM(A=(0.000102832,'m^3/(mol*s)'), n=2.95217, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O",
    kinetics = ArrheniusBM(A=(17131.3,'m^3/(mol*s)'), n=0.58155, w0=(527900,'J/mol'), E0=(25638.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5992656159672699, var=0.9288934931646743, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O
    Total Standard Deviation in ln(k): 3.437838544960444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O
Total Standard Deviation in ln(k): 3.437838544960444""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O
Total Standard Deviation in ln(k): 3.437838544960444
""",
)

entry(
    index = 217,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C_Ext-5CO-R_Ext-4C-R_Ext-7R!H-R_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=0, w0=(561500,'J/mol'), E0=(36677.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C_Ext-5CO-R_Ext-4C-R_Ext-7R!H-R_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C_Ext-5CO-R_Ext-4C-R_Ext-7R!H-R_Ext-5CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C_Ext-5CO-R_Ext-4C-R_Ext-7R!H-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_N-2R!H->C_Ext-5CO-R_Ext-4C-R_Ext-7R!H-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_4R->C",
    kinetics = ArrheniusBM(A=(0.000469765,'m^3/(mol*s)'), n=3.00326, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_N-4R->C",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_Ext-1C-R_N-5CO->O_Sp-5C-4R_Ext-5C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(18903,'m^3/(mol*s)'), n=0.566317, w0=(520500,'J/mol'), E0=(13889.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.411410111805513, var=3.5814264498435353, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R
    Total Standard Deviation in ln(k): 7.340148946681023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R
Total Standard Deviation in ln(k): 7.340148946681023""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R
Total Standard Deviation in ln(k): 7.340148946681023
""",
)

entry(
    index = 221,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.000648848,'m^3/(mol*s)'), n=3.00006, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_1C-inRing",
    kinetics = ArrheniusBM(A=(0.000675,'m^3/(mol*s)'), n=2.7, w0=(483500,'J/mol'), E0=(35785.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(15.8953,'m^3/(mol*s)'), n=1.45251, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5372653849817526, var=5.203323361860222, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing
    Total Standard Deviation in ln(k): 8.43543578750035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing
Total Standard Deviation in ln(k): 8.43543578750035""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing
Total Standard Deviation in ln(k): 8.43543578750035
""",
)

entry(
    index = 224,
    label = "Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.000194398,'m^3/(mol*s)'), n=2.95919, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-Sp-5R!H#4R_N-5R!H->S_5CO-u0_Ext-1C-R_N-Sp-6R!H=1C_4R->C_N-Sp-5CCOO=4C_2R!H->C_N-5CO->O_Ext-4C-R_N-1C-inRing_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

