#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(110.345,'m^3/(mol*s)'), n=1.50019, w0=(579365,'J/mol'), E0=(15548.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.019669128973821174, var=2.255144172782069, Tref=1000.0, N=163, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 163 training reactions at node Root
    Total Standard Deviation in ln(k): 3.0599581434253174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 163 training reactions at node Root
Total Standard Deviation in ln(k): 3.0599581434253174""",
    longDesc = 
"""
BM rule fitted to 163 training reactions at node Root
Total Standard Deviation in ln(k): 3.0599581434253174
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(1016.14,'m^3/(mol*s)'), n=1.22322, w0=(559770,'J/mol'), E0=(58886.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0318903845861089, var=2.6870857293178845, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 102 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 3.36635504052571"""),
    rank = 11,
    shortDesc = """BM rule fitted to 102 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.36635504052571""",
    longDesc = 
"""
BM rule fitted to 102 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.36635504052571
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
    label = "Root_1R!H->C_4R->O",
    kinetics = ArrheniusBM(A=(118.179,'m^3/(mol*s)'), n=1.57967, w0=(580610,'J/mol'), E0=(75290.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012214750634996207, var=1.226662916173026, Tref=1000.0, N=41, data_mean=0.0, correlation='Root_1R!H->C_4R->O',), comment="""BM rule fitted to 41 training reactions at node Root_1R!H->C_4R->O
    Total Standard Deviation in ln(k): 2.251030964939162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 41 training reactions at node Root_1R!H->C_4R->O
Total Standard Deviation in ln(k): 2.251030964939162""",
    longDesc = 
"""
BM rule fitted to 41 training reactions at node Root_1R!H->C_4R->O
Total Standard Deviation in ln(k): 2.251030964939162
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-4R->O",
    kinetics = ArrheniusBM(A=(605.535,'m^3/(mol*s)'), n=1.24986, w0=(545762,'J/mol'), E0=(50333.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0244512260988796, var=4.110911095964789, Tref=1000.0, N=61, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O',), comment="""BM rule fitted to 61 training reactions at node Root_1R!H->C_N-4R->O
    Total Standard Deviation in ln(k): 4.126112163821497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 61 training reactions at node Root_1R!H->C_N-4R->O
Total Standard Deviation in ln(k): 4.126112163821497""",
    longDesc = 
"""
BM rule fitted to 61 training reactions at node Root_1R!H->C_N-4R->O
Total Standard Deviation in ln(k): 4.126112163821497
""",
)

entry(
    index = 6,
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
    index = 7,
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
    index = 8,
    label = "Root_1R!H->C_4R->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(861.407,'m^3/(mol*s)'), n=1.30445, w0=(583125,'J/mol'), E0=(78022.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.764368065221838, var=20.722877490308985, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R',), comment="""BM rule fitted to 32 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R
    Total Standard Deviation in ln(k): 11.046555447436553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R
Total Standard Deviation in ln(k): 11.046555447436553""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R
Total Standard Deviation in ln(k): 11.046555447436553
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_4R->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4837.88,'m^3/(mol*s)'), n=0.973302, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09222638344445135, var=13.19948790734544, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R
    Total Standard Deviation in ln(k): 7.515147537915094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R
Total Standard Deviation in ln(k): 7.515147537915094""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R
Total Standard Deviation in ln(k): 7.515147537915094
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_4R->O_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(2492.55,'m^3/(mol*s)'), n=1.24309, w0=(581000,'J/mol'), E0=(58100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0483022450089369, var=3.484343477961573, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Sp-2R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 3.863480351476364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C
Total Standard Deviation in ln(k): 3.863480351476364""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C
Total Standard Deviation in ln(k): 3.863480351476364
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_4R->O_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(559.766,'m^3/(mol*s)'), n=1.30288, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05026334756798283, var=1.0164326719305483, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_4R->O_N-Sp-2R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 2.1474293546542333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 2.1474293546542333""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 2.1474293546542333
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1",
    kinetics = ArrheniusBM(A=(591.068,'m^3/(mol*s)'), n=1.25288, w0=(544517,'J/mol'), E0=(50333.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02505385602921301, var=4.056400363409935, Tref=1000.0, N=58, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1',), comment="""BM rule fitted to 58 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1
    Total Standard Deviation in ln(k): 4.100587543241366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 58 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1
Total Standard Deviation in ln(k): 4.100587543241366""",
    longDesc = 
"""
BM rule fitted to 58 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1
Total Standard Deviation in ln(k): 4.100587543241366
""",
)

entry(
    index = 13,
    label = "Root_1R!H->C_N-4R->O_N-4CHNS-u1",
    kinetics = ArrheniusBM(A=(2.65103e+18,'m^3/(mol*s)'), n=-2.996, w0=(569833,'J/mol'), E0=(56983.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41352317381529535, var=218.8359188126463, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_N-4CHNS-u1',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1
    Total Standard Deviation in ln(k): 30.695256957677078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1
Total Standard Deviation in ln(k): 30.695256957677078""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1
Total Standard Deviation in ln(k): 30.695256957677078
""",
)

entry(
    index = 14,
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
    index = 15,
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
    index = 16,
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
    index = 17,
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
    index = 18,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(51.2817,'m^3/(mol*s)'), n=1.66584, w0=(594278,'J/mol'), E0=(71005.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.593949603255487, var=32.14366730844496, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0',), comment="""BM rule fitted to 18 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0
    Total Standard Deviation in ln(k): 12.85825847952329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 12.85825847952329""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 12.85825847952329
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(0.00115552,'m^3/(mol*s)'), n=2.36408, w0=(568786,'J/mol'), E0=(22572.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03668723919388507, var=13.484382262335048, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0',), comment="""BM rule fitted to 14 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 7.453784100302378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 7.453784100302378""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 7.453784100302378
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(1.70765e+07,'m^3/(mol*s)'), n=7.53848e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9494596051172368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 1.9534182263699047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 1.9534182263699047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 1.9534182263699047
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1",
    kinetics = ArrheniusBM(A=(383.414,'m^3/(mol*s)'), n=1.41908, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2983662469973947, var=5.131928286299004, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1
    Total Standard Deviation in ln(k): 7.803705422168636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1
Total Standard Deviation in ln(k): 7.803705422168636""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1
Total Standard Deviation in ln(k): 7.803705422168636
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_4R->O_Sp-2R!H-1C_N-4O-u1",
    kinetics = ArrheniusBM(A=(500,'m^3/(mol*s)'), n=1.5, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Sp-2R!H-1C_N-4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_N-4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1",
    kinetics = ArrheniusBM(A=(178.214,'m^3/(mol*s)'), n=1.42089, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 25,
    label = "Root_1R!H->C_4R->O_N-Sp-2R!H-1C_N-4O-u1",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_N-Sp-2R!H-1C_N-4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C_N-4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H",
    kinetics = ArrheniusBM(A=(14298.2,'m^3/(mol*s)'), n=1.06507, w0=(568857,'J/mol'), E0=(47106.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.030183570175825583, var=0.9560857360428918, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H
    Total Standard Deviation in ln(k): 2.0360607922358094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H
Total Standard Deviation in ln(k): 2.0360607922358094""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H
Total Standard Deviation in ln(k): 2.0360607922358094
""",
)

entry(
    index = 27,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H",
    kinetics = ArrheniusBM(A=(146.74,'m^3/(mol*s)'), n=1.30398, w0=(541176,'J/mol'), E0=(46896.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.031248829396794364, var=1.0406633856677976, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H',), comment="""BM rule fitted to 51 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H
    Total Standard Deviation in ln(k): 2.1236032418800375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H
Total Standard Deviation in ln(k): 2.1236032418800375""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H
Total Standard Deviation in ln(k): 2.1236032418800375
""",
)

entry(
    index = 28,
    label = "Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C",
    kinetics = ArrheniusBM(A=(7.3811e+06,'m^3/(mol*s)'), n=4.74224e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=15.80567206157525, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C
    Total Standard Deviation in ln(k): 7.970094538116895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C
Total Standard Deviation in ln(k): 7.970094538116895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C
Total Standard Deviation in ln(k): 7.970094538116895
""",
)

entry(
    index = 29,
    label = "Root_1R!H->C_N-4R->O_N-4CHNS-u1_N-2R!H->C",
    kinetics = ArrheniusBM(A=(6.90291e-05,'m^3/(mol*s)'), n=4.10425, w0=(631500,'J/mol'), E0=(63150,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_N-4CHNS-u1_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
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
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C",
    kinetics = ArrheniusBM(A=(0.00116073,'m^3/(mol*s)'), n=2.81919, w0=(563000,'J/mol'), E0=(-12229.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03365747214953182, var=114.31831797435886, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C
    Total Standard Deviation in ln(k): 21.51914277085266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C
Total Standard Deviation in ln(k): 21.51914277085266""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C
Total Standard Deviation in ln(k): 21.51914277085266
""",
)

entry(
    index = 37,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C",
    kinetics = ArrheniusBM(A=(8.26419,'m^3/(mol*s)'), n=1.89458, w0=(643429,'J/mol'), E0=(58552.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21351124886884315, var=4.014055527784434, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C
    Total Standard Deviation in ln(k): 4.552968804026087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C
Total Standard Deviation in ln(k): 4.552968804026087""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C
Total Standard Deviation in ln(k): 4.552968804026087
""",
)

entry(
    index = 38,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_1C-inRing",
    kinetics = ArrheniusBM(A=(4.76242,'m^3/(mol*s)'), n=2.49162, w0=(563000,'J/mol'), E0=(17534.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing",
    kinetics = ArrheniusBM(A=(0.000257119,'m^3/(mol*s)'), n=2.46251, w0=(569231,'J/mol'), E0=(21082,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05652996567394083, var=4.228379477985215, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing
    Total Standard Deviation in ln(k): 4.26437660054394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing
Total Standard Deviation in ln(k): 4.26437660054394""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing
Total Standard Deviation in ln(k): 4.26437660054394
""",
)

entry(
    index = 40,
    label = "Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_2R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_N-2R!H->C",
    kinetics = ArrheniusBM(A=(3.6,'m^3/(mol*s)'), n=2, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Sp-2R!H-1C_4O-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_N-Sp-2R!H-1C_4O-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C",
    kinetics = ArrheniusBM(A=(1.80766e+06,'m^3/(mol*s)'), n=1.76405e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3986168174433896e-07, var=1.078433666146626, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C
    Total Standard Deviation in ln(k): 2.081870835278338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C
Total Standard Deviation in ln(k): 2.081870835278338""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C
Total Standard Deviation in ln(k): 2.081870835278338
""",
)

entry(
    index = 45,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C",
    kinetics = ArrheniusBM(A=(14210.3,'m^3/(mol*s)'), n=1.06643, w0=(583375,'J/mol'), E0=(48221.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006942402741823475, var=0.9857268348599192, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C
    Total Standard Deviation in ln(k): 2.0078199239458105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C
Total Standard Deviation in ln(k): 2.0078199239458105""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C
Total Standard Deviation in ln(k): 2.0078199239458105
""",
)

entry(
    index = 46,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(723.197,'m^3/(mol*s)'), n=0.902545, w0=(535868,'J/mol'), E0=(-20081.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0297831863127156, var=33.8269091687174, Tref=1000.0, N=34, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R',), comment="""BM rule fitted to 34 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R
    Total Standard Deviation in ln(k): 16.759678473261754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R
Total Standard Deviation in ln(k): 16.759678473261754""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R
Total Standard Deviation in ln(k): 16.759678473261754
""",
)

entry(
    index = 47,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2078.94,'m^3/(mol*s)'), n=1.02188, w0=(540167,'J/mol'), E0=(62330.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01154323623087242, var=0.6940893210264124, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.6991884589554576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6991884589554576""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6991884589554576
""",
)

entry(
    index = 48,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C",
    kinetics = ArrheniusBM(A=(6.06686e+07,'m^3/(mol*s)'), n=-0.492908, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0007493390676072279, var=0.16585651816455974, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C
    Total Standard Deviation in ln(k): 0.8183208577945337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C
Total Standard Deviation in ln(k): 0.8183208577945337""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C
Total Standard Deviation in ln(k): 0.8183208577945337
""",
)

entry(
    index = 49,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C",
    kinetics = ArrheniusBM(A=(98.6867,'m^3/(mol*s)'), n=1.34599, w0=(574667,'J/mol'), E0=(46353.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05168583155597725, var=0.6703531207465165, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C
    Total Standard Deviation in ln(k): 1.7712426507049475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C
Total Standard Deviation in ln(k): 1.7712426507049475""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C
Total Standard Deviation in ln(k): 1.7712426507049475
""",
)

entry(
    index = 50,
    label = "Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_N-4CHNS-u1_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C",
    kinetics = ArrheniusBM(A=(10114.1,'m^3/(mol*s)'), n=1.0662, w0=(591667,'J/mol'), E0=(59166.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04115737528167287, var=0.520316344789736, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C
    Total Standard Deviation in ln(k): 1.5494851767639202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C
Total Standard Deviation in ln(k): 1.5494851767639202""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C
Total Standard Deviation in ln(k): 1.5494851767639202
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C",
    kinetics = ArrheniusBM(A=(587.901,'m^3/(mol*s)'), n=1.41727, w0=(618000,'J/mol'), E0=(45060,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06640401910100215, var=0.26094188700249565, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C
    Total Standard Deviation in ln(k): 1.190912488846253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C
Total Standard Deviation in ln(k): 1.190912488846253""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C
Total Standard Deviation in ln(k): 1.190912488846253
""",
)

entry(
    index = 53,
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
    index = 54,
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
    index = 55,
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
    index = 56,
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
    index = 57,
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
    index = 58,
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
    index = 59,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C",
    kinetics = ArrheniusBM(A=(0.615829,'m^3/(mol*s)'), n=1.96425, w0=(571875,'J/mol'), E0=(75296.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3104586047403263, var=0.9595215316593622, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C
    Total Standard Deviation in ln(k): 2.743788397345642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C
Total Standard Deviation in ln(k): 2.743788397345642""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C
Total Standard Deviation in ln(k): 2.743788397345642
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C",
    kinetics = ArrheniusBM(A=(29.5049,'m^3/(mol*s)'), n=1.59245, w0=(592750,'J/mol'), E0=(19598.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.069596137450727, var=1.5113316212548111, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C
    Total Standard Deviation in ln(k): 2.6394103572058367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C
Total Standard Deviation in ln(k): 2.6394103572058367""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C
Total Standard Deviation in ln(k): 2.6394103572058367
""",
)

entry(
    index = 61,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(266748,'m^3/(mol*s)'), n=0.413307, w0=(563000,'J/mol'), E0=(41908,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26213255434780447, var=160.7129237554734, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 26.07317252501959"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 26.07317252501959""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 26.07317252501959
""",
)

entry(
    index = 62,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.0167484,'m^3/(mol*s)'), n=2.99233, w0=(563000,'J/mol'), E0=(42133.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.49089e-25,'m^3/(mol*s)'), n=8.48743, w0=(563000,'J/mol'), E0=(-29967.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.022519170807503302, var=20.03041458596872, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 9.028843070886655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.028843070886655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.028843070886655
""",
)

entry(
    index = 64,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.77348e-05,'m^3/(mol*s)'), n=3.6443, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.85542,'m^3/(mol*s)'), n=1.90074, w0=(641417,'J/mol'), E0=(64141.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0252634224345596, var=3.124392796769721, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 6.11959885314522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 6.11959885314522""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 6.11959885314522
""",
)

entry(
    index = 66,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(97648.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(0.00116599,'m^3/(mol*s)'), n=2.22344, w0=(571409,'J/mol'), E0=(2119.89,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22001670721257607, var=1.4233331077126632, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C',), comment="""BM rule fitted to 11 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 2.944525411234082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C
Total Standard Deviation in ln(k): 2.944525411234082""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C
Total Standard Deviation in ln(k): 2.944525411234082
""",
)

entry(
    index = 68,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(2.6e+09,'m^3/(mol*s)'), n=-1.26, w0=(551500,'J/mol'), E0=(34913.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.27916e+06,'m^3/(mol*s)'), n=-3.7648e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9639738002758667, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.9682923503688117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.9682923503688117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.9682923503688117
""",
)

entry(
    index = 70,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Ext-2NOS-R",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(46201.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Ext-2NOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Ext-2NOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Ext-2NOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Ext-2NOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(23588.5,'m^3/(mol*s)'), n=1.06552, w0=(609250,'J/mol'), E0=(60925,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6761713695632989, var=0.41113237262952895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C
    Total Standard Deviation in ln(k): 2.984351249045606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C
Total Standard Deviation in ln(k): 2.984351249045606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C
Total Standard Deviation in ln(k): 2.984351249045606
""",
)

entry(
    index = 72,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_N-Sp-2NOS-1C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(55750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_N-Sp-2NOS-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_N-Sp-2NOS-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_N-Sp-2NOS-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.96574e+06,'m^3/(mol*s)'), n=-0.201858, w0=(534200,'J/mol'), E0=(53420,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005671921424960416, var=0.8834587473346993, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.898551401026908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.898551401026908""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.898551401026908
""",
)

entry(
    index = 74,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(574.841,'m^3/(mol*s)'), n=0.925485, w0=(536075,'J/mol'), E0=(-11225,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.047151296960897, var=51.55032510896758, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 20 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 22.049867224151285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 22.049867224151285""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 22.049867224151285
""",
)

entry(
    index = 75,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.3989e+09,'m^3/(mol*s)'), n=-0.478623, w0=(539000,'J/mol'), E0=(98981.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2217062696518021, var=2.946286050630058, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.998128351758182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.998128351758182""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.998128351758182
""",
)

entry(
    index = 76,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_2R!H->C",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(26972.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1713.08,'m^3/(mol*s)'), n=1.04631, w0=(540750,'J/mol'), E0=(61802.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6075970314782776, var=0.6553537765114736, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C
    Total Standard Deviation in ln(k): 3.149537412505626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 3.149537412505626""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 3.149537412505626
""",
)

entry(
    index = 78,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(5.05038e+07,'m^3/(mol*s)'), n=-0.466181, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0008563873315993835, var=0.2016325975453334, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.9023483137133729"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.9023483137133729""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.9023483137133729
""",
)

entry(
    index = 79,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O",
    kinetics = ArrheniusBM(A=(138.869,'m^3/(mol*s)'), n=1.32417, w0=(631500,'J/mol'), E0=(63150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0821589152023126, var=17.193440351792404, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O
    Total Standard Deviation in ln(k): 11.031620954031357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O
Total Standard Deviation in ln(k): 11.031620954031357""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O
Total Standard Deviation in ln(k): 11.031620954031357
""",
)

entry(
    index = 80,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O",
    kinetics = ArrheniusBM(A=(98.658,'m^3/(mol*s)'), n=1.34601, w0=(546250,'J/mol'), E0=(46225.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.051647666175929925, var=0.6691031392404413, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O
    Total Standard Deviation in ln(k): 1.769615736047944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O
Total Standard Deviation in ln(k): 1.769615736047944""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O
Total Standard Deviation in ln(k): 1.769615736047944
""",
)

entry(
    index = 81,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi",
    kinetics = ArrheniusBM(A=(13116.2,'m^3/(mol*s)'), n=1.06552, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009683765652408772, var=0.10971138960797763, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 0.6883536488758378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi
Total Standard Deviation in ln(k): 0.6883536488758378""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi
Total Standard Deviation in ln(k): 0.6883536488758378
""",
)

entry(
    index = 82,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_N-Sp-2C-1BrClFINOPSSi",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(545000,'J/mol'), E0=(54500,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_N-Sp-2C-1BrClFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_N-Sp-2C-1BrClFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_N-Sp-2C-1BrClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_N-Sp-2C-1BrClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(648500,'J/mol'), E0=(59319.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1367.9,'m^3/(mol*s)'), n=1.28344, w0=(602750,'J/mol'), E0=(60275,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3312627342341653, var=0.027192120539529588, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 1.1628999139155172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.1628999139155172""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.1628999139155172
""",
)

entry(
    index = 85,
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
    index = 86,
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
    index = 87,
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
    index = 88,
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
    index = 89,
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
    index = 90,
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
    index = 91,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_4O-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_N-Sp-2R!H-1BrClFINOPSSi_N-4O-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
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
    index = 96,
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
    index = 97,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->S",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(513500,'J/mol'), E0=(42507.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_1NS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S",
    kinetics = ArrheniusBM(A=(34.41,'m^3/(mol*s)'), n=1.44661, w0=(544000,'J/mol'), E0=(54400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43780050013999694, var=0.5999111817527254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S
    Total Standard Deviation in ln(k): 2.6527474307051118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S
Total Standard Deviation in ln(k): 2.6527474307051118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S
Total Standard Deviation in ln(k): 2.6527474307051118
""",
)

entry(
    index = 99,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1",
    kinetics = ArrheniusBM(A=(0.000312293,'m^3/(mol*s)'), n=2.90354, w0=(587833,'J/mol'), E0=(53849,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1230320030307755, var=0.5384824975894967, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1
    Total Standard Deviation in ln(k): 1.7802276338704983"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1
Total Standard Deviation in ln(k): 1.7802276338704983""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1
Total Standard Deviation in ln(k): 1.7802276338704983
""",
)

entry(
    index = 100,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R",
    kinetics = ArrheniusBM(A=(44.6712,'m^3/(mol*s)'), n=1.62801, w0=(610875,'J/mol'), E0=(25269,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.619295161377688, var=5.687851574571153, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R
    Total Standard Deviation in ln(k): 6.337154207222094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R
Total Standard Deviation in ln(k): 6.337154207222094""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R
Total Standard Deviation in ln(k): 6.337154207222094
""",
)

entry(
    index = 102,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1",
    kinetics = ArrheniusBM(A=(116.606,'m^3/(mol*s)'), n=1.35374, w0=(594500,'J/mol'), E0=(42446.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07505693938603511, var=0.5657537030769392, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1
    Total Standard Deviation in ln(k): 1.6964788544158005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1
Total Standard Deviation in ln(k): 1.6964788544158005""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1
Total Standard Deviation in ln(k): 1.6964788544158005
""",
)

entry(
    index = 103,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(8.9512e-14,'m^3/(mol*s)'), n=5.66037, w0=(563000,'J/mol'), E0=(46200.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17507112726918075, var=4.749411396126074, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 4.808825291892647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R
Total Standard Deviation in ln(k): 4.808825291892647""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R
Total Standard Deviation in ln(k): 4.808825291892647
""",
)

entry(
    index = 105,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.35472e+37,'m^3/(mol*s)'), n=-8.93425, w0=(563000,'J/mol'), E0=(99348.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.024776490261907, var=554.6631210297729, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 49.788906540063884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 49.788906540063884""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 49.788906540063884
""",
)

entry(
    index = 106,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(6.05279e-06,'m^3/(mol*s)'), n=2.75866, w0=(563000,'J/mol'), E0=(118179,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(1430.42,'m^3/(mol*s)'), n=0.998435, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18936590804054595, var=2.2302102796052043, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O
    Total Standard Deviation in ln(k): 3.469642765548054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O
Total Standard Deviation in ln(k): 3.469642765548054""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O
Total Standard Deviation in ln(k): 3.469642765548054
""",
)

entry(
    index = 108,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C",
    kinetics = ArrheniusBM(A=(0.0337834,'m^3/(mol*s)'), n=1.77326, w0=(563000,'J/mol'), E0=(4756.14,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.35425002481536716, var=1.4344800175828984, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C
    Total Standard Deviation in ln(k): 3.2911422288849943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 3.2911422288849943""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 3.2911422288849943
""",
)

entry(
    index = 110,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.000371804,'m^3/(mol*s)'), n=2.67859, w0=(655500,'J/mol'), E0=(88984.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_2R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_2NOS->O",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(642000,'J/mol'), E0=(64200,'J/mol'), Tmin=(300,'K'), Tmax=(1000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_2NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_2NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_N-2NOS->O",
    kinetics = ArrheniusBM(A=(720,'m^3/(mol*s)'), n=1.5, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_N-2NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_N-2NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_N-2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_4CHNS->H_N-2R!H->C_Sp-2NOS-1C_N-2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C",
    kinetics = ArrheniusBM(A=(3.49726e+06,'m^3/(mol*s)'), n=-0.185408, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0007493433970125864, var=1.201264637628474, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C
    Total Standard Deviation in ln(k): 2.1991168991914556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C
Total Standard Deviation in ln(k): 2.1991168991914556""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C
Total Standard Deviation in ln(k): 2.1991168991914556
""",
)

entry(
    index = 115,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C",
    kinetics = ArrheniusBM(A=(6.55713e+06,'m^3/(mol*s)'), n=-0.267658, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27677043112298655, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C
    Total Standard Deviation in ln(k): 0.6954030932738355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C
Total Standard Deviation in ln(k): 0.6954030932738355""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C
Total Standard Deviation in ln(k): 0.6954030932738355
""",
)

entry(
    index = 116,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(538.082,'m^3/(mol*s)'), n=0.933483, w0=(533250,'J/mol'), E0=(-11436.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2485250225615583, var=55.499376703670556, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C',), comment="""BM rule fitted to 18 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 23.096979265979172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C
Total Standard Deviation in ln(k): 23.096979265979172""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C
Total Standard Deviation in ln(k): 23.096979265979172
""",
)

entry(
    index = 117,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.7641e+06,'m^3/(mol*s)'), n=-0.0462319, w0=(561500,'J/mol'), E0=(17554.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2144940523654643, var=1.5169644222011907, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 3.008063935012343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.008063935012343""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.008063935012343
""",
)

entry(
    index = 118,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0",
    kinetics = ArrheniusBM(A=(32.7938,'m^3/(mol*s)'), n=1.79449, w0=(539000,'J/mol'), E0=(83642.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005600626578768594, var=3.586951999710419, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0
    Total Standard Deviation in ln(k): 3.810889857326085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0
Total Standard Deviation in ln(k): 3.810889857326085""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0
Total Standard Deviation in ln(k): 3.810889857326085
""",
)

entry(
    index = 119,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_N-7R!H-u0",
    kinetics = ArrheniusBM(A=(0.00336809,'m^3/(mol*s)'), n=2.5889, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_N-7R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_N-7R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_4CNS->C",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(47358.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_4CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_4CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_N-4CNS->C",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_N-4CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_N-4CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_N-4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-2R!H-R_N-2R!H->C_N-4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS",
    kinetics = ArrheniusBM(A=(7.83959e+07,'m^3/(mol*s)'), n=-0.543877, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.000999118113520444, var=0.1419297158816419, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS
    Total Standard Deviation in ln(k): 0.7577654287519907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS
Total Standard Deviation in ln(k): 0.7577654287519907""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS
Total Standard Deviation in ln(k): 0.7577654287519907
""",
)

entry(
    index = 124,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(0.150092,'m^3/(mol*s)'), n=1.93096, w0=(631500,'J/mol'), E0=(63150,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_2NOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C",
    kinetics = ArrheniusBM(A=(187.67,'m^3/(mol*s)'), n=1.32723, w0=(551750,'J/mol'), E0=(56426,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5573994562006273, var=0.006231762284864146, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C
    Total Standard Deviation in ln(k): 1.5587579639955673"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C
Total Standard Deviation in ln(k): 1.5587579639955673""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C
Total Standard Deviation in ln(k): 1.5587579639955673
""",
)

entry(
    index = 126,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C",
    kinetics = ArrheniusBM(A=(71.6919,'m^3/(mol*s)'), n=1.35508, w0=(540750,'J/mol'), E0=(54075,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5686374312163178, var=0.771149536995697, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C
    Total Standard Deviation in ln(k): 3.1891977861734815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C
Total Standard Deviation in ln(k): 3.1891977861734815""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C
Total Standard Deviation in ln(k): 3.1891977861734815
""",
)

entry(
    index = 127,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(666000,'J/mol'), E0=(66600,'J/mol'), Tmin=(295,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(400,'m^3/(mol*s)'), n=1.5, w0=(564000,'J/mol'), E0=(56400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_2CN->C_Sp-2C-1BrClFINOPSSi_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_Sp-2N-1N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_Sp-2N-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_Sp-2N-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_Sp-2N-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_Sp-2N-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_N-Sp-2N-1N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(671000,'J/mol'), E0=(67100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_N-Sp-2N-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_N-Sp-2N-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_N-Sp-2N-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_4R->H_N-2R!H->O_2CN-u1_N-2CN->C_N-1BrClFINOPSSi->O_N-Sp-2N-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.41468e+08,'m^3/(mol*s)'), n=-0.287748, w0=(679500,'J/mol'), E0=(39776.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8677516935997125, var=3.3515988232698968, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 5.85042378949206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 5.85042378949206""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 5.85042378949206
""",
)

entry(
    index = 132,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(9.04e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_N-4O-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.06823e-33,'m^3/(mol*s)'), n=11.5608, w0=(648500,'J/mol'), E0=(-37786,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1311443344629586, var=3.4442370952847847, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 9.075152857245785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 9.075152857245785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 9.075152857245785
""",
)

entry(
    index = 136,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(573833,'J/mol'), E0=(21511.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03872283658228287, var=0.003687235162771551, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 0.2190263021681399"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 0.2190263021681399""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 0.2190263021681399
""",
)

entry(
    index = 137,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(662000,'J/mol'), E0=(66200,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(200.038,'m^3/(mol*s)'), n=1.42089, w0=(573833,'J/mol'), E0=(57383.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.054874661098006004, var=0.36033975866889256, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 1.3412845505876048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.3412845505876048""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.3412845505876048
""",
)

entry(
    index = 139,
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
    index = 140,
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
    index = 141,
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
    index = 142,
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
    index = 143,
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
    index = 144,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_Sp-2C-1N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(553500,'J/mol'), E0=(55350,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_N-Sp-2C-1N",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_N-Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_N-Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_2R!H->C_N-1BrClFINOPSSi->O_N-1NS->S_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(638000,'J/mol'), E0=(77381.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.00010394,'m^3/(mol*s)'), n=3.02774, w0=(562750,'J/mol'), E0=(47277.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8568478925825855, var=0.083327900484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 2.73158245570468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.73158245570468""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.73158245570468
""",
)

entry(
    index = 148,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_5R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(24711.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(24.3822,'m^3/(mol*s)'), n=1.74624, w0=(615000,'J/mol'), E0=(4836.05,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06763263468134857, var=0.8943979206627513, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N
    Total Standard Deviation in ln(k): 2.0658615974961876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N
Total Standard Deviation in ln(k): 2.0658615974961876""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N
Total Standard Deviation in ln(k): 2.0658615974961876
""",
)

entry(
    index = 150,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi",
    kinetics = ArrheniusBM(A=(97.18,'m^3/(mol*s)'), n=1.38035, w0=(581125,'J/mol'), E0=(36551.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11740613771597475, var=0.9685448374036849, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi
    Total Standard Deviation in ln(k): 2.2679438188850685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi
Total Standard Deviation in ln(k): 2.2679438188850685""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi
Total Standard Deviation in ln(k): 2.2679438188850685
""",
)

entry(
    index = 151,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(648000,'J/mol'), E0=(64800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_N-Sp-2NO-1BrClFINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.13319e-11,'m^3/(mol*s)'), n=4.87187, w0=(563000,'J/mol'), E0=(52252.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7604232513774859, var=9.626659727212548, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 8.130674420636078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.130674420636078""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.130674420636078
""",
)

entry(
    index = 153,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.28068e+54,'m^3/(mol*s)'), n=-13.6729, w0=(563000,'J/mol'), E0=(98492.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-14.503715032808914, var=306.25422247726704, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 71.52460076653797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 71.52460076653797""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 71.52460076653797
""",
)

entry(
    index = 154,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2122.75,'m^3/(mol*s)'), n=0.881357, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20022133163381345, var=1.263127558546822, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.756169331918214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.756169331918214""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.756169331918214
""",
)

entry(
    index = 155,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.17653,'m^3/(mol*s)'), n=1.10567, w0=(563000,'J/mol'), E0=(3072.28,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.314520698902224, var=1.2584318477413958, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.0391617910341244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.0391617910341244""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.0391617910341244
""",
)

entry(
    index = 156,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.23617e+06,'m^3/(mol*s)'), n=-0.166181, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0008563821550657155, var=1.421847219875964, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.39262258497754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.39262258497754""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.39262258497754
""",
)

entry(
    index = 157,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C_Ext-4S-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C_Ext-4S-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C_Ext-4S-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C_Ext-4S-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_N-4CNS->C_Ext-4S-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(19765.4,'m^3/(mol*s)'), n=0.561746, w0=(499250,'J/mol'), E0=(1847.19,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.064385616845779, var=9.132239647558421, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 8.732564074770606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 8.732564074770606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 8.732564074770606
""",
)

entry(
    index = 159,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C",
    kinetics = ArrheniusBM(A=(7.58651e-07,'m^3/(mol*s)'), n=3.15042, w0=(539000,'J/mol'), E0=(-22094.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.0511922627328874, var=96.85517886726262, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C
    Total Standard Deviation in ln(k): 27.395918248625478"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C
Total Standard Deviation in ln(k): 27.395918248625478""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C
Total Standard Deviation in ln(k): 27.395918248625478
""",
)

entry(
    index = 160,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_N-4CNS->C",
    kinetics = ArrheniusBM(A=(7.19e-07,'m^3/(mol*s)'), n=3.13, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_N-4CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_N-4CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_N-4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_N-4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C_Ext-4CNS-R_Ext-6R!H-R_Ext-4CNS-R_Ext-7R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=0, w0=(561500,'J/mol'), E0=(36677.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C_Ext-4CNS-R_Ext-6R!H-R_Ext-4CNS-R_Ext-7R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C_Ext-4CNS-R_Ext-6R!H-R_Ext-4CNS-R_Ext-7R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C_Ext-4CNS-R_Ext-6R!H-R_Ext-4CNS-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_N-2R!H->C_Ext-4CNS-R_Ext-6R!H-R_Ext-4CNS-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(5.02669e-06,'m^3/(mol*s)'), n=3.68836, w0=(539000,'J/mol'), E0=(30229.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007352480326336509, var=0.21863088705753284, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.9558472331216682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.9558472331216682""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_N-5R!H->C_Ext-4CNS-R_Ext-6R!H-R_7R!H-u0_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.9558472331216682
""",
)

entry(
    index = 163,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C",
    kinetics = ArrheniusBM(A=(1.51696e+08,'m^3/(mol*s)'), n=-0.652653, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011989420510271538, var=0.09452433595411674, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C
    Total Standard Deviation in ln(k): 0.6193644135015641"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C
Total Standard Deviation in ln(k): 0.6193644135015641""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C
Total Standard Deviation in ln(k): 0.6193644135015641
""",
)

entry(
    index = 164,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.89e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_2NS->S",
    kinetics = ArrheniusBM(A=(979000,'m^3/(mol*s)'), n=0, w0=(537500,'J/mol'), E0=(38210.6,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_2NS->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_2NS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_2NS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_2NS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_N-2NS->S",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=1.87, w0=(566000,'J/mol'), E0=(56600,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_N-2NS->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_N-2NS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_N-2NS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_Sp-2NS-1C_N-2NS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_4CNS->C",
    kinetics = ArrheniusBM(A=(0.81,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(54700,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_4CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_4CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_N-4CNS->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_N-4CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_N-4CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_N-4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_N-2R!H->C_N-2NOS->O_N-Sp-2NS-1C_N-4CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(1.89499e+08,'m^3/(mol*s)'), n=-0.346565, w0=(679500,'J/mol'), E0=(38476.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1578984580421725, var=4.595591047124435, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R
    Total Standard Deviation in ln(k): 7.206909289886282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R
Total Standard Deviation in ln(k): 7.206909289886282""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R
Total Standard Deviation in ln(k): 7.206909289886282
""",
)

entry(
    index = 170,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_2NO->O",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(635000,'J/mol'), E0=(6270.39,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.0294,'m^3/(mol*s)'), n=2.69, w0=(662000,'J/mol'), E0=(33464.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_2NO->O",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(625500,'J/mol'), E0=(26705.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(548000,'J/mol'), E0=(31955.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0426036023134155, var=0.11276809873671895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O
    Total Standard Deviation in ln(k): 3.2928163591177713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 3.2928163591177713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 3.2928163591177713
""",
)

entry(
    index = 174,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_2NO->O",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(625500,'J/mol'), E0=(55947.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(178.214,'m^3/(mol*s)'), n=1.42089, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 176,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(662000,'J/mol'), E0=(47976.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(323.865,'m^3/(mol*s)'), n=1.46107, w0=(586750,'J/mol'), E0=(42728,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23284945485790864, var=0.6476388655306268, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 2.1983797414238784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.1983797414238784""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.1983797414238784
""",
)

entry(
    index = 178,
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
    index = 179,
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
    index = 180,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_2NO->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(601500,'J/mol'), E0=(75336.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_4CNS->C_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(13374.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi",
    kinetics = ArrheniusBM(A=(30.945,'m^3/(mol*s)'), n=1.66369, w0=(623250,'J/mol'), E0=(10593.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1931314392317747, var=7.293392619087761, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi
    Total Standard Deviation in ln(k): 10.924424563505077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi
Total Standard Deviation in ln(k): 10.924424563505077""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi
Total Standard Deviation in ln(k): 10.924424563505077
""",
)

entry(
    index = 184,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1222.75,'m^3/(mol*s)'), n=1.08731, w0=(612000,'J/mol'), E0=(51891.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.880107590500096, var=0.27344860374733626, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 3.2596479531592055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 3.2596479531592055""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 3.2596479531592055
""",
)

entry(
    index = 185,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(81.7183,'m^3/(mol*s)'), n=1.38035, w0=(550250,'J/mol'), E0=(14285.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6204493662846748, var=3.9540263770573922, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 5.545280338111078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 5.545280338111078""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 5.545280338111078
""",
)

entry(
    index = 186,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.47923e-05,'m^3/(mol*s)'), n=2.95159, w0=(563000,'J/mol'), E0=(48771.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-2C-R_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.06018e-05,'m^3/(mol*s)'), n=3.06568, w0=(563000,'J/mol'), E0=(-121532,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_2R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(0.000815523,'m^3/(mol*s)'), n=2.84763, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.19405e-06,'m^3/(mol*s)'), n=3.85287, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.10728e-06,'m^3/(mol*s)'), n=3.28624, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_5R!H-u0_N-2R!H->C_N-5R!H->C_2NO->O_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(935562,'m^3/(mol*s)'), n=-0.468454, w0=(563000,'J/mol'), E0=(41637.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07198394380306895, var=0.29387018829524825, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C
    Total Standard Deviation in ln(k): 1.2676269578242534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 1.2676269578242534""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 1.2676269578242534
""",
)

entry(
    index = 192,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(602200,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(40463,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_Sp-7R!H#4C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_Sp-7R!H#4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_Sp-7R!H#4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_Sp-7R!H#4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_Sp-7R!H#4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C",
    kinetics = ArrheniusBM(A=(2.91732e+06,'m^3/(mol*s)'), n=-0.193877, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0009991190442675043, var=0.7512416561916286, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C
    Total Standard Deviation in ln(k): 1.7400983954314215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C
Total Standard Deviation in ln(k): 1.7400983954314215""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C
Total Standard Deviation in ln(k): 1.7400983954314215
""",
)

entry(
    index = 195,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_1C-inRing",
    kinetics = ArrheniusBM(A=(0.000675,'m^3/(mol*s)'), n=2.7, w0=(483500,'J/mol'), E0=(35785.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(515000,'J/mol'), E0=(39525.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_Ext-2C-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(2.08448e-07,'m^3/(mol*s)'), n=3.20805, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.883213386123314, var=150.4660351143206, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C
    Total Standard Deviation in ln(k): 36.860382529230534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C
Total Standard Deviation in ln(k): 36.860382529230534""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C
Total Standard Deviation in ln(k): 36.860382529230534
""",
)

entry(
    index = 198,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(380.667,'m^3/(mol*s)'), n=1.06464, w0=(539000,'J/mol'), E0=(77196.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17954591455064195, var=5.988389109992552, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 5.356944748096939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 5.356944748096939""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 5.356944748096939
""",
)

entry(
    index = 199,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS",
    kinetics = ArrheniusBM(A=(1.51619e+08,'m^3/(mol*s)'), n=-0.640816, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.001498677849822722, var=0.06565633740733616, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS
    Total Standard Deviation in ln(k): 0.517448666852609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS
Total Standard Deviation in ln(k): 0.517448666852609""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS
Total Standard Deviation in ln(k): 0.517448666852609
""",
)

entry(
    index = 200,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_N-Sp-5C-4CNS",
    kinetics = ArrheniusBM(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_N-Sp-5C-4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_N-Sp-5C-4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_N-Sp-5C-4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_N-Sp-5C-4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(2.11547e+08,'m^3/(mol*s)'), n=-0.313028, w0=(679500,'J/mol'), E0=(76755.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12167865343175763, var=0.6437215165799257, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0
    Total Standard Deviation in ln(k): 1.914169472146607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 1.914169472146607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 1.914169472146607
""",
)

entry(
    index = 202,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(5.7209e+06,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(20296,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_N-5R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(39565.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_Ext-4O-R_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_4O-u1_N-1BrClFINOPSSi->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_2NO->O",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(625500,'J/mol'), E0=(52128.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_N-2R!H->C_N-4O-u1_2NO-u1_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
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
    index = 210,
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
    index = 211,
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
    index = 212,
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
    index = 213,
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
    index = 214,
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
    index = 215,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(17330.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(648000,'J/mol'), E0=(54170.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_Ext-4NS-R_N-5R!H->N_N-Sp-5BrCClFIOPSSi-4BrCClFINOPSSSi_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_2NO->O",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(35268.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(625500,'J/mol'), E0=(51859.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_2NO->O",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(589000,'J/mol'), E0=(45404.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.46,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_N-4CNOS->O_N-2R!H->C_N-4CNS->C_2NO-u1_Sp-2NO-1BrClFINNOOPSSi_N-1BrClFINOPSSi->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-1.94626e-08, w0=(563000,'J/mol'), E0=(19905.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.122945412774981e-10, var=4.0371937089716863e-17, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.452755392867016e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.452755392867016e-08""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.452755392867016e-08
""",
)

entry(
    index = 222,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10974.5,'m^3/(mol*s)'), n=7.68845e-08, w0=(563000,'J/mol'), E0=(19802.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2290956255676566e-17, var=0.06917824979652494, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.5272805777722495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805777722495
""",
)

entry(
    index = 223,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C",
    kinetics = ArrheniusBM(A=(4.80372e+06,'m^3/(mol*s)'), n=-0.232653, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011989427634325857, var=0.3951773289456139, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C
    Total Standard Deviation in ln(k): 1.263251664934538"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C
Total Standard Deviation in ln(k): 1.263251664934538""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C
Total Standard Deviation in ln(k): 1.263251664934538
""",
)

entry(
    index = 224,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C",
    kinetics = ArrheniusBM(A=(241000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.26662e-08,'m^3/(mol*s)'), n=3.36145, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.347116510200216, var=161.36629395733547, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R
    Total Standard Deviation in ln(k): 38.90112249797567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 38.90112249797567""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 38.90112249797567
""",
)

entry(
    index = 226,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(934.663,'m^3/(mol*s)'), n=0.944116, w0=(539000,'J/mol'), E0=(77381.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27391051117805787, var=7.943538623916611, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R
    Total Standard Deviation in ln(k): 6.338419633545027"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 6.338419633545027""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 6.338419633545027
""",
)

entry(
    index = 227,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(7.76827e+08,'m^3/(mol*s)'), n=-0.9, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0763652085225523e-17, var=0.04891149884417046, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.4433660913390881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390881
""",
)

entry(
    index = 228,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.29e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(55695.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-4R->H_4CNOS->O_Sp-2R!H-1BrClFINOPSSi_2R!H->C_4O-u1_1BrClFINOPSSi->O_Ext-4O-R_5R!H-u0_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
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
    index = 232,
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
    index = 233,
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
    index = 234,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=5.24452e-08, w0=(563000,'J/mol'), E0=(21124.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 235,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.25814e+07,'m^3/(mol*s)'), n=-0.55, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.5036392791388526, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 3.7524652808647927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.7524652808647927""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.7524652808647927
""",
)

entry(
    index = 236,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(783000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_6R!H->S",
    kinetics = ArrheniusBM(A=(3.37e-12,'m^3/(mol*s)'), n=4.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_6R!H->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_6R!H->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_6R!H->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_6R!H->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S",
    kinetics = ArrheniusBM(A=(5.41335e+06,'m^3/(mol*s)'), n=-0.166181, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0008563831386432426, var=1.0055111747152845, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S
    Total Standard Deviation in ln(k): 2.0124034261200174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S
Total Standard Deviation in ln(k): 2.0124034261200174""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S
Total Standard Deviation in ln(k): 2.0124034261200174
""",
)

entry(
    index = 241,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(84300,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(76690.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.000740847,'m^3/(mol*s)'), n=2.91991, w0=(539000,'J/mol'), E0=(35253.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004220313209984355, var=8.94173911161422, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 6.005311154003196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 6.005311154003196""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 6.005311154003196
""",
)

entry(
    index = 243,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Sp-6R!H-4C",
    kinetics = ArrheniusBM(A=(964000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(92497.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Sp-6R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Sp-6R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Sp-6R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Sp-6R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_N-Sp-6R!H-4C",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_N-Sp-6R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_N-Sp-6R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_N-Sp-6R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_N-Sp-6R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.86e+09,'m^3/(mol*s)'), n=-1.1, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_2R!H->C_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_5R!H->C_Sp-5C-4CNS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(20706.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_4R->O_Ext-4O-R_N-5R!H-u0_N-1C-inRing_Sp-2R!H-1C_2R!H->C_Ext-1C-R_Sp-6R!H-1C_Ext-6R!H-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_Ext-1C-R_4CNS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C",
    kinetics = ArrheniusBM(A=(8.10096e+06,'m^3/(mol*s)'), n=-0.193877, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0009991181655658735, var=0.7345784173125115, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C
    Total Standard Deviation in ln(k): 1.7207196713689143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C
Total Standard Deviation in ln(k): 1.7207196713689143""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C
Total Standard Deviation in ln(k): 1.7207196713689143
""",
)

entry(
    index = 249,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_N-6BrCClFINOPSi->C",
    kinetics = ArrheniusBM(A=(482000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_N-6BrCClFINOPSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_N-6BrCClFINOPSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_N-6BrCClFINOPSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_N-6BrCClFINOPSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(85952.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_N-Sp-5C-1C_Ext-4C-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_Sp-6C#4C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_Sp-6C#4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_Sp-6C#4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_Sp-6C#4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_Sp-6C#4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C",
    kinetics = ArrheniusBM(A=(8.5937e+06,'m^3/(mol*s)'), n=-0.232653, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011989422368355676, var=0.48457443718748106, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C
    Total Standard Deviation in ln(k): 1.3985361914751913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C
Total Standard Deviation in ln(k): 1.3985361914751913""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C
Total Standard Deviation in ln(k): 1.3985361914751913
""",
)

entry(
    index = 253,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.05265e+08,'m^3/(mol*s)'), n=-0.55, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.513977146582821, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R
    Total Standard Deviation in ln(k): 3.75799723098171"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R
Total Standard Deviation in ln(k): 3.75799723098171""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R
Total Standard Deviation in ln(k): 3.75799723098171
""",
)

entry(
    index = 254,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C",
    kinetics = ArrheniusBM(A=(1.8697e+06,'m^3/(mol*s)'), n=-0.0316323, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0327092327690802, var=0.00213978781668374, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C
    Total Standard Deviation in ln(k): 0.1749187175813773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C
Total Standard Deviation in ln(k): 0.1749187175813773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C
Total Standard Deviation in ln(k): 0.1749187175813773
""",
)

entry(
    index = 255,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_N-Sp-6C-4C",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_N-Sp-6C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_N-Sp-6C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_N-Sp-6C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_N-Sp-6C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.16e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-4R->O_4CHNS-u1_N-4CHNS->H_Ext-1C-R_5R!H->C_2R!H->C_4CNS->C_Sp-5C-1C_Ext-4C-R_N-6R!H->S_6BrCClFINOPSi->C_N-Sp-6C#4C_Sp-6C-4C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

