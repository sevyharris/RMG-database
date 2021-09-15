#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.25564e+08,'m^3/(mol*s)'), n=-0.063585, w0=(156071,'J/mol'), E0=(15607.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.476826989839096e-05, var=33.368379815951414, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 11.580589102085586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 11.580589102085586""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 11.580589102085586
sensitivities = [{'dA': -0.01997039045420699, 'dE0': 0.0, 'dn': -0.05296462173915751, 'dA_dEa': -0.04134901110575584, 'dE0_dEa': 0.0, 'dn_dEa': -0.08975240696422064, 'name': 'NH + NO2_r <=> HNNO2'}, {'dA': 0.4825177081678154, 'dE0': 0.0, 'dn': -0.021868066329339974, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'S + NO <=> SNO'}, {'dA': 0.4872135168874618, 'dE0': 0.0, 'dn': -0.01125148846319294, 'dA_dEa': 2.8915888710588775, 'dE0_dEa': 0.0, 'dn_dEa': 5.8336043330236755, 'name': '[N]=O + [O] <=> NO2_p'}, {'dA': -0.019974763102228434, 'dE0': 0.0, 'dn': -0.05297450662766033, 'dA_dEa': 0.008612665990171802, 'dE0_dEa': 0.0, 'dn_dEa': 0.011065533363672773, 'name': 'CC[O] + [O] <=> CH3CH2OO'}, {'dA': -0.02003220424740214, 'dE0': 0.0, 'dn': -0.05310435705487175, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'H + O <=> HO'}, {'dA': -0.02003220424740214, 'dE0': 0.0, 'dn': -0.05310435705487175, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'H + S <=> HS'}, {'dA': -0.02003220424740214, 'dE0': 0.0, 'dn': -0.05310435705487175, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'H + NH <=> H2N'}]
""",
)

entry(
    index = 2,
    label = "Root_2R->H",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.21648e-07, w0=(201333,'J/mol'), E0=(20133.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1858725180105822e-08, var=1.6421466378806452e-47, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2R->H',), comment="""BM rule fitted to 3 training reactions at node Root_2R->H
    Total Standard Deviation in ln(k): 5.4921420050517145e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2R->H
Total Standard Deviation in ln(k): 5.4921420050517145e-08""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2R->H
Total Standard Deviation in ln(k): 5.4921420050517145e-08
sensitivities = [{'dA': 0.33361329644780235, 'dE0': 0.0, 'dn': -523.9196538505649, 'dA_dEa': 0.00031817739198917343, 'dE0_dEa': 0.0, 'dn_dEa': -338.6844813881315, 'name': 'H + O <=> HO'}, {'dA': 0.33361329644780235, 'dE0': 0.0, 'dn': -523.9196538549169, 'dA_dEa': 0.00031817739198917343, 'dE0_dEa': 0.0, 'dn_dEa': -338.6844813881315, 'name': 'H + S <=> HS'}, {'dA': 0.33361329644780235, 'dE0': 0.0, 'dn': -523.9196538528936, 'dA_dEa': 0.00031817739198917343, 'dE0_dEa': 0.0, 'dn_dEa': -338.6844813881315, 'name': 'H + NH <=> H2N'}]
""",
)

entry(
    index = 3,
    label = "Root_N-2R->H",
    kinetics = ArrheniusBM(A=(1.28632e+08,'m^3/(mol*s)'), n=-0.0641915, w0=(122125,'J/mol'), E0=(12212.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01904387942530516, var=34.85684078884004, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2R->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-2R->H
    Total Standard Deviation in ln(k): 11.883741137555582"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2R->H
Total Standard Deviation in ln(k): 11.883741137555582""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2R->H
Total Standard Deviation in ln(k): 11.883741137555582
sensitivities = [{'dA': 0.006992784822302471, 'dE0': 0.0, 'dn': 0.007837831040312292, 'dA_dEa': -0.014592478052579069, 'dE0_dEa': 0.0, 'dn_dEa': -0.028956042735629836, 'name': 'NH + NO2_r <=> HNNO2'}, {'dA': 0.4887891995118393, 'dE0': 0.0, 'dn': -0.018132927963006088, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'S + NO <=> SNO'}, {'dA': 0.48538265888359095, 'dE0': 0.0, 'dn': -0.025760838568784795, 'dA_dEa': 2.9097867560355803, 'dE0_dEa': 0.0, 'dn_dEa': 5.812568922289014, 'name': '[N]=O + [O] <=> NO2_p'}, {'dA': 0.0069952072472297885, 'dE0': 0.0, 'dn': 0.007843255135606627, 'dA_dEa': 0.03585533415062909, 'dE0_dEa': 0.0, 'dn_dEa': 0.07188332606785296, 'name': 'CC[O] + [O] <=> CH3CH2OO'}]
""",
)

entry(
    index = 4,
    label = "Root_2R->H_1R!H->O",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2R->H_1R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_2R->H_1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2R->H_1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2R->H_1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'H + O <=> HO'}]
""",
)

entry(
    index = 5,
    label = "Root_2R->H_N-1R!H->O",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.28714e-07, w0=(187250,'J/mol'), E0=(18725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2R->H_N-1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_2R->H_N-1R!H->O
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R->H_N-1R!H->O
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R->H_N-1R!H->O
Total Standard Deviation in ln(k): 0.0
sensitivities = [{'dA': 0.5000735495635507, 'dE0': 0.0, 'dn': -349.271392895984, 'dA_dEa': 0.0001677933987309828, 'dE0_dEa': 0.0, 'dn_dEa': -166.20800961112155, 'name': 'H + S <=> HS'}, {'dA': 0.5000735495635507, 'dE0': 0.0, 'dn': -349.27139289752057, 'dA_dEa': 0.0001677933987309828, 'dE0_dEa': 0.0, 'dn_dEa': -166.20800961112155, 'name': 'H + NH <=> H2N'}]
""",
)

