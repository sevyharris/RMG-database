#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(111.018,'m^3/(mol*s)'), n=1.49949, w0=(577822,'J/mol'), E0=(15564.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01975156566475164, var=2.246644780649379, Tref=1000.0, N=152, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 152 training reactions at node Root
    Total Standard Deviation in ln(k): 3.0544867203718837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 152 training reactions at node Root
Total Standard Deviation in ln(k): 3.0544867203718837""",
    longDesc = 
"""
BM rule fitted to 152 training reactions at node Root
Total Standard Deviation in ln(k): 3.0544867203718837
""",
)

entry(
    index = 2,
    label = "Root_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(114.61,'m^3/(mol*s)'), n=1.18033, w0=(553932,'J/mol'), E0=(38501.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0038666922066979, var=29.235873741105824, Tref=1000.0, N=59, data_mean=0.0, correlation='Root_Ext-1R!H-R',), comment="""BM rule fitted to 59 training reactions at node Root_Ext-1R!H-R
    Total Standard Deviation in ln(k): 13.361922347761693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 59 training reactions at node Root_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.361922347761693""",
    longDesc = 
"""
BM rule fitted to 59 training reactions at node Root_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.361922347761693
""",
)

entry(
    index = 3,
    label = "Root_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(154.299,'m^3/(mol*s)'), n=1.47088, w0=(553571,'J/mol'), E0=(50333,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09034233551283415, var=3.449210481961154, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.9501948399034092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.9501948399034092""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.9501948399034092
""",
)

