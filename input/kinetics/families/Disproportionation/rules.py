#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(109.843,'m^3/(mol*s)'), n=1.50066, w0=(574008,'J/mol'), E0=(15529.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.019654029184858927, var=2.2721425359980247, Tref=1000.0, N=190, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 190 training reactions at node Root
    Total Standard Deviation in ln(k): 3.071245012637827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 190 training reactions at node Root
Total Standard Deviation in ln(k): 3.071245012637827""",
    longDesc = 
"""
BM rule fitted to 190 training reactions at node Root
Total Standard Deviation in ln(k): 3.071245012637827
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(1033.16,'m^3/(mol*s)'), n=1.22074, w0=(555981,'J/mol'), E0=(59335.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03334987398230725, var=2.7618467270254925, Tref=1000.0, N=129, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 129 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 3.4154237442379927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 129 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.4154237442379927""",
    longDesc = 
"""
BM rule fitted to 129 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.4154237442379927
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
    kinetics = ArrheniusBM(A=(183.317,'m^3/(mol*s)'), n=1.38807, w0=(555432,'J/mol'), E0=(64280.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8242563743914577, var=14.657151400355877, Tref=1000.0, N=95, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R',), comment="""BM rule fitted to 95 training reactions at node Root_1R!H->C_Ext-4R-R
    Total Standard Deviation in ln(k): 12.258618678176452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 95 training reactions at node Root_1R!H->C_Ext-4R-R
Total Standard Deviation in ln(k): 12.258618678176452""",
    longDesc = 
"""
BM rule fitted to 95 training reactions at node Root_1R!H->C_Ext-4R-R
Total Standard Deviation in ln(k): 12.258618678176452
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_2R!H->O",
    kinetics = ArrheniusBM(A=(2.48793e+24,'m^3/(mol*s)'), n=-4.494, w0=(636750,'J/mol'), E0=(63675,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.7689806400213985, var=155.85764606703128, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->O
    Total Standard Deviation in ln(k): 42.03519510900516"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->O
Total Standard Deviation in ln(k): 42.03519510900516""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->O
Total Standard Deviation in ln(k): 42.03519510900516
""",
)

entry(
    index = 6,
    label = "Root_1R!H->C_N-2R!H->O",
    kinetics = ArrheniusBM(A=(812.56,'m^3/(mol*s)'), n=1.25596, w0=(552562,'J/mol'), E0=(38799.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0052368854419668626, var=2.5491886522680782, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O',), comment="""BM rule fitted to 32 training reactions at node Root_1R!H->C_N-2R!H->O
    Total Standard Deviation in ln(k): 3.213953871304504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_1R!H->C_N-2R!H->O
Total Standard Deviation in ln(k): 3.213953871304504""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_1R!H->C_N-2R!H->O
Total Standard Deviation in ln(k): 3.213953871304504
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
    label = "Root_1R!H->C_Ext-4R-R_4R->O",
    kinetics = ArrheniusBM(A=(2899.71,'m^3/(mol*s)'), n=1.15219, w0=(581400,'J/mol'), E0=(81396,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.571882727608042, var=29.785043381586256, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O',), comment="""BM rule fitted to 35 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O
    Total Standard Deviation in ln(k): 17.402993974985634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O
Total Standard Deviation in ln(k): 17.402993974985634""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O
Total Standard Deviation in ln(k): 17.402993974985634
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O",
    kinetics = ArrheniusBM(A=(628.461,'m^3/(mol*s)'), n=0.922077, w0=(540283,'J/mol'), E0=(-5461.63,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2554306812308083, var=23.271990517499905, Tref=1000.0, N=60, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O',), comment="""BM rule fitted to 60 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O
    Total Standard Deviation in ln(k): 12.825401260544679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O
Total Standard Deviation in ln(k): 12.825401260544679""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O
Total Standard Deviation in ln(k): 12.825401260544679
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_2R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.90291e-05,'m^3/(mol*s)'), n=4.10425, w0=(631500,'J/mol'), E0=(63150,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R",
    kinetics = ArrheniusBM(A=(537.343,'m^3/(mol*s)'), n=1.29822, w0=(544400,'J/mol'), E0=(39837.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03615449733908228, var=3.6842405498130377, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R
    Total Standard Deviation in ln(k): 3.938804252580842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R
Total Standard Deviation in ln(k): 3.938804252580842""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R
Total Standard Deviation in ln(k): 3.938804252580842
""",
)

entry(
    index = 13,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.95546e+14,'m^3/(mol*s)'), n=-2.38034, w0=(549333,'J/mol'), E0=(125694,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47938148972763794, var=1.609492015626017, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 3.747798425331565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.747798425331565""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.747798425331565
""",
)

entry(
    index = 14,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1",
    kinetics = ArrheniusBM(A=(506.737,'m^3/(mol*s)'), n=1.2871, w0=(559400,'J/mol'), E0=(55940,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04961527843058267, var=2.8611171696146305, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1
    Total Standard Deviation in ln(k): 3.5156382467133573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1
Total Standard Deviation in ln(k): 3.5156382467133573""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1
Total Standard Deviation in ln(k): 3.5156382467133573
""",
)

entry(
    index = 15,
    label = "Root_1R!H->C_N-2R!H->O_N-4R-u1",
    kinetics = ArrheniusBM(A=(9519.83,'m^3/(mol*s)'), n=1.0662, w0=(566667,'J/mol'), E0=(56666.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04145593490271482, var=2.3209494963655675, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_N-4R-u1',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1
    Total Standard Deviation in ln(k): 3.158306924667806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1
Total Standard Deviation in ln(k): 3.158306924667806""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1
Total Standard Deviation in ln(k): 3.158306924667806
""",
)

entry(
    index = 16,
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
    index = 17,
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
    index = 18,
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
    index = 19,
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
    index = 20,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0",
    kinetics = ArrheniusBM(A=(699.619,'m^3/(mol*s)'), n=1.33988, w0=(589810,'J/mol'), E0=(79259,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5147822880561181, var=38.14597768965762, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0',), comment="""BM rule fitted to 21 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0
    Total Standard Deviation in ln(k): 16.1877166523466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0
Total Standard Deviation in ln(k): 16.1877166523466""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0
Total Standard Deviation in ln(k): 16.1877166523466
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(0.00115552,'m^3/(mol*s)'), n=2.36408, w0=(568786,'J/mol'), E0=(22572.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03668723919388507, var=13.484382262335048, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0',), comment="""BM rule fitted to 14 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0
    Total Standard Deviation in ln(k): 7.453784100302378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0
Total Standard Deviation in ln(k): 7.453784100302378""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0
Total Standard Deviation in ln(k): 7.453784100302378
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S",
    kinetics = ArrheniusBM(A=(3.12126e-13,'m^3/(mol*s)'), n=4.70087, w0=(527000,'J/mol'), E0=(17509.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=10.238614422136449, var=279.3313223037818, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S
    Total Standard Deviation in ln(k): 59.23071623718318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S
Total Standard Deviation in ln(k): 59.23071623718318""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S
Total Standard Deviation in ln(k): 59.23071623718318
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S",
    kinetics = ArrheniusBM(A=(5875.59,'m^3/(mol*s)'), n=0.682378, w0=(540741,'J/mol'), E0=(22570.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.650236456765115, var=7.014683843750474, Tref=1000.0, N=58, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S',), comment="""BM rule fitted to 58 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S
    Total Standard Deviation in ln(k): 6.943350597642823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 58 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S
Total Standard Deviation in ln(k): 6.943350597642823""",
    longDesc = 
"""
BM rule fitted to 58 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S
Total Standard Deviation in ln(k): 6.943350597642823
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.50555e+07,'m^3/(mol*s)'), n=0.49554, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24415953896921155, var=7.60425192383308, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.141685156926082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.141685156926082""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.141685156926082
""",
)

entry(
    index = 25,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_4R->H",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(46201.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_4R->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_4R->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_4R->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_4R->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H",
    kinetics = ArrheniusBM(A=(345653,'m^3/(mol*s)'), n=0.432137, w0=(547875,'J/mol'), E0=(77646.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011544780355912906, var=0.41290969266706845, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H
    Total Standard Deviation in ln(k): 1.3172106443703449"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H
Total Standard Deviation in ln(k): 1.3172106443703449""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H
Total Standard Deviation in ln(k): 1.3172106443703449
""",
)

entry(
    index = 27,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(4.81255e+06,'m^3/(mol*s)'), n=-0.0914287, w0=(548857,'J/mol'), E0=(54885.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3615528573222535e-08, var=2.518599985282002, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 3.1815341726363338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.1815341726363338""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.1815341726363338
""",
)

entry(
    index = 28,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(12.6303,'m^3/(mol*s)'), n=1.57424, w0=(551000,'J/mol'), E0=(84114.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.066877773658311, var=4.470346121191037, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 9.431810309774876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 9.431810309774876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 9.431810309774876
""",
)

entry(
    index = 29,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_4R->C",
    kinetics = ArrheniusBM(A=(108.077,'m^3/(mol*s)'), n=1.32854, w0=(550667,'J/mol'), E0=(55066.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05156472802023765, var=2.3527369978816193, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C
    Total Standard Deviation in ln(k): 3.2045494245042048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C
Total Standard Deviation in ln(k): 3.2045494245042048""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C
Total Standard Deviation in ln(k): 3.2045494245042048
""",
)

entry(
    index = 30,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C",
    kinetics = ArrheniusBM(A=(940.235,'m^3/(mol*s)'), n=1.27053, w0=(563143,'J/mol'), E0=(56314.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.049001405527540294, var=2.957763507284317, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C
    Total Standard Deviation in ln(k): 3.5708924925088597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C
Total Standard Deviation in ln(k): 3.5708924925088597""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C
Total Standard Deviation in ln(k): 3.5708924925088597
""",
)

entry(
    index = 31,
    label = "Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C",
    kinetics = ArrheniusBM(A=(16399.1,'m^3/(mol*s)'), n=1.06552, w0=(564500,'J/mol'), E0=(56450,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1948601205724478, var=0.35256865674022686, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C
    Total Standard Deviation in ln(k): 1.6799597049858794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C
Total Standard Deviation in ln(k): 1.6799597049858794""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C
Total Standard Deviation in ln(k): 1.6799597049858794
""",
)

entry(
    index = 32,
    label = "Root_1R!H->C_N-2R!H->O_N-4R-u1_N-Sp-2CNS-1C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_N-4R-u1_N-Sp-2CNS-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_N-Sp-2CNS-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_N-Sp-2CNS-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_N-Sp-2CNS-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
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
    index = 34,
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
    index = 35,
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
    index = 36,
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
    index = 37,
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
    index = 38,
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
    index = 39,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.11524e+10,'m^3/(mol*s)'), n=-0.956897, w0=(597688,'J/mol'), E0=(19466,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2656336030328322, var=165.20075583867893, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 26.43437050130346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R
Total Standard Deviation in ln(k): 26.43437050130346""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R
Total Standard Deviation in ln(k): 26.43437050130346
""",
)

entry(
    index = 40,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C",
    kinetics = ArrheniusBM(A=(2.57491e-18,'m^3/(mol*s)'), n=7.06884, w0=(563000,'J/mol'), E0=(-19361.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4205024110303872, var=22.984059089905276, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C
    Total Standard Deviation in ln(k): 10.667578044727026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C
Total Standard Deviation in ln(k): 10.667578044727026""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C
Total Standard Deviation in ln(k): 10.667578044727026
""",
)

entry(
    index = 41,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C",
    kinetics = ArrheniusBM(A=(7.88985,'m^3/(mol*s)'), n=1.90017, w0=(634375,'J/mol'), E0=(63437.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.587280486392339, var=6.154133239557905, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C
    Total Standard Deviation in ln(k): 8.961393591121764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C
Total Standard Deviation in ln(k): 8.961393591121764""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C
Total Standard Deviation in ln(k): 8.961393591121764
""",
)

entry(
    index = 42,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_1C-inRing",
    kinetics = ArrheniusBM(A=(4.76242,'m^3/(mol*s)'), n=2.49162, w0=(563000,'J/mol'), E0=(17534.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing",
    kinetics = ArrheniusBM(A=(0.000257119,'m^3/(mol*s)'), n=2.46251, w0=(569231,'J/mol'), E0=(21082,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05652996567394083, var=4.228379477985215, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing
    Total Standard Deviation in ln(k): 4.26437660054394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing
Total Standard Deviation in ln(k): 4.26437660054394""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing
Total Standard Deviation in ln(k): 4.26437660054394
""",
)

entry(
    index = 44,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(515000,'J/mol'), E0=(39525.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(8722.8,'m^3/(mol*s)'), n=0.656527, w0=(536225,'J/mol'), E0=(16341.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.376711151284461, var=11.967838979594562, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R',), comment="""BM rule fitted to 20 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R
    Total Standard Deviation in ln(k): 10.39436695299593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.39436695299593""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.39436695299593
""",
)

entry(
    index = 46,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS",
    kinetics = ArrheniusBM(A=(5.08215e+06,'m^3/(mol*s)'), n=-2.156e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.8487835248037475e-08, var=0.19740695447292192, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS
    Total Standard Deviation in ln(k): 0.8907139134007048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS
Total Standard Deviation in ln(k): 0.8907139134007048""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS
Total Standard Deviation in ln(k): 0.8907139134007048
""",
)

entry(
    index = 47,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS",
    kinetics = ArrheniusBM(A=(500.292,'m^3/(mol*s)'), n=0.885708, w0=(543471,'J/mol'), E0=(41045.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47380395034952344, var=10.521960962313823, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS',), comment="""BM rule fitted to 35 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS
    Total Standard Deviation in ln(k): 7.693336086836804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS
Total Standard Deviation in ln(k): 7.693336086836804""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS
Total Standard Deviation in ln(k): 7.693336086836804
""",
)

entry(
    index = 48,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1",
    kinetics = ArrheniusBM(A=(44108,'m^3/(mol*s)'), n=1.12377, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16581165333766865, var=3.194798716833971, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1
    Total Standard Deviation in ln(k): 3.9998756474426704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1
Total Standard Deviation in ln(k): 3.9998756474426704""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1
Total Standard Deviation in ln(k): 3.9998756474426704
""",
)

entry(
    index = 49,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1",
    kinetics = ArrheniusBM(A=(9.49416e+10,'m^3/(mol*s)'), n=-0.446812, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.946919299265185, var=6.0275901730058195, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1
    Total Standard Deviation in ln(k): 14.838738029138707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1
Total Standard Deviation in ln(k): 14.838738029138707""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1
Total Standard Deviation in ln(k): 14.838738029138707
""",
)

entry(
    index = 50,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N",
    kinetics = ArrheniusBM(A=(340831,'m^3/(mol*s)'), n=0.433821, w0=(550833,'J/mol'), E0=(77633.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018504166564283952, var=0.42535074633987874, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N
    Total Standard Deviation in ln(k): 1.3539594375362136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N
Total Standard Deviation in ln(k): 1.3539594375362136""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N
Total Standard Deviation in ln(k): 1.3539594375362136
""",
)

entry(
    index = 51,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_N-2CNS->N",
    kinetics = ArrheniusBM(A=(4.71002,'m^3/(mol*s)'), n=1.97886, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_N-2CNS->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_N-2CNS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_N-2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_N-2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O",
    kinetics = ArrheniusBM(A=(1.70765e+07,'m^3/(mol*s)'), n=7.53848e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9494596051172368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O
    Total Standard Deviation in ln(k): 1.9534182263699047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O
Total Standard Deviation in ln(k): 1.9534182263699047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O
Total Standard Deviation in ln(k): 1.9534182263699047
""",
)

entry(
    index = 53,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O",
    kinetics = ArrheniusBM(A=(2.89977e+06,'m^3/(mol*s)'), n=-0.128, w0=(543200,'J/mol'), E0=(54320,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.034574770212034e-10, var=0.30382074570218065, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O
    Total Standard Deviation in ln(k): 1.1050087140840554"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O
Total Standard Deviation in ln(k): 1.1050087140840554""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O
Total Standard Deviation in ln(k): 1.1050087140840554
""",
)

entry(
    index = 54,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_4R->C",
    kinetics = ArrheniusBM(A=(3.01e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(98632.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_N-4R->C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_N-Sp-5R!H-1C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C",
    kinetics = ArrheniusBM(A=(187.635,'m^3/(mol*s)'), n=1.32726, w0=(552500,'J/mol'), E0=(55250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1546561267678964, var=0.37853885495848577, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C
    Total Standard Deviation in ln(k): 1.6220067411055652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C
Total Standard Deviation in ln(k): 1.6220067411055652""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C
Total Standard Deviation in ln(k): 1.6220067411055652
""",
)

entry(
    index = 57,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_N-Sp-2CNS-1C",
    kinetics = ArrheniusBM(A=(0.81,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(54700,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_N-Sp-2CNS-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_N-Sp-2CNS-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_N-Sp-2CNS-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_N-Sp-2CNS-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_4HNO->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_4HNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_4HNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_4HNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_4HNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N",
    kinetics = ArrheniusBM(A=(1726.25,'m^3/(mol*s)'), n=1.24309, w0=(567917,'J/mol'), E0=(56791.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04792877945204523, var=2.4049595839144975, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N
    Total Standard Deviation in ln(k): 3.229353617259098"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N
Total Standard Deviation in ln(k): 3.229353617259098""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N
Total Standard Deviation in ln(k): 3.229353617259098
""",
)

entry(
    index = 60,
    label = "Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_2CNS->N",
    kinetics = ArrheniusBM(A=(500,'m^3/(mol*s)'), n=1.5, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_2CNS->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_2CNS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_N-2CNS->N",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_N-2CNS->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_N-2CNS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_N-2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_N-4R-u1_Sp-2CNS-1C_N-2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
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
    index = 63,
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
    index = 64,
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
    index = 65,
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
    index = 66,
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
    index = 67,
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
    index = 68,
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
    index = 69,
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
    index = 70,
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
    index = 71,
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
    index = 72,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.18687e-07,'m^3/(mol*s)'), n=2.6595, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C",
    kinetics = ArrheniusBM(A=(2.72275e+27,'m^3/(mol*s)'), n=-5.85801, w0=(563000,'J/mol'), E0=(90348.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8288912624635575, var=314.2119907375145, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C
    Total Standard Deviation in ln(k): 37.61862707128233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C
Total Standard Deviation in ln(k): 37.61862707128233""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C
Total Standard Deviation in ln(k): 37.61862707128233
""",
)

entry(
    index = 74,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.57897e+06,'m^3/(mol*s)'), n=0.428492, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.291174470317604, var=31.6875934834746, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C
    Total Standard Deviation in ln(k): 12.016595574546544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C
Total Standard Deviation in ln(k): 12.016595574546544""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C
Total Standard Deviation in ln(k): 12.016595574546544
""",
)

entry(
    index = 75,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.82058e-15,'m^3/(mol*s)'), n=6.25802, w0=(563000,'J/mol'), E0=(-21678.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.281960920587293, var=20.366256871402374, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 9.755611336227025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 9.755611336227025""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 9.755611336227025
""",
)

entry(
    index = 76,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.49089e-25,'m^3/(mol*s)'), n=8.48743, w0=(563000,'J/mol'), E0=(-29967.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.022519170807503302, var=20.03041458596872, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 9.028843070886655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.028843070886655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.028843070886655
""",
)

entry(
    index = 77,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_2NO->N",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N",
    kinetics = ArrheniusBM(A=(144749,'m^3/(mol*s)'), n=0.248873, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2330371550646505, var=2.006236663152901, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N
    Total Standard Deviation in ln(k): 3.4250610124226775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 3.4250610124226775""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 3.4250610124226775
""",
)

entry(
    index = 79,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(97648.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(0.00116599,'m^3/(mol*s)'), n=2.22344, w0=(571409,'J/mol'), E0=(2119.89,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22001670721257607, var=1.4233331077126632, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C',), comment="""BM rule fitted to 11 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 2.944525411234082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C
Total Standard Deviation in ln(k): 2.944525411234082""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C
Total Standard Deviation in ln(k): 2.944525411234082
""",
)

entry(
    index = 81,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(2.6e+09,'m^3/(mol*s)'), n=-1.26, w0=(551500,'J/mol'), E0=(34913.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(10266.1,'m^3/(mol*s)'), n=0.63343, w0=(535531,'J/mol'), E0=(11503.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8029739131842744, var=16.25714966644934, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 16 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 12.613208282062358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 12.613208282062358""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 12.613208282062358
""",
)

entry(
    index = 83,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0",
    kinetics = ArrheniusBM(A=(7.64916,'m^3/(mol*s)'), n=1.72326, w0=(539000,'J/mol'), E0=(52014.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07342189628348637, var=0.15508824837400983, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0
    Total Standard Deviation in ln(k): 0.9739667653851731"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0
Total Standard Deviation in ln(k): 0.9739667653851731""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0
Total Standard Deviation in ln(k): 0.9739667653851731
""",
)

entry(
    index = 84,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_N-7R!H-u0",
    kinetics = ArrheniusBM(A=(9.67941e-05,'m^3/(mol*s)'), n=2.94878, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_N-7R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_N-7R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=-5.78148e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 86,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R",
    kinetics = ArrheniusBM(A=(119.05,'m^3/(mol*s)'), n=1.03265, w0=(537962,'J/mol'), E0=(3557.87,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6893627734122612, var=12.52669997584652, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R',), comment="""BM rule fitted to 26 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R
    Total Standard Deviation in ln(k): 8.827441843467705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R
Total Standard Deviation in ln(k): 8.827441843467705""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R
Total Standard Deviation in ln(k): 8.827441843467705
""",
)

entry(
    index = 87,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C",
    kinetics = ArrheniusBM(A=(7.83959e+07,'m^3/(mol*s)'), n=-0.543877, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.000999118113520444, var=0.1419297158816419, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C
    Total Standard Deviation in ln(k): 0.7577654287519907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C
Total Standard Deviation in ln(k): 0.7577654287519907""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C
Total Standard Deviation in ln(k): 0.7577654287519907
""",
)

entry(
    index = 88,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C",
    kinetics = ArrheniusBM(A=(7183.77,'m^3/(mol*s)'), n=0.757336, w0=(600167,'J/mol'), E0=(50890.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02233372141659651, var=7.773576902351321, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C
    Total Standard Deviation in ln(k): 5.645543815979605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C
Total Standard Deviation in ln(k): 5.645543815979605""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C
Total Standard Deviation in ln(k): 5.645543815979605
""",
)

entry(
    index = 89,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.56849e+06,'m^3/(mol*s)'), n=0.546429, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.3469560063465247, var=6.597041539464937, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.045977618358917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.045977618358917""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.045977618358917
""",
)

entry(
    index = 90,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(0.115772,'m^3/(mol*s)'), n=2.98873, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(0.0136611,'m^3/(mol*s)'), n=3.34686, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(0.00149689,'m^3/(mol*s)'), n=3.39346, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_N-4R-u1_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_4CNO->O",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_4CNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_4CNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_4CNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_4CNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O",
    kinetics = ArrheniusBM(A=(1713.08,'m^3/(mol*s)'), n=1.04631, w0=(540750,'J/mol'), E0=(61802.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6075970314782776, var=0.6553537765114736, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O
    Total Standard Deviation in ln(k): 3.149537412505626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O
Total Standard Deviation in ln(k): 3.149537412505626""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O
Total Standard Deviation in ln(k): 3.149537412505626
""",
)

entry(
    index = 95,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_4R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.33283e+06,'m^3/(mol*s)'), n=-0.16, w0=(544250,'J/mol'), E0=(54425,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.19778088927846924, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R
    Total Standard Deviation in ln(k): 0.8915570777141144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.8915570777141144""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.8915570777141144
""",
)

entry(
    index = 97,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_4CH->H",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_4CH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_4CH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_4CH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_4CH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H",
    kinetics = ArrheniusBM(A=(4.56235e+06,'m^3/(mol*s)'), n=-0.16, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.26130883078297484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H
    Total Standard Deviation in ln(k): 1.0247880034798968"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H
Total Standard Deviation in ln(k): 1.0247880034798968""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H
Total Standard Deviation in ln(k): 1.0247880034798968
""",
)

entry(
    index = 99,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_2CNS->N",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=1.87, w0=(566000,'J/mol'), E0=(56600,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_2CNS->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_2CNS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_N-2CNS->N",
    kinetics = ArrheniusBM(A=(2.19e+08,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_N-2CNS->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_N-2CNS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_N-2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_4R->C_Sp-2CNS-1C_N-2CNS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C",
    kinetics = ArrheniusBM(A=(3004.26,'m^3/(mol*s)'), n=1.2423, w0=(569750,'J/mol'), E0=(56975,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04720985726748525, var=5.655843163774084, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C
    Total Standard Deviation in ln(k): 4.886282032610383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C
Total Standard Deviation in ln(k): 4.886282032610383""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C
Total Standard Deviation in ln(k): 4.886282032610383
""",
)

entry(
    index = 102,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C",
    kinetics = ArrheniusBM(A=(991.203,'m^3/(mol*s)'), n=1.24388, w0=(564250,'J/mol'), E0=(56425,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5233477243052834, var=6.258416902202596, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C
    Total Standard Deviation in ln(k): 6.3301553207937475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C
Total Standard Deviation in ln(k): 6.3301553207937475""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C
Total Standard Deviation in ln(k): 6.3301553207937475
""",
)

entry(
    index = 103,
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
    index = 104,
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
    index = 105,
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
    index = 106,
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
    index = 107,
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
    index = 108,
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
    index = 109,
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
    index = 110,
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
    index = 111,
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
    index = 112,
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
    index = 113,
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
    index = 114,
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
    index = 115,
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
    index = 116,
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
    index = 117,
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
    index = 118,
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
    index = 119,
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
    index = 120,
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
    index = 121,
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
    index = 122,
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
    index = 123,
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
    index = 124,
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
    index = 125,
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
    index = 126,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.35472e+37,'m^3/(mol*s)'), n=-8.93425, w0=(563000,'J/mol'), E0=(99348.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.024776490261907, var=554.6631210297729, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 49.788906540063884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 49.788906540063884""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 49.788906540063884
""",
)

entry(
    index = 127,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.77348e-05,'m^3/(mol*s)'), n=3.6443, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.40519,'m^3/(mol*s)'), n=2.12278, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3516360389451068, var=3.6158740378042107, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 7.208164755401575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 7.208164755401575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 7.208164755401575
""",
)

entry(
    index = 129,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2.47459e-18,'m^3/(mol*s)'), n=7.10033, w0=(563000,'J/mol'), E0=(39052.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.527801049256424, var=2.9656582218354606, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C
    Total Standard Deviation in ln(k): 4.778504918637625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C
Total Standard Deviation in ln(k): 4.778504918637625""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C
Total Standard Deviation in ln(k): 4.778504918637625
""",
)

entry(
    index = 130,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.0167484,'m^3/(mol*s)'), n=2.99233, w0=(563000,'J/mol'), E0=(42133.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(6.05279e-06,'m^3/(mol*s)'), n=2.75866, w0=(563000,'J/mol'), E0=(118179,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(114517,'m^3/(mol*s)'), n=0.361874, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.7971529641329, var=5.895632360122158, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.89570438685961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.89570438685961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.89570438685961
""",
)

entry(
    index = 133,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C",
    kinetics = ArrheniusBM(A=(0.0337834,'m^3/(mol*s)'), n=1.77326, w0=(563000,'J/mol'), E0=(4756.14,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.35425002481536716, var=1.4344800175828984, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C
    Total Standard Deviation in ln(k): 3.2911422288849943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 3.2911422288849943""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 3.2911422288849943
""",
)

entry(
    index = 134,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.000371804,'m^3/(mol*s)'), n=2.67859, w0=(655500,'J/mol'), E0=(88984.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS",
    kinetics = ArrheniusBM(A=(1.88905,'m^3/(mol*s)'), n=1.50702, w0=(539000,'J/mol'), E0=(36719.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14056969916318032, var=21.163418380015138, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS',), comment="""BM rule fitted to 12 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS
    Total Standard Deviation in ln(k): 9.575716410304029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS
Total Standard Deviation in ln(k): 9.575716410304029""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS
Total Standard Deviation in ln(k): 9.575716410304029
""",
)

entry(
    index = 136,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS",
    kinetics = ArrheniusBM(A=(17474.1,'m^3/(mol*s)'), n=0.579066, w0=(525125,'J/mol'), E0=(23961.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17935027518483065, var=1.0454755561185696, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS
    Total Standard Deviation in ln(k): 2.5004403590015207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS
Total Standard Deviation in ln(k): 2.5004403590015207""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS
Total Standard Deviation in ln(k): 2.5004403590015207
""",
)

entry(
    index = 137,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_7R!H->C",
    kinetics = ArrheniusBM(A=(38.5792,'m^3/(mol*s)'), n=1.51619, w0=(539000,'J/mol'), E0=(54735,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4442751940758767, var=1.3197878046999132, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_7R!H->C
    Total Standard Deviation in ln(k): 5.93191225727079"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_7R!H->C
Total Standard Deviation in ln(k): 5.93191225727079""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_7R!H->C
Total Standard Deviation in ln(k): 5.93191225727079
""",
)

entry(
    index = 138,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_N-7R!H->C",
    kinetics = ArrheniusBM(A=(0.000417723,'m^3/(mol*s)'), n=2.95473, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-5CO-R_7R!H-u0_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R",
    kinetics = ArrheniusBM(A=(515.383,'m^3/(mol*s)'), n=1.09241, w0=(543500,'J/mol'), E0=(25813.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23785084563458356, var=1.3157994133583233, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R
    Total Standard Deviation in ln(k): 2.8972127207246126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R
Total Standard Deviation in ln(k): 2.8972127207246126""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R
Total Standard Deviation in ln(k): 2.8972127207246126
""",
)

entry(
    index = 141,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(8.48093e+10,'m^3/(mol*s)'), n=-1.62411, w0=(533857,'J/mol'), E0=(104624,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.199646688598447, var=9.322873390976193, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 14 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 9.135321598847954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 9.135321598847954""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 9.135321598847954
""",
)

entry(
    index = 142,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.05254e+08,'m^3/(mol*s)'), n=-0.256206, w0=(539000,'J/mol'), E0=(80495.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0172224868708053, var=3.360979523950043, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 8.743673904658397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.743673904658397""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.743673904658397
""",
)

entry(
    index = 143,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C",
    kinetics = ArrheniusBM(A=(1.51696e+08,'m^3/(mol*s)'), n=-0.652653, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011989420510271538, var=0.09452433595411674, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C
    Total Standard Deviation in ln(k): 0.6193644135015641"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C
Total Standard Deviation in ln(k): 0.6193644135015641""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C
Total Standard Deviation in ln(k): 0.6193644135015641
""",
)

entry(
    index = 144,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_N-5CO->C",
    kinetics = ArrheniusBM(A=(2.89e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_N-5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_N-5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_Ext-4CHNS-R",
    kinetics = ArrheniusBM(A=(0.150092,'m^3/(mol*s)'), n=1.93096, w0=(631500,'J/mol'), E0=(63150,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_Ext-4CHNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_Ext-4CHNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_Ext-4CHNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_Ext-4CHNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_2OS->O",
    kinetics = ArrheniusBM(A=(0.00636185,'m^3/(mol*s)'), n=2.81045, w0=(631500,'J/mol'), E0=(63150,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_2OS->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_2OS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_2OS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_2OS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_N-2OS->O",
    kinetics = ArrheniusBM(A=(979000,'m^3/(mol*s)'), n=0, w0=(537500,'J/mol'), E0=(38210.6,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_N-2OS->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_N-2OS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_N-2OS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_N-2R!H->C_N-2OS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_6R!H-u0",
    kinetics = ArrheniusBM(A=(0.00818526,'m^3/(mol*s)'), n=2.80402, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_6R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_6R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_6R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_6R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_N-6R!H-u0",
    kinetics = ArrheniusBM(A=(0.0430993,'m^3/(mol*s)'), n=2.82821, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_N-6R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_N-6R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_N-6R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_Ext-5R!H-R_4R-u1_Sp-6R!H-5R!H_N-6R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_4CN->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_4CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_4CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_4CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_4CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_N-4CN->N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(47358.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_N-4CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_N-4CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_N-4CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-2CNS-R_N-4R->H_2CNS->N_N-4CNO->O_N-4CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_4CH->H",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_4CH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_4CH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_4CH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_4CH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_N-4CH->H",
    kinetics = ArrheniusBM(A=(6.02e+06,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_N-4CH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_N-4CH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_N-4CH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_Ext-1C-R_N-4CH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_4C-u1",
    kinetics = ArrheniusBM(A=(1.15e+07,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_N-4C-u1",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_Ext-1C-R_Sp-5R!H-1C_N-4R->O_N-4CH->H_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N",
    kinetics = ArrheniusBM(A=(2973.61,'m^3/(mol*s)'), n=1.24388, w0=(583250,'J/mol'), E0=(58325,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5233477243052835, var=6.258416902202596, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N
    Total Standard Deviation in ln(k): 6.3301553207937475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N
Total Standard Deviation in ln(k): 6.3301553207937475""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N
Total Standard Deviation in ln(k): 6.3301553207937475
""",
)

entry(
    index = 157,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N",
    kinetics = ArrheniusBM(A=(9.32738e+06,'m^3/(mol*s)'), n=7.6044e-07, w0=(556250,'J/mol'), E0=(55625,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=7.208635393578017, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N
    Total Standard Deviation in ln(k): 5.382493565699981"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N
Total Standard Deviation in ln(k): 5.382493565699981""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N
Total Standard Deviation in ln(k): 5.382493565699981
""",
)

entry(
    index = 158,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_4HO->H",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(55750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_N-4HO->H",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_N-4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_N-4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_N-Sp-2CNS-1C_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
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
    index = 161,
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
    index = 162,
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
    index = 163,
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
    index = 164,
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
    index = 165,
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
    index = 166,
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
    index = 167,
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
    index = 168,
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
    index = 169,
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
    index = 170,
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
    index = 171,
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
    index = 172,
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
    index = 173,
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
    index = 174,
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
    index = 175,
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
    index = 176,
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
    index = 177,
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
    index = 178,
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
    index = 179,
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
    index = 180,
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
    index = 181,
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
    index = 182,
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
    index = 183,
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
    index = 184,
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
    index = 185,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.28068e+54,'m^3/(mol*s)'), n=-13.6729, w0=(563000,'J/mol'), E0=(98492.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-14.503715032808914, var=306.25422247726704, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 71.52460076653797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 71.52460076653797""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 71.52460076653797
""",
)

entry(
    index = 186,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_6R!H-u0",
    kinetics = ArrheniusBM(A=(1.19405e-06,'m^3/(mol*s)'), n=3.85287, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_6R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_6R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_6R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_6R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_N-6R!H-u0",
    kinetics = ArrheniusBM(A=(0.00124175,'m^3/(mol*s)'), n=3.00696, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_N-6R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_N-6R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_N-6R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_N-2R!H->C_N-5R!H->C_N-6R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C",
    kinetics = ArrheniusBM(A=(1.03912e-05,'m^3/(mol*s)'), n=3.41391, w0=(563000,'J/mol'), E0=(104987,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18434729851362863, var=3.7977980581618107, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C
    Total Standard Deviation in ln(k): 4.3699998594512754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C
Total Standard Deviation in ln(k): 4.3699998594512754""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C
Total Standard Deviation in ln(k): 4.3699998594512754
""",
)

entry(
    index = 189,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C",
    kinetics = ArrheniusBM(A=(8.01158e-05,'m^3/(mol*s)'), n=3.51961, w0=(563000,'J/mol'), E0=(117328,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(0.000815523,'m^3/(mol*s)'), n=2.84763, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_N-2R!H->C_N-2NO->N_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.17653,'m^3/(mol*s)'), n=1.10567, w0=(563000,'J/mol'), E0=(3072.28,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.314520698902224, var=1.2584318477413958, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.0391617910341244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.0391617910341244""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.0391617910341244
""",
)

entry(
    index = 192,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0",
    kinetics = ArrheniusBM(A=(3451.8,'m^3/(mol*s)'), n=0.698007, w0=(539000,'J/mol'), E0=(62183.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13446901460644572, var=16.20769933107721, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0
    Total Standard Deviation in ln(k): 8.408682098935197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0
Total Standard Deviation in ln(k): 8.408682098935197""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0
Total Standard Deviation in ln(k): 8.408682098935197
""",
)

entry(
    index = 193,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0",
    kinetics = ArrheniusBM(A=(1.57821e+15,'m^3/(mol*s)'), n=-3.1331, w0=(539000,'J/mol'), E0=(138715,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8742981715297636, var=27.54903945473918, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0
    Total Standard Deviation in ln(k): 12.719017933118632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0
Total Standard Deviation in ln(k): 12.719017933118632""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0
Total Standard Deviation in ln(k): 12.719017933118632
""",
)

entry(
    index = 194,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0",
    kinetics = ArrheniusBM(A=(18619.2,'m^3/(mol*s)'), n=0.568569, w0=(520500,'J/mol'), E0=(14237.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.370647514564338, var=3.1198123602506067, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0
    Total Standard Deviation in ln(k): 6.984799653874818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0
Total Standard Deviation in ln(k): 6.984799653874818""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0
Total Standard Deviation in ln(k): 6.984799653874818
""",
)

entry(
    index = 195,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_N-7R!H-u0",
    kinetics = ArrheniusBM(A=(0.00571627,'m^3/(mol*s)'), n=2.95155, w0=(539000,'J/mol'), E0=(48692.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_N-7R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_N-7R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(2.28933e+07,'m^3/(mol*s)'), n=-0.391223, w0=(546500,'J/mol'), E0=(31878.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19737560655667852, var=1.0209442061282195, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C
    Total Standard Deviation in ln(k): 2.5215386908915827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 2.5215386908915827""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 2.5215386908915827
""",
)

entry(
    index = 197,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(0.000319726,'m^3/(mol*s)'), n=3.09733, w0=(539000,'J/mol'), E0=(52542.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10581930014891375, var=1.6653449979429737, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C
    Total Standard Deviation in ln(k): 2.8529531071618046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 2.8529531071618046""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 2.8529531071618046
""",
)

entry(
    index = 198,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C",
    kinetics = ArrheniusBM(A=(246.617,'m^3/(mol*s)'), n=0.807605, w0=(532455,'J/mol'), E0=(53245.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6474045914186497, var=19.356191671800048, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C',), comment="""BM rule fitted to 11 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C
    Total Standard Deviation in ln(k): 12.95917423568159"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 12.95917423568159""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 12.95917423568159
""",
)

entry(
    index = 199,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C",
    kinetics = ArrheniusBM(A=(9.96326e+08,'m^3/(mol*s)'), n=-0.939212, w0=(539000,'J/mol'), E0=(99630.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08269372345061361, var=0.3446234839425939, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C
    Total Standard Deviation in ln(k): 1.3846456986205788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C
Total Standard Deviation in ln(k): 1.3846456986205788""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C
Total Standard Deviation in ln(k): 1.3846456986205788
""",
)

entry(
    index = 200,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_7R!H-u0",
    kinetics = ArrheniusBM(A=(0.0977826,'m^3/(mol*s)'), n=2.66551, w0=(539000,'J/mol'), E0=(68786.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_7R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_7R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_N-7R!H-u0",
    kinetics = ArrheniusBM(A=(0.00336809,'m^3/(mol*s)'), n=2.5889, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_N-7R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_N-7R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_N-6R!H->C_Ext-5CO-R_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS",
    kinetics = ArrheniusBM(A=(1.51619e+08,'m^3/(mol*s)'), n=-0.640816, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.001498677849822722, var=0.06565633740733616, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS
    Total Standard Deviation in ln(k): 0.517448666852609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS
Total Standard Deviation in ln(k): 0.517448666852609""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS
Total Standard Deviation in ln(k): 0.517448666852609
""",
)

entry(
    index = 203,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_N-Sp-5C-4CHNS",
    kinetics = ArrheniusBM(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_N-Sp-5C-4CHNS',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_N-Sp-5C-4CHNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_N-Sp-5C-4CHNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_N-Sp-5C-4CHNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_4HO->H",
    kinetics = ArrheniusBM(A=(720,'m^3/(mol*s)'), n=1.5, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_N-4HO->H",
    kinetics = ArrheniusBM(A=(3.6,'m^3/(mol*s)'), n=2, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_N-4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_N-4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_2CNS->N_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_4HO->H",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_N-4HO->H",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_N-4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_N-4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->O_4R-u1_N-4R->C_N-4HNO->N_Sp-2CNS-1C_N-2CNS->N_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
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
    index = 209,
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
    index = 210,
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
    index = 211,
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
    index = 212,
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
    index = 213,
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
    index = 214,
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
    index = 215,
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
    index = 216,
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
    index = 217,
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
    index = 218,
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
    index = 219,
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
    index = 220,
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
    index = 221,
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
    index = 222,
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
    index = 223,
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
    index = 224,
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
    index = 225,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.06018e-05,'m^3/(mol*s)'), n=3.06568, w0=(563000,'J/mol'), E0=(-121532,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_Ext-1C-R_2R!H->C_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.13319e-11,'m^3/(mol*s)'), n=4.87187, w0=(563000,'J/mol'), E0=(52252.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7604232513774859, var=9.626659727212548, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 8.130674420636078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.130674420636078""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.130674420636078
""",
)

entry(
    index = 227,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(935562,'m^3/(mol*s)'), n=-0.468454, w0=(563000,'J/mol'), E0=(41637.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07198394380306895, var=0.29387018829524825, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C
    Total Standard Deviation in ln(k): 1.2676269578242534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 1.2676269578242534""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 1.2676269578242534
""",
)

entry(
    index = 228,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(602200,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(40463,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(85317.5,'m^3/(mol*s)'), n=0.507944, w0=(539000,'J/mol'), E0=(76678.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38565393443981943, var=6.259911683362028, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 5.984789913784306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 5.984789913784306""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 5.984789913784306
""",
)

entry(
    index = 230,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(356.108,'m^3/(mol*s)'), n=0.71805, w0=(539000,'J/mol'), E0=(25900.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3721653743406529, var=46.9903889240978, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 14.677454825724896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 14.677454825724896""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 14.677454825724896
""",
)

entry(
    index = 231,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(0.305186,'m^3/(mol*s)'), n=1.55342, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.389299284428404, var=3.22953578295321, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R
    Total Standard Deviation in ln(k): 7.093392928837358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R
Total Standard Deviation in ln(k): 7.093392928837358""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R
Total Standard Deviation in ln(k): 7.093392928837358
""",
)

entry(
    index = 232,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C",
    kinetics = ArrheniusBM(A=(19606.7,'m^3/(mol*s)'), n=0.562334, w0=(511250,'J/mol'), E0=(12520.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.244150977695564, var=0.006296441851900142, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C
    Total Standard Deviation in ln(k): 5.797646268566209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C
Total Standard Deviation in ln(k): 5.797646268566209""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C
Total Standard Deviation in ln(k): 5.797646268566209
""",
)

entry(
    index = 233,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_N-5CO->C",
    kinetics = ArrheniusBM(A=(0.172768,'m^3/(mol*s)'), n=1.97207, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_N-5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_N-5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R",
    kinetics = ArrheniusBM(A=(1.52735e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 235,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C",
    kinetics = ArrheniusBM(A=(3.62392e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.9663235732869484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C
    Total Standard Deviation in ln(k): 1.9706898352295663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 1.9706898352295663""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 1.9706898352295663
""",
)

entry(
    index = 236,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.7641e+06,'m^3/(mol*s)'), n=-0.0462319, w0=(561500,'J/mol'), E0=(17554.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2144940523654643, var=1.5169644222011907, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C
    Total Standard Deviation in ln(k): 3.008063935012343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 3.008063935012343""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 3.008063935012343
""",
)

entry(
    index = 237,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-4CHNS-R",
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(85952.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-4CHNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-4CHNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-4CHNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-4CHNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(5.02669e-06,'m^3/(mol*s)'), n=3.68836, w0=(539000,'J/mol'), E0=(30229.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007352480326336509, var=0.21863088705753284, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-5CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-5CO-R
    Total Standard Deviation in ln(k): 0.9558472331216682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-5CO-R
Total Standard Deviation in ln(k): 0.9558472331216682""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_N-Sp-6R!H-1C_Ext-5CO-R
Total Standard Deviation in ln(k): 0.9558472331216682
""",
)

entry(
    index = 239,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C",
    kinetics = ArrheniusBM(A=(906156,'m^3/(mol*s)'), n=-0.0158163, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0014986669398614483, var=0.4970363515235185, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C
    Total Standard Deviation in ln(k): 1.4171198638670948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C
Total Standard Deviation in ln(k): 1.4171198638670948""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C
Total Standard Deviation in ln(k): 1.4171198638670948
""",
)

entry(
    index = 240,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C",
    kinetics = ArrheniusBM(A=(6.41947,'m^3/(mol*s)'), n=1.17357, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.5769113207128034, var=36.01419836199652, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C
    Total Standard Deviation in ln(k): 21.017996600377636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C
Total Standard Deviation in ln(k): 21.017996600377636""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C
Total Standard Deviation in ln(k): 21.017996600377636
""",
)

entry(
    index = 241,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(84300,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(76690.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Ext-5CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Sp-5CO-4CCHNOS",
    kinetics = ArrheniusBM(A=(964000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(92497.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Sp-5CO-4CCHNOS',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Sp-5CO-4CCHNOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Sp-5CO-4CCHNOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_Sp-5CO-4CCHNOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_N-Sp-5CO-4CCHNOS",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_N-Sp-5CO-4CCHNOS',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_N-Sp-5CO-4CCHNOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_N-Sp-5CO-4CCHNOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_N-Sp-6C-1C_N-Sp-5CO-4CCHNOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R",
    kinetics = ArrheniusBM(A=(7.76827e+08,'m^3/(mol*s)'), n=-0.9, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0763652085225523e-17, var=0.04891149884417046, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R
    Total Standard Deviation in ln(k): 0.4433660913390881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R
Total Standard Deviation in ln(k): 0.4433660913390881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R
Total Standard Deviation in ln(k): 0.4433660913390881
""",
)

entry(
    index = 245,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.29e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
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
    index = 247,
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
    index = 248,
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
    index = 249,
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
    index = 250,
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
    index = 251,
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
    index = 252,
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
    index = 253,
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
    index = 254,
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
    index = 255,
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
    index = 256,
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
    index = 257,
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
    index = 258,
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
    index = 259,
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
    index = 260,
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
    index = 261,
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
    index = 262,
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
    index = 263,
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
    index = 264,
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
    index = 265,
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
    index = 266,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.47923e-05,'m^3/(mol*s)'), n=2.95159, w0=(563000,'J/mol'), E0=(48771.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_5R!H-u0_2R!H->C_Ext-2C-R_6R!H->C_Ext-6C-R_Sp-7R!H-6C_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-1.94626e-08, w0=(563000,'J/mol'), E0=(19905.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.122945412774981e-10, var=4.0371937089716863e-17, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.452755392867016e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.452755392867016e-08""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.452755392867016e-08
""",
)

entry(
    index = 268,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10974.5,'m^3/(mol*s)'), n=7.68845e-08, w0=(563000,'J/mol'), E0=(19802.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2290956255676566e-17, var=0.06917824979652494, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.5272805777722495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495
""",
)

entry(
    index = 269,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R",
    kinetics = ArrheniusBM(A=(1.51978,'m^3/(mol*s)'), n=1.84974, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1529830156382754, var=2.8072952341908874, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R
    Total Standard Deviation in ln(k): 6.255872871813162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R
Total Standard Deviation in ln(k): 6.255872871813162""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R
Total Standard Deviation in ln(k): 6.255872871813162
""",
)

entry(
    index = 270,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-5CO-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(555.239,'m^3/(mol*s)'), n=0.880729, w0=(539000,'J/mol'), E0=(54160.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0814286213754447, var=0.6626228803060366, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-5CO-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-5CO-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 6.861607607543792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-5CO-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 6.861607607543792""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-5CO-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 6.861607607543792
""",
)

entry(
    index = 271,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0",
    kinetics = ArrheniusBM(A=(3.43746e+08,'m^3/(mol*s)'), n=-0.679201, w0=(539000,'J/mol'), E0=(73726,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.089000841221037, var=14.551055632632918, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0
    Total Standard Deviation in ln(k): 10.383414561485337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0
Total Standard Deviation in ln(k): 10.383414561485337""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0
Total Standard Deviation in ln(k): 10.383414561485337
""",
)

entry(
    index = 272,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_N-8R!H-u0",
    kinetics = ArrheniusBM(A=(2.32921e-06,'m^3/(mol*s)'), n=2.10129, w0=(539000,'J/mol'), E0=(47978.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_N-8R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_N-8R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_N-8R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_N-8R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 273,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R_Ext-4CHNS-R",
    kinetics = ArrheniusBM(A=(1.88635e-06,'m^3/(mol*s)'), n=2.93543, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R_Ext-4CHNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R_Ext-4CHNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R_Ext-4CHNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_N-7R!H-u0_Ext-5CO-R_Ext-4CHNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_1C-inRing",
    kinetics = ArrheniusBM(A=(0.000675,'m^3/(mol*s)'), n=2.7, w0=(483500,'J/mol'), E0=(35785.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 275,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(0.000166502,'m^3/(mol*s)'), n=2.99554, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_N-Sp-5CO-4CCHNOS_7R!H-u0_5CO->C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 276,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_Ext-4CHNS-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.56e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C_Ext-7R!H-R_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=0, w0=(561500,'J/mol'), E0=(36677.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C_Ext-7R!H-R_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C_Ext-7R!H-R_Ext-5CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C_Ext-7R!H-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_Ext-4CHNS-R_Sp-6R!H-1C_N-2R!H->C_Ext-7R!H-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C",
    kinetics = ArrheniusBM(A=(1.25533e+06,'m^3/(mol*s)'), n=-0.0210882, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0019982334851446305, var=0.12034253857762967, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C
    Total Standard Deviation in ln(k): 0.7004717475701124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C
Total Standard Deviation in ln(k): 0.7004717475701124""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C
Total Standard Deviation in ln(k): 0.7004717475701124
""",
)

entry(
    index = 280,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C",
    kinetics = ArrheniusBM(A=(340826,'m^3/(mol*s)'), n=-2.03079e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 281,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.55713e+06,'m^3/(mol*s)'), n=-0.267658, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27677043112298655, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.6954030932738355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.6954030932738355""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.6954030932738355
""",
)

entry(
    index = 282,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R_Ext-4CHNS-R",
    kinetics = ArrheniusBM(A=(2.86e+09,'m^3/(mol*s)'), n=-1.1, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R_Ext-4CHNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R_Ext-4CHNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R_Ext-4CHNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_2R!H->C_5CO->C_Sp-5C-4CHNS_Ext-4CHNS-R_Ext-4CHNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
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
    index = 284,
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
    index = 285,
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
    index = 286,
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
    index = 287,
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
    index = 288,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=5.24452e-08, w0=(563000,'J/mol'), E0=(21124.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 289,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(9.6486e-05,'m^3/(mol*s)'), n=2.97719, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R_Ext-5CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_Sp-7R!H-6R!H_Ext-4CHNS-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R",
    kinetics = ArrheniusBM(A=(532734,'m^3/(mol*s)'), n=-0.112321, w0=(539000,'J/mol'), E0=(53199,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.670735619744284, var=0.13435373553625868, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R
    Total Standard Deviation in ln(k): 4.932649703217485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R
Total Standard Deviation in ln(k): 4.932649703217485""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R
Total Standard Deviation in ln(k): 4.932649703217485
""",
)

entry(
    index = 291,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(974410,'m^3/(mol*s)'), n=-0.0210882, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00199823545031128, var=3.088879903029536e-05, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.01616254705267359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.01616254705267359""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.01616254705267359
""",
)

entry(
    index = 292,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(1.8697e+06,'m^3/(mol*s)'), n=-0.0316323, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0327092327690802, var=0.00213978781668374, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C
    Total Standard Deviation in ln(k): 0.1749187175813773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C
Total Standard Deviation in ln(k): 0.1749187175813773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C
Total Standard Deviation in ln(k): 0.1749187175813773
""",
)

entry(
    index = 293,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(241000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_N-5CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R_Ext-5CO-R",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R_Ext-5CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R_Ext-5CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_N-4CHNS->C_Ext-1C-R_Ext-5CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(20706.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_4R->O_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_Sp-8R!H-5CO",
    kinetics = ArrheniusBM(A=(3.74759e-05,'m^3/(mol*s)'), n=2.98945, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_Sp-8R!H-5CO',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_Sp-8R!H-5CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_Sp-8R!H-5CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_Sp-8R!H-5CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_N-Sp-8R!H-5CO",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(26972.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_N-Sp-8R!H-5CO',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_N-Sp-8R!H-5CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_N-Sp-8R!H-5CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_Ext-2R!H-R_Ext-6R!H-R_Sp-5CO-4CCHNOS_7R!H-u0_N-Sp-7R!H-6R!H_Ext-5CO-R_8R!H-u0_Ext-4CHNS-R_N-Sp-8R!H-5CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(783000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Ext-1C-R_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_Ext-4R-R_N-4R->O_N-5R!H->S_N-Sp-5CCCCCHHNNOOOSS#4CCCCCCHHHNNNOOOSSS_Ext-1C-R_6R!H->C_Sp-6C-1C_4CHNS->C_5CO->C_Sp-5C-4C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