entry(
    index = 6,
    label = "Root_N-2R->H_1R!H->S",
    kinetics = ArrheniusBM(A=(1.3e+08,'m^3/(mol*s)'), n=0.24, w0=(233500,'J/mol'), E0=(23350,'J/mol'), Tmin=(300,'K'), Tmax=(800,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2R->H_1R!H->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-2R->H_1R!H->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2R->H_1R!H->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2R->H_1R!H->S
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'S + NO <=> SNO'}]
""",
)

entry(
    index = 7,
    label = "Root_N-2R->H_N-1R!H->S",
    kinetics = ArrheniusBM(A=(1.27293e+08,'m^3/(mol*s)'), n=-0.364536, w0=(85000,'J/mol'), E0=(8500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8230805490603663, var=6.779062865807092, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S',), comment="""BM rule fitted to 3 training reactions at node Root_N-2R->H_N-1R!H->S
    Total Standard Deviation in ln(k): 9.800259651978573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2R->H_N-1R!H->S
Total Standard Deviation in ln(k): 9.800259651978573""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2R->H_N-1R!H->S
Total Standard Deviation in ln(k): 9.800259651978573
sensitivities = [{'dA': 0.005125087916724734, 'dE0': 0.0, 'dn': -0.00046956041550676804, 'dA_dEa': -0.037772121434191674, 'dE0_dEa': 0.0, 'dn_dEa': -0.01334561767834676, 'name': 'NH + NO2_r <=> HNNO2'}, {'dA': 0.9862439608420124, 'dE0': 0.0, 'dn': -0.0002462248546515408, 'dA_dEa': 5.807013065535855, 'dE0_dEa': 0.0, 'dn_dEa': 2.0439485985673063, 'name': '[N]=O + [O] <=> NO2_p'}, {'dA': 0.005109986481955383, 'dE0': 0.0, 'dn': -0.00047551355894377446, 'dA_dEa': 0.06248152762467618, 'dE0_dEa': 0.0, 'dn_dEa': 0.021942054250747155, 'name': 'CC[O] + [O] <=> CH3CH2OO'}]
""",
)

entry(
    index = 8,
    label = "Root_2R->H_N-1R!H->O_1NS->S",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(181500,'J/mol'), E0=(18150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2R->H_N-1R!H->O_1NS->S',), comment="""BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->O_1NS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->O_1NS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->O_1NS->S
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'H + S <=> HS'}]
""",
)

entry(
    index = 9,
    label = "Root_2R->H_N-1R!H->O_N-1NS->S",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(193000,'J/mol'), E0=(19300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2R->H_N-1R!H->O_N-1NS->S',), comment="""BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->O_N-1NS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->O_N-1NS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2R->H_N-1R!H->O_N-1NS->S
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': nan, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': nan, 'name': 'H + NH <=> H2N'}]
""",
)

entry(
    index = 10,
    label = "Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(4.84265e+08,'m^3/(mol*s)'), n=-0.296706, w0=(77250,'J/mol'), E0=(7725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22847199987885378, var=0.037066746561076835, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi
    Total Standard Deviation in ln(k): 0.9600164061664855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi
Total Standard Deviation in ln(k): 0.9600164061664855""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi
Total Standard Deviation in ln(k): 0.9600164061664855
sensitivities = [{'dA': 0.4997738716597251, 'dE0': 0.0, 'dn': 1.1479043488918358e-05, 'dA_dEa': -2.8942920960414034, 'dE0_dEa': 0.0, 'dn_dEa': -1.2516354764830766, 'name': 'NH + NO2_r <=> HNNO2'}, {'dA': 0.4997505910929174, 'dE0': 0.0, 'dn': 2.0090432009929826e-07, 'dA_dEa': 5.0379762415287965, 'dE0_dEa': 0.0, 'dn_dEa': 2.1786715819101343, 'name': 'CC[O] + [O] <=> CH3CH2OO'}]
""",
)

entry(
    index = 11,
    label = "Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(349106,'m^3/(mol*s)'), n=0.389287, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_N-Sp-3R!H-2BrCClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': '[N]=O + [O] <=> NO2_p'}]
""",
)

entry(
    index = 12,
    label = "Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->O",
    kinetics = ArrheniusBM(A=(226935,'m^3/(mol*s)'), n=0.706701, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': 0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': 0.0, 'name': 'CC[O] + [O] <=> CH3CH2OO'}]
""",
)

entry(
    index = 13,
    label = "Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->O",
    kinetics = ArrheniusBM(A=(1.42e+10,'m^3/(mol*s)'), n=-0.75, w0=(83500,'J/mol'), E0=(8350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2R->H_N-1R!H->S_Ext-2BrCClFINOPSSi-R_Sp-3R!H-2BrCClFINOPSSi_N-1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
sensitivities = [{'dA': 0.9995003330837129, 'dE0': 0.0, 'dn': -0.0, 'dA_dEa': 0.0, 'dE0_dEa': 0.0, 'dn_dEa': -0.0, 'name': 'NH + NO2_r <=> HNNO2'}]
""",
)