entry(
    index = 4,
    label = "Root_4R->H",
    kinetics = ArrheniusBM(A=(8648.38,'m^3/(mol*s)'), n=1.10157, w0=(591750,'J/mol'), E0=(66871.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06784737978773892, var=0.27416574596904336, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_4R->H',), comment="""BM rule fitted to 12 training reactions at node Root_4R->H
    Total Standard Deviation in ln(k): 1.2201669095283179"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_4R->H
Total Standard Deviation in ln(k): 1.2201669095283179""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_4R->H
Total Standard Deviation in ln(k): 1.2201669095283179
""",
)

entry(
    index = 5,
    label = "Root_N-4R->H",
    kinetics = ArrheniusBM(A=(49.7688,'m^3/(mol*s)'), n=1.57231, w0=(596905,'J/mol'), E0=(-2129.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0033137602877095803, var=2.095981329147553, Tref=1000.0, N=74, data_mean=0.0, correlation='Root_N-4R->H',), comment="""BM rule fitted to 74 training reactions at node Root_N-4R->H
    Total Standard Deviation in ln(k): 2.9106821161498964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 74 training reactions at node Root_N-4R->H
Total Standard Deviation in ln(k): 2.9106821161498964""",
    longDesc = 
"""
BM rule fitted to 74 training reactions at node Root_N-4R->H
Total Standard Deviation in ln(k): 2.9106821161498964
""",
)

entry(
    index = 6,
    label = "Root_Ext-1R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.607826,'m^3/(mol*s)'), n=1.89124, w0=(554220,'J/mol'), E0=(38464.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3880352747228053, var=29.700678141584937, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C',), comment="""BM rule fitted to 50 training reactions at node Root_Ext-1R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 14.412996905163531"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 14.412996905163531""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 14.412996905163531
""",
)

entry(
    index = 7,
    label = "Root_Ext-1R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.17838e+08,'m^3/(mol*s)'), n=-0.326383, w0=(552333,'J/mol'), E0=(12753.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12397587702922071, var=94.99015775638017, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-1R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 19.85022548382039"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 19.85022548382039""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 19.85022548382039
""",
)

entry(
    index = 8,
    label = "Root_Ext-2R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.58723e+13,'m^3/(mol*s)'), n=-2.23598, w0=(551000,'J/mol'), E0=(91278.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2202160600853793, var=10.39330756070133, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 9.528865376815661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 9.528865376815661""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 9.528865376815661
""",
)

entry(
    index = 9,
    label = "Root_Ext-2R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(528.116,'m^3/(mol*s)'), n=1.29972, w0=(554600,'J/mol'), E0=(41855.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.036891273548675274, var=3.635785350605757, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.915267451704155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.915267451704155""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.915267451704155
""",
)

entry(
    index = 10,
    label = "Root_4R->H_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(59256.5,'m^3/(mol*s)'), n=0.883826, w0=(591944,'J/mol'), E0=(73853.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0022378488613151682, var=0.2794645572503271, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H',), comment="""BM rule fitted to 9 training reactions at node Root_4R->H_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.0654140549582392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_4R->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.0654140549582392""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_4R->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.0654140549582392
""",
)

entry(
    index = 11,
    label = "Root_4R->H_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(591167,'J/mol'), E0=(59116.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04104070874570528, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->H_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 0.10311735865755094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.10311735865755094""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.10311735865755094
""",
)

entry(
    index = 12,
    label = "Root_N-4R->H_4CNOS-u1",
    kinetics = ArrheniusBM(A=(20.5646,'m^3/(mol*s)'), n=1.64165, w0=(595677,'J/mol'), E0=(-6323.55,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.001966439871152369, var=1.8063523685167153, Tref=1000.0, N=62, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1',), comment="""BM rule fitted to 62 training reactions at node Root_N-4R->H_4CNOS-u1
    Total Standard Deviation in ln(k): 2.699316955476462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 62 training reactions at node Root_N-4R->H_4CNOS-u1
Total Standard Deviation in ln(k): 2.699316955476462""",
    longDesc = 
"""
BM rule fitted to 62 training reactions at node Root_N-4R->H_4CNOS-u1
Total Standard Deviation in ln(k): 2.699316955476462
""",
)

entry(
    index = 13,
    label = "Root_N-4R->H_N-4CNOS-u1",
    kinetics = ArrheniusBM(A=(5294.86,'m^3/(mol*s)'), n=1.122, w0=(603250,'J/mol'), E0=(53974.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.048317425240651427, var=0.23779518721757892, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->H_N-4CNOS-u1
    Total Standard Deviation in ln(k): 1.0989945485886636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->H_N-4CNOS-u1
Total Standard Deviation in ln(k): 1.0989945485886636""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->H_N-4CNOS-u1
Total Standard Deviation in ln(k): 1.0989945485886636
""",
)

entry(
    index = 14,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1",
    kinetics = ArrheniusBM(A=(672.553,'m^3/(mol*s)'), n=0.899659, w0=(552927,'J/mol'), E0=(1626.34,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6298181154372702, var=29.380037193621234, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1',), comment="""BM rule fitted to 48 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1
    Total Standard Deviation in ln(k): 14.961357146917859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1
Total Standard Deviation in ln(k): 14.961357146917859""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1
Total Standard Deviation in ln(k): 14.961357146917859
""",
)

entry(
    index = 15,
    label = "Root_Ext-1R!H-R_5R!H->C_N-4R-u1",
    kinetics = ArrheniusBM(A=(7.86752e+23,'m^3/(mol*s)'), n=-4.494, w0=(585250,'J/mol'), E0=(58525,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.768980640021399, var=247.76784347197372, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_N-4R-u1',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_N-4R-u1
    Total Standard Deviation in ln(k): 48.56330829845029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_N-4R-u1
Total Standard Deviation in ln(k): 48.56330829845029""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_N-4R-u1
Total Standard Deviation in ln(k): 48.56330829845029
""",
)

entry(
    index = 16,
    label = "Root_Ext-1R!H-R_N-5R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(1.3989e+09,'m^3/(mol*s)'), n=-0.478623, w0=(539000,'J/mol'), E0=(98981.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2217062696518021, var=2.946286050630058, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_4R->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C
    Total Standard Deviation in ln(k): 3.998128351758182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C
Total Standard Deviation in ln(k): 3.998128351758182""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C
Total Standard Deviation in ln(k): 3.998128351758182
""",
)

entry(
    index = 17,
    label = "Root_Ext-1R!H-R_N-5R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(2.01886e+16,'m^3/(mol*s)'), n=-2.53677, w0=(563000,'J/mol'), E0=(29649.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2201063162156773, var=254.49390921012923, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_N-4R->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C
    Total Standard Deviation in ln(k): 32.53429946706639"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C
Total Standard Deviation in ln(k): 32.53429946706639""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C
Total Standard Deviation in ln(k): 32.53429946706639
""",
)

entry(
    index = 18,
    label = "Root_Ext-2R!H-R_5R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(26972.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(97648.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_Ext-2R!H-R_N-5R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(0.0167484,'m^3/(mol*s)'), n=2.99233, w0=(563000,'J/mol'), E0=(42133.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(528.581,'m^3/(mol*s)'), n=1.29948, w0=(552500,'J/mol'), E0=(41383.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03742144078335467, var=3.6378754547057093, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 3.9176981144902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.9176981144902""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.9176981144902
""",
)

entry(
    index = 22,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1",
    kinetics = ArrheniusBM(A=(100953,'m^3/(mol*s)'), n=0.813929, w0=(599125,'J/mol'), E0=(74644.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10915397846467265, var=0.5254344262735094, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1',), comment="""BM rule fitted to 8 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1
    Total Standard Deviation in ln(k): 1.7274256518777682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1
Total Standard Deviation in ln(k): 1.7274256518777682""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1
Total Standard Deviation in ln(k): 1.7274256518777682
""",
)

entry(
    index = 23,
    label = "Root_4R->H_Sp-2R!H-1R!H_N-2R!H-u1",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(55750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(608000,'J/mol'), E0=(60800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 26,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O",
    kinetics = ArrheniusBM(A=(0.144382,'m^3/(mol*s)'), n=2.33924, w0=(647000,'J/mol'), E0=(-6940.45,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27065935295436483, var=3.5200015939923177, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O',), comment="""BM rule fitted to 22 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O
    Total Standard Deviation in ln(k): 4.441265877637721"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O
Total Standard Deviation in ln(k): 4.441265877637721""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O
Total Standard Deviation in ln(k): 4.441265877637721
""",
)

entry(
    index = 27,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O",
    kinetics = ArrheniusBM(A=(31.2789,'m^3/(mol*s)'), n=1.57498, w0=(567450,'J/mol'), E0=(-18460.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014453480351379801, var=1.68293609920252, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O',), comment="""BM rule fitted to 40 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O
    Total Standard Deviation in ln(k): 2.6370185399546906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O
Total Standard Deviation in ln(k): 2.6370185399546906""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O
Total Standard Deviation in ln(k): 2.6370185399546906
""",
)

entry(
    index = 28,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O",
    kinetics = ArrheniusBM(A=(1.32353e+06,'m^3/(mol*s)'), n=0.450565, w0=(665667,'J/mol'), E0=(69586.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0728645453454118, var=4.66309051561373, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_1R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O
    Total Standard Deviation in ln(k): 7.024702622775238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O
Total Standard Deviation in ln(k): 7.024702622775238""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O
Total Standard Deviation in ln(k): 7.024702622775238
""",
)

entry(
    index = 29,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O",
    kinetics = ArrheniusBM(A=(5558.75,'m^3/(mol*s)'), n=1.11269, w0=(582444,'J/mol'), E0=(54576.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.015877944550363166, var=0.2594700756206364, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O
    Total Standard Deviation in ln(k): 1.0610704018991224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O
Total Standard Deviation in ln(k): 1.0610704018991224""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O
Total Standard Deviation in ln(k): 1.0610704018991224
""",
)

entry(
    index = 30,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.20479e+06,'m^3/(mol*s)'), n=0.0340971, w0=(565167,'J/mol'), E0=(51350.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.773422037082824, var=38.915904885707455, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R
    Total Standard Deviation in ln(k): 24.49958409105011"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R
Total Standard Deviation in ln(k): 24.49958409105011""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R
Total Standard Deviation in ln(k): 24.49958409105011
""",
)

entry(
    index = 31,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O",
    kinetics = ArrheniusBM(A=(1.57897e+06,'m^3/(mol*s)'), n=0.428492, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.291174470317604, var=31.6875934834746, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O
    Total Standard Deviation in ln(k): 12.016595574546544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O
Total Standard Deviation in ln(k): 12.016595574546544""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O
Total Standard Deviation in ln(k): 12.016595574546544
""",
)

entry(
    index = 32,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O",
    kinetics = ArrheniusBM(A=(0.0772252,'m^3/(mol*s)'), n=1.80776, w0=(543154,'J/mol'), E0=(28977.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5322812653494102, var=31.392788327299876, Tref=1000.0, N=39, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O',), comment="""BM rule fitted to 39 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O
    Total Standard Deviation in ln(k): 12.569773934618867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 39 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O
Total Standard Deviation in ln(k): 12.569773934618867""",
    longDesc = 
"""
BM rule fitted to 39 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O
Total Standard Deviation in ln(k): 12.569773934618867
""",
)

entry(
    index = 33,
    label = "Root_Ext-1R!H-R_5R!H->C_N-4R-u1_2R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_N-4R-u1_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_N-4R-u1_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_N-4R-u1_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_N-4R-u1_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_Ext-1R!H-R_5R!H->C_N-4R-u1_N-2R!H->C",
    kinetics = ArrheniusBM(A=(6.90291e-05,'m^3/(mol*s)'), n=4.10425, w0=(631500,'J/mol'), E0=(63150,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_N-4R-u1_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_N-4R-u1_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_N-4R-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_N-4R-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0",
    kinetics = ArrheniusBM(A=(32.7938,'m^3/(mol*s)'), n=1.79449, w0=(539000,'J/mol'), E0=(83642.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005600626578768594, var=3.586951999710419, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0
    Total Standard Deviation in ln(k): 3.810889857326085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0
Total Standard Deviation in ln(k): 3.810889857326085""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0
Total Standard Deviation in ln(k): 3.810889857326085
""",
)

entry(
    index = 36,
    label = "Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_N-7R!H-u0",
    kinetics = ArrheniusBM(A=(0.00336809,'m^3/(mol*s)'), n=2.5889, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_N-7R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_N-7R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_N-7R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(9.35472e+37,'m^3/(mol*s)'), n=-8.93425, w0=(563000,'J/mol'), E0=(99348.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.024776490261907, var=554.6631210297729, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 49.788906540063884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 49.788906540063884""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 49.788906540063884
""",
)

entry(
    index = 38,
    label = "Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_1R!H-inRing",
    kinetics = ArrheniusBM(A=(4.76242,'m^3/(mol*s)'), n=2.49162, w0=(563000,'J/mol'), E0=(17534.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(0.000555362,'m^3/(mol*s)'), n=3.11141, w0=(563000,'J/mol'), E0=(57677.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_4R->H",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(46201.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_4R->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_4R->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_4R->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_4R->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H",
    kinetics = ArrheniusBM(A=(340831,'m^3/(mol*s)'), n=0.433821, w0=(550833,'J/mol'), E0=(77633.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018504166564283952, var=0.42535074633987874, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H
    Total Standard Deviation in ln(k): 1.3539594375362136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H
Total Standard Deviation in ln(k): 1.3539594375362136""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H
Total Standard Deviation in ln(k): 1.3539594375362136
""",
)

entry(
    index = 42,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O",
    kinetics = ArrheniusBM(A=(677.321,'m^3/(mol*s)'), n=1.44792, w0=(657250,'J/mol'), E0=(58842.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03633496085430713, var=0.028750657654443026, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O
    Total Standard Deviation in ln(k): 0.43121712987894956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O
Total Standard Deviation in ln(k): 0.43121712987894956""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O
Total Standard Deviation in ln(k): 0.43121712987894956
""",
)

entry(
    index = 43,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O",
    kinetics = ArrheniusBM(A=(119884,'m^3/(mol*s)'), n=0.793481, w0=(579750,'J/mol'), E0=(76821.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13451436586717408, var=0.7097248998690975, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O
    Total Standard Deviation in ln(k): 2.02686830694364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O
Total Standard Deviation in ln(k): 2.02686830694364""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O
Total Standard Deviation in ln(k): 2.02686830694364
""",
)

entry(
    index = 44,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(545000,'J/mol'), E0=(54500,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(671000,'J/mol'), E0=(67100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C",
    kinetics = ArrheniusBM(A=(7.04353e+07,'m^3/(mol*s)'), n=-0.0906618, w0=(662885,'J/mol'), E0=(46772.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7230627371508705, var=4.869454767012759, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C
    Total Standard Deviation in ln(k): 6.240557588233397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 6.240557588233397""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 6.240557588233397
""",
)

entry(
    index = 47,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.133634,'m^3/(mol*s)'), n=2.34863, w0=(624056,'J/mol'), E0=(-7437.86,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24395271444071867, var=3.452049631590798, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C
    Total Standard Deviation in ln(k): 4.337682591669927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 4.337682591669927""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 4.337682591669927
""",
)

entry(
    index = 48,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O",
    kinetics = ArrheniusBM(A=(50.1876,'m^3/(mol*s)'), n=1.60079, w0=(590706,'J/mol'), E0=(27735.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.022078530933952043, var=1.5107681962068622, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O',), comment="""BM rule fitted to 17 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O
    Total Standard Deviation in ln(k): 2.519559951413002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O
Total Standard Deviation in ln(k): 2.519559951413002""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O
Total Standard Deviation in ln(k): 2.519559951413002
""",
)

entry(
    index = 49,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O",
    kinetics = ArrheniusBM(A=(11.1937,'m^3/(mol*s)'), n=1.62627, w0=(550261,'J/mol'), E0=(58703,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02753775146300797, var=1.3346672187543256, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O',), comment="""BM rule fitted to 23 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O
    Total Standard Deviation in ln(k): 2.385216627620847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O
Total Standard Deviation in ln(k): 2.385216627620847""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O
Total Standard Deviation in ln(k): 2.385216627620847
""",
)

entry(
    index = 50,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O_4CNOS->C",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_1R!H->O_4CNOS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_4CNOS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_4CNOS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_4CNOS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C",
    kinetics = ArrheniusBM(A=(3.08924e+06,'m^3/(mol*s)'), n=0.344613, w0=(670750,'J/mol'), E0=(71316.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2522028424953557, var=6.0581551465221715, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C
    Total Standard Deviation in ln(k): 8.080556867668387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C
Total Standard Deviation in ln(k): 8.080556867668387""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C
Total Standard Deviation in ln(k): 8.080556867668387
""",
)

entry(
    index = 52,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(8156.05,'m^3/(mol*s)'), n=1.09251, w0=(571333,'J/mol'), E0=(58822.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04148672189933723, var=0.2869361411102575, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 1.1781028172976358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 1.1781028172976358""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 1.1781028172976358
""",
)

entry(
    index = 53,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(604667,'J/mol'), E0=(60466.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04104071632119799, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 0.10311737769145222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 0.10311737769145222""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 0.10311737769145222
""",
)

entry(
    index = 54,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_1R!H-inRing",
    kinetics = ArrheniusBM(A=(0.000675,'m^3/(mol*s)'), n=2.7, w0=(483500,'J/mol'), E0=(35785.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(0.489015,'m^3/(mol*s)'), n=1.34505, w0=(581500,'J/mol'), E0=(13394.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07668869974909989, var=2.5660219355255696, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing
    Total Standard Deviation in ln(k): 3.4040317035157863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 3.4040317035157863""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 3.4040317035157863
""",
)

entry(
    index = 56,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.77348e-05,'m^3/(mol*s)'), n=3.6443, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.40519,'m^3/(mol*s)'), n=2.12278, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3516360389451068, var=3.6158740378042107, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C
    Total Standard Deviation in ln(k): 7.208164755401575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.208164755401575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.208164755401575
""",
)

entry(
    index = 58,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O",
    kinetics = ArrheniusBM(A=(4.95029e+14,'m^3/(mol*s)'), n=-2.5834, w0=(563000,'J/mol'), E0=(85327.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06553022637848653, var=4.37939982076235, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O
    Total Standard Deviation in ln(k): 4.3599610345813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O
Total Standard Deviation in ln(k): 4.3599610345813""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O
Total Standard Deviation in ln(k): 4.3599610345813
""",
)

entry(
    index = 59,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O",
    kinetics = ArrheniusBM(A=(0.0333837,'m^3/(mol*s)'), n=1.89343, w0=(538032,'J/mol'), E0=(-5525.29,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6147796908094463, var=34.171075565968565, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O',), comment="""BM rule fitted to 31 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O
    Total Standard Deviation in ln(k): 13.263558166763818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O
Total Standard Deviation in ln(k): 13.263558166763818""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O
Total Standard Deviation in ln(k): 13.263558166763818
""",
)

entry(
    index = 60,
    label = "Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.02669e-06,'m^3/(mol*s)'), n=3.68836, w0=(539000,'J/mol'), E0=(30229.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007352480326336509, var=0.21863088705753284, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0_Ext-4C-R
    Total Standard Deviation in ln(k): 0.9558472331216682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0_Ext-4C-R
Total Standard Deviation in ln(k): 0.9558472331216682""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_4R->C_Ext-4C-R_Ext-6R!H-R_7R!H-u0_Ext-4C-R
Total Standard Deviation in ln(k): 0.9558472331216682
""",
)

entry(
    index = 61,
    label = "Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.28068e+54,'m^3/(mol*s)'), n=-13.6729, w0=(563000,'J/mol'), E0=(98492.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-14.503715032808914, var=306.25422247726704, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 71.52460076653797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 71.52460076653797""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 71.52460076653797
""",
)

entry(
    index = 62,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_4CNO->O",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_4CNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_4CNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_4CNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_4CNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O",
    kinetics = ArrheniusBM(A=(1713.08,'m^3/(mol*s)'), n=1.04631, w0=(540750,'J/mol'), E0=(61802.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6075970314782776, var=0.6553537765114736, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O
    Total Standard Deviation in ln(k): 3.149537412505626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O
Total Standard Deviation in ln(k): 3.149537412505626""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O
Total Standard Deviation in ln(k): 3.149537412505626
""",
)

entry(
    index = 64,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_2R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(666000,'J/mol'), E0=(66600,'J/mol'), Tmin=(295,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(648500,'J/mol'), E0=(59319.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C",
    kinetics = ArrheniusBM(A=(23739.9,'m^3/(mol*s)'), n=1.06417, w0=(589333,'J/mol'), E0=(58933.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4757799687165822, var=4.841357739016837, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C
    Total Standard Deviation in ln(k): 8.119025613270948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C
Total Standard Deviation in ln(k): 8.119025613270948""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C
Total Standard Deviation in ln(k): 8.119025613270948
""",
)

entry(
    index = 67,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C",
    kinetics = ArrheniusBM(A=(841.375,'m^3/(mol*s)'), n=1.39007, w0=(570167,'J/mol'), E0=(60295,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01764788437096908, var=0.7683247228970326, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C
    Total Standard Deviation in ln(k): 1.8015745915808237"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C
Total Standard Deviation in ln(k): 1.8015745915808237""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C
Total Standard Deviation in ln(k): 1.8015745915808237
""",
)

entry(
    index = 68,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R",
    kinetics = ArrheniusBM(A=(2.48022e+07,'m^3/(mol*s)'), n=-0.122388, w0=(662045,'J/mol'), E0=(32870.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.058087502478837684, var=2.2696482883792095, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R
    Total Standard Deviation in ln(k): 3.166152445846663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R
Total Standard Deviation in ln(k): 3.166152445846663""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R
Total Standard Deviation in ln(k): 3.166152445846663
""",
)

entry(
    index = 69,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_4CNOS->C",
    kinetics = ArrheniusBM(A=(8.49e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_4CNOS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_4CNOS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_4CNOS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_4CNOS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_N-4CNOS->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_N-4CNOS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_N-4CNOS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_N-4CNOS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_N-4CNOS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O",
    kinetics = ArrheniusBM(A=(38.8295,'m^3/(mol*s)'), n=1.74787, w0=(653000,'J/mol'), E0=(4988.82,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.689723018234242, var=32.74750905895635, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O
    Total Standard Deviation in ln(k): 20.74284540317009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O
Total Standard Deviation in ln(k): 20.74284540317009""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O
Total Standard Deviation in ln(k): 20.74284540317009
""",
)

entry(
    index = 72,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O",
    kinetics = ArrheniusBM(A=(0.727112,'m^3/(mol*s)'), n=2.07451, w0=(609583,'J/mol'), E0=(-638.381,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.39946878707435085, var=5.3650007428215964, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O
    Total Standard Deviation in ln(k): 5.6471522786450326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O
Total Standard Deviation in ln(k): 5.6471522786450326""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O
Total Standard Deviation in ln(k): 5.6471522786450326
""",
)

entry(
    index = 73,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(5.28325,'m^3/(mol*s)'), n=1.90949, w0=(597000,'J/mol'), E0=(27735.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05617766447116569, var=4.394118094017228, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R
    Total Standard Deviation in ln(k): 4.343506018133987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R
Total Standard Deviation in ln(k): 4.343506018133987""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R
Total Standard Deviation in ln(k): 4.343506018133987
""",
)

entry(
    index = 74,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(238.641,'m^3/(mol*s)'), n=1.42052, w0=(575333,'J/mol'), E0=(57533.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05496955953230046, var=0.24629949405939466, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 1.133035818416807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 1.133035818416807""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 1.133035818416807
""",
)

entry(
    index = 75,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(604667,'J/mol'), E0=(60466.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05487466445996819, var=7.222237291452136e-35, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 0.137876041356704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 0.137876041356704""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 0.137876041356704
""",
)

entry(
    index = 76,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(144.129,'m^3/(mol*s)'), n=1.40126, w0=(547200,'J/mol'), E0=(49527,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16910414071229812, var=0.19020277656122364, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R
    Total Standard Deviation in ln(k): 1.2991947151220047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 1.2991947151220047""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 1.2991947151220047
""",
)

entry(
    index = 77,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C",
    kinetics = ArrheniusBM(A=(15.5022,'m^3/(mol*s)'), n=1.55852, w0=(548688,'J/mol'), E0=(78412.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.25928468397828397, var=0.6789949022997033, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C
    Total Standard Deviation in ln(k): 2.3033937528292485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C
Total Standard Deviation in ln(k): 2.3033937528292485""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C
Total Standard Deviation in ln(k): 2.3033937528292485
""",
)

entry(
    index = 78,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C",
    kinetics = ArrheniusBM(A=(94.0763,'m^3/(mol*s)'), n=1.38035, w0=(558900,'J/mol'), E0=(33104.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.013303844099125002, var=0.5817728254752961, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C
    Total Standard Deviation in ln(k): 1.5625190574735903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C
Total Standard Deviation in ln(k): 1.5625190574735903""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C
Total Standard Deviation in ln(k): 1.5625190574735903
""",
)

entry(
    index = 79,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(9.04e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(662000,'J/mol'), E0=(47976.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_1R!H->O_N-4CNOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(16399.1,'m^3/(mol*s)'), n=1.06552, w0=(564500,'J/mol'), E0=(56450,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1948601205724478, var=0.35256865674022686, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 1.6799597049858794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 1.6799597049858794""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 1.6799597049858794
""",
)

entry(
    index = 82,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(4919.75,'m^3/(mol*s)'), n=1.14078, w0=(574750,'J/mol'), E0=(55918.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014663380331153596, var=0.27208609719602533, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 1.08255002480332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 1.08255002480332""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 1.08255002480332
""",
)

entry(
    index = 83,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 85,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-1.94626e-08, w0=(563000,'J/mol'), E0=(19905.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.122945412774981e-10, var=4.0371937089716863e-17, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C
    Total Standard Deviation in ln(k): 1.452755392867016e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 1.452755392867016e-08""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 1.452755392867016e-08
""",
)

entry(
    index = 86,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.000371804,'m^3/(mol*s)'), n=2.67859, w0=(655500,'J/mol'), E0=(88984.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_5C-u0",
    kinetics = ArrheniusBM(A=(1.19405e-06,'m^3/(mol*s)'), n=3.85287, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_5C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_5C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_5C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_5C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_N-5C-u0",
    kinetics = ArrheniusBM(A=(0.00124175,'m^3/(mol*s)'), n=3.00696, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_N-5C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_N-5C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_N-5C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_2R!H->O_Ext-4R-R_N-6R!H->C_N-5C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(0.00826928,'m^3/(mol*s)'), n=1.9902, w0=(563000,'J/mol'), E0=(3581.37,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5512577764814506, var=2.7189573097661635, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R
    Total Standard Deviation in ln(k): 4.690729798967232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R
Total Standard Deviation in ln(k): 4.690729798967232""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R
Total Standard Deviation in ln(k): 4.690729798967232
""",
)

entry(
    index = 90,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(1.70765e+07,'m^3/(mol*s)'), n=7.53848e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9494596051172368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H
    Total Standard Deviation in ln(k): 1.9534182263699047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.9534182263699047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.9534182263699047
""",
)

entry(
    index = 91,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_N-Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_N-Sp-5C-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_N-Sp-5C-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.46694e+06,'m^3/(mol*s)'), n=-0.183507, w0=(535591,'J/mol'), E0=(53559.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005156292503894267, var=0.7799766411144538, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.7834630776456517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.7834630776456517""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.7834630776456517
""",
)

entry(
    index = 93,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(1.4028e-05,'m^3/(mol*s)'), n=2.75396, w0=(539536,'J/mol'), E0=(-32109.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9010172179074781, var=49.67473058719176, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H',), comment="""BM rule fitted to 14 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H
    Total Standard Deviation in ln(k): 16.393295851184707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H
Total Standard Deviation in ln(k): 16.393295851184707""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H
Total Standard Deviation in ln(k): 16.393295851184707
""",
)

entry(
    index = 94,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(380.667,'m^3/(mol*s)'), n=1.06464, w0=(539000,'J/mol'), E0=(77196.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17954591455064195, var=5.988389109992552, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H
    Total Standard Deviation in ln(k): 5.356944748096939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 5.356944748096939""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 5.356944748096939
""",
)

entry(
    index = 95,
    label = "Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.06018e-05,'m^3/(mol*s)'), n=3.06568, w0=(563000,'J/mol'), E0=(-121532,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_N-5R!H->C_N-4R->C_Ext-4HOS-R_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_4CN->C",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(47358.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_4CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_4CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_4CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_4CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-4CN->C",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-4CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-4CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-4CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-2R!H->C_N-4R->H_N-4CNO->O_N-4CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(23588.5,'m^3/(mol*s)'), n=1.06552, w0=(609250,'J/mol'), E0=(60925,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6761713695632989, var=0.41113237262952895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.984351249045606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.984351249045606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.984351249045606
""",
)

entry(
    index = 100,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(400,'m^3/(mol*s)'), n=1.5, w0=(564000,'J/mol'), E0=(56400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(33.4541,'m^3/(mol*s)'), n=1.78536, w0=(573250,'J/mol'), E0=(50750.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20147811603791788, var=0.27148248712845674, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 1.5507732128102802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.5507732128102802""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.5507732128102802
""",
)

entry(
    index = 102,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS",
    kinetics = ArrheniusBM(A=(7.38113e+07,'m^3/(mol*s)'), n=-8.07774e-08, w0=(655500,'J/mol'), E0=(1088.46,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06280608228446091, var=6.8952486502763435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS
    Total Standard Deviation in ln(k): 5.421999069670699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS
Total Standard Deviation in ln(k): 5.421999069670699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS
Total Standard Deviation in ln(k): 5.421999069670699
""",
)

entry(
    index = 103,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS",
    kinetics = ArrheniusBM(A=(1.28861e+07,'m^3/(mol*s)'), n=-0.0980402, w0=(663500,'J/mol'), E0=(25180,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011781235605113797, var=1.1566524068008952, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS
    Total Standard Deviation in ln(k): 2.1856490798314985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS
Total Standard Deviation in ln(k): 2.1856490798314985""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS
Total Standard Deviation in ln(k): 2.1856490798314985
""",
)

entry(
    index = 104,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(3.06823e-33,'m^3/(mol*s)'), n=11.5608, w0=(648500,'J/mol'), E0=(-37786,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1311443344629586, var=3.4442370952847847, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R
    Total Standard Deviation in ln(k): 9.075152857245785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R
Total Standard Deviation in ln(k): 9.075152857245785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R
Total Standard Deviation in ln(k): 9.075152857245785
""",
)

entry(
    index = 105,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_4CN->C",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(638000,'J/mol'), E0=(77381.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_4CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_4CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_4CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_4CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C",
    kinetics = ArrheniusBM(A=(14.9839,'m^3/(mol*s)'), n=1.72681, w0=(603900,'J/mol'), E0=(21616.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0830025531621363, var=3.5244950023275647, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C
    Total Standard Deviation in ln(k): 3.9721662794163075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C
Total Standard Deviation in ln(k): 3.9721662794163075""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C
Total Standard Deviation in ln(k): 3.9721662794163075
""",
)

entry(
    index = 107,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(11.4006,'m^3/(mol*s)'), n=1.91038, w0=(595400,'J/mol'), E0=(21798.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02609482959117017, var=0.3875004658147189, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0
    Total Standard Deviation in ln(k): 1.313503170250616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 1.313503170250616""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0
Total Standard Deviation in ln(k): 1.313503170250616
""",
)

entry(
    index = 108,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(641031,'m^3/(mol*s)'), n=-0.261209, w0=(599667,'J/mol'), E0=(40245.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.5735654798279715, var=10.520824999975016, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 12.968767786078786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 12.968767786078786""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0
Total Standard Deviation in ln(k): 12.968767786078786
""",
)

entry(
    index = 109,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(383.414,'m^3/(mol*s)'), n=1.41908, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2983662469973947, var=5.131928286299004, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 7.803705422168636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 7.803705422168636""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 7.803705422168636
""",
)

entry(
    index = 110,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(211.933,'m^3/(mol*s)'), n=1.42089, w0=(574750,'J/mol'), E0=(57475,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05487466092377532, var=0.21353467425975017, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 1.064260346634528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 1.064260346634528""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 1.064260346634528
""",
)

entry(
    index = 111,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 113,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_Sp-5R!H#4CCCNNNSSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS",
    kinetics = ArrheniusBM(A=(142.296,'m^3/(mol*s)'), n=1.40303, w0=(548111,'J/mol'), E0=(49521.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2522136834508012, var=0.23871629099131667, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS
    Total Standard Deviation in ln(k): 1.613188238550468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS
Total Standard Deviation in ln(k): 1.613188238550468""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS
Total Standard Deviation in ln(k): 1.613188238550468
""",
)

entry(
    index = 115,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C",
    kinetics = ArrheniusBM(A=(108.077,'m^3/(mol*s)'), n=1.32854, w0=(550667,'J/mol'), E0=(55066.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05156472802023765, var=2.3527369978816193, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C
    Total Standard Deviation in ln(k): 3.2045494245042048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C
Total Standard Deviation in ln(k): 3.2045494245042048""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C
Total Standard Deviation in ln(k): 3.2045494245042048
""",
)

entry(
    index = 116,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C",
    kinetics = ArrheniusBM(A=(7.09295,'m^3/(mol*s)'), n=1.65039, w0=(547500,'J/mol'), E0=(77955.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30489593354048355, var=0.601219041897682, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C
    Total Standard Deviation in ln(k): 2.320508000280878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C
Total Standard Deviation in ln(k): 2.320508000280878""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C
Total Standard Deviation in ln(k): 2.320508000280878
""",
)

entry(
    index = 117,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(102.582,'m^3/(mol*s)'), n=1.38035, w0=(537333,'J/mol'), E0=(29158.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025198432495246517, var=1.4552981462220207, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 2.4817396149274193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 2.4817396149274193""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 2.4817396149274193
""",
)

entry(
    index = 118,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(82.6213,'m^3/(mol*s)'), n=1.38035, w0=(591250,'J/mol'), E0=(59125,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5787018105298811, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 1.4540246495725655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 1.4540246495725655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 1.4540246495725655
""",
)

entry(
    index = 119,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(500,'m^3/(mol*s)'), n=1.5, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2694.35,'m^3/(mol*s)'), n=1.20848, w0=(573833,'J/mol'), E0=(53393.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013509522983567888, var=0.546879820607096, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 1.516471641883916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.516471641883916""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.516471641883916
""",
)

entry(
    index = 123,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=5.24452e-08, w0=(563000,'J/mol'), E0=(21124.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 126,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(319178,'m^3/(mol*s)'), n=-0.245206, w0=(563000,'J/mol'), E0=(46965.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07202141574023016, var=0.7791555646275343, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H
    Total Standard Deviation in ln(k): 1.9505337533955611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.9505337533955611""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.9505337533955611
""",
)

entry(
    index = 127,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_N-Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(602200,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(40463,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_N-Sp-5C-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_N-Sp-5C-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C",
    kinetics = ArrheniusBM(A=(3.49726e+06,'m^3/(mol*s)'), n=-0.185408, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0007493433970125864, var=1.201264637628474, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C
    Total Standard Deviation in ln(k): 2.1991168991914556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C
Total Standard Deviation in ln(k): 2.1991168991914556""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C
Total Standard Deviation in ln(k): 2.1991168991914556
""",
)

entry(
    index = 130,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C",
    kinetics = ArrheniusBM(A=(3.38739e+06,'m^3/(mol*s)'), n=-0.178439, w0=(526500,'J/mol'), E0=(52650,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01690815967858609, var=0.010031744164233037, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C
    Total Standard Deviation in ln(k): 0.24327426208047448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C
Total Standard Deviation in ln(k): 0.24327426208047448""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C
Total Standard Deviation in ln(k): 0.24327426208047448
""",
)

entry(
    index = 131,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R",
    kinetics = ArrheniusBM(A=(0.000239522,'m^3/(mol*s)'), n=2.38854, w0=(538750,'J/mol'), E0=(11214.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.898627876943308, var=51.72430607986995, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R
    Total Standard Deviation in ln(k): 16.675835904940108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R
Total Standard Deviation in ln(k): 16.675835904940108""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R
Total Standard Deviation in ln(k): 16.675835904940108
""",
)

entry(
    index = 132,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_4CHS->H",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_4CHS->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_4CHS->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_4CHS->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_4CHS->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_N-4CHS->H",
    kinetics = ArrheniusBM(A=(1.15e+07,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_N-4CHS->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_N-4CHS->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_N-4CHS->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_N-4CHS->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R",
    kinetics = ArrheniusBM(A=(934.663,'m^3/(mol*s)'), n=0.944116, w0=(539000,'J/mol'), E0=(77381.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27391051117805787, var=7.943538623916611, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R
    Total Standard Deviation in ln(k): 6.338419633545027"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R
Total Standard Deviation in ln(k): 6.338419633545027""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R
Total Standard Deviation in ln(k): 6.338419633545027
""",
)

entry(
    index = 135,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(642000,'J/mol'), E0=(64200,'J/mol'), Tmin=(300,'K'), Tmax=(1000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(720,'m^3/(mol*s)'), n=1.5, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(612000,'J/mol'), E0=(63724.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H-u1_N-1R!H->O_N-1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_5R!H->C",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56853,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_Sp-5R!H=4CCNNOOSS_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R",
    kinetics = ArrheniusBM(A=(2.85561e+07,'m^3/(mol*s)'), n=-0.375, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.06912283083491383, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R
    Total Standard Deviation in ln(k): 0.5270693322083513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R
Total Standard Deviation in ln(k): 0.5270693322083513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R
Total Standard Deviation in ln(k): 0.5270693322083513
""",
)

entry(
    index = 142,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56999.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C",
    kinetics = ArrheniusBM(A=(5.18979e+06,'m^3/(mol*s)'), n=9.83609e-08, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.622093093931151e-07, var=1.4637540157724285, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C
    Total Standard Deviation in ln(k): 2.4254432199274203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C
Total Standard Deviation in ln(k): 2.4254432199274203""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C
Total Standard Deviation in ln(k): 2.4254432199274203
""",
)

entry(
    index = 144,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C",
    kinetics = ArrheniusBM(A=(1.89499e+08,'m^3/(mol*s)'), n=-0.346565, w0=(679500,'J/mol'), E0=(38476.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1578984580421725, var=4.595591047124435, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C
    Total Standard Deviation in ln(k): 7.206909289886282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C
Total Standard Deviation in ln(k): 7.206909289886282""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C
Total Standard Deviation in ln(k): 7.206909289886282
""",
)

entry(
    index = 145,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_2NOS->O",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(635000,'J/mol'), E0=(6270.39,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_2NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_2NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_N-2NOS->O",
    kinetics = ArrheniusBM(A=(0.0294,'m^3/(mol*s)'), n=2.69, w0=(662000,'J/mol'), E0=(33464.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_N-2NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_N-2NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_N-2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_4CNOS->O_Ext-4O-R_N-2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R",
    kinetics = ArrheniusBM(A=(1.8853e+06,'m^3/(mol*s)'), n=0.332417, w0=(598500,'J/mol'), E0=(40111.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4844082918224548, var=6.9157034187503745, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R
    Total Standard Deviation in ln(k): 6.4891034436544075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R
Total Standard Deviation in ln(k): 6.4891034436544075""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R
Total Standard Deviation in ln(k): 6.4891034436544075
""",
)

entry(
    index = 148,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_2NOS->O",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(35268.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_2NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_2NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_N-2NOS->O",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(625500,'J/mol'), E0=(51859.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_N-2NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_N-2NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_N-2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_N-2NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(573833,'J/mol'), E0=(21511.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03872283658228287, var=0.003687235162771551, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 0.2190263021681399"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 0.2190263021681399""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 0.2190263021681399
""",
)

entry(
    index = 151,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(7.45181,'m^3/(mol*s)'), n=1.90892, w0=(627750,'J/mol'), E0=(62775,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8809875394276374, var=0.011502560091510204, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 2.4285443457657907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 2.4285443457657907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 2.4285443457657907
""",
)

entry(
    index = 152,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(92345.7,'J/mol'), Tmin=(700,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_Sp-2R!H-1CNS',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(665601,'m^3/(mol*s)'), n=-0.266607, w0=(618000,'J/mol'), E0=(21094.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.394125347182226, var=15.830042173788614, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 11.479064056591858"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 11.479064056591858""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 11.479064056591858
""",
)

entry(
    index = 154,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(3.6,'m^3/(mol*s)'), n=2, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N",
    kinetics = ArrheniusBM(A=(178.214,'m^3/(mol*s)'), n=1.42089, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 157,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N",
    kinetics = ArrheniusBM(A=(252.033,'m^3/(mol*s)'), n=1.42089, w0=(601500,'J/mol'), E0=(60150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 158,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_N-Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_2R!H->S",
    kinetics = ArrheniusBM(A=(979000,'m^3/(mol*s)'), n=0, w0=(537500,'J/mol'), E0=(38210.6,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_2R!H->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_2R!H->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_2R!H->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_2R!H->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S",
    kinetics = ArrheniusBM(A=(139.69,'m^3/(mol*s)'), n=1.40572, w0=(549438,'J/mol'), E0=(42012.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.174540731278139, var=0.1180303671254295, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S
    Total Standard Deviation in ln(k): 1.1272822706579717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S
Total Standard Deviation in ln(k): 1.1272822706579717""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S
Total Standard Deviation in ln(k): 1.1272822706579717
""",
)

entry(
    index = 162,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(187.635,'m^3/(mol*s)'), n=1.32726, w0=(552500,'J/mol'), E0=(55250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1546561267678964, var=0.37853885495848577, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 1.6220067411055652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 1.6220067411055652""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 1.6220067411055652
""",
)

entry(
    index = 163,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(0.81,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(54700,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_N-Sp-2R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(34.41,'m^3/(mol*s)'), n=1.44661, w0=(544000,'J/mol'), E0=(54400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43780050013999694, var=0.5999111817527254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C
    Total Standard Deviation in ln(k): 2.6527474307051118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 2.6527474307051118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C
Total Standard Deviation in ln(k): 2.6527474307051118
""",
)

entry(
    index = 165,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.790644,'m^3/(mol*s)'), n=1.92933, w0=(549833,'J/mol'), E0=(76804.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.029938595334405658, var=1.8854180731063452, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.8279348942078038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.8279348942078038""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.8279348942078038
""",
)

entry(
    index = 166,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->O",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(589000,'J/mol'), E0=(45404.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O",
    kinetics = ArrheniusBM(A=(81.7183,'m^3/(mol*s)'), n=1.38035, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5787018105298811, var=3.7227133182354435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O
    Total Standard Deviation in ln(k): 5.322027504076752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O
Total Standard Deviation in ln(k): 5.322027504076752""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O
Total Standard Deviation in ln(k): 5.322027504076752
""",
)

entry(
    index = 168,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(648000,'J/mol'), E0=(64800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(323.865,'m^3/(mol*s)'), n=1.46107, w0=(586750,'J/mol'), E0=(42728,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23284945485790864, var=0.6476388655306268, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 2.1983797414238784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.1983797414238784""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.1983797414238784
""",
)

entry(
    index = 171,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(20706.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_Ext-5C-R_N-1R!H-inRing_2R!H->C_Ext-1R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(10974.5,'m^3/(mol*s)'), n=7.68845e-08, w0=(563000,'J/mol'), E0=(19802.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2290956255676566e-17, var=0.06917824979652494, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.5272805777722495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.5272805777722495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_4R->O_Ext-4O-R_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.5272805777722495
""",
)

entry(
    index = 174,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.23617e+06,'m^3/(mol*s)'), n=-0.166181, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0008563821550657155, var=1.421847219875964, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.39262258497754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.39262258497754""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.39262258497754
""",
)

entry(
    index = 175,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_4HS->H",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_4HS->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_4HS->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_4HS->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_4HS->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H",
    kinetics = ArrheniusBM(A=(6.55713e+06,'m^3/(mol*s)'), n=-0.267658, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27677043112298655, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H
    Total Standard Deviation in ln(k): 0.6954030932738355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H
Total Standard Deviation in ln(k): 0.6954030932738355""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H
Total Standard Deviation in ln(k): 0.6954030932738355
""",
)

entry(
    index = 177,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S",
    kinetics = ArrheniusBM(A=(3.12126e-13,'m^3/(mol*s)'), n=4.70087, w0=(527000,'J/mol'), E0=(17509.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=10.238614422136449, var=279.3313223037818, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S
    Total Standard Deviation in ln(k): 59.23071623718318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S
Total Standard Deviation in ln(k): 59.23071623718318""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S
Total Standard Deviation in ln(k): 59.23071623718318
""",
)

entry(
    index = 178,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S",
    kinetics = ArrheniusBM(A=(263.727,'m^3/(mol*s)'), n=0.816154, w0=(541100,'J/mol'), E0=(-863.021,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.036165589318776, var=27.18226287672188, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S
    Total Standard Deviation in ln(k): 15.568003387761646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S
Total Standard Deviation in ln(k): 15.568003387761646""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S
Total Standard Deviation in ln(k): 15.568003387761646
""",
)

entry(
    index = 179,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(84300,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(76690.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R",
    kinetics = ArrheniusBM(A=(0.000740847,'m^3/(mol*s)'), n=2.91991, w0=(539000,'J/mol'), E0=(35253.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004220313209984355, var=8.94173911161422, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R
    Total Standard Deviation in ln(k): 6.005311154003196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R
Total Standard Deviation in ln(k): 6.005311154003196""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R
Total Standard Deviation in ln(k): 6.005311154003196
""",
)

entry(
    index = 181,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Sp-6R!H-4CHS",
    kinetics = ArrheniusBM(A=(964000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(92497.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Sp-6R!H-4CHS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Sp-6R!H-4CHS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Sp-6R!H-4CHS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Sp-6R!H-4CHS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_N-Sp-6R!H-4CHS",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_N-Sp-6R!H-4CHS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_N-Sp-6R!H-4CHS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_N-Sp-6R!H-4CHS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_N-Sp-6R!H-4CHS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R_Ext-4CNOS-R",
    kinetics = ArrheniusBM(A=(3.47e+08,'m^3/(mol*s)'), n=-0.75, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R_Ext-4CNOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R_Ext-4CNOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R_Ext-4CNOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_Ext-4CNOS-R_Ext-4CNOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(3.40826e+06,'m^3/(mol*s)'), n=-2.28069e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 185,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_N-Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(1.20333e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_N-Sp-5R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_N-Sp-5R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0",
    kinetics = ArrheniusBM(A=(2.11547e+08,'m^3/(mol*s)'), n=-0.313028, w0=(679500,'J/mol'), E0=(76755.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12167865343175763, var=0.6437215165799257, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0
    Total Standard Deviation in ln(k): 1.914169472146607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0
Total Standard Deviation in ln(k): 1.914169472146607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0
Total Standard Deviation in ln(k): 1.914169472146607
""",
)

entry(
    index = 187,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(5.7209e+06,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(20296,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_N-5R!H-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_N-5R!H-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_N-5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_N-5R!H-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_5R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(24711.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(10.725,'m^3/(mol*s)'), n=1.90892, w0=(598500,'J/mol'), E0=(11124.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8611054555760191, var=1.2141850405896415, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N
    Total Standard Deviation in ln(k): 4.372600429820919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N
Total Standard Deviation in ln(k): 4.372600429820919""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N
Total Standard Deviation in ln(k): 4.372600429820919
""",
)

entry(
    index = 190,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->O",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(625500,'J/mol'), E0=(26705.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(548000,'J/mol'), E0=(31955.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0426036023134155, var=0.11276809873671895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O
    Total Standard Deviation in ln(k): 3.2928163591177713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O
Total Standard Deviation in ln(k): 3.2928163591177713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O
Total Standard Deviation in ln(k): 3.2928163591177713
""",
)

entry(
    index = 192,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(2.6e+09,'m^3/(mol*s)'), n=-1.26, w0=(551500,'J/mol'), E0=(34913.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=-0.34, w0=(684500,'J/mol'), E0=(61174.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_N-5R!H-u0_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_2N-u1",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(625500,'J/mol'), E0=(55947.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_N-2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_N-2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O",
    kinetics = ArrheniusBM(A=(127.638,'m^3/(mol*s)'), n=1.41908, w0=(593500,'J/mol'), E0=(30111.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2786278929612721, var=0.671686074395935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O
    Total Standard Deviation in ln(k): 2.3430799122511208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O
Total Standard Deviation in ln(k): 2.3430799122511208""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O
Total Standard Deviation in ln(k): 2.3430799122511208
""",
)

entry(
    index = 201,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.38436e+07,'m^3/(mol*s)'), n=-0.304179, w0=(534750,'J/mol'), E0=(27148.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1610975619575171, var=0.25986302638912895, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O
    Total Standard Deviation in ln(k): 1.4267167727232863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O
Total Standard Deviation in ln(k): 1.4267167727232863""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O
Total Standard Deviation in ln(k): 1.4267167727232863
""",
)

entry(
    index = 202,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_2R!H->C",
    kinetics = ArrheniusBM(A=(2.19e+08,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=1.87, w0=(566000,'J/mol'), E0=(56600,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_1CNS->C_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_Sp-2C-1N",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(553500,'J/mol'), E0=(55350,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_N-Sp-2C-1N",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_N-Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_N-Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_2R!H->C_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(0.00010394,'m^3/(mol*s)'), n=3.02774, w0=(562750,'J/mol'), E0=(47277.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8568478925825855, var=0.083327900484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 2.73158245570468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.73158245570468""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.73158245570468
""",
)

entry(
    index = 207,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_2N-u1",
    kinetics = ArrheniusBM(A=(0.46,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_N-4CNS->C_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(625500,'J/mol'), E0=(52128.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_N-4CNOS-u1_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_Sp-7R!H#4C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_Sp-7R!H#4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_Sp-7R!H#4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_Sp-7R!H#4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_Sp-7R!H#4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C",
    kinetics = ArrheniusBM(A=(2.91732e+06,'m^3/(mol*s)'), n=-0.193877, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0009991190442675043, var=0.7512416561916286, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C
    Total Standard Deviation in ln(k): 1.7400983954314215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C
Total Standard Deviation in ln(k): 1.7400983954314215""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C
Total Standard Deviation in ln(k): 1.7400983954314215
""",
)

entry(
    index = 214,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H_Ext-4S-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H_Ext-4S-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H_Ext-4S-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H_Ext-4S-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_N-4CHS->C_N-4HS->H_Ext-4S-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S_Ext-2CS-R",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(515000,'J/mol'), E0=(39525.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S_Ext-2CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S_Ext-2CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S_Ext-2CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_6R!H->S_Ext-2CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C",
    kinetics = ArrheniusBM(A=(4.53586e+06,'m^3/(mol*s)'), n=-0.149164, w0=(544000,'J/mol'), E0=(32451.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1420922462876188, var=0.9613525670784362, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C
    Total Standard Deviation in ln(k): 2.3226301370530593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C
Total Standard Deviation in ln(k): 2.3226301370530593""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C
Total Standard Deviation in ln(k): 2.3226301370530593
""",
)

entry(
    index = 217,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_N-4CHS->C",
    kinetics = ArrheniusBM(A=(7.19e-07,'m^3/(mol*s)'), n=3.13, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_N-4CHS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_N-4CHS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_N-4CHS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_N-4CHS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R_Ext-4CHS-R",
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(85952.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R_Ext-4CHS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R_Ext-4CHS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R_Ext-4CHS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_N-Sp-5C-1R!H_Ext-4CHS-R_Ext-4CHS-R_Ext-4CHS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.82e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_4CNOS->C_Sp-5R!H-4C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(55695.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_2R!H->C_Ext-4CNOS-R_N-Sp-5R!H=4CCNNOOSS_N-4CNOS->C_5R!H-u0_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_5BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(17330.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_5BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_5BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_5BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_5BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_N-5BrCClFIOPSSi->C",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(13374.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_N-5BrCClFIOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_N-5BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_N-5BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_1R!H->O_N-2R!H->C_N-4CNOS->O_N-4CN->C_Ext-4N-R_N-5R!H->N_N-5BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(39565.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_4CNOS->O_Ext-4O-R_5R!H-u0_Sp-2R!H-1CNS_N-2R!H->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_1CNS->C",
    kinetics = ArrheniusBM(A=(2.89e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_N-1CNS->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(648000,'J/mol'), E0=(54170.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_5R!H->O_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS",
    kinetics = ArrheniusBM(A=(8.57298e+06,'m^3/(mol*s)'), n=-0.225015, w0=(533900,'J/mol'), E0=(31128.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19506345554400223, var=0.22967145394007588, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS
    Total Standard Deviation in ln(k): 1.4508594195758966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.4508594195758966""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.4508594195758966
""",
)

entry(
    index = 230,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_N-Sp-5CS-4CCNSS",
    kinetics = ArrheniusBM(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_N-Sp-5CS-4CCNSS',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_N-Sp-5CS-4CCNSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_N-Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_N-Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(601500,'J/mol'), E0=(75336.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_4CNS->C_N-1CNS->C_N-2R!H->C_2NO-u1_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C",
    kinetics = ArrheniusBM(A=(4.80372e+06,'m^3/(mol*s)'), n=-0.232653, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011989427634325857, var=0.3951773289456139, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C
    Total Standard Deviation in ln(k): 1.263251664934538"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C
Total Standard Deviation in ln(k): 1.263251664934538""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C
Total Standard Deviation in ln(k): 1.263251664934538
""",
)

entry(
    index = 234,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C",
    kinetics = ArrheniusBM(A=(241000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C",
    kinetics = ArrheniusBM(A=(4.09881e+06,'m^3/(mol*s)'), n=-0.159099, w0=(544625,'J/mol'), E0=(30212.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12986260823020596, var=0.7033009269391155, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C
    Total Standard Deviation in ln(k): 2.0075197152876667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C
Total Standard Deviation in ln(k): 2.0075197152876667""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C
Total Standard Deviation in ln(k): 2.0075197152876667
""",
)

entry(
    index = 237,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(7.76827e+08,'m^3/(mol*s)'), n=-0.9, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0763652085225523e-17, var=0.04891149884417046, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.4433660913390881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390881
""",
)

entry(
    index = 238,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C",
    kinetics = ArrheniusBM(A=(2.95928e+07,'m^3/(mol*s)'), n=-0.381632, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.032709232769080235, var=0.0016076635746038646, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C
    Total Standard Deviation in ln(k): 0.16256521857885725"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C
Total Standard Deviation in ln(k): 0.16256521857885725""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C
Total Standard Deviation in ln(k): 0.16256521857885725
""",
)

entry(
    index = 239,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(513500,'J/mol'), E0=(42507.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.25814e+07,'m^3/(mol*s)'), n=-0.55, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.5036392791388526, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 3.7524652808647927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.7524652808647927""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.7524652808647927
""",
)

entry(
    index = 241,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(783000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Sp-7C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_N-Sp-7C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C",
    kinetics = ArrheniusBM(A=(5.66041e+06,'m^3/(mol*s)'), n=-0.183878, w0=(545429,'J/mol'), E0=(31878.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.181236994230568, var=0.610682226143694, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C
    Total Standard Deviation in ln(k): 2.021992805530194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C
Total Standard Deviation in ln(k): 2.021992805530194""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C
Total Standard Deviation in ln(k): 2.021992805530194
""",
)

entry(
    index = 245,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_N-6BrCClFINOPSi->C",
    kinetics = ArrheniusBM(A=(482000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_N-6BrCClFINOPSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_N-6BrCClFINOPSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_N-6BrCClFINOPSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_N-6BrCClFINOPSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.86e+09,'m^3/(mol*s)'), n=-1.1, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R",
    kinetics = ArrheniusBM(A=(2.29e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_4CNOS-u1_N-1R!H->O_N-4CNOS->O_Ext-4CNS-R_N-Sp-5R!H#4CCCNNNSSS_N-2R!H->S_N-5R!H->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Ext-1R!H-R_4CHS->C_Ext-4C-R_N-Sp-7R!H#4C_7R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.90756e+07,'m^3/(mol*s)'), n=-0.342329, w0=(550250,'J/mol'), E0=(34700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24736840561813153, var=1.6912697757834065, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 3.228663137206951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.228663137206951""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.228663137206951
""",
)

entry(
    index = 250,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C",
    kinetics = ArrheniusBM(A=(1.8697e+06,'m^3/(mol*s)'), n=-0.0316323, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0327092327690802, var=0.00213978781668374, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C
    Total Standard Deviation in ln(k): 0.1749187175813773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C
Total Standard Deviation in ln(k): 0.1749187175813773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C
Total Standard Deviation in ln(k): 0.1749187175813773
""",
)

entry(
    index = 251,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-Sp-6C-4C",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-Sp-6C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-Sp-6C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-Sp-6C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_N-Sp-6C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C",
    kinetics = ArrheniusBM(A=(1.05265e+08,'m^3/(mol*s)'), n=-0.55, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.513977146582821, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C
    Total Standard Deviation in ln(k): 3.75799723098171"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C
Total Standard Deviation in ln(k): 3.75799723098171""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C
Total Standard Deviation in ln(k): 3.75799723098171
""",
)

entry(
    index = 253,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C",
    kinetics = ArrheniusBM(A=(1.7641e+06,'m^3/(mol*s)'), n=-0.0462319, w0=(561500,'J/mol'), E0=(17554.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2144940523654643, var=1.5169644222011907, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C
    Total Standard Deviation in ln(k): 3.008063935012343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C
Total Standard Deviation in ln(k): 3.008063935012343""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C
Total Standard Deviation in ln(k): 3.008063935012343
""",
)

entry(
    index = 254,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Sp-6C-4C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.16e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_2CS->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C_Ext-7R!H-R_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=0, w0=(561500,'J/mol'), E0=(36677.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C_Ext-7R!H-R_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C_Ext-7R!H-R_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C_Ext-7R!H-R_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1R!H-R_5R!H->C_4R-u1_N-2R!H->O_N-4R->O_Sp-5C-1R!H_Ext-4CHS-R_N-6R!H->S_4CHS->C_N-Sp-6BrBrBrCCCClClClFFFIIINNNOOOPPPSiSiSi#4C_6BrCClFINOPSi->C_Ext-4C-R_N-2CS->C_Ext-7R!H-R_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

